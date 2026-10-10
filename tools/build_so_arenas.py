#!/usr/bin/env python3
"""Generador de so_arenas v2 — el Coliseo VorNeX (lo donde pasa).

Unica fuente del datapack datapacks/so-arenas (no editar los .mcfunction a mano).
- Coliseo ovalado 84x100 centrado en -5000 96 -5000: foso, muro del foso, 8 filas de gradas
  macizas, muralla con ventanas, 8 torres hasta y=170, tunel con reja y lobby cerrado.
- Construccion blindada: forceload del area + pasos programados (schedule) para que cada
  /fill caiga sobre chunks cargados, sin depender de la distancia de renderizado.
- Viaje como so_crates: /trigger arena (guarda donde estabas) y /trigger volver (te devuelve).
- Menu por 4 vias: aldeanos con hitbox de interaccion (Java), carteles con clic (Java y
  Bedrock), placas del piso (Java y Bedrock), dialogos y menu del chat.
- Mercaderes reales en el lobby (comercio vanilla, funciona en Java y Bedrock).
- Enemigos de so_events:api/mob, retageados al instante a so_ar_mob (sin so_ev_mob) para que
  la limpieza de eventos de la isla no los toque y viceversa.
Salida: datapacks/so-arenas + /mnt/documents/so_arenas-v2.zip (raiz limpia).
"""
import json, os, shutil, zipfile, math, random

ROOT = os.path.join(os.path.dirname(__file__), "..", "datapacks", "so-arenas")
NS = "so_arenas"
CX, CZ = -5000, -5000
G = 95                 # bloque del piso; se camina en y=96
AX, BZ = 42, 50        # semiejes exteriores: 84 x 100
TOP_Y = 170
R_PIT, R_PITWALL, R_GRADA, R_WALL = 0.62, 0.65, 0.93, 1.0
LZ0, LZ1 = CZ + BZ + 10, CZ + BZ + 30      # lobby: muro norte / muro sur
LX = 11                                   # lobby: medio ancho (muros en CX±11)
ARR = (CX, 96, LZ1 - 6)                   # punto de llegada
PIT_IN = (CX, 96, CZ + 14)                # entrada al foso
# caja del foso (participantes) y de la zona completa (coliseo + lobby)
PIT_BOX = f"x={CX - 27},y=90,z={CZ - 32},dx=54,dy=50,dz=64"
ZONE_BOX = f"x={CX - 50},y=80,z={CZ - 58},dx=100,dy=130,dz={LZ1 - (CZ - 58) + 4}"
MOB_BOX = f"x={CX - 32},y=88,z={CZ - 38},dx=64,dy=60,dz=76"
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
ZONE = "@a[tag=so_ar_zone]"
LOAN = "*[minecraft:custom_data~{so_arena_loan:1b}]"

# ---------------------------------------------------------------- pack
W("pack.mcmeta", {"pack": {"description": "Simply OneBlock Expansion - Arenas v2 (/trigger arena)",
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
        "functions": [{"function": "minecraft:set_name", "target": "item_name",
                       "name": {"text": "Fragmento de Victoria", "color": "gold"}}]}
W(f"data/{NS}/loot_table/contract.json", {"type": "minecraft:chest", "pools": [{"rolls": 3, "entries": [
    item("experience_bottle", 6, 8, 16), item("emerald", 6, 8, 18), item("diamond", 2, 1, 2), FRAG]}]})

# ---------------------------------------------------------------- load / tick
TRIGGERS = ["arena", "volver", "arena_pr", "arena_con", "levelrank"]
F("load", [
    "scoreboard objectives add so_ar dummy",
    *[f"scoreboard objectives add {t} trigger" for t in TRIGGERS],
    "scoreboard objectives add so_ar_air dummy",
    "scoreboard objectives add so_ar_rank dummy",
    "scoreboard objectives add so_ar_x dummy", "scoreboard objectives add so_ar_y dummy",
    "scoreboard objectives add so_ar_z dummy", "scoreboard objectives add so_ar_saved dummy",
    "execute unless score #enabled so_ar matches 0..1 run scoreboard players set #enabled so_ar 1",
    "execute unless score #mode so_ar matches 0..3 run scoreboard players set #mode so_ar 0",
    "scoreboard players set #beat so_ar 0",
    "scoreboard players set #twentyfive so_ar 25",
    "scoreboard players set #anticamp so_ar 1",
    f"bossbar add {NS}:fight {T({'text': 'Coliseo'})}",
    f"bossbar set {NS}:fight max 100", f"bossbar set {NS}:fight visible false",
    f"tellraw @a[tag=oneblock_admin] {T({'text': '[SO Arenas] ', 'color': 'gold'}, {'text': 'v2 cargado. Ayuda: /function so_arenas:admin/help', 'color': 'gray'})}",
])
F("tick", [
    "scoreboard players add #beat so_ar 1",
    f"execute as @a[scores={{arena=1..}}] at @s run function {NS}:lib/go",
    f"execute as @a[scores={{volver=1..}}] at @s run function {NS}:lib/volver",
    f"execute as @a[scores={{arena_pr=1..}}] at @s run function {NS}:lib/start_pr",
    f"execute as @a[scores={{arena_con=1..}}] at @s run function {NS}:lib/start_con",
    f"execute as @a[scores={{levelrank=1..}}] run function {NS}:lib/rank",
    *[f"scoreboard players reset @a {t}" for t in TRIGGERS],
    *[f"scoreboard players enable @a {t}" for t in TRIGGERS],
    f"execute if score #beat so_ar matches 10 run function {NS}:lib/pads",
    f"execute if score #beat so_ar matches 20.. run function {NS}:lib/pads",
    f"execute if score #beat so_ar matches 20.. run function {NS}:lib/second",
    "execute if score #beat so_ar matches 20.. run scoreboard players set #beat so_ar 0",
])
F("lib/second", [
    "# Zona: quien sale (o muere y reaparece afuera) pierde marcas y kit; quien entra volando queda marcado.",
    f"execute as {ZONE} at @s unless dimension minecraft:overworld run function {NS}:lib/leave",
    f"execute as {ZONE} at @s unless entity @s[{ZONE_BOX}] run function {NS}:lib/leave",
    f"execute as @a[tag=!so_ar_zone,{ZONE_BOX}] at @s if dimension minecraft:overworld run function {NS}:lib/enter_zone",
    "# Participantes: quienes están dentro del foso.",
    "tag @a remove so_ar_in",
    f"execute as @a[tag=so_ar_zone,{PIT_BOX}] run tag @s add so_ar_in",
    "# Kits prestados tirados al piso: se borran (no se exportan).",
    f"kill @e[type=minecraft:item,{ZONE_BOX},nbt={{Item:{{components:{{\"minecraft:custom_data\":{{so_arena_loan:1b}}}}}}}}]",
    f"execute if score #mode so_ar matches 1 run function {NS}:mode/practice/second",
    f"execute if score #mode so_ar matches 2 run function {NS}:mode/caza/second",
    f"execute if score #mode so_ar matches 4 run function {NS}:mode/caza2/second",
    f"execute if score #mode so_ar matches 3 run function {NS}:mode/defensa/second",
    f"execute if score #mode so_ar matches 1.. if score #anticamp so_ar matches 1 run function {NS}:lib/anticamp",
    f"execute if score #mode so_ar matches 1.. unless entity {IN} run function {NS}:lib/vacio",
    f"execute if score #mode so_ar matches 0 as @a[tag=so_ar_zone,tag=!so_ar_in] run title @s actionbar {T({'text': 'Menú: aldeanos, carteles, placas del piso o /trigger arena', 'color': 'gray'})}",
])

# ---------------------------------------------------------------- viaje (igual que so_crates)
F("lib/go", [
    f"execute if score @s arena matches 2 run return run function {NS}:lib/volver",
    f'execute if score #enabled so_ar matches 0 run return run {say("@s", "La arena está desactivada por un administrador.", "red")}',
    f"execute if entity @s[tag=so_ar_zone] run return run function {NS}:lib/menu",
    f'execute unless dimension minecraft:overworld run return run {say("@s", "Solo podés viajar desde el mundo normal (no desde el Nether, el End ni las fases).", "red")}',
    "execute store result score @s so_ar_x run data get entity @s Pos[0]",
    "execute store result score @s so_ar_y run data get entity @s Pos[1]",
    "execute store result score @s so_ar_z run data get entity @s Pos[2]",
    "scoreboard players set @s so_ar_saved 1",
    f"tp @s {ARR[0]} {ARR[1]} {ARR[2]} 180 0",
    f"function {NS}:lib/enter_zone",
    "effect give @s minecraft:resistance 3 4 true",
    f'title @s title {T({"text": "Coliseo VorNeX", "color": "gold", "bold": True})}',
    f'title @s subtitle {T({"text": "Aldeanos, carteles o placas del piso", "color": "gray"})}',
    "playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1",
    f"function {NS}:lib/menu",
])
F("lib/enter_zone", [
    "tag @s add so_ar_zone",
    "execute unless entity @s[tag=oneblock_admin] if entity @s[gamemode=survival] run tag @s add so_ar_gm",
    "execute if entity @s[tag=so_ar_gm] run gamemode adventure @s",
])
F("lib/leave", [
    "tag @s remove so_ar_zone", "tag @s remove so_ar_in", "tag @s remove so_ar_pad",
    f"clear @s {LOAN}",
    "tag @s remove so_ar_loan",
    "execute if entity @s[tag=so_ar_gm,gamemode=adventure] run gamemode survival @s",
    "tag @s remove so_ar_gm",
    "scoreboard players reset @s so_ar_air",
])
F("lib/volver", [
    f'execute unless entity @s[tag=so_ar_zone] run return run {say("@s", "Este comando solo funciona dentro del Coliseo. Para ir: /trigger arena", "red")}',
    f"execute if score #mode so_ar matches 1.. if entity @s[tag=so_ar_in] run function {NS}:lib/abandono",
    f"function {NS}:lib/leave",
    "execute store result storage so_arenas:tmp x int 1 run scoreboard players get @s so_ar_x",
    "execute store result storage so_arenas:tmp y int 1 run scoreboard players get @s so_ar_y",
    "execute store result storage so_arenas:tmp z int 1 run scoreboard players get @s so_ar_z",
    f"execute if score @s so_ar_saved matches 1 run function {NS}:lib/back_tp with storage so_arenas:tmp",
    "execute unless score @s so_ar_saved matches 1 in minecraft:overworld run tp @s 0 65 0",
    "scoreboard players reset @s so_ar_saved",
    "effect give @s minecraft:slow_falling 5 0 true",
    "execute at @s run playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1",
    f"title @s actionbar {T({'text': 'De vuelta a la isla.', 'color': 'green'})}",
])
F("lib/back_tp", ["$execute in minecraft:overworld run tp @s $(x) $(y) $(z)"])
F("lib/abandono", [
    "# Huyó en pleno desafío: pierde recompensa y kit. El resto sigue peleando.",
    f'title @s title {T({"text": "¡ABANDONASTE,", "color": "red", "bold": True}, {"text": " CAGÓN!", "color": "dark_red", "bold": True})}',
    "title @s times 0 60 20",
    "playsound minecraft:entity.villager.no master @s ~ ~ ~ 1 0.7",
    say("@a[tag=so_ar_zone]", "Un gladiador abandonó el desafío.", "red"),
])
F("lib/menu", [
    f"dialog show @s {NS}:main",
    f"function {NS}:lib/chat_main",
])


# ---------------------------------------------------------------- menú del chat (Java)
def link(label, cmd, color, tip):
    return {"text": label, "color": color, "click_event": {"action": "run_command", "command": cmd},
            "hover_event": {"action": "show_text", "value": tip}}


F("lib/chat_main", [
    f"tellraw @s {T({'text': '━━━ Coliseo VorNeX ━━━', 'color': 'gold', 'bold': True})}",
    f"tellraw @s {T({'text': ' Práctica: ', 'color': 'gray'}, *[x for t in range(1, 5) for x in (link(f'[T{t}]', f'/trigger arena_pr set {t}', 'yellow', f'Tier {t} con kit prestado'), link(f'[T{t}+propio] ', f'/trigger arena_pr set {t + 10}', 'gold', f'Tier {t} con tu equipo'))])}",
    f"tellraw @s {T({'text': ' Contratos: ', 'color': 'gray'}, link('[Caza] ', '/trigger arena_con set 1', 'aqua', '15 bajas objetivo (400+)'), link('[Oleadas] ', '/trigger arena_con set 2', 'aqua', '3 oleadas (400+)'), link('[Defensa] ', '/trigger arena_con set 3', 'aqua', 'Proteger el Núcleo (2.501+)'))}",
    f"tellraw @s {T({'text': ' ', 'color': 'gray'}, link('[Unirse al desafío] ', '/trigger arena_con set 9', 'green', 'Entrar al foso si hay un desafío en curso'), link('[Mi rango] ', '/trigger levelrank', 'gray', 'Rango oculto'), link('[Volver a la isla]', '/trigger volver', 'red', 'Salir (si hay desafío: abandono)'))}",
])

# ---------------------------------------------------------------- placas del piso (Java y Bedrock)
PADS = [  # (x, acción, etiqueta, color de concreto)
    (CX - 3, "pad_pr", "Práctica", "yellow"),
    (CX - 1, "pad_con", "Contratos", "light_blue"),
    (CX + 1, "pad_join", "Unirse", "lime"),
    (CX + 3, "pad_back", "Volver", "red"),
]
PAD_Z = LZ0 + 9
F("lib/pads", [
    f"execute as @a[tag=so_ar_pad] at @s unless block ~ ~ ~ minecraft:light_weighted_pressure_plate run tag @s remove so_ar_pad",
    *[f"execute as @a[tag=so_ar_zone,tag=!so_ar_pad,x={x},y=96,z={PAD_Z},dx=0,dy=0,dz=0] run function {NS}:lib/{fn}" for x, fn, _, _ in PADS],
])
F("lib/pad_pr", ["tag @s add so_ar_pad", f"dialog show @s {NS}:practice", f"function {NS}:lib/chat_main",
                 "playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.4"])
F("lib/pad_con", ["tag @s add so_ar_pad", f"dialog show @s {NS}:contracts", f"function {NS}:lib/chat_main",
                  "playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.4"])
F("lib/pad_join", ["tag @s add so_ar_pad", f"function {NS}:lib/join"])
F("lib/pad_back", ["tag @s add so_ar_pad", f"function {NS}:lib/volver"])

# ---------------------------------------------------------------- aldeanos con menú (hitbox de interacción)
NPCS = [  # (id, nombre, color, x, z, acción)
    ("main", "Guía del Coliseo", "gold", CX, LZ1 - 2, [f"function {NS}:lib/menu"]),
    ("pr", "Maestro de Armas", "yellow", CX - 7, LZ0 + 4, [f"dialog show @s {NS}:practice", f"function {NS}:lib/chat_main"]),
    ("con", "Comandante de Contratos", "aqua", CX + 7, LZ0 + 4, [f"dialog show @s {NS}:contracts", f"function {NS}:lib/chat_main"]),
]
for nid, _, _, _, _, acts in NPCS:
    W(f"data/{NS}/advancement/npc/{nid}.json", {
        "criteria": {"click": {"trigger": "minecraft:player_interacted_with_entity", "conditions": {
            "entity": [{"condition": "minecraft:entity_properties", "entity": "this",
                        "predicate": {"nbt": f"{{Tags:[\"so_ar_npc_{nid}\"]}}"}}]}}},
        "rewards": {"function": f"{NS}:npc/{nid}"}})
    F(f"npc/{nid}", [f"advancement revoke @s only {NS}:npc/{nid}",
                     "playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1", *acts])

# mercaderes reales: comercio vanilla
def offer(cost, sid, count=1, comp=None, uses=999999):
    s = f'{{id:"minecraft:{sid}",count:{count}' + (f",components:{{{comp}}}" if comp else "") + "}"
    return f'{{buy:{{id:"minecraft:emerald",count:{cost}}},sell:{s},maxUses:{uses},rewardExp:0b}}'


def potion(cost, item_id, p):
    return offer(cost, item_id, 1, f'"minecraft:potion_contents":{{potion:"minecraft:{p}"}}')


TRADERS = [
    ("Intendente del Coliseo", "green", CX - 7, LZ1 - 4, [
        offer(2, "arrow", 16), offer(3, "spectral_arrow", 8), offer(2, "cooked_beef", 8),
        offer(8, "golden_apple", 2), potion(4, "splash_potion", "strong_healing"),
        potion(5, "splash_potion", "regeneration"), potion(6, "splash_potion", "strength"),
        potion(4, "splash_potion", "fire_resistance"), potion(4, "splash_potion", "swiftness"),
    ]),
    ("Armero del Coliseo", "red", CX + 7, LZ1 - 4, [
        offer(4, "shield"), offer(24, "totem_of_undying"), offer(20, "iron_golem_spawn_egg"),
        offer(8, "snow_golem_spawn_egg"), offer(8, "ender_pearl"), offer(3, "firework_rocket", 8),
        offer(6, "crossbow"), offer(5, "bow"), offer(1, "snowball", 16),
    ]),
]


def npc_summons():
    out = [f"kill @e[tag=so_ar_npc,{ZONE_BOX}]"]
    for nid, name, color, x, z, _ in NPCS:
        out.append(f'summon minecraft:villager {x} 96 {z} {{Tags:["so_ar_npc"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomNameVisible:1b,CustomName:{{text:"{name}",color:"{color}",bold:true}}}}')
        out.append(f'summon minecraft:interaction {x} 96 {z} {{Tags:["so_ar_npc","so_ar_npc_{nid}"],width:1.0f,height:2.1f,response:1b}}')
    for name, color, x, z, offers in TRADERS:
        out.append(f'summon minecraft:wandering_trader {x} 96 {z} {{Tags:["so_ar_npc"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,DespawnDelay:0,CustomNameVisible:1b,CustomName:{{text:"{name}",color:"{color}",bold:true}},Offers:{{Recipes:[{",".join(offers)}]}}}}')
    return out


# ---------------------------------------------------------------- rango
F("lib/rank", [
    "# Rangos ocultos: solo se ven con /trigger levelrank.",
    "scoreboard players operation #c so_ar = @s so_ar_rank",
    "execute unless score #c so_ar matches 0.. run scoreboard players set #c so_ar 0",
    *[f'execute if score #c so_ar matches {rng} run tellraw @s {T(PFX, {"text": "Rango: ", "color": "gray", "bold": False}, {"text": n, "color": c, "bold": True}, {"text": " · Contratos cumplidos: ", "color": "gray", "bold": False}, {"score": {"name": "#c", "objective": "so_ar"}, "color": "white"})}'
      for rng, n, c in [("..2", "Recluta (C)", "white"), ("3..5", "Veterano (B)", "green"), ("6..9", "Élite (A)", "aqua"), ("10..", "Leyenda (S)", "gold")]],
    say("@s", "Próximos rangos: 3 / 6 / 10 contratos cumplidos.", "gray"),
])

# ---------------------------------------------------------------- progreso
F("lib/blocks", [
    "scoreboard players set #blk so_ar 0",
    "execute if score fake_player ib_minedcount matches -2147483648.. run scoreboard players operation #blk so_ar = fake_player ib_minedcount",
    "execute if score #blocks so_core matches -2147483648.. run scoreboard players operation #blk so_ar = #blocks so_core",
    "# modo prueba admin: bloques simulados",
    "execute if score #fake so_ar matches 0.. run scoreboard players operation #blk so_ar = #fake so_ar",
])
TIERS = [  # (tier, nombre, mobs, bloques mínimos)
    (1, "Novato", ["zombie", "skeleton", "spider", "husk"], 0),
    (2, "Veterano", ["zombie_armor", "skeleton_armor", "piglin", "cave_spider", "slime_big"], 3334),
    (3, "Élite", ["vindicator", "pillager", "witch", "drowned_trident", "spider_big"], 7501),
    (4, "Maestro", ["enderman", "breeze", "zombie_ominous", "skeleton_ominous", "bogged", "wither_skeleton"], 15000),
]


def spawn(m, t=0):
    return f'function {NS}:lib/spawn {{m:"{m}",t:{t}}}'


def busy_guard():
    return [
        f'execute unless entity @s[tag=so_ar_zone] run return run {say("@s", "Primero entrá al Coliseo con /trigger arena.", "red")}',
        f'execute unless score #mode so_ar matches 0 run return run {say("@s", "Ya hay un desafío en curso. Podés unirte con el botón Unirse.", "red")}',
    ]


F("lib/start_pr", [
    *busy_guard(),
    f"function {NS}:lib/blocks",
    "scoreboard players operation #tier so_ar = @s arena_pr",
    "execute if score #tier so_ar matches 11..14 run scoreboard players remove #tier so_ar 10",
    "scoreboard players set #loan so_ar 1",
    "execute if score @s arena_pr matches 11..14 run scoreboard players set #loan so_ar 0",
    f'execute unless score #tier so_ar matches 1..4 run return run {say("@s", "Opción de práctica inválida.", "red")}',
    *[f'execute if score #tier so_ar matches {t} unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches {thr}.. run return run {say("@s", f"El Tier {n} se desbloquea a los {thr:,} bloques.".replace(",", "."), "red")}'
      for t, n, _, thr in TIERS if thr > 0],
    f"execute if score #loan so_ar matches 1 run function {NS}:lib/kit",
    f'execute if score #loan so_ar matches 0 run {say("@s", "Entrás con tu propio equipo: si morís, tus cosas quedan en el foso.", "yellow")}',
    f"function {NS}:lib/enter_pit",
    "scoreboard players set #mode so_ar 1",
    "scoreboard players set #wave so_ar 0", "scoreboard players set #t so_ar 0", "scoreboard players set #anticamp so_ar 1",
    f'bossbar set {NS}:fight name {T({"text": "Práctica", "color": "yellow"})}',
    f"bossbar set {NS}:fight color yellow", f"bossbar set {NS}:fight max 2", f"bossbar set {NS}:fight value 0",
    f"bossbar set {NS}:fight players {IN}", f"bossbar set {NS}:fight visible true",
    f'title @s title {T({"text": "¡Práctica!", "color": "yellow", "bold": True})}',
    say(ZONE, "La práctica comienza: 2 oleadas. ¡Golpeá, esquivá y sobreviví!", "yellow"),
    f"function {NS}:mode/practice/wave",
])
KIT = {
    1: ["stone_sword", "leather_helmet", "leather_chestplate", "leather_leggings", "leather_boots", ("bread", 8)],
    2: ["iron_sword", "iron_chestplate", "leather_helmet", "leather_leggings", "bow", ("arrow", 24), ("bread", 8)],
    3: ["diamond_sword", "iron_helmet", "iron_chestplate", "iron_leggings", "iron_boots", "shield", "bow", ("arrow", 32), ("golden_apple", 2)],
    4: ["diamond_sword", "diamond_helmet", "diamond_chestplate", "iron_leggings", "iron_boots", "shield", "crossbow", ("arrow", 48), ("golden_apple", 3)],
}
F("lib/kit", [
    "# Kit prestado: todo lleva so_arena_loan y se borra al salir, terminar o tirarlo.",
    *[f'execute if score #tier so_ar matches {t} run give @s {(i if isinstance(i, str) else i[0])}[minecraft:custom_data={{so_arena_loan:1b}},minecraft:lore=[{{text:"Prestado por el Coliseo",color:"gray",italic:false}}]] {1 if isinstance(i, str) else i[1]}'
      for t, items in KIT.items() for i in items],
    "tag @s add so_ar_loan",
    say("@s", "Kit prestado entregado. Se retira solo al terminar o salir.", "yellow"),
])
F("lib/enter_pit", [
    f"tp @s {PIT_IN[0]} {PIT_IN[1]} {PIT_IN[2]} 180 0",
    "tag @s add so_ar_in",
    "effect give @s minecraft:resistance 3 3 true",
    "playsound minecraft:item.trident.thunder master @s ~ ~ ~ 0.6 1.2",
])
F("lib/join", [
    f'execute unless entity @s[tag=so_ar_zone] run return run {say("@s", "Primero entrá al Coliseo con /trigger arena.", "red")}',
    f'execute if score #mode so_ar matches 0 run return run {say("@s", "No hay ningún desafío en curso. Elegí una práctica o un contrato.", "gray")}',
    f'execute if entity @s[tag=so_ar_in] run return run {say("@s", "Ya estás en el foso.", "gray")}',
    f"function {NS}:lib/enter_pit",
    f"bossbar set {NS}:fight players {IN}",
    say(ZONE, "¡Un gladiador más se suma al desafío!", "green"),
])

F("mode/practice/wave", [
    "scoreboard players add #wave so_ar 1",
    f"execute store result bossbar {NS}:fight value run scoreboard players get #wave so_ar",
    *[f"execute if score #tier so_ar matches {t} if score #wave so_ar matches {w} run {spawn(m)}"
      for t, _, mobs, _ in TIERS for w, reps in ((1, 1), (2, 2)) for m in mobs for _ in range(reps)],
    f"execute as {IN} at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 1.3",
])
F("mode/practice/second", [
    "scoreboard players add #t so_ar 1",
    "execute store result score #alive so_ar if entity @e[tag=so_ar_mob]",
    f"title {IN} actionbar {T({'text': 'Oleada ', 'color': 'yellow', 'bold': True}, {'score': {'name': '#wave', 'objective': 'so_ar'}, 'color': 'white'}, {'text': '/2 · enemigos: ', 'color': 'gray'}, {'score': {'name': '#alive', 'objective': 'so_ar'}, 'color': 'white'})}",
    f"execute if score #t so_ar matches 3.. if score #alive so_ar matches 0 if score #wave so_ar matches 2.. run return run function {NS}:lib/win_practice",
    f"execute if score #t so_ar matches 3.. if score #alive so_ar matches 0 if score #wave so_ar matches 1 run function {NS}:mode/practice/wave",
    f"execute if score #t so_ar matches 300.. run function {NS}:lib/fail",
])
F("lib/win_practice", [
    f"execute as {IN} run loot give @s loot {NS}:practice",
    f"title {IN} title {T({'text': '¡Victoria!', 'color': 'green', 'bold': True})}",
    say(ZONE, "Práctica superada. La recompensa ya es de ustedes.", "green"),
    f"function {NS}:lib/celebrar",
    f"function {NS}:lib/end",
])
F("lib/fail", [
    say(ZONE, "Se acabó el tiempo: desafío cancelado sin recompensa.", "gray"),
    f"function {NS}:lib/end",
])
F("lib/vacio", [
    say(ZONE, "El desafío terminó: ya no quedaba nadie en el foso.", "gray"),
    f"function {NS}:lib/end",
])

# ---------------------------------------------------------------- contratos
PHASES = [  # bloques mínimos: (objetivos, apoyo)
    (0, ["zombie", "husk", "skeleton", "spider"], ["skeleton", "spider"]),
    (3334, ["zombie_armor", "piglin", "bogged", "cave_spider"], ["witch", "skeleton_armor"]),
    (7501, ["vindicator", "pillager", "witch", "drowned_trident"], ["spider_big", "skeleton_ominous"]),
    (15000, ["zombie_ominous", "breeze", "bogged", "enderman"], ["wither_skeleton", "skeleton_ominous"]),
]


def by_phase(build):
    """Genera líneas condicionadas por la fase (#blk)."""
    out = []
    for i, (thr, tg, sup) in enumerate(PHASES):
        cond = f"execute if score #blk so_ar matches {thr}.."
        if i < len(PHASES) - 1:
            cond += f" unless score #blk so_ar matches {PHASES[i + 1][0]}.."
        out += [f"{cond} run {c}" for c in build(tg, sup)]
    return out


F("lib/start_con", [
    f"execute if score @s arena_con matches 9 run return run function {NS}:lib/join",
    *busy_guard(),
    f"function {NS}:lib/blocks",
    f'execute unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 400.. run return run {say("@s", "Los contratos se abren a los 400 bloques. Mientras, probá la práctica.", "red")}',
    f'execute if score @s arena_con matches 3 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 2501.. run return run {say("@s", "La Defensa del Núcleo se desbloquea a los 2.501 bloques.", "red")}',
    "scoreboard players operation #con so_ar = @s arena_con",
    f"execute unless score #con so_ar matches 1..3 run return run {say('@s', 'Contrato inválido.', 'red')}",
    f"function {NS}:lib/enter_pit",
    "scoreboard players set #t so_ar 0", "scoreboard players set #wave so_ar 0",
    "scoreboard players set #spawned so_ar 0", "scoreboard players set #anticamp so_ar 1",
    f"bossbar set {NS}:fight players {IN}", f"bossbar set {NS}:fight visible true",
    f"execute if score #con so_ar matches 1 run function {NS}:mode/caza/start",
    f"execute if score #con so_ar matches 2 run function {NS}:mode/caza2/start",
    f"execute if score #con so_ar matches 3 run function {NS}:mode/defensa/start",
])
# caza: 15 objetivos en tandas de 5
F("mode/caza/start", [
    "scoreboard players set #mode so_ar 2",
    f'bossbar set {NS}:fight name {T({"text": "Caza: objetivos restantes", "color": "aqua"})}',
    f"bossbar set {NS}:fight color blue", f"bossbar set {NS}:fight max 15", f"bossbar set {NS}:fight value 15",
    f'title {IN} title {T({"text": "¡Caza de monstruos!", "color": "aqua", "bold": True})}',
    say(ZONE, "Contrato: 15 bajas objetivo (en tandas de 5). Los de apoyo son extra.", "aqua"),
    f"function {NS}:mode/caza/batch",
])
F("mode/caza/batch", [
    "scoreboard players add #spawned so_ar 5",
    *by_phase(lambda tg, sup: [spawn(m, 1) for m in tg + tg[:1]]),
    f"execute as {IN} at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 1.1",
])
F("mode/caza/second", [
    "scoreboard players add #t so_ar 1",
    "execute store result score #alive so_ar if entity @e[tag=so_ar_target]",
    "scoreboard players set #left so_ar 15",
    "scoreboard players operation #left so_ar -= #spawned so_ar",
    "scoreboard players operation #left so_ar += #alive so_ar",
    f"execute store result bossbar {NS}:fight value run scoreboard players get #left so_ar",
    f"title {IN} actionbar {T({'text': 'Caza · quedan ', 'color': 'aqua'}, {'score': {'name': '#left', 'objective': 'so_ar'}, 'color': 'white', 'bold': True}, {'text': ' objetivos', 'color': 'gray'})}",
    f"execute if score #t so_ar matches 3.. if score #left so_ar matches ..0 run return run function {NS}:lib/win_contract",
    f"execute if score #alive so_ar matches ..1 if score #spawned so_ar matches ..10 run function {NS}:mode/caza/batch",
    "scoreboard players operation #m so_ar = #t so_ar", "scoreboard players operation #m so_ar %= #twentyfive so_ar",
    f"execute if score #m so_ar matches 0 run function {NS}:lib/blocks",
    *[l.replace("execute if score #blk", "execute if score #m so_ar matches 0 if score #blk") for l in by_phase(lambda tg, sup: [spawn(m) for m in sup])],
    f"execute if score #t so_ar matches 420.. run function {NS}:lib/fail",
])
# oleadas dobles: 3 oleadas por fase
F("mode/caza2/start", [
    "scoreboard players set #mode so_ar 4",
    f'bossbar set {NS}:fight name {T({"text": "Oleadas dobles", "color": "aqua"})}',
    f"bossbar set {NS}:fight color blue", f"bossbar set {NS}:fight max 3", f"bossbar set {NS}:fight value 0",
    f'title {IN} title {T({"text": "¡Oleadas dobles!", "color": "aqua", "bold": True})}',
    say(ZONE, "Contrato: superá 3 oleadas, cada una más dura.", "aqua"),
    f"function {NS}:mode/caza2/wave",
])
F("mode/caza2/wave", [
    "scoreboard players add #wave so_ar 1",
    f"execute store result bossbar {NS}:fight value run scoreboard players get #wave so_ar",
    *[l.replace("execute if score #blk", f"execute if score #wave so_ar matches {w}.. if score #blk")
      for w in (1, 2, 3) for l in by_phase(lambda tg, sup: [spawn(m) for m in tg + sup[:1]])],
    f"execute as {IN} at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 1.0",
])
F("mode/caza2/second", [
    "scoreboard players add #t so_ar 1",
    "execute store result score #alive so_ar if entity @e[tag=so_ar_mob]",
    f"title {IN} actionbar {T({'text': 'Oleada ', 'color': 'aqua', 'bold': True}, {'score': {'name': '#wave', 'objective': 'so_ar'}, 'color': 'white'}, {'text': '/3 · enemigos: ', 'color': 'gray'}, {'score': {'name': '#alive', 'objective': 'so_ar'}, 'color': 'white'})}",
    f"execute if score #t so_ar matches 3.. if score #alive so_ar matches 0 if score #wave so_ar matches 3.. run return run function {NS}:lib/win_contract",
    f"execute if score #t so_ar matches 3.. if score #alive so_ar matches 0 if score #wave so_ar matches 1..2 run function {NS}:mode/caza2/wave",
    f"execute if score #t so_ar matches 480.. run function {NS}:lib/fail",
])
# defensa del núcleo
F("mode/defensa/start", [
    f"setblock {CX} 96 {CZ} minecraft:crying_obsidian",
    "scoreboard players set #mode so_ar 3", "scoreboard players set #hp so_ar 100", "scoreboard players set #anticamp so_ar 0",
    f"bossbar set {NS}:fight color purple", f"bossbar set {NS}:fight max 100", f"bossbar set {NS}:fight value 100",
    f'bossbar set {NS}:fight name {T({"text": "Núcleo", "color": "dark_purple"})}',
    f"title {IN} title {T({'text': '¡Defiendan el Núcleo!', 'color': 'dark_purple', 'bold': True})}",
    say(ZONE, "Contrato: protegé el Núcleo (obsidiana llorosa del centro) 2 minutos. Acá la altura está permitida.", "dark_purple"),
    f"function {NS}:mode/defensa/wave",
])
F("mode/defensa/wave", [
    "scoreboard players add #wave so_ar 1",
    *by_phase(lambda tg, sup: [spawn(m) for m in tg[:3] + sup[:1]]),
])
F("mode/defensa/second", [
    "scoreboard players add #t so_ar 1",
    f"execute positioned {CX} 96 {CZ} store result score #near so_ar if entity @e[tag=so_ar_mob,distance=..5]",
    "scoreboard players operation #hp so_ar -= #near so_ar",
    f"execute store result bossbar {NS}:fight value run scoreboard players get #hp so_ar",
    f"title {IN} actionbar {T({'text': 'Núcleo: ', 'color': 'dark_purple'}, {'score': {'name': '#hp', 'objective': 'so_ar'}, 'color': 'white', 'bold': True}, {'text': '% · tiempo: ', 'color': 'gray'}, {'score': {'name': '#t', 'objective': 'so_ar'}, 'color': 'white'}, {'text': '/120 s', 'color': 'gray'})}",
    f"execute if score #hp so_ar matches ..0 run return run function {NS}:lib/fail",
    f"execute if score #t so_ar matches 120.. run return run function {NS}:lib/win_contract",
    "scoreboard players operation #m so_ar = #t so_ar", "scoreboard players operation #m so_ar %= #twentyfive so_ar",
    f"execute if score #m so_ar matches 0 run function {NS}:mode/defensa/wave",
])
F("lib/win_contract", [
    f"execute as {IN} run loot give @s loot {NS}:contract",
    f"scoreboard players add {IN} so_ar_rank 1",
    f"title {IN} title {T({'text': '¡Contrato cumplido!', 'color': 'green', 'bold': True})}",
    say(ZONE, "¡Contrato cumplido! Esmeraldas, botellas de XP y Fragmentos de Victoria.", "green"),
    f"function {NS}:lib/celebrar",
    f"function {NS}:lib/end",
])
F("lib/end", [
    "# Fin de desafío: limpia mobs, núcleo, barra y kits; a los 3 s devuelve el foso al lobby.",
    "tp @e[tag=so_ar_mob] -5000 -300 -5000",
    "kill @e[tag=so_ar_mob]",
    f"setblock {CX} 96 {CZ} minecraft:air",
    f"bossbar set {NS}:fight visible false",
    "scoreboard players set #mode so_ar 0", "scoreboard players set #wave so_ar 0",
    "scoreboard players set #t so_ar 0", "scoreboard players set #anticamp so_ar 1",
    "scoreboard players reset @a so_ar_air",
    f"schedule function {NS}:lib/to_lobby 60t",
])
F("lib/to_lobby", [
    f"execute as @a[tag=so_ar_zone] run clear @s {LOAN}",
    "tag @a remove so_ar_loan",
    f"execute as @a[tag=so_ar_zone,{PIT_BOX}] run tp @s {ARR[0]} {ARR[1]} {ARR[2]} 180 0",
    "tag @a remove so_ar_in",
    say(ZONE, "De vuelta en el lobby. Otro desafío, o /trigger volver para ir a la isla.", "gray"),
])

# ---------------------------------------------------------------- spawn de enemigos
F("lib/spawn", [
    "# $(m): id de so_events:api/mob · $(t): 1 = objetivo de caza. Punto al azar dentro del foso.",
    "$data modify storage so_arenas:tmp m set value \"$(m)\"",
    "execute store result storage so_arenas:tmp a int 1 run random value 0..359",
    "execute store result storage so_arenas:tmp d int 1 run random value 5..20",
    f"function {NS}:lib/spawn_at with storage so_arenas:tmp",
    "$scoreboard players set #tg so_ar $(t)",
    f"execute as @e[tag=so_ev_mob,{MOB_BOX}] run function {NS}:lib/claim",
])
F("lib/spawn_at", [f'$execute positioned {CX} 96 {CZ} rotated $(a) 0 positioned ^ ^ ^$(d) run function so_events:api/mob {{id:"$(m)"}}'])
F("lib/claim", [
    "tag @s add so_ar_mob",
    "tag @s remove so_ev_mob",
    "execute if score #tg so_ar matches 1 run tag @s add so_ar_target",
])


# ---------------------------------------------------------------- torres / festejo / anticamping
TOWERS = []
for k in range(8):
    ang = math.pi / 8 + k * math.pi / 4
    TOWERS.append((CX + round(AX * 0.965 * math.cos(ang)), CZ + round(BZ * 0.965 * math.sin(ang))))
FW = '{{LifeTime:{lt},FireworksItem:{{id:"minecraft:firework_rocket",count:1,components:{{"minecraft:fireworks":{{flight_duration:1b,explosions:[{{shape:"large_ball",colors:[I;16750848,16711680,16776960],has_trail:1b,has_twinkle:1b}}]}}}}}}}}'
F("lib/celebrar", [
    "# Fuegos artificiales desde las 8 torres.",
    *[f"summon minecraft:firework_rocket {x} {TOP_Y + 3} {z} {FW.format(lt=20 + 4 * i)}" for i, (x, z) in enumerate(TOWERS)],
    f"execute as {ZONE} at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1",
    f"execute as {ZONE} at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 0.8",
])
F("lib/anticamp", [
    "# Anti-camping: 3 s por encima del muro del foso y te baja al centro.",
    f"execute as {IN} at @s if entity @s[y=101,dy=80] run scoreboard players add @s so_ar_air 1",
    f"execute as {IN} at @s unless entity @s[y=101,dy=80] run scoreboard players set @s so_ar_air 0",
    f'execute as @a[tag=so_ar_in,scores={{so_ar_air=3..}}] run title @s actionbar {T({"text": "¡Nada de campear en las gradas!", "color": "red", "bold": True})}',
    f"execute as @a[tag=so_ar_in,scores={{so_ar_air=3..}}] run tp @s {PIT_IN[0]} 96 {PIT_IN[2]}",
    "scoreboard players set @a[scores={so_ar_air=3..}] so_ar_air 0",
])


# ---------------------------------------------------------------- diálogos
def act(cmd, label, tip=None, color=None, w=170):
    a = {"label": {"text": label} | ({"color": color} if color else {}), "width": w,
         "action": {"type": "minecraft:run_command", "command": cmd}}
    if tip: a["tooltip"] = {"text": tip, "color": "gray"}
    return a


CLOSE = {"label": {"text": "✕ Cerrar", "color": "gray"}, "width": 170}
BACK = {"label": {"text": "« Volver"}, "width": 170, "action": {"type": "minecraft:show_dialog", "dialog": f"{NS}:main"}}
W(f"data/{NS}/dialog/main.json", {
    "type": "minecraft:multi_action", "title": {"text": "Coliseo VorNeX", "color": "gold", "bold": True},
    "external_title": {"text": "Arena"},
    "body": [{"type": "minecraft:plain_message", "contents": {"text": "Practicá, cumplí contratos y volvé con botín. Los mercaderes del lobby venden flechas, pociones, tótems y más.", "color": "gray"}}],
    "columns": 2, "can_close_with_escape": True, "exit_action": CLOSE, "pause": False,
    "actions": [
        {"label": {"text": "Práctica por tiers", "color": "yellow"}, "width": 170, "action": {"type": "minecraft:show_dialog", "dialog": f"{NS}:practice"}},
        {"label": {"text": "Contratos", "color": "aqua"}, "width": 170, "action": {"type": "minecraft:show_dialog", "dialog": f"{NS}:contracts"}},
        act("/trigger arena_con set 9", "Unirse al desafío", "Entrar al foso si ya hay un desafío en curso.", "green"),
        act("/trigger levelrank", "Ver mi rango", "Se muestra en el chat.", "gray"),
        act("/trigger volver", "Volver a la isla", "Si hay desafío activo, cuenta como abandono.", "red"),
    ]})
W(f"data/{NS}/dialog/practice.json", {
    "type": "minecraft:multi_action", "title": {"text": "Práctica por tiers", "color": "yellow", "bold": True},
    "body": [{"type": "minecraft:plain_message", "contents": {"text": "El kit prestado se retira solo al terminar. Con equipo propio, si morís tus cosas quedan en el foso.", "color": "gray"}}],
    "columns": 2, "can_close_with_escape": True, "exit_action": CLOSE, "pause": False,
    "actions": [x for t, n, mobs, thr in TIERS for x in (
        act(f"/trigger arena_pr set {t}", f"Tier {t} · {n} (kit)", f"Desde {thr:,} bloques.".replace(",", "."), "yellow"),
        act(f"/trigger arena_pr set {t + 10}", f"Tier {t} · {n} (propio)", f"Desde {thr:,} bloques.".replace(",", "."), "gold"))] + [BACK]})
W(f"data/{NS}/dialog/contracts.json", {
    "type": "minecraft:multi_action", "title": {"text": "Contratos", "color": "aqua", "bold": True},
    "body": [{"type": "minecraft:plain_message", "contents": {"text": "Un contrato por vez. Los enemigos escalan con tu fase. Cumplirlo sube tu rango oculto.", "color": "gray"}}],
    "columns": 1, "can_close_with_escape": True, "exit_action": CLOSE | {"width": 250}, "pause": False,
    "actions": [
        act("/trigger arena_con set 1", "Caza: 15 bajas objetivo", "Desde 400 bloques.", "aqua", 250),
        act("/trigger arena_con set 2", "Oleadas dobles", "3 oleadas. Desde 400 bloques.", "aqua", 250),
        act("/trigger arena_con set 3", "Defensa del Núcleo", "2 minutos. Desde 2.501 bloques. Altura permitida.", "aqua", 250),
        BACK | {"width": 250},
    ]})

# ---------------------------------------------------------------- construcción
GRAD_MIX = ["minecraft:stone_bricks", "minecraft:polished_deepslate", "minecraft:cut_sandstone", "minecraft:smooth_sandstone"]
FLOOR_MIX = ["minecraft:sandstone", "minecraft:smooth_sandstone", "minecraft:coarse_dirt", "minecraft:packed_mud"]


def zr(dx, r):
    """Mitad del largo en z del óvalo de radio r en la columna dx (-1 si no lo toca)."""
    a = 1 - (dx / (AX * r)) ** 2
    return int(BZ * r * math.sqrt(a)) if a >= 0 else -1


def band(x, dx, r0, r1, y0, y1, blk):
    """Rellena las celdas de la columna x con r0 < r <= r1 (dos tramos, o uno si la columna no toca r0)."""
    za, zb = zr(dx, r0), zr(dx, r1)
    if zb < 0: return []
    if za < 0:
        return [f"fill {x} {y0} {CZ - zb} {x} {y1} {CZ + zb} {blk}"]
    if zb <= za: return []
    return [f"fill {x} {y0} {CZ - zb} {x} {y1} {CZ - za - 1} {blk}",
            f"fill {x} {y0} {CZ + za + 1} {x} {y1} {CZ + zb} {blk}"]


steps = []  # cada paso = un archivo admin/build_NN (se ejecutan con 10 ticks de separación)
# paso 1-2: limpiar el aire y la base
cur = []
for dx in range(-AX, AX + 1):
    x, zb = CX + dx, zr(dx, 1.0)
    if zb < 0: continue
    cur.append(f"fill {x} 96 {CZ - zb} {x} {TOP_Y + 4} {CZ + zb} minecraft:air")
    cur.append(f"fill {x} 90 {CZ - zb} {x} 94 {CZ - zb + 2 * zb} minecraft:deepslate_bricks")
    cur.append(f"fill {x} {G} {CZ - zb} {x} {G} {CZ + zb} {FLOOR_MIX[(dx // 3) % len(FLOOR_MIX)]}")
steps += [cur[:len(cur) // 2], cur[len(cur) // 2:]]
# paso 3: muro del foso + anillo
cur = []
for dx in range(-AX, AX + 1):
    cur += band(CX + dx, dx, R_PIT - 0.03, R_PIT, G, G, "minecraft:chiseled_sandstone")
    cur += band(CX + dx, dx, R_PIT, R_PITWALL, G, 99, "minecraft:polished_blackstone_bricks")
steps.append(cur)
# pasos 4-5: gradas macizas (8 filas, cada una 1 más alta)
cur = []
n = 8
for i in range(n):
    r0 = R_PITWALL + (R_GRADA - R_PITWALL) * i / n
    r1 = R_PITWALL + (R_GRADA - R_PITWALL) * (i + 1) / n
    for dx in range(-AX, AX + 1):
        cur += band(CX + dx, dx, r0, r1, G, 100 + i, GRAD_MIX[i % len(GRAD_MIX)])
steps += [cur[:len(cur) // 2], cur[len(cur) // 2:]]
# paso 6: muralla exterior con ventanas y almenas
cur = []
for dx in range(-AX, AX + 1):
    x = CX + dx
    blk = "minecraft:cut_sandstone" if (dx // 6) % 2 == 0 else "minecraft:stone_bricks"
    cur += band(x, dx, R_GRADA, R_WALL, G, 125, blk)
    cur += band(x, dx, R_GRADA, R_WALL, 126, 127, "minecraft:polished_deepslate")
    if dx % 2 == 0:
        cur += band(x, dx, R_GRADA, R_WALL, 128, 128, "minecraft:polished_deepslate_wall")
    if abs(dx) % 10 in (4, 5):
        cur += band(x, dx, R_GRADA, R_WALL, 110, 116, "minecraft:air")
steps.append(cur)
# paso 7: torres
cur = []
for tx, tz in TOWERS:
    cur += [f"fill {tx - 2} {G} {tz - 2} {tx + 2} {TOP_Y} {tz + 2} minecraft:polished_tuff",
            f"fill {tx - 1} 96 {tz - 1} {tx + 1} {TOP_Y - 1} {tz + 1} minecraft:air",
            f"fill {tx - 3} {TOP_Y + 1} {tz - 3} {tx + 3} {TOP_Y + 1} {tz + 3} minecraft:cut_sandstone",
            f"fill {tx - 1} {TOP_Y + 2} {tz - 1} {tx + 1} {TOP_Y + 2} {tz + 1} minecraft:glowstone"]
steps.append(cur)


# paso 8: túnel, lobby, carteles, placas
def sign_snbt(lines, cmd=None):
    msgs = []
    for i in range(4):
        t = lines[i] if i < len(lines) else ("", "black")
        if isinstance(t, str): t = (t, "black")
        comp = f'{{text:"{t[0]}",color:"{t[1]}",bold:{"true" if i == 1 else "false"}'
        if i == 1 and cmd:
            comp += f',click_event:{{action:"run_command",command:"{cmd}"}}'
        msgs.append(comp + "}")
    return f'{{is_waxed:1b,front_text:{{messages:[{",".join(msgs)}]}}}}'


cur = []
TZ0 = CZ + int(R_PIT * BZ) + 1
cur += [f"fill {CX - 4} {G} {TZ0} {CX + 4} 101 {LZ0} minecraft:stone_bricks",
        f"fill {CX - 3} 96 {TZ0} {CX + 3} 100 {LZ0} minecraft:air",
        f"fill {CX - 3} {G} {TZ0} {CX + 3} {G} {LZ0} minecraft:polished_deepslate",
        f"fill {CX - 3} 96 {TZ0} {CX + 3} 100 {TZ0} minecraft:iron_bars",
        f"setblock {CX} 100 {TZ0 + 8} minecraft:lantern[hanging=true]",
        f"setblock {CX} 100 {TZ0 + 16} minecraft:lantern[hanging=true]",
        # lobby cerrado
        f"fill {CX - LX} {G} {LZ0} {CX + LX} 105 {LZ1} minecraft:stone_bricks hollow",
        f"fill {CX - LX + 1} {G} {LZ0 + 1} {CX + LX - 1} {G} {LZ1 - 1} minecraft:polished_deepslate",
        f"fill {CX - LX + 1} 105 {LZ0 + 1} {CX + LX - 1} 105 {LZ1 - 1} minecraft:chiseled_sandstone",
        f"fill {CX - 3} 96 {LZ0} {CX + 3} 100 {LZ0} minecraft:air",
        f"fill {CX - 3} 96 {LZ0} {CX + 3} 100 {LZ0} minecraft:iron_bars",
        f"fill {CX} {G} {LZ0 + 1} {CX} {G} {LZ1 - 1} minecraft:red_terracotta"]
for lx in (CX - 6, CX, CX + 6):
    for lz in (LZ0 + 5, LZ0 + 12, LZ1 - 4):
        cur.append(f"setblock {lx} 104 {lz} minecraft:lantern[hanging=true]")
for x, fn, label, col in PADS:
    cur += [f"setblock {x} {G} {PAD_Z} minecraft:{col}_concrete",
            f"setblock {x} 96 {PAD_Z} minecraft:light_weighted_pressure_plate",
            f"setblock {x} 96 {PAD_Z - 1} minecraft:oak_sign[rotation=0]{sign_snbt(['Pisá la placa', (label, 'dark_blue'), '(o tocá el cartel)'], {'pad_pr': f'/trigger arena_pr set 0', 'pad_con': '/trigger arena_con set 0', 'pad_join': '/trigger arena_con set 9', 'pad_back': '/trigger volver'}[fn])}"]
# carteles: muro oeste = práctica (fila alta kit, fila baja equipo propio); muro este = contratos
for idx, (t, n, _, thr) in enumerate(TIERS):
    z = LZ0 + 6 + idx * 3
    cur.append(f"setblock {CX - LX + 1} 98 {z} minecraft:oak_wall_sign[facing=east]{sign_snbt([f'Práctica T{t}', (n, 'dark_green'), 'kit prestado', f'{thr} bloques+'], f'/trigger arena_pr set {t}')}")
    cur.append(f"setblock {CX - LX + 1} 97 {z} minecraft:oak_wall_sign[facing=east]{sign_snbt([f'Práctica T{t}', (n, 'dark_red'), 'equipo propio', ''], f'/trigger arena_pr set {t + 10}')}")
EAST = [("Contrato", ("Caza 15 bajas", "dark_aqua"), "400 bloques+", "/trigger arena_con set 1"),
        ("Contrato", ("Oleadas dobles", "dark_aqua"), "400 bloques+", "/trigger arena_con set 2"),
        ("Contrato", ("Defensa Núcleo", "dark_purple"), "2501 bloques+", "/trigger arena_con set 3"),
        ("Desafío en curso", ("Unirse", "dark_green"), "", "/trigger arena_con set 9")]
for idx, (a, b, c, cmd) in enumerate(EAST):
    cur.append(f"setblock {CX + LX - 1} 98 {LZ0 + 6 + idx * 3} minecraft:oak_wall_sign[facing=west]{sign_snbt([a, b, c], cmd)}")
EAST2 = [("Tu rango", ("Ver rango", "dark_gray"), "(oculto)", "/trigger levelrank"),
         ("Salir", ("Volver a la isla", "dark_red"), "", "/trigger volver"),
         ("Menú", ("Abrir menú", "gold"), "", "/trigger arena")]
for idx, (a, b, c, cmd) in enumerate(EAST2):
    cur.append(f"setblock {CX + LX - 1} 97 {LZ0 + 6 + idx * 3} minecraft:oak_wall_sign[facing=west]{sign_snbt([a, b, c], cmd)}")
# carteles bajo cada aldeano de menú (por si la hitbox no responde en Bedrock)
for nid, name, color, x, z, _ in NPCS:
    cmd = {"main": "/trigger arena", "pr": "/trigger arena_pr set 0", "con": "/trigger arena_con set 0"}[nid]
    rot = 8 if z > LZ0 + 10 else 0
    dz = -1 if rot == 8 else 1
    cur.append(f"setblock {x} 96 {z + dz} minecraft:oak_sign[rotation={rot}]{sign_snbt([name[:15], ('Tocá acá', 'dark_blue'), 'o al aldeano'], cmd)}")
steps.append(cur)

# arena_pr/arena_con = 0 desde carteles: abrir el submenú correspondiente (para Bedrock)
# (trigger set 0 no dispara el tick, así que los carteles usan valores 20 y 20 dedicados)
for i, s in enumerate(steps):
    steps[i] = [l.replace("/trigger arena_pr set 0", "/trigger arena_pr set 20").replace("/trigger arena_con set 0", "/trigger arena_con set 20") for l in s]

N = len(steps)
for i, s in enumerate(steps):
    F(f"admin/build_{i + 1:02d}", [f"# coliseo: paso {i + 1}/{N}"] + s)
FL = f"{CX - AX - 6} {CZ - BZ - 6} {CX + AX + 6} {LZ1 + 4}"
F("admin/build", [
    f"forceload add {FL}",
    "scoreboard players set #bstep so_ar 0",
    say("@a", f"Construyendo el Coliseo en {N} pasos (~{2 + N // 2} s). Cargando chunks...", "yellow"),
    f"schedule function {NS}:admin/build_step 40t",
])
F("admin/build_dispatch", [f"function {NS}:admin/build"])
F("admin/build_step", [
    "scoreboard players add #bstep so_ar 1",
    *[f"execute if score #bstep so_ar matches {i + 1} run function {NS}:admin/build_{i + 1:02d}" for i in range(N)],
    f'title @a[tag=so_ar_zone] actionbar [{{"text":"Construyendo paso ","color":"yellow"}},{{"score":{{"name":"#bstep","objective":"so_ar"}},"color":"white"}},{{"text":"/{N}","color":"yellow"}}]',
    f"execute if score #bstep so_ar matches ..{N - 1} run schedule function {NS}:admin/build_step 10t",
    f"execute if score #bstep so_ar matches {N} run function {NS}:admin/build_finish",
])
F("admin/build_finish", [
    *npc_summons(),
    f"forceload remove {FL}",
    say("@a", "¡El Coliseo VorNeX está listo! Entrá con /trigger arena.", "green"),
    "execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1",
])
F("admin/npcs", [*npc_summons(), say("@s", "Aldeanos del lobby recolocados.", "green")])

# submenús desde carteles (valor 20)
_pr = open(os.path.join(ROOT, f"data/{NS}/function/lib/start_pr.mcfunction"), encoding="utf-8").read().splitlines()
F("lib/start_pr", [f"execute if score @s arena_pr matches 20 run return run function {NS}:npc_menu_pr"] + _pr)
_con = open(os.path.join(ROOT, f"data/{NS}/function/lib/start_con.mcfunction"), encoding="utf-8").read().splitlines()
F("lib/start_con", [f"execute if score @s arena_con matches 20 run return run function {NS}:npc_menu_con"] + _con)
F("npc_menu_pr", [f"dialog show @s {NS}:practice", f"function {NS}:lib/chat_main"])
F("npc_menu_con", [f"dialog show @s {NS}:contracts", f"function {NS}:lib/chat_main"])

# ---------------------------------------------------------------- admin
F("admin/help", [f"tellraw @s {T({'text': h, 'color': 'gold' if i == 0 else 'gray'})}" for i, h in enumerate([
    "SO Arenas v2 — ayuda admin",
    "Construir: /trigger arena (o volá a -5000 100 -5000) y /function so_arenas:admin/build",
    "Recolocar aldeanos: /function so_arenas:admin/npcs",
    "/function so_arenas:admin/status | stop | enable | disable",
    "Probar todo: /function so_arenas:admin/test",
    "Jugadores: /trigger arena (ir/menú), /trigger volver (salir o abandono), /trigger levelrank",
])])
F("admin/test", [
    f"tellraw @s {T({'text': '━━━ SO Arenas · Modo prueba ━━━', 'color': 'gold', 'bold': True})}",
    f"tellraw @s {T({'text': 'Como admin entrás a todo sin importar los bloques. Fase simulada para los enemigos:', 'color': 'gray'})}",
    f"tellraw @s {T(*[link(f'[{n}] ', f'/function so_arenas:admin/fase_{i}', 'aqua', f'Simular {v} bloques') for i, (n, v) in enumerate([('Fase 1', 0), ('Fase 2', 3500), ('Fase 3', 8000), ('Fase 4', 16000)])], link('[Real]', '/function so_arenas:admin/fase_real', 'gray', 'Usar los bloques reales'))}",
    f"tellraw @s {T({'text': ' Práctica: ', 'color': 'gray'}, *[link(f'[T{t}] ', f'/trigger arena_pr set {t}', 'yellow', f'Tier {t} con kit') for t in range(1, 5)])}",
    f"tellraw @s {T({'text': ' Contratos: ', 'color': 'gray'}, link('[Caza] ', '/trigger arena_con set 1', 'aqua', 'Caza'), link('[Oleadas] ', '/trigger arena_con set 2', 'aqua', 'Oleadas'), link('[Defensa] ', '/trigger arena_con set 3', 'aqua', 'Defensa'))}",
    f"tellraw @s {T(link('[Ganar ya] ', '/function so_arenas:admin/win', 'green', 'Forzar victoria'), link('[Detener]', '/function so_arenas:admin/stop', 'red', 'Cancelar desafío'))}",
    "Tip: primero /trigger arena para estar en el coliseo." and f"tellraw @s {T({'text': 'Primero entrá con /trigger arena.', 'color': 'dark_gray'})}",
])
for i, v in enumerate([0, 3500, 8000, 16000]):
    F(f"admin/fase_{i}", [f"scoreboard players set #fake so_ar {v}", say("@s", f"Fase simulada: {v} bloques.", "aqua")])
F("admin/fase_real", ["scoreboard players reset #fake so_ar", say("@s", "Usando bloques reales.", "gray")])
F("admin/win", [
    f"execute if score #mode so_ar matches 1 run return run function {NS}:lib/win_practice",
    f"execute unless score #mode so_ar matches 0 run return run function {NS}:lib/win_contract",
    say("@s", "No hay desafío en curso.", "gray"),
])
F("admin/status", [f"function {NS}:lib/blocks",
    f"tellraw @s {T(PFX, {'text': 'modo=', 'color': 'gray', 'bold': False}, {'score': {'name': '#mode', 'objective': 'so_ar'}, 'color': 'white'}, {'text': '  bloques=', 'color': 'gray'}, {'score': {'name': '#blk', 'objective': 'so_ar'}, 'color': 'white'}, {'text': '  activo=', 'color': 'gray'}, {'score': {'name': '#enabled', 'objective': 'so_ar'}, 'color': 'white'})}"])
F("admin/stop", [f"function {NS}:lib/end", say("@a", "Desafío del coliseo detenido por un administrador.", "gray")])
F("admin/enable", ["scoreboard players set #enabled so_ar 1", say("@s", "Arena activada.", "green")])
F("admin/disable", [f"function {NS}:lib/end", "scoreboard players set #enabled so_ar 0", say("@s", "Arena desactivada.", "red")])
F("uninstall", [f"function {NS}:lib/end", f"bossbar remove {NS}:fight",
    *[f"scoreboard objectives remove {o}" for o in ["so_ar", *TRIGGERS, "so_ar_air", "so_ar_rank", "so_ar_x", "so_ar_y", "so_ar_z", "so_ar_saved"]],
    say("@s", "so_arenas desinstalado (el coliseo queda en el mundo). Quitá el datapack y hacé /reload.", "gray")])

W("README.md", f"""# so_arenas v2 — el Coliseo VorNeX

Zona en **-5000 100 -5000** (Overworld). Enemigos de `so_events:api/mob` (sin duplicar mobs).

## Construcción (admin)
1. `/trigger arena` (o volá hasta -5000 100 -5000).
2. `/function so_arenas:admin/build` → fuerza la carga del área y construye en {N} pasos (~{2 + N // 2} s). Al final aparecen los aldeanos y se libera la carga forzada.
3. Si algún aldeano se pierde: `/function so_arenas:admin/npcs`.

## Jugadores
- `/trigger arena`: viaja al lobby (guarda dónde estabas). Dentro, vuelve a abrir el menú.
- `/trigger volver`: vuelve al lugar de donde viniste. En pleno desafío = abandono.
- `/trigger levelrank`: rango oculto.
- Menú por 4 vías: aldeanos (Guía, Maestro de Armas, Comandante), carteles de los muros, placas de colores del piso y menú del chat (Java).
- Mercaderes: Intendente (flechas, pociones arrojadizas, manzanas doradas, comida) y Armero (escudos, tótems, huevos de gólem de hierro y de nieve, perlas, cohetes, arcos).

## Desafíos
- Práctica Tier I–IV (0 / 3.334 / 7.501 / 15.000 bloques), con kit prestado o equipo propio.
- Contratos: Caza 15 bajas (400+), Oleadas dobles (400+), Defensa del Núcleo (2.501+).
- Otros jugadores pueden sumarse con "Unirse". Victoria: cohetes en las 8 torres y recompensa.
""")

# ---------------------------------------------------------------- zip
os.makedirs("/mnt/documents", exist_ok=True)
out = "/mnt/documents/so_arenas-v2.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for d, _, files in os.walk(ROOT):
        for f in files:
            full = os.path.join(d, f); z.write(full, os.path.relpath(full, ROOT))
print("ok", out, "pasos", N)
