#!/usr/bin/env python3
"""Generador de so_events v1 (lo que pasa: eventos, oleadas y jefes).
Salida: datapacks/so-events  +  /mnt/documents/so_events-v1.zip (raiz limpia)."""
import json, os, shutil, zipfile

ROOT = os.path.join(os.path.dirname(__file__), "..", "datapacks", "so-events")
NS = "so_events"
shutil.rmtree(ROOT, ignore_errors=True)

def W(rel, obj):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(obj if isinstance(obj, str) else json.dumps(obj, ensure_ascii=False, indent=2))

def F(name, lines):
    W(f"data/{NS}/function/{name}.mcfunction", "\n".join(lines) + "\n")

def T(*parts):
    return json.dumps(list(parts) if len(parts) > 1 else parts[0], ensure_ascii=False)

PFX = {"text": "[Evento] ", "color": "gold", "bold": True}
def say(sel, text, color="yellow"):
    return f"tellraw {sel} {T(PFX, {'text': text, 'color': color, 'bold': False})}"

IN = "@a[tag=so_ev_in]"
NEAR = "execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in"

# ---------------------------------------------------------------- pack
W("pack.mcmeta", {"pack": {"description": "Simply OneBlock Expansion - Events (eventos, oleadas y jefes)",
                           "min_format": [107, 1], "max_format": [107, 1]}})
W("data/minecraft/tags/function/load.json", {"replace": False, "values": [f"{NS}:load"]})
W("data/minecraft/tags/function/tick.json", {"replace": False, "values": [f"{NS}:tick"]})

# ---------------------------------------------------------------- mobs
def eq(**slots):
    parts = [f'{k}:{{id:"minecraft:{v}",count:1}}' if isinstance(v, str) else f"{k}:{v}" for k, v in slots.items()]
    drops = ",".join(f"{k}:0.0f" for k in slots)
    return f"equipment:{{{','.join(parts)}}},drop_chances:{{{drops}}}"

BASE = 'Tags:["so_ev_mob"],PersistenceRequired:1b'
MOBS = {
    "husk": ("husk", BASE),
    "zombie": ("zombie", f"{BASE},{eq(head='leather_helmet')}"),
    "skeleton": ("skeleton", f"{BASE},{eq(head='leather_helmet', mainhand='bow')}"),
    "spider": ("spider", BASE),
    "slime": ("slime", f"{BASE},Size:1"),
    "slime_big": ("slime", f"{BASE},Size:2"),
    "zombie_armor": ("zombie", f"{BASE},{eq(head='iron_helmet', chest='iron_chestplate', mainhand='iron_sword')}"),
    "skeleton_armor": ("skeleton", f"{BASE},{eq(head='iron_helmet', chest='chainmail_chestplate', mainhand='bow')}"),
    "pillager": ("pillager", f"{BASE},{eq(mainhand='crossbow')},PatrolLeader:0b"),
    "vindicator": ("vindicator", f"{BASE},{eq(mainhand='iron_axe')}"),
    "blaze": ("blaze", BASE),
    "wither_skeleton": ("wither_skeleton", f"{BASE},{eq(mainhand='stone_sword')}"),
    "magma_cube": ("magma_cube", f"{BASE},Size:1"),
}
for name, (eid, nbt) in MOBS.items():
    F(f"mob/{name}", [f"summon minecraft:{eid} ~ ~ ~ {{{nbt}}}", "scoreboard players set #ok so_ev 1"])

def boss(name, eid, hp, label, color, extra):
    nbt = (f'Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,'
           f'CustomName:{{text:"{label}",color:"{color}",bold:true}},'
           f'attributes:[{{id:"minecraft:max_health",base:{hp}d}},{{id:"minecraft:knockback_resistance",base:0.6d}}],Health:{hp}f,{extra}')
    F(f"boss/{name}", [
        f"summon minecraft:{eid} ~ ~ ~ {{{nbt}}}",
        "scoreboard players set #ok so_ev 1",
        f"bossbar set {NS}:boss name {T({'text': label, 'color': color, 'bold': True})}",
        f"bossbar set {NS}:boss max {hp}", f"bossbar set {NS}:boss value {hp}",
        f"bossbar set {NS}:boss players @a", f"bossbar set {NS}:boss visible true",
        f"playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3",
        say("@a", f"¡Apareció {label}!", "red")])

SHARP = lambda item, lvl: f'{{id:"minecraft:{item}",count:1,components:{{"minecraft:enchantments":{{"minecraft:sharpness":{lvl}}}}}}}'
BOSSES = {
    "rey_zombi": ("zombie", 120, "Rey Zombi", "dark_green", eq(head="golden_helmet", chest="iron_chestplate", mainhand=SHARP("iron_sword", 2))),
    "slime_rey": ("slime", 64, "Slime Rey", "green", 'Tags:["so_ev_mob","so_ev_boss"],Size:5'),
    "comandante": ("skeleton", 110, "Comandante Óseo", "white", eq(head="diamond_helmet", chest="iron_chestplate", mainhand="bow")),
    "capitan": ("vindicator", 130, "Capitán Saqueador", "dark_red", eq(head="white_banner", mainhand=SHARP("diamond_axe", 1))),
    "caballero": ("wither_skeleton", 160, "Caballero del Nether", "dark_purple", eq(head="netherite_helmet", mainhand=SHARP("netherite_sword", 2))),
}
for n, (eid, hp, label, col, extra) in BOSSES.items():
    extra = extra.replace('Tags:["so_ev_mob","so_ev_boss"],', "")
    boss(n, eid, hp, label, col, extra)

# ---------------------------------------------------------------- spawn seguro
F("lib/spawn", [
    "# $(mob): nombre de mob/ o boss/. Busca suelo cerca del jugador (nunca en el vacío).",
    "scoreboard players set #ok so_ev 0",
    "$data modify storage so_events:tmp mob set value \"$(mob)\"",
    "function so_events:lib/spawn_roll",
    "function so_events:lib/spawn_try with storage so_events:tmp",
    "execute if score #ok so_ev matches 0 run function so_events:lib/spawn_roll",
    "execute if score #ok so_ev matches 0 run function so_events:lib/spawn_try with storage so_events:tmp",
    "execute if score #ok so_ev matches 0 run function so_events:lib/spawn_roll",
    "execute if score #ok so_ev matches 0 run function so_events:lib/spawn_try with storage so_events:tmp",
    "execute if score #ok so_ev matches 0 run function so_events:lib/spawn_here with storage so_events:tmp",
])
F("lib/spawn_roll", [
    "execute store result storage so_events:tmp a int 1 run random value 0..359",
    "execute store result storage so_events:tmp d int 1 run random value 4..9",
])
F("lib/spawn_try", ["$execute rotated $(a) 0 positioned ^ ^ ^$(d) if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:$(mob)"])
F("lib/spawn_here", ["$execute positioned ~ ~ ~ run function so_events:$(mob)"])

def spawn(mob, sel=IN):
    return f'execute as {sel} at @s run function {NS}:lib/spawn {{mob:"mob/{mob}"}}'

# ---------------------------------------------------------------- loot
def item(name, w, lo=1, hi=1):
    e = {"type": "minecraft:item", "name": f"minecraft:{name}", "weight": w}
    if hi > 1: e["functions"] = [{"function": "minecraft:set_count", "count": {"min": lo, "max": hi}}]
    return e
LOOT = {
    "rain": [1, [item("cobblestone", 8, 8, 24), item("oak_log", 6, 4, 12), item("iron_ingot", 4, 1, 4), item("coal", 5, 4, 12),
                 item("bread", 4, 2, 6), item("emerald", 3, 1, 3), item("gold_ingot", 2, 1, 3), item("experience_bottle", 2, 1, 4), item("diamond", 1)]],
    "supply": [3, [item("iron_ingot", 6, 4, 10), item("emerald", 6, 4, 10), item("golden_carrot", 4, 4, 10), item("arrow", 4, 16, 32),
                   item("ender_pearl", 2, 1, 3), item("diamond", 2, 1, 2), item("golden_apple", 2), item("experience_bottle", 3, 4, 10)]],
    "reward_small": [2, [item("emerald", 8, 4, 10), item("iron_ingot", 4, 4, 8), item("experience_bottle", 4, 4, 8), item("golden_carrot", 3, 4, 8), item("diamond", 1)]],
    "reward_big": [3, [item("emerald", 8, 10, 24), item("diamond", 4, 1, 4), item("golden_apple", 3, 1, 2), item("experience_bottle", 4, 8, 16),
                       item("netherite_scrap", 1), item("ender_pearl", 3, 2, 4), item("totem_of_undying", 1)]],
}
for n, (rolls, entries) in LOOT.items():
    W(f"data/{NS}/loot_table/{n}.json", {"type": "minecraft:chest", "pools": [{"rolls": rolls, "entries": entries}]})

# ---------------------------------------------------------------- nucleo
F("load", [
    "scoreboard objectives add so_ev dummy",
    "scoreboard objectives add evento trigger",
    "execute unless score #enabled so_ev matches 0..1 run scoreboard players set #enabled so_ev 1",
    "execute unless score #auto so_ev matches 0..1 run scoreboard players set #auto so_ev 1",
    "execute unless score #every so_ev matches 1.. run scoreboard players set #every so_ev 400",
    "execute unless score #min so_ev matches 0.. run scoreboard players set #min so_ev 300",
    "execute unless score #mine_goal so_ev matches 1.. run scoreboard players set #mine_goal so_ev 150",
    "execute unless score #active so_ev matches 0.. run scoreboard players set #active so_ev 0",
    f"bossbar add {NS}:ev {T({'text': 'Evento'})}",
    f"bossbar add {NS}:boss {T({'text': 'Jefe'})}",
    f"bossbar set {NS}:ev color yellow", f"bossbar set {NS}:boss color red",
    f"tellraw @a[tag=oneblock_admin] {T({'text': '[SO Events] ', 'color': 'gold'}, {'text': 'cargado. Ayuda: /function so_events:admin/help', 'color': 'gray'})}",
])
F("tick", [
    f"execute as @a[scores={{evento=1..}}] run function {NS}:lib/info",
    "scoreboard players reset @a evento", "scoreboard players enable @a evento",
    "scoreboard players add #beat so_ev 1",
    f"execute if score #beat so_ev matches 20.. run function {NS}:lib/second",
    "execute if score #beat so_ev matches 20.. run scoreboard players set #beat so_ev 0",
])
F("lib/blocks", [
    "# Lee el progreso sin escribir el contador de Simply OneBlock.",
    "scoreboard players set #blk so_ev 0",
    "execute if score fake_player ib_minedcount matches -2147483648.. run scoreboard players operation #blk so_ev = fake_player ib_minedcount",
    "execute if score #blocks so_core matches -2147483648.. run scoreboard players operation #blk so_ev = #blocks so_core",
])
F("lib/second", [
    f"function {NS}:lib/blocks",
    "execute unless score #next so_ev matches 1.. run scoreboard players operation #next so_ev = #blk so_ev",
    "execute unless score #next so_ev matches 1.. run scoreboard players operation #next so_ev += #every so_ev",
    "execute if score #next so_ev < #min so_ev run scoreboard players operation #next so_ev = #min so_ev",
    f"execute if score #enabled so_ev matches 1 if score #auto so_ev matches 1 if score #active so_ev matches 0 if score #blk so_ev >= #next so_ev run function {NS}:lib/auto",
    f"execute if score #active so_ev matches 1 run function {NS}:event/rain/second",
    f"execute if score #active so_ev matches 3 run function {NS}:event/mining/second",
    f"execute if score #active so_ev matches 4 run function {NS}:event/trader/second",
    f"execute if score #active so_ev matches 5 run function {NS}:event/invasion/second",
    f"execute if score #active so_ev matches 6 run function {NS}:event/dark/second",
    f"execute if entity @e[tag=so_ev_boss,limit=1] store result bossbar {NS}:boss value run data get entity @e[tag=so_ev_boss,limit=1] Health",
    f"execute unless entity @e[tag=so_ev_boss,limit=1] run bossbar set {NS}:boss visible false",
])
F("lib/auto", [
    "scoreboard players operation #next so_ev = #blk so_ev",
    "scoreboard players operation #next so_ev += #every so_ev",
    "scoreboard players set #n so_ev 0",
    "execute positioned 0 64 0 store result score #n so_ev if entity @a[distance=..64,gamemode=!spectator]",
    "# Sin nadie en la isla: se pospone un poco.",
    "execute if score #n so_ev matches 0 run scoreboard players operation #next so_ev = #blk so_ev",
    "execute if score #n so_ev matches 0 run scoreboard players add #next so_ev 50",
    "execute if score #n so_ev matches 0 run return 0",
    "execute store result score #r so_ev run random value 1..6",
    "# Noche oscura solo desde la fase 5 (1668 bloques).",
    "execute if score #r so_ev matches 6 if score #blk so_ev matches ..1667 run scoreboard players set #r so_ev 1",
    f"execute if score #r so_ev matches 1 run function {NS}:event/rain/start",
    f"execute if score #r so_ev matches 2 run function {NS}:event/supply/start",
    f"execute if score #r so_ev matches 3 run function {NS}:event/mining/start",
    f"execute if score #r so_ev matches 4 run function {NS}:event/trader/start",
    f"execute if score #r so_ev matches 5 run function {NS}:event/invasion/start",
    f"execute if score #r so_ev matches 6 run function {NS}:event/dark/start",
])
F("lib/begin", [
    "# Comun a todo evento: participantes, alerta y temporizador.",
    "tag @a remove so_ev_in", NEAR,
    "scoreboard players set #t so_ev 0",
    f"bossbar set {NS}:ev players {IN}", f"bossbar set {NS}:ev visible true",
    "playsound minecraft:block.bell.use master @a ~ ~ ~ 1 0.8",
])
F("lib/cleanup", [
    "# Limpieza total: mobs al vacío (sin drops), barras, marcas y regla de griefing.",
    "tp @e[tag=so_ev_mob] 0 -300 0", "kill @e[tag=so_ev_mob]",
    f"bossbar set {NS}:ev visible false", f"bossbar set {NS}:boss visible false",
    "execute if score #mg_saved so_ev matches 1 if score #mg_prev so_ev matches 1 run gamerule mob_griefing true",
    "scoreboard players set #mg_saved so_ev 0",
    "effect clear @a[tag=so_ev_in] minecraft:darkness",
    "tag @a remove so_ev_in",
    "scoreboard players set #active so_ev 0", "scoreboard players set #t so_ev 0",
    "scoreboard players set #stage so_ev 0", "scoreboard players set #wave so_ev 0",
])
F("lib/no_grief", [
    "execute unless score #mg_saved so_ev matches 1 store result score #mg_prev so_ev run gamerule mob_griefing",
    "scoreboard players set #mg_saved so_ev 1",
    "gamerule mob_griefing false",
])
F("lib/info", [
    f"execute if score #active so_ev matches 0 run tellraw @s {T(PFX, {'text': 'No hay ningún evento activo. Próximo cerca de los ', 'color': 'gray', 'bold': False}, {'score': {'name': '#next', 'objective': 'so_ev'}, 'color': 'white'}, {'text': ' bloques.', 'color': 'gray'})}",
    f"execute if score #active so_ev matches 1 run tellraw @s {T(PFX, {'text': 'Lluvia de recursos en la isla.', 'color': 'aqua', 'bold': False})}",
    f"execute if score #active so_ev matches 3 run tellraw @s {T(PFX, {'text': 'Desafío de minería: ', 'color': 'aqua', 'bold': False}, {'score': {'name': '#prog', 'objective': 'so_ev'}, 'color': 'white'}, {'text': '/', 'color': 'gray'}, {'score': {'name': '#mine_goal', 'objective': 'so_ev'}, 'color': 'white'})}",
    f"execute if score #active so_ev matches 4 run tellraw @s {T(PFX, {'text': 'Un mercader errante visita la isla.', 'color': 'aqua', 'bold': False})}",
    f"execute if score #active so_ev matches 5 run tellraw @s {T(PFX, {'text': 'Invasión en curso: oleada ', 'color': 'red', 'bold': False}, {'score': {'name': '#wave', 'objective': 'so_ev'}, 'color': 'white'}, {'text': '/3', 'color': 'gray'})}",
    f"execute if score #active so_ev matches 6 run tellraw @s {T(PFX, {'text': 'Noche oscura: sobreviví hasta el amanecer.', 'color': 'dark_purple', 'bold': False})}",
])

# ---------------------------------------------------------------- 1 lluvia de recursos (60 s)
F("event/rain/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 1",
    f"bossbar set {NS}:ev name {T({'text': 'Lluvia de recursos', 'color': 'aqua'})}", f"bossbar set {NS}:ev max 60", f"bossbar set {NS}:ev color blue",
    f"title {IN} title {T({'text': '¡Lluvia de recursos!', 'color': 'aqua', 'bold': True})}",
    say("@a", "Cae una lluvia de recursos sobre la isla durante 60 segundos.", "aqua")])
F("event/rain/second", ["scoreboard players add #t so_ev 1", NEAR,
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    "execute store result score #r so_ev run random value 1..3",
    f"execute if score #r so_ev matches 1 as {IN} at @s run loot spawn ~ ~4 ~ loot {NS}:rain",
    f"execute as {IN} at @s run particle minecraft:happy_villager ~ ~3 ~ 2 1 2 0 10",
    f"execute if score #t so_ev matches 60.. run function {NS}:lib/cleanup"])

# ---------------------------------------------------------------- 2 suministro (instantaneo)
F("event/supply/start", ["tag @a remove so_ev_in", NEAR,
    f"execute as {IN} at @s run loot spawn ~ ~3 ~ loot {NS}:supply",
    f"execute as {IN} at @s run particle minecraft:firework ~ ~3 ~ 0.4 0.4 0.4 0.05 40",
    "execute as @a[tag=so_ev_in] at @s run playsound minecraft:entity.firework_rocket.blast master @s ~ ~ ~ 1 1",
    f"title {IN} title {T({'text': '¡Suministro!', 'color': 'gold', 'bold': True})}",
    say("@a", "Cayó un suministro sobre la isla. ¡Juntalo antes que caiga al vacío!", "gold"),
    "tag @a remove so_ev_in"])

# ---------------------------------------------------------------- 3 desafio de mineria (180 s)
F("event/mining/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 3",
    "scoreboard players operation #start so_ev = #blk so_ev", "scoreboard players set #prog so_ev 0",
    f"bossbar set {NS}:ev name {T({'text': 'Desafío de minería', 'color': 'green'})}", f"bossbar set {NS}:ev color green",
    f"execute store result bossbar {NS}:ev max run scoreboard players get #mine_goal so_ev", f"bossbar set {NS}:ev value 0",
    f"title {IN} title {T({'text': '¡Desafío de minería!', 'color': 'green', 'bold': True})}",
    f"tellraw @a {T(PFX, {'text': 'Rompan ', 'color': 'green', 'bold': False}, {'score': {'name': '#mine_goal', 'objective': 'so_ev'}, 'color': 'white'}, {'text': ' bloques del OneBlock entre todos en 3 minutos.', 'color': 'green'})}"])
F("event/mining/second", ["scoreboard players add #t so_ev 1", NEAR,
    "scoreboard players operation #prog so_ev = #blk so_ev", "scoreboard players operation #prog so_ev -= #start so_ev",
    f"execute store result bossbar {NS}:ev value run scoreboard players get #prog so_ev",
    f"bossbar set {NS}:ev players {IN}",
    f"execute if score #prog so_ev >= #mine_goal so_ev run function {NS}:event/mining/win",
    f"execute if score #active so_ev matches 3 if score #t so_ev matches 180.. run function {NS}:event/mining/fail"])
F("event/mining/win", [f"execute as {IN} run loot give @s loot {NS}:reward_small",
    say("@a", "¡Desafío superado! Recompensa entregada a los participantes.", "green"),
    "execute as @a[tag=so_ev_in] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1", f"function {NS}:lib/cleanup"])
F("event/mining/fail", [say("@a", "Se acabó el tiempo del desafío de minería.", "gray"), f"function {NS}:lib/cleanup"])

# ---------------------------------------------------------------- 4 mercader errante especial (5 min)
def offer(buy, bc, sell, sc, uses):
    return f'{{buy:{{id:"minecraft:{buy}",count:{bc}}},sell:{{id:"minecraft:{sell}",count:{sc}}},maxUses:{uses}}}'
OFFERS = ",".join([offer("emerald", 10, "diamond", 1, 4), offer("emerald", 6, "golden_apple", 1, 3), offer("emerald", 4, "ender_pearl", 2, 4),
                   offer("emerald", 8, "experience_bottle", 16, 3), offer("emerald", 16, "netherite_scrap", 1, 1), offer("emerald", 12, "heart_of_the_sea", 1, 1),
                   offer("diamond", 2, "emerald", 24, 4), offer("emerald", 20, "totem_of_undying", 1, 1)])
F("event/trader/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 4",
    f"bossbar set {NS}:ev name {T({'text': 'Mercader errante', 'color': 'aqua'})}", f"bossbar set {NS}:ev max 300", f"bossbar set {NS}:ev color blue",
    f'execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run summon minecraft:wandering_trader ~ ~ ~ {{Tags:["so_ev_mob"],Invulnerable:1b,NoAI:1b,PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{{text:"Mercader de Eventos",color:"aqua",bold:true}},Offers:{{Recipes:[{OFFERS}]}}}}',
    say("@a", "Un mercader especial apareció en la isla por 5 minutos.", "aqua")])
F("event/trader/second", ["scoreboard players add #t so_ev 1",
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    f"execute if score #t so_ev matches 300.. run tellraw @a {T(PFX, {'text': 'El mercader se fue.', 'color': 'gray', 'bold': False})}",
    f"execute if score #t so_ev matches 300.. run function {NS}:lib/cleanup"])

# ---------------------------------------------------------------- 5 invasion: cuenta atras, 3 oleadas, jefe
INV = {  # tipo: (nombre, color, oleadas, jefe)
    1: ("Horda de zombis", "dark_green", [["husk", "zombie"], ["husk", "zombie", "zombie"], ["zombie", "husk", "zombie_armor"]], "rey_zombi"),
    2: ("Ataque de slimes", "green", [["slime", "slime"], ["slime", "slime_big"], ["slime_big", "slime_big", "slime"]], "slime_rey"),
    3: ("Oleada acorazada", "gray", [["zombie_armor", "skeleton"], ["zombie_armor", "skeleton_armor"], ["zombie_armor", "skeleton_armor", "spider"]], "comandante"),
    4: ("Raid de saqueadores", "dark_red", [["pillager", "pillager"], ["pillager", "vindicator"], ["vindicator", "pillager", "vindicator"]], "capitan"),
    5: ("Invasión del Nether", "dark_purple", [["magma_cube", "blaze"], ["blaze", "wither_skeleton"], ["wither_skeleton", "blaze", "magma_cube"]], "caballero"),
}
F("event/invasion/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 5",
    "scoreboard players set #stage so_ev 0", "scoreboard players set #wave so_ev 0", f"function {NS}:lib/no_grief",
    "execute unless score #force_type so_ev matches 1..5 run function so_events:event/invasion/pick",
    "execute if score #force_type so_ev matches 1..5 run scoreboard players operation #type so_ev = #force_type so_ev",
    "scoreboard players set #force_type so_ev 0",
    f"bossbar set {NS}:ev color red", f"bossbar set {NS}:ev max 10",
    *[f"execute if score #type so_ev matches {k} run bossbar set {NS}:ev name {T({'text': '¡' + v[0] + '!', 'color': v[1], 'bold': True})}" for k, v in INV.items()],
    *[f"execute if score #type so_ev matches {k} run tellraw @a {T(PFX, {'text': '¡ALERTA! ' + v[0] + ' en 10 segundos. Defiendan la isla.', 'color': 'red', 'bold': True})}" for k, v in INV.items()],
    "playsound minecraft:event.raid.horn master @a ~ ~ ~ 1 1"])
F("event/invasion/pick", [
    "# Tipo segun fase: slimes/zombis al inicio, acorazados y raid luego, Nether desde 6667.",
    "execute store result score #type so_ev run random value 1..2",
    "execute if score #blk so_ev matches 2501.. store result score #type so_ev run random value 1..4",
    "execute if score #blk so_ev matches 6667.. store result score #type so_ev run random value 1..5"])
F("event/invasion/second", ["scoreboard players add #t so_ev 1", NEAR, f"bossbar set {NS}:ev players {IN}",
    f"execute if score #stage so_ev matches 0 run function {NS}:event/invasion/countdown",
    f"execute if score #stage so_ev matches 1 run function {NS}:event/invasion/waves",
    f"execute if score #stage so_ev matches 2 unless entity @e[tag=so_ev_boss] run function {NS}:event/invasion/win",
    f"execute if score #active so_ev matches 5 if score #t so_ev matches 420.. run function {NS}:event/invasion/fail",
    f"execute if score #active so_ev matches 5 unless entity @a[tag=so_ev_in] run function {NS}:event/invasion/fail"])
F("event/invasion/countdown", [
    "scoreboard players set #cd so_ev 10", "scoreboard players operation #cd so_ev -= #t so_ev",
    f"execute store result bossbar {NS}:ev value run scoreboard players get #cd so_ev",
    f"execute if score #cd so_ev matches 1.. run title {IN} actionbar {T({'text': 'La invasión empieza en ', 'color': 'red'}, {'score': {'name': '#cd', 'objective': 'so_ev'}, 'color': 'white', 'bold': True})}",
    f"execute if score #cd so_ev matches ..0 run function {NS}:event/invasion/next"])
F("event/invasion/next", [
    "scoreboard players set #stage so_ev 1", "scoreboard players add #wave so_ev 1", "scoreboard players set #wt so_ev 0",
    f"bossbar set {NS}:ev max 3", f"execute store result bossbar {NS}:ev value run scoreboard players get #wave so_ev",
    f"execute if score #wave so_ev matches 4.. run function {NS}:event/invasion/boss",
    *[f"execute if score #wave so_ev matches {w} if score #type so_ev matches {k} run function {NS}:event/invasion/w_{k}_{w}" for k in INV for w in (1, 2, 3)],
    f"execute if score #wave so_ev matches 1..3 run title {IN} title {T({'text': 'Oleada ', 'color': 'red', 'bold': True}, {'score': {'name': '#wave', 'objective': 'so_ev'}, 'color': 'white'})}",
    "execute if score #wave so_ev matches 1..3 run playsound minecraft:entity.zombie.ambient hostile @a[tag=so_ev_in] ~ ~ ~ 1 0.7"])
for k, (_, _, waves, bname) in INV.items():
    for w, mobs in enumerate(waves, 1):
        F(f"event/invasion/w_{k}_{w}", [spawn(m) for m in mobs])
F("event/invasion/waves", [
    "scoreboard players add #wt so_ev 1",
    "execute store result score #alive so_ev if entity @e[tag=so_ev_mob]",
    f"title {IN} actionbar {T({'text': 'Enemigos restantes: ', 'color': 'red'}, {'score': {'name': '#alive', 'objective': 'so_ev'}, 'color': 'white', 'bold': True})}",
    f"execute if score #alive so_ev matches 0 if score #wt so_ev matches 3.. run function {NS}:event/invasion/next",
    f"execute if score #wt so_ev matches 90.. run function {NS}:event/invasion/next"])
F("event/invasion/boss", ["scoreboard players set #stage so_ev 2",
    *[f'execute if score #type so_ev matches {k} as @a[tag=so_ev_in,limit=1,sort=random] at @s run function {NS}:lib/spawn {{mob:"boss/{v[3]}"}}' for k, v in INV.items()],
    f"title {IN} title {T({'text': '¡JEFE INVASOR!', 'color': 'dark_red', 'bold': True})}"])
F("event/invasion/win", [f"execute as {IN} run loot give @s loot {NS}:reward_big",
    say("@a", "¡Invasión derrotada! Cada defensor recibió su recompensa.", "green"),
    f"title {IN} title {T({'text': '¡Victoria!', 'color': 'green', 'bold': True})}",
    "execute as @a[tag=so_ev_in] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1", f"function {NS}:lib/cleanup"])
F("event/invasion/fail", [say("@a", "La invasión se retiró sin vencedores. No hubo recompensa.", "gray"), f"function {NS}:lib/cleanup"])

# ---------------------------------------------------------------- 6 noche oscura (90 s)
F("event/dark/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 6", f"function {NS}:lib/no_grief",
    f"bossbar set {NS}:ev name {T({'text': 'Noche oscura', 'color': 'dark_purple'})}", f"bossbar set {NS}:ev max 90", f"bossbar set {NS}:ev color purple",
    f"title {IN} title {T({'text': 'Noche oscura', 'color': 'dark_purple', 'bold': True})}",
    say("@a", "La oscuridad cubre la plataforma. Sobrevivan 90 segundos.", "dark_purple")])
F("event/dark/second", ["scoreboard players add #t so_ev 1", NEAR,
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    f"effect give {IN} minecraft:darkness 3 0 true",
    "scoreboard players operation #m so_ev = #t so_ev", "scoreboard players operation #m so_ev %= #twenty so_ev",
    f"execute if score #m so_ev matches 1 run function {NS}:event/dark/spawn",
    f"execute if score #t so_ev matches 90.. run function {NS}:event/dark/end"])
F("event/dark/spawn", [spawn("zombie"), spawn("skeleton"), spawn("spider")])
F("event/dark/end", [f"execute as {IN} run loot give @s loot {NS}:reward_small",
    say("@a", "Amaneció. Los sobrevivientes recibieron una recompensa.", "green"), f"function {NS}:lib/cleanup"])
# constante para el modulo
lines = open(os.path.join(ROOT, f"data/{NS}/function/load.mcfunction"), encoding="utf-8").read()
W(f"data/{NS}/function/load.mcfunction", lines + "scoreboard players set #twenty so_ev 20\n")

# ---------------------------------------------------------------- API para so_arenas
F("api/boss", ["# Uso: execute positioned X Y Z run function so_events:api/boss {id:\"rey_zombi\"}", "$function so_events:boss/$(id)"])
F("api/mob", ["# Uso: execute positioned X Y Z run function so_events:api/mob {id:\"husk\"}", "$function so_events:mob/$(id)"])
F("api/cleanup", [f"function {NS}:lib/cleanup"])

# ---------------------------------------------------------------- admin
EVS = {"lluvia": "rain", "suministro": "supply", "mineria": "mining", "mercader": "trader", "invasion": "invasion", "oscuridad": "dark"}
for es, en in EVS.items():
    F(f"admin/start_{es}", [f"function {NS}:lib/blocks", f"execute unless score #active so_ev matches 0 run function {NS}:lib/cleanup",
                            f"function {NS}:event/{en}/start"])
for k in INV:
    F(f"admin/start_invasion_{k}", [f"scoreboard players set #force_type so_ev {k}", f"function {NS}:admin/start_invasion"])
F("admin/stop", [f"function {NS}:lib/cleanup", say("@a", "Evento detenido por un administrador.", "gray")])
F("admin/enable", ["scoreboard players set #enabled so_ev 1", say("@s", "Eventos activados.", "green")])
F("admin/disable", [f"function {NS}:lib/cleanup", "scoreboard players set #enabled so_ev 0", say("@s", "Eventos desactivados.", "red")])
F("admin/auto_on", ["scoreboard players set #auto so_ev 1", say("@s", "Eventos automáticos por bloques: ON.", "green")])
F("admin/auto_off", ["scoreboard players set #auto so_ev 0", say("@s", "Eventos automáticos por bloques: OFF.", "red")])
F("admin/status", [f"function {NS}:lib/blocks",
    f"tellraw @s {T(PFX, {'text': 'activo=', 'color': 'gray', 'bold': False}, {'score': {'name': '#active', 'objective': 'so_ev'}, 'color': 'white'}, {'text': '  bloques=', 'color': 'gray'}, {'score': {'name': '#blk', 'objective': 'so_ev'}, 'color': 'white'}, {'text': '  próximo=', 'color': 'gray'}, {'score': {'name': '#next', 'objective': 'so_ev'}, 'color': 'white'}, {'text': '  cada=', 'color': 'gray'}, {'score': {'name': '#every', 'objective': 'so_ev'}, 'color': 'white'})}"])
HELP = ["SO Events — ayuda admin",
        "/function so_events:admin/start_<lluvia|suministro|mineria|mercader|invasion|oscuridad>",
        "/function so_events:admin/start_invasion_<1..5>  (1 zombis, 2 slimes, 3 acorazados, 4 raid, 5 Nether)",
        "/function so_events:admin/stop | status | enable | disable | auto_on | auto_off",
        "/scoreboard players set #every so_ev 400   (bloques entre eventos)",
        "/scoreboard players set #min so_ev 300     (primer evento posible)",
        "/scoreboard players set #mine_goal so_ev 150",
        "Jugadores: /trigger evento  (estado del evento actual)"]
F("admin/help", [f"tellraw @s {T({'text': h, 'color': 'gold' if i == 0 else 'gray'})}" for i, h in enumerate(HELP)])
F("uninstall", [f"function {NS}:lib/cleanup", f"bossbar remove {NS}:ev", f"bossbar remove {NS}:boss",
                "scoreboard objectives remove so_ev", "scoreboard objectives remove evento",
                say("@s", "so_events desinstalado. Quitá el datapack y hacé /reload.", "gray")])

W("README.md", """# so_events v1 — lo que pasa en la isla

Eventos automáticos cada `#every` bloques minados (por defecto 400, el primero desde 300), solo si hay alguien en la isla (64 bloques alrededor de 0 64 0).

| Evento | Duración | Qué pasa |
|---|---|---|
| Lluvia de recursos | 60 s | Caen materiales sobre los jugadores |
| Suministro | instantáneo | Cae un paquete de botín sobre cada jugador |
| Desafío de minería | 3 min | Romper `#mine_goal` bloques entre todos |
| Mercader errante | 5 min | Mercader especial con ofertas raras |
| Invasión | hasta 7 min | Alerta, cuenta atrás, 3 oleadas y jefe invasor |
| Noche oscura | 90 s | Oscuridad + mobs cada 20 s (desde fase 5) |

Invasiones según fase: zombis/slimes al inicio, acorazados y raid desde 2501, Nether desde 6667.
Sin creepers, `mob_griefing` desactivado durante el evento y restaurado al final, mobs que nunca aparecen sobre el vacío, limpieza total al terminar y recompensa para todos los participantes.

Jefes: Rey Zombi, Slime Rey, Comandante Óseo, Capitán Saqueador, Caballero del Nether.

Para `so_arenas`: `function so_events:api/boss {id:"rey_zombi"}`, `api/mob {id:"husk"}`, `api/cleanup`.
Ayuda admin: `/function so_events:admin/help`. Jugadores: `/trigger evento`.
""")

# ---------------------------------------------------------------- zip (raiz limpia)
os.makedirs("/mnt/documents", exist_ok=True)
out = "/mnt/documents/so_events-v1.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for d, _, files in os.walk(ROOT):
        for f in files:
            full = os.path.join(d, f); z.write(full, os.path.relpath(full, ROOT))
print("ok", out)
