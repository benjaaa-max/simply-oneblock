#!/usr/bin/env python3
"""Generador de so_arenas v1 — el Coliseo VorNeX (lo donde pasa).

Construye: coliseo ovalado 84x100 (exterior) con gradas, arcadas, 8 torres (80 de alto),
lobby/tunel, NPCs; sistemas: viaje (/trigger arena, /trigger volver), practica por tiers
con kit prestado, contratos con rangos ocultos (/trigger levelrank), anti-camping,
mecanica de abandono y fuegos artificiales de victoria.
Los enemigos vienen de so_events:api (mob/boss), retageados a so_ar_mob dentro del coliseo.
Salida: datapacks/so-arenas + /mnt/documents/so_arenas-v1.zip (raiz limpia).
"""
import json, os, shutil, zipfile, math, random

ROOT = os.path.join(os.path.dirname(__file__), "..", "datapacks", "so-arenas")
NS = "so_arenas"
CX, CZ, FLOOR = -5000, -5000, 96   # piso del foso (gradas arrancan en 97)
AX, BZ = 42, 50                    # semiejes: exterior 84 x 100
TOP_Y = 170                        # torres
shutil.rmtree(ROOT, ignore_errors=True)
random.seed(7)

def W(rel, obj):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(obj if isinstance(obj, str) else json.dumps(obj, ensure_ascii=False, indent=2))

def F(name, lines):
    W(f"data/{NS}/function/{name}.mcfunction", "\n".join(lines) + "\n")

def T(*parts):
    return json.dumps(list(parts) if len(parts) > 1 else parts[0], ensure_ascii=False)

PFX = {"text": "[Arena] ", "color": "gold", "bold": True}
def say(sel, text, color="yellow"):
    return f"tellraw {sel} {T(PFX, {'text': text, 'color': color, 'bold': False})}"

IN = "@a[tag=so_ar_in]"
def norm(dx, dz): return (dx / AX) ** 2 + (dz / BZ) ** 2
def dzmax(dx, r):
    a = 1 - (dx / AX) ** 2 / (r ** 2)
    return int(BZ * r * math.sqrt(a)) if a > 0 else 0

FLOOR_MIX = ["minecraft:sandstone", "minecraft:packed_mud", "minecraft:coarse_dirt",
             "minecraft:polished_tuff", "minecraft:sandstone_bricks"]
GRAD_MIX = ["minecraft:stone_bricks", "minecraft:polished_deepslate", "minecraft:sandstone_bricks"]

# ---------------------------------------------------------------- pack
W("pack.mcmeta", {"pack": {"description": "Simply OneBlock Expansion - Arenas (coliseo, practica y contratos)",
                           "min_format": [107, 1], "max_format": [107, 1]}})
W("data/minecraft/tags/function/load.json", {"replace": False, "values": [f"{NS}:load"]})
W("data/minecraft/tags/function/tick.json", {"replace": False, "values": [f"{NS}:tick"]})

# ---------------------------------------------------------------- loot
def item(name, w, lo=1, hi=1):
    e = {"type": "minecraft:item", "name": f"minecraft:{name}", "weight": w}
    if hi > 1: e["functions"] = [{"function": "minecraft:set_count", "count": {"min": lo, "max": hi}}]
    return e
W(f"data/{NS}/loot_table/practice.json", {"type": "minecraft:chest", "pools": [{"rolls": 2, "entries": [
    item("experience_bottle", 6, 4, 8), item("emerald", 5, 2, 6), item("bread", 4, 2, 6), item("iron_ingot", 3, 1, 4)]}]})
FRAG = {"type": "minecraft:item", "name": "minecraft:echo_shard", "weight": 1,
        "functions": [{"function": "minecraft:set_name", "name": {"text": "Fragmento de Victoria", "color": "gold", "italic": False}}]}
W(f"data/{NS}/loot_table/contract.json", {"type": "minecraft:chest", "pools": [{"rolls": 3, "entries": [
    item("experience_bottle", 6, 8, 16), item("emerald", 6, 8, 18), item("diamond", 2, 1, 2), FRAG]}]})

# ---------------------------------------------------------------- load
F("load", [
    "scoreboard objectives add so_ar dummy",
    "scoreboard objectives add arena trigger",
    "scoreboard objectives add arena_pr trigger",
    "scoreboard objectives add arena_con trigger",
    "scoreboard objectives add levelrank trigger",
    "scoreboard objectives add so_ar_air dummy",
    "scoreboard objectives add so_ar_rank dummy",
    "execute unless score #enabled so_ar matches 0..1 run scoreboard players set #enabled so_ar 1",
    "execute unless score #mode so_ar matches 0..4 run scoreboard players set #mode so_ar 0",
    "execute unless score #beat so_ar matches 0.. run scoreboard players set #beat so_ar 0",
    f"bossbar add {NS}:fight {T({'text': 'Coliseo'})}",
    f"bossbar set {NS}:fight color red", f"bossbar set {NS}:fight max 100",
    f"bossbar set {NS}:fight visible false",
    f"tellraw @a[tag=oneblock_admin] {T({'text': '[SO Arenas] ', 'color': 'gold'}, {'text': 'cargado. Ayuda: /function so_arenas:admin/help', 'color': 'gray'})}",
])
F("tick", [
    "scoreboard players add #beat so_ar 1",
    f"execute if score #beat so_ar matches 20.. run function {NS}:lib/second",
    "execute if score #beat so_ar matches 20.. run scoreboard players set #beat so_ar 0",
])
F("lib/second", [
    "# Marca de presencia dentro del coliseo (por segundo).",
    "tag @a[tag=so_ar_in] remove so_ar_in",
    f"execute as @a[x={CX - AX - 4},y={FLOOR - 2},z={CZ - BZ - 4},dx={2 * AX + 8},dy={TOP_Y - FLOOR},dz={2 * BZ + 8}] run tag @s add so_ar_in",
    "# Retagea los mobs de so_events que quedaron dentro del coliseo para no pisar eventos de la isla.",
    f'execute as @e[tag=so_ev_mob,tag=!so_ar_mob,x={CX - AX},y={FLOOR - 1},z={CZ - BZ},dx={2 * AX},dy={TOP_Y - FLOOR},dz={2 * BZ}] run tag @s add so_ar_mob',
    "execute as @a[scores={levelrank=1..}] run function so_arenas:lib/rank",
    "scoreboard players reset @a levelrank", "scoreboard players enable @a levelrank",
    f"execute if score #mode so_ar matches 1 run function {NS}:mode/practice/second",
    f"execute if score #mode so_ar matches 2 run function {NS}:mode/caza/second",
    f"execute if score #mode so_ar matches 3 run function {NS}:mode/defensa/second",
    f"execute if score #mode so_ar matches 1..3 run function {NS}:lib/watch",
    f"execute unless score #mode so_ar matches 1..3 run function {NS}:lib/idle",
])

# ---------------------------------------------------------------- viaje
F("lib/go", [
    f'execute if score #enabled so_ar matches 0 run return run {say("@s", "La arena está desactivada por un administrador.", "red")}',
    f"execute if entity @s[tag=so_ar_in] run return run dialog show @s {NS}:main",
    f'tp @s {CX} {FLOOR + 2} {CZ + 62}',
    "effect give @s minecraft:resistance 3 4 true",
    f'title @s title {T({"text": "Coliseo VorNeX", "color": "gold", "bold": True})}',
    f'subtitle @s subtitle {T({"text": "Habla con los aldeanos o abre el menú.", "color": "gray"})}',
    "playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1",
    f"dialog show @s {NS}:main",
])
F("lib/volver", [
    f'execute if score #mode so_ar matches 1..3 if entity @s[tag=so_ar_in] run return run function {NS}:lib/abandono',
    f'tp @s 0 70 2',
    "effect give @s minecraft:slow_falling 5 0 true",
    "effect give @s minecraft:resistance 3 4 true",
    f"title @s actionbar {T({'text': 'De vuelta a la isla.', 'color': 'green'})}",
])
F("lib/abandono", [
    "# El jugador huyó en pleno desafío.",
    f"function {NS}:lib/end",
    f'title @s title {T({"text": "¡ABANDONASTE,", "color": "red", "bold": True}, {"text": " CAGÓN!", "color": "dark_red", "bold": True})}',
    "title @s times 0 60 20",
    "playsound minecraft:entity.villager.no hostile @s ~ ~ ~ 1 0.7",
    "playsound minecraft:ui.toast.challenge_failed master @s ~ ~ ~ 1 0.9",
    f'execute positioned {CX} {FLOOR} {CZ} run summon minecraft:wind_charge ~ ~2 ~',
    f'execute positioned {CX} {FLOOR} {CZ} as @s run tellraw @s {T(PFX, {"text": "Ya podés volver a la isla con ", "color": "gray", "bold": False}, {"text": "/trigger volver", "color": "yellow", "bold": True})}',
])
F("lib/end", [
    "# Fin de desafio: limpia mobs del coliseo, núcleo, barras y kits prestados.",
    "tp @e[tag=so_ar_mob] -5000 -300 -5000",
    "kill @e[tag=so_ar_mob]",
    f'setblock {CX} {FLOOR} {CZ} minecraft:air',
    f"bossbar set {NS}:fight visible false",
    "tag @a[tag=so_ar_loan] remove so_ar_loan",
    "execute as @a[tag=so_ar_loan] run clear @s stone_sword[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s leather_helmet[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s leather_chestplate[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s leather_leggings[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s leather_boots[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s iron_chestplate[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s bow[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s arrow[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s bread[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s crossbow[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s iron_sword[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s diamond_sword[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s golden_apple[minecraft:custom_data={so_arena_loan:1b}]",
    "execute as @a[tag=so_ar_loan] run clear @s splash_potion[minecraft:custom_data={so_arena_loan:1b}]",
    "tag @a[tag=so_ar_loan] remove so_ar_loan",
    "scoreboard players set #mode so_ar 0", "scoreboard players set #wave so_ar 0",
    "scoreboard players set #t so_ar 0", "scoreboard players set #anticamp so_ar 1",
    "scoreboard players reset @a so_ar_air",
])
F("lib/watch", [
    "# Nadie vivo dentro del coliseo con desafío activo = fin sin recompensa.",
    f"execute unless entity {IN} run function {NS}:lib/vacio",
])
F("lib/vacio", [
    f"function {NS}:lib/end",
    say("@a", "El desafío terminó: ya no quedaba nadie en el coliseo.", "gray"),
])
F("lib/idle", [
    "# Pista en el lobby.",
    f'execute as @a[x={CX - 7},y={FLOOR - 1},z={CZ + 60},dx=14,dy=8,dz=20] run title @s actionbar {T({"text": "Aldeanos del lobby: menú táctil o /trigger arena", "color": "gray"})}',
])
F("lib/rank", [
    "# Rangos ocultos: solo se ven con /trigger levelrank.",
    'scoreboard players operation #c so_ar = @s so_ar_rank',
    f'execute if score #c so_ar matches ..2 run tellraw @s {T(PFX, {"text": "Rango: ", "color": "gray", "bold": False}, {"text": "Recluta (C)", "color": "white", "bold": True}, {"text": " · Contratos completados: ", "color": "gray"}, {"score": {"name": "@s", "objective": "so_ar_rank"}, "color": "white"})}',
    f'execute if score #c so_ar matches 3..5 run tellraw @s {T(PFX, {"text": "Rango: ", "color": "gray", "bold": False}, {"text": "Veterano (B)", "color": "green", "bold": True}, {"text": " · Contratos completados: ", "color": "gray"}, {"score": {"name": "@s", "objective": "so_ar_rank"}, "color": "white"})}',
    f'execute if score #c so_ar matches 6..9 run tellraw @s {T(PFX, {"text": "Rango: ", "color": "gray", "bold": False}, {"text": "Élite (A)", "color": "aqua", "bold": True}, {"text": " · Contratos completados: ", "color": "gray"}, {"score": {"name": "@s", "objective": "so_ar_rank"}, "color": "white"})}',
    f'execute if score #c so_ar matches 10.. run tellraw @s {T(PFX, {"text": "Rango: ", "color": "gray", "bold": False}, {"text": "Leyenda (S)", "color": "gold", "bold": True}, {"text": " · Contratos completados: ", "color": "gray"}, {"score": {"name": "@s", "objective": "so_ar_rank"}, "color": "white"})}',
    say("@s", "Próximo rango: 3 / 6 / 10 contratos completados según el nivel.", "gray"),
])

# ---------------------------------------------------------------- despacho de triggers
F("lib/dispatch", [
    f"execute if score @s arena matches 1 run function {NS}:lib/go",
    f"execute if score @s arena matches 2 run function {NS}:lib/volver",
    f"execute if score @s arena_pr matches 1..14 run function {NS}:lib/start_pr",
    f"execute if score @s arena_con matches 1..3 run function {NS}:lib/start_con",
    "scoreboard players reset @a arena", "scoreboard players reset @a arena_pr", "scoreboard players reset @a arena_con",
    "scoreboard players enable @a arena", "scoreboard players enable @a arena_pr",
    "scoreboard players enable @a arena_con", "scoreboard players enable @a levelrank",
])

# ---------------------------------------------------------------- lectores de progreso
F("lib/blocks", [
    "scoreboard players set #blk so_ar 0",
    "execute if score fake_player ib_minedcount matches -2147483648.. run scoreboard players operation #blk so_ar = fake_player ib_minedcount",
    "execute if score #blocks so_core matches -2147483648.. run scoreboard players operation #blk so_ar = #blocks so_core",
])
TIERS = [  # tier: (nombre, mobs de oleada, bloques minimos, kit)
    (1, "Novato", ["zombie", "skeleton", "spider", "husk"], 0, "cuero"),
    (2, "Veterano", ["zombie_armor", "skeleton_armor", "piglin", "cave_spider", "slime_big"], 3334, "hierro"),
    (3, "Élite", ["vindicator", "pillager", "witch", "drowned_trident", "spider_big"], 7501, "diamante"),
    (4, "Maestro", ["enderman", "breeze", "zombie_ominous", "skeleton_ominous", "bogged", "wither_skeleton"], 15000, "avanzado"),
]
def mob_fn(m): return f'so_events:api/mob {{id:"{m}"}}'

F("lib/start_pr", [
    f"execute unless score #mode so_ar matches 0 run return run {say('@s', 'Ya hay un desafío en curso en el coliseo.', 'red')}",
    f"function {NS}:lib/blocks",
    f"execute unless score #blk so_ar matches 3334.. if score @s arena_pr matches 2.. if score @s arena_pr matches 12.. run return run {say('@s', 'Tier Veterano se desbloquea a los 3.334 bloques.', 'red')}",
    f"execute unless score #blk so_ar matches 7501.. if score @s arena_pr matches 3..13 run return run {say('@s', 'Tier Élite se desbloquea a los 7.501 bloques.', 'red')}",
    f"execute unless score #blk so_ar matches 15000.. if score @s arena_pr matches 4..14 run return run {say('@s', 'Tier Maestro se desbloquea en el After Phase (15.000).', 'red')}",
    "# Identifica tier (1-4) y si usa kit prestado (1-4) o equipo propio (11-14).",
    "scoreboard players operation #tier so_ar = @s arena_pr",
    "execute if score @s arena_pr matches 11..14 run scoreboard players remove #tier so_ar 10",
    "execute if score @s arena_pr matches 11..14 run scoreboard players set #loan so_ar 0",
    "execute unless score @s arena_pr matches 11..14 run scoreboard players set #loan so_ar 1",
    "scoreboard players reset @s arena_pr",
    f'execute if score #loan so_ar matches 1 run function {NS}:lib/kit',
    f'execute positioned {CX} {FLOOR} {CZ} run function {NS}:lib/enter',
    f"scoreboard players set #mode so_ar 1",
    "scoreboard players set #wave so_ar 0", "scoreboard players set #t so_ar 0",
    f'bossbar set {NS}:fight name {T({"text": "Práctica", "color": "yellow"})}',
    f"bossbar set {NS}:fight color yellow", f"bossbar set {NS}:fight max 2", f"bossbar set {NS}:fight value 0",
    f"bossbar set {NS}:fight players {IN}", f"bossbar set {NS}:fight visible true",
    f'execute as {IN} run title @s title {T({"text": "¡Práctica!", "color": "yellow", "bold": True})}',
    say("@a", "La práctica comienza: 2 oleadas. ¡Golpe, esquiva y sobreviví!", "yellow"),
    f"function {NS}:mode/practice/wave",
])
F("lib/kit", [
    "# Kit prestado según tier. Todos los ítems llevan marca so_arena_loan (no salen del coliseo).",
    f'execute if score #tier so_ar matches 1 run give @s stone_sword[minecraft:custom_data={{so_arena_loan:1b}},minecraft:custom_name={{text:"Kit de Práctica",color:"yellow",italic:false}}]',
    f'execute if score #tier so_ar matches 1 run give @s leather_helmet[minecraft:custom_data={{so_arena_loan:1b}}]',
    f'execute if score #tier so_ar matches 1 run give @s leather_chestplate[minecraft:custom_data={{so_arena_loan:1b}}]',
    f'execute if score #tier so_ar matches 1 run give @s leather_leggings[minecraft:custom_data={{so_arena_loan:1b}}]',
    f'execute if score #tier so_ar matches 1 run give @s leather_boots[minecraft:custom_data={{so_arena_loan:1b}}]',
    f'execute if score #tier so_ar matches 1 run give @s bread[minecraft:custom_data={{so_arena_loan:1b}}] 8',
    f'execute if score #tier so_ar matches 2 run give @s iron_sword[minecraft:custom_data={{so_arena_loan:1b}},minecraft:custom_name={{text:"Kit de Práctica",color:"yellow",italic:false}}]',
    f'execute if score #tier so_ar matches 2 run give @s iron_chestplate[minecraft:custom_data={{so_arena_loan:1b}}]',
    f'execute if score #tier so_ar matches 2 run give @s leather_helmet[minecraft:custom_data={{so_arena_loan:1b}}]',
    f'execute if score #tier so_ar matches 2 run give @s bread[minecraft:custom_data={{so_arena_loan:1b}}] 8',
    f'execute if score #tier so_ar matches 2 run give @s bow[minecraft:custom_data={{so_arena_loan:1b}}]',
    f'execute if score #tier so_ar matches 2 run give @s arrow[minecraft:custom_data={{so_arena_loan:1b}}] 24',
    f'execute if score #tier so_ar matches 3 run give @s diamond_sword[minecraft:custom_data={{so_arena_loan:1b}},minecraft:custom_name={{text:"Kit de Práctica",color:"yellow",italic:false}}]',
    f'execute if score #tier so_ar matches 3 run give @s iron_chestplate[minecraft:custom_data={{so_arena_loan:1b}}]',
    f'execute if score #tier so_ar matches 3 run give @s iron_helmet[minecraft:custom_data={{so_arena_loan:1b}}]',
    f'execute if score #tier so_ar matches 3 run give @s bow[minecraft:custom_data={{so_arena_loan:1b}}]',
    f'execute if score #tier so_ar matches 3 run give @s arrow[minecraft:custom_data={{so_arena_loan:1b}}] 32',
    f'execute if score #tier so_ar matches 3 run give @s golden_apple[minecraft:custom_data={{so_arena_loan:1b}}] 2',
    f'execute if score #tier so_ar matches 4 run give @s diamond_sword[minecraft:custom_data={{so_arena_loan:1b}},minecraft:custom_name={{text:"Kit de Práctica",color:"yellow",italic:false}}]',
    f'execute if score #tier so_ar matches 4 run give @s golden_apple[minecraft:custom_data={{so_arena_loan:1b}}] 2',
    f'execute if score #tier so_ar matches 4 run give @s crossbow[minecraft:custom_data={{so_arena_loan:1b}}]',
    f'execute if score #tier so_ar matches 4 run give @s arrow[minecraft:custom_data={{so_arena_loan:1b}}] 48',
    "tag @s add so_ar_loan",
    f'execute if score #loan so_ar matches 1 run {say("@s", "Kit prestado entregado. Vuelve con el botón o /trigger volver al terminar (se retira solo).", "yellow")}',
    f'execute if score #loan so_ar matches 0 run {say("@s", "Entrás con tu propio equipo: si morís, lo recuperás al volver a la isla.", "yellow")}',
])
F("lib/enter", [
    "# Coloca a los participantes en el foso.",
    f'tp @a[tag=so_ar_loan] {CX} {FLOOR + 1} {CZ}',
    f'tp @a[tag=!so_ar_loan,scores={{arena_pr=1..}}] {CX} {FLOOR + 1} {CZ}',
    "effect give @s minecraft:resistance 2 3 true",
])
# dejo tags limpios tras tp: los participantes ya llevan so_ar_loan o eran quienes iniciaron
F("mode/practice/wave", [
    "scoreboard players add #wave so_ar 1",
    f"execute store result bossbar {NS}:fight value run scoreboard players get #wave so_ar",
    *[f"execute if score #tier so_ar matches {t} if score #wave so_ar matches {w} as {IN} at @s run function {NS}:lib/spawn_near {{m:\"{m}\"}}"
      for t, _, mobs, _, _ in TIERS for w, reps in ((1, 1), (2, 2)) for m in mobs for _ in range(reps)],
    f"playsound minecraft:entity.zombie.ambient hostile {IN} ~ ~ ~ 1 0.8",
])
F("mode/practice/second", [
    "scoreboard players add #t so_ar 1",
    "execute store result score #alive so_ar if entity @e[tag=so_ar_mob]",
    f"title {IN} actionbar {T({'text': 'Oleada ', 'color': 'yellow', 'bold': True}, {'score': {'name': '#wave', 'objective': 'so_ar'}, 'color': 'white'}, {'text': ' · enemigos: ', 'color': 'gray'}, {'score': {'name': '#alive', 'objective': 'so_ar'}, 'color': 'white'})}",
    f"execute if score #alive so_ar matches 0 if score #wave so_ar matches 1 run function {NS}:mode/practice/wave",
    f"execute if score #alive so_ar matches 0 if score #wave so_ar matches 2.. run function {NS}:lib/win_practice",
    f"execute if score #t so_ar matches 300.. run function {NS}:lib/fail_practice",
])
F("lib/win_practice", [
    f"execute as {IN} run loot give @s loot {NS}:practice",
    f"title {IN} title {T({'text': '¡Victoria!', 'color': 'green', 'bold': True})}",
    say("@a", "Práctica superada. La recompensa ya es de ustedes.", "green"),
    f"function {NS}:lib/celebrar",
    f"function {NS}:lib/end",
    say("@a", "Ya podés volver a la isla con /trigger volver.", "gray"),
])
F("lib/fail_practice", [
    say("@a", "La práctica se canceló por tiempo.", "gray"),
    f"function {NS}:lib/end",
])

# ---------------------------------------------------------------- caza (contratos 1 y 2)
F("lib/start_con", [
    f"execute unless score #mode so_ar matches 0 run return run {say('@s', 'Ya hay un desafío en curso en el coliseo.', 'red')}",
    f"function {NS}:lib/blocks",
    f"execute unless score #blk so_ar matches 400.. run return run {say('@s', 'Los contratos se abren a los 400 bloques: preparate en la isla o entrá a la práctica.', 'red')}",
    f"execute unless score #blk so_ar matches 2501.. if score @s arena_con matches 3 run return run {say('@s', 'El contrato de defensa se desbloquea a los 2.501 bloques.', 'red')}",
    "scoreboard players operation #con so_ar = @s arena_con",
    "scoreboard players reset @s arena_con",
    f"execute if score #con so_ar matches 1 run function {NS}:mode/caza/start",
    f"execute if score #con so_ar matches 2 run function {NS}:mode/caza2/start",
    f"execute if score #con so_ar matches 3 run function {NS}:mode/defensa/start",
])
CAZA = {  # bloques minimos: (objetivos x5 = 18, apoyo)
    0: (["zombie", "husk", "skeleton", "spider"], ["skeleton", "spider"]),
    3334: (["zombie_armor", "piglin", "bogged", "cave_spider"], ["witch", "skeleton_armor"]),
    7501: (["vindicator", "pillager", "witch", "drowned_trident"], ["spider_big", "skeleton_ominous"]),
    15000: (["zombie_ominous", "breeze", "bogged", "enderman"], ["shulker", "skeleton_ominous"]),
}
def caza_targets():
    thrs = list(CAZA)
    out = []
    for i, thr in enumerate(thrs):
        cond = f"execute if score #blk so_ar matches {thr}.."
        if i < len(thrs) - 1:
            cond += f" unless score #blk so_ar matches {thrs[i + 1]}.."
        for m in CAZA[thr][0] * 5:
            out.append(f'{cond} as @a[tag=so_ar_in,limit=1,sort=random] at @s run function {NS}:lib/spawn_near {{m:"{m}"}}')
    return out
F("mode/caza/start", [f"function {NS}:lib/enter_con",
    "scoreboard players set #mode so_ar 2", "scoreboard players set #t so_ar 0",
    f'bossbar set {NS}:fight name {T({"text": "Caza: 15 bajas", "color": "aqua"})}',
    f"bossbar set {NS}:fight color aqua", f"bossbar set {NS}:fight max 15", f"bossbar set {NS}:fight value 0",
    f"bossbar set {NS}:fight players {IN}", f"bossbar set {NS}:fight visible true",
    f'execute as {IN} run title @s title {T({"text": "¡Caza de monstruos!", "color": "aqua", "bold": True})}',
    say("@a", "Contrato: 15 bajas objetivo. Los molestos de apoyo son extra.", "aqua"),
    *caza_targets(),
])
F("mode/caza2/start", [f"function {NS}:lib/enter_con",
    "scoreboard players set #mode so_ar 2", "scoreboard players set #t so_ar 0", "scoreboard players set #wave so_ar 0",
    f'bossbar set {NS}:fight name {T({"text": "Oleadas dobles", "color": "aqua"})}',
    f"bossbar set {NS}:fight color aqua", f"bossbar set {NS}:fight max 3", f"bossbar set {NS}:fight value 0",
    f"bossbar set {NS}:fight players {IN}", f"bossbar set {NS}:fight visible true",
    f'execute as {IN} run title @s title {T({"text": "¡Oleadas dobles!", "color": "aqua", "bold": True})}',
    say("@a", "Contrato: superá 3 oleadas mixtas.", "aqua"),
    f"function {NS}:mode/caza2/wave",
])
F("mode/caza2/wave", [
    "scoreboard players add #wave so_ar 1",
    f"execute store result bossbar {NS}:fight value run scoreboard players get #wave so_ar",
    *[f"execute if score #wave so_ar matches {w} as {IN} at @s run function {NS}:lib/spawn_near {{m:\"{m}\"}}"
      for m, reps in [("zombie_armor", 2), ("skeleton_armor", 2), ("pillager", 1), ("vindicator", 1), ("witch", 1), ("spider_big", 1)]
      for w in (1, 2, 3) for _ in range(reps)],
    f"playsound minecraft:entity.zombie.ambient hostile {IN} ~ ~ ~ 1 0.8",
])
F("mode/caza/second", [
    "scoreboard players add #t so_ar 1",
    f"execute unless entity @e[tag=so_ar_target,limit=3] run function {NS}:lib/win_contract",
    f"execute if score #t so_ar matches 420.. run function {NS}:lib/fail_contract",
    f"title {IN} actionbar {T({'text': 'Caza en curso: quedan ', 'color': 'aqua'}, {'score': {'name': '#alive', 'objective': 'so_ar'}, 'color': 'white', 'bold': True}, {'text': ' bajas objetivo', 'color': 'gray'})}",
    f"execute store result score #alive so_ar if entity @e[tag=so_ar_target,limit=4]",
    "execute unless entity @e[tag=so_ar_target,limit=4] run scoreboard players set #alive so_ar 3",
    f"execute store result bossbar {NS}:fight value run scoreboard players get #alive so_ar",
    "scoreboard players operation #m so_ar = #t so_ar", "scoreboard players operation #m so_ar %= #twentyfive so_ar",
    f'execute if score #m so_ar matches 1 as {IN.replace("]", ",limit=1,sort=random]")} at @s run function {NS}:lib/spawn_near {{m:"skeleton"}}',
    f'execute if score #m so_ar matches 1 as {IN.replace("]", ",limit=1,sort=random]")} at @s run function {NS}:lib/spawn_near {{m:"spider"}}',
])
F("mode/caza2/second", [
    "scoreboard players add #t so_ar 1",
    "execute store result score #alive so_ar if entity @e[tag=so_ar_mob]",
    f"title {IN} actionbar {T({'text': 'Oleada ', 'color': 'aqua', 'bold': True}, {'score': {'name': '#wave', 'objective': 'so_ar'}, 'color': 'white'}, {'text': ' · enemigos: ', 'color': 'gray'}, {'score': {'name': '#alive', 'objective': 'so_ar'}, 'color': 'white'})}",
    f"execute if score #alive so_ar matches 0 if score #wave so_ar matches 1..2 run function {NS}:mode/caza2/wave",
    f"execute if score #alive so_ar matches 0 if score #wave so_ar matches 3.. run function {NS}:lib/win_contract",
    f"execute if score #t so_ar matches 480.. run function {NS}:lib/fail_contract",
])
F("lib/win_contract", [
    f"execute as {IN} run loot give @s loot {NS}:contract",
    "scoreboard players add @a[tag=so_ar_in] so_ar_rank 1",
    f"title {IN} title {T({'text': '¡Contrato cumplido!', 'color': 'green', 'bold': True})}",
    say("@a", "¡Contrato cumplido! Esmeraldas, botellas de XP y un Fragmento de Victoria.", "green"),
    f"function {NS}:lib/celebrar", f"function {NS}:lib/end",
    say("@a", "Ya podés volver a la isla con /trigger volver.", "gray"),
])
F("lib/fail_contract", [
    say("@a", "El contrato se canceló por tiempo. Sin recompensa.", "gray"),
    f"function {NS}:lib/end",
])

# ---------------------------------------------------------------- defensa (contrato 3)
F("mode/defensa/start", [f"function {NS}:lib/enter_con",
    f"setblock {CX} {FLOOR} {CZ} minecraft:crying_obsidian",
    "scoreboard players set #mode so_ar 3", "scoreboard players set #t so_ar 0", "scoreboard players set #wave so_ar 0",
    "scoreboard players set #hp so_ar 100", "scoreboard players set #anticamp so_ar 0",
    f"bossbar set {NS}:fight color purple", f"bossbar set {NS}:fight max 100", f"bossbar set {NS}:fight value 100",
    f"bossbar set {NS}:fight players {IN}", f"bossbar set {NS}:fight visible true",
    f"execute as {IN} run title @s title {T({'text': '¡Defendan el Núcleo!', 'color': 'dark_purple', 'bold': True})}",
    say("@a", "Contrato: protegí el Núcleo 2 minutos. Aquí sí se puede usar la altura.", "dark_purple"),
    f"function {NS}:mode/defensa/wave",
])
F("mode/defensa/wave", [
    "scoreboard players add #wave so_ar 1",
    *[f"execute if score #wave so_ar matches {w} as {IN} at @s run function {NS}:lib/spawn_near {{m:\"{m}\"}}"
      for m, reps in [("zombie_armor", 2), ("skeleton_armor", 1), ("cave_spider", 1), ("bogged", 1), ("witch", 1)]
      for w in (1, 2, 3, 4, 5) for _ in range(reps)],
])
F("mode/defensa/second", [
    "scoreboard players add #t so_ar 1",
    f"execute positioned {CX} {FLOOR} {CZ} store result score #near so_ar if entity @e[tag=so_ar_mob,distance=..6]",
    f"execute if score #hp so_ar matches 1.. run scoreboard players operation #hp so_ar -= #near so_ar",
    f"execute if score #hp so_ar matches ..0 run function {NS}:lib/fail_contract",
    f"execute if score #hp so_ar matches 1.. run bossbar set {NS}:fight name {T({'text': 'Núcleo: ', 'color': 'dark_purple'}, {'score': {'name': '#hp', 'objective': 'so_ar'}, 'color': 'white', 'bold': True}, {'text': '%', 'color': 'gray'})}",
    f"execute if score #hp so_ar matches 1.. store result bossbar {NS}:fight value run scoreboard players get #hp so_ar",
    "scoreboard players operation #m so_ar = #t so_ar", "scoreboard players operation #m so_ar %= #twentyfive so_ar",
    f"execute if score #m so_ar matches 1 if score #wave so_ar matches ..5 run function {NS}:mode/defensa/wave",
    f"execute if score #t so_ar matches 120.. run function {NS}:lib/win_contract",
])

# ---------------------------------------------------------------- spawn, entrada y festejo
F("lib/spawn_near", [
    "# $(m): id de mob de so_events. Spawnea cerca del jugador sobre suelo firme.",
    "scoreboard players set #ok so_ar 0",
    "$data modify storage so_arenas:tmp m set value \"$(m)\"",
    *(["function so_arenas:lib/spawn_roll", "execute if score #ok so_ar matches 0 run function so_arenas:lib/spawn_try with storage so_arenas:tmp"] * 4),
    "execute if score #ok so_ar matches 0 run function so_arenas:lib/spawn_here with storage so_arenas:tmp",
])
F("lib/spawn_roll", [
    "execute store result storage so_arenas:tmp a int 1 run random value 0..359",
    "execute store result storage so_arenas:tmp d int 1 run random value 6..14",
])
F("lib/spawn_try", ["$execute rotated $(a) 0 positioned ^ ^ ^$(d) if block ~ ~ ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:api/mob {id:$(m)}"])
F("lib/spawn_here", ["$execute run function so_events:api/mob {id:$(m)}"])
F("lib/enter_con", [
    "tp @s -5000 97 -5000",
    "effect give @s minecraft:resistance 2 3 true",
    "scoreboard players set #loan so_ar 0",
])
F("lib/celebrar", [
    "# Fuegos artificiales desde las 8 torres.",
    *[f'summon minecraft:firework_rocket {x} 172 {z} {{LifeTime:20,FireworksItem:{{id:"minecraft:firework_rocket",count:1,components:{{"minecraft:fireworks":{{flight_duration:1,explosions:[{{shape:"large_ball",colors:[I;16750848,16711680,16776960],flicker:1b,trail:1b}}]}}}}}}}}'
      for x, z in [(CX + AX, CZ), (CX - AX, CZ), (CX, CZ + BZ), (CX, CZ - BZ),
                   (CX + 30, CZ + 35), (CX - 30, CZ + 35), (CX + 30, CZ - 35), (CX - 30, CZ - 35)]],
    "playsound minecraft:ui.toast.challenge_complete master @a ~ ~ ~ 1 1",
    "playsound minecraft:block.note_block.chime master @a ~ ~ ~ 1 1.2",
])
F("lib/anticamp", [
    "# Anti-camping por altura: 3 s sobre el foso (6 s en defensa) y el viento te baja.",
    f'execute as @a[tag=so_ar_in,scores={{so_ar_air=6..}}] at @s if score #anticamp so_ar matches 1 run summon minecraft:wind_charge ~ ~2 ~',
    f'execute as @a[tag=so_ar_in,scores={{so_ar_air=6..}}] at @s run title @s actionbar {T({"text": "¡El viento del coliseo te empuja al piso!", "color": "red", "bold": True})}',
    f'execute as @a[tag=so_ar_in,scores={{so_ar_air=6..}}] run scoreboard players set @s so_ar_air 0',
    "execute as @a[tag=so_ar_in] at @s if entity @s[y=104..] run scoreboard players add @s so_ar_air 1",
    "execute as @a[tag=so_ar_in] at @s unless entity @s[y=104..] run scoreboard players set @s so_ar_air 0",
])
