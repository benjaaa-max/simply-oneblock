#!/usr/bin/env python3
"""Generador de so_arenas v3 — el Coliseo VorNeX (donde pasa).

Unica fuente del datapack datapacks/so-arenas (no editar los .mcfunction a mano).
v3:
- Flujo de combate: menú -> túnel de preparación (DJ + mutadores) -> campana/placa/cartel
  (o 30 s) -> saludo de jueces + música -> foso. Victoria: portones abiertos 60 s, cofre
  de recompensa variable en el lobby, salida a pie o por la placa del túnel.
- Limpieza quirúrgica: solo ítems/flechas del foso y bloques dentro del óvalo interior
  (R_RESET). Nunca toca muros, gradas, lobby, tocadiscos ni terraza.
- Contratos: Caza, Oleadas, Defensa (cebo vivo + barricadas), Rey de la Colina,
  Asedio Volador, Duelo de Campeones, Desafío de Jefes. PvP amistoso aparte.
- Racha, mutadores, médica, tribunas (espectador), cestas de donación, cohetes en gradas,
  tablero en vivo, palco de jueces, público, terraza con jardines e iluminación integrada.
Salida: datapacks/so-arenas + /mnt/documents/so_arenas-v3.zip (raiz limpia).
"""
import json, os, shutil, zipfile, math, random

ROOT = os.path.join(os.path.dirname(__file__), "..", "datapacks", "so-arenas")
NS = "so_arenas"
VER = "v3"
CX, CZ = -5000, -5000
G = 95                 # bloque del piso; se camina en y=96
AX, BZ = 42, 50        # semiejes exteriores: 84 x 100
TOP_Y = 170
R_PIT, R_PITWALL, R_GRADA, R_WALL = 0.62, 0.65, 0.93, 1.0
R_RESET = 0.58         # óvalo interior que se limpia (siempre dentro del labio/anillo)
R_LIP = R_PIT - 0.035  # labio anti-arañas (losas invertidas) en y=99
TR = 1.22              # borde exterior de la terraza
LZ0, LZ1 = CZ + BZ + 10, CZ + BZ + 30      # lobby: muro norte / muro sur
LX = 11
TZ0 = CZ + int(R_PIT * BZ) + 1            # portón del foso (túnel)
ARR = (CX, 96, LZ1 - 6)                   # llegada al lobby
PIT_IN = (CX, 96, CZ + 14)                # entrada al foso
PIT_IN2 = (CX, 96, CZ - 14)               # lado opuesto (duelo)
STAGE = (CX, 96, TZ0 + 8)                 # preparación en el túnel
JUKE = (CX - 3, 96, TZ0 + 3)              # tocadiscos del DJ
BELL = (CX + 3, 96, TZ0 + 3)              # campana de inicio
START_PLATE = (CX, 96, TZ0 + 1)
EXIT_PLATE = (CX, 96, LZ0 - 1)
REWARD = (CX + 3, 96, LZ0 + 2)            # pedestal del cofre de recompensa
TRASH = (CX - 3, 96, LZ0 + 2)             # tacho de descarte
JUDGE_Z = CZ - 44
PIT_BOX = f"x={CX - 27},y=90,z={CZ - 32},dx=54,dy=50,dz=64"
PIT_FLOOR_BOX = f"x={CX - 27},y=94,z={CZ - 33},dx=54,dy=5,dz=66"
TUNNEL_BOX = f"x={CX - 3},y=95,z={TZ0},dx=6,dy=6,dz={LZ0 - TZ0}"
ZONE_BOX = f"x={CX - 56},y=80,z={CZ - 66},dx=112,dy=130,dz={LZ1 + 12 - (CZ - 66)}"
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


def P(p, dy=0):
    return f"{p[0]} {p[1] + dy} {p[2]}"


IN = "@a[tag=so_ar_in]"
ZONE = "@a[tag=so_ar_zone]"
LOAN = "*[minecraft:custom_data~{so_arena_loan:1b}]"
LOAN_C = 'minecraft:custom_data={so_arena_loan:1b},minecraft:lore=[{text:"Prestado por el Coliseo",color:"gray",italic:false}]'
ANYBLOCK = "minecraft:can_place_on=[{}]"

# ---------------------------------------------------------------- pack
W("pack.mcmeta", {"pack": {"description": f"Simply OneBlock Expansion - Arenas {VER} (/trigger arena)",
                           "min_format": [107, 1], "max_format": [107, 1]}})
W("data/minecraft/tags/function/load.json", {"replace": False, "values": [f"{NS}:load"]})
W("data/minecraft/tags/function/tick.json", {"replace": False, "values": [f"{NS}:tick"]})


# ---------------------------------------------------------------- loot
def item(name, w, lo=1, hi=1):
    e = {"type": "minecraft:item", "name": f"minecraft:{name}", "weight": w}
    if hi > 1: e["functions"] = [{"function": "minecraft:set_count", "count": {"min": lo, "max": hi}}]
    return e


FRAG = {"type": "minecraft:item", "name": "minecraft:echo_shard", "weight": 1,
        "functions": [{"function": "minecraft:set_name", "target": "item_name",
                       "name": {"text": "Fragmento de Victoria", "color": "gold"}}]}
PR_LOOT = {
    1: [item("experience_bottle", 6, 4, 8), item("bread", 4, 3, 6), item("emerald", 4, 2, 5), item("iron_ingot", 3, 1, 3), item("arrow", 3, 8, 16)],
    2: [item("experience_bottle", 6, 6, 12), item("emerald", 5, 3, 8), item("iron_ingot", 4, 2, 5), item("golden_carrot", 3, 3, 6), item("gold_ingot", 2, 1, 4)],
    3: [item("experience_bottle", 6, 10, 18), item("emerald", 5, 5, 12), item("diamond", 2, 1, 2), item("golden_apple", 2, 1, 2), item("ender_pearl", 2, 1, 3)],
    4: [item("experience_bottle", 6, 14, 24), item("emerald", 5, 8, 16), item("diamond", 3, 1, 3), item("golden_apple", 3, 1, 3), item("netherite_scrap", 1)],
}
for t, entries in PR_LOOT.items():
    W(f"data/{NS}/loot_table/practice_t{t}.json", {"type": "minecraft:chest", "pools": [{"rolls": 2 + t // 2, "entries": entries}]})
W(f"data/{NS}/loot_table/contract.json", {"type": "minecraft:chest", "pools": [{"rolls": 4, "entries": [
    item("experience_bottle", 6, 10, 20), item("emerald", 6, 8, 18), item("diamond", 2, 1, 3), item("golden_apple", 2, 1, 2), FRAG]}]})
W(f"data/{NS}/loot_table/boss.json", {"type": "minecraft:chest", "pools": [{"rolls": 6, "entries": [
    item("experience_bottle", 6, 16, 32), item("emerald", 5, 12, 24), item("diamond", 3, 2, 4), item("enchanted_golden_apple", 1),
    item("netherite_scrap", 1, 1, 2), item("totem_of_undying", 1), FRAG]}]})
W(f"data/{NS}/loot_table/streak.json", {"type": "minecraft:chest", "pools": [{"rolls": 3, "entries": [
    item("experience_bottle", 5, 16, 32), item("diamond", 3, 2, 4), item("golden_apple", 3, 2, 4), item("totem_of_undying", 1), FRAG]}]})

# ---------------------------------------------------------------- música
SONGS = [  # (n, id, nombre, duración en s)
    (1, "pigstep", "Pigstep", 148), (2, "otherside", "Otherside", 195), (3, "creator", "Creator", 176),
    (4, "relic", "Relic", 218), (5, "precipice", "Precipice", 299), (6, "strad", "Strad", 188), (7, "chirp", "Chirp", 185),
]

# ---------------------------------------------------------------- load / tick
TRIGGERS = ["arena", "volver", "arena_pr", "arena_con", "levelrank", "arena_dj", "arena_mut", "arena_ver", "arena_pvp"]
OBJS = ["so_ar_air", "so_ar_rank", "so_ar_x", "so_ar_y", "so_ar_z", "so_ar_saved", "so_ar_streak", "so_ar_hp"]
F("load", [
    "scoreboard objectives add so_ar dummy",
    *[f"scoreboard objectives add {t} trigger" for t in TRIGGERS],
    *[f"scoreboard objectives add {o} dummy" for o in OBJS],
    "scoreboard objectives add so_ar_death deathCount",
    "execute unless score #enabled so_ar matches 0..1 run scoreboard players set #enabled so_ar 1",
    "execute unless score #mode so_ar matches 0..10 run scoreboard players set #mode so_ar 0",
    "execute unless score #exit so_ar matches 0..1 run scoreboard players set #exit so_ar 0",
    *[f"execute unless score #{m} so_ar matches 0..1 run scoreboard players set #{m} so_ar 0" for m in ("mut_n", "mut_f", "mut_v", "playing")],
    "execute unless score #song so_ar matches 0..7 run scoreboard players set #song so_ar 0",
    "scoreboard players set #beat so_ar 0",
    "scoreboard players set #twentyfive so_ar 25",
    "scoreboard players set #ten so_ar 10",
    "scoreboard players set #fifteen so_ar 15",
    "scoreboard players set #anticamp so_ar 1",
    f"bossbar add {NS}:fight {T({'text': 'Coliseo'})}",
    f"bossbar set {NS}:fight max 100", f"bossbar set {NS}:fight visible false",
    f"tellraw @a[tag=oneblock_admin] {T({'text': '[SO Arenas] ', 'color': 'gold'}, {'text': VER + ' cargado. Ayuda: /function so_arenas:admin/help', 'color': 'gray'})}",
])
F("tick", [
    "scoreboard players add #beat so_ar 1",
    f"execute as @a[scores={{arena=1..}}] at @s run function {NS}:lib/go",
    f"execute as @a[scores={{volver=1..}}] at @s run function {NS}:lib/volver",
    f"execute as @a[scores={{arena_pr=1..}}] at @s run function {NS}:lib/start_pr",
    f"execute as @a[scores={{arena_con=1..}}] at @s run function {NS}:lib/start_con",
    f"execute as @a[scores={{levelrank=1..}}] run function {NS}:lib/rank",
    f"execute as @a[scores={{arena_dj=1..}}] run function {NS}:lib/dj",
    f"execute as @a[scores={{arena_mut=1..}}] run function {NS}:lib/mut",
    f"execute as @a[scores={{arena_ver=1..}}] at @s run function {NS}:lib/ver",
    f"execute as @a[scores={{arena_pvp=1..}}] at @s run function {NS}:lib/pvp",
    *[f"scoreboard players reset @a {t}" for t in TRIGGERS],
    *[f"scoreboard players enable @a {t}" for t in TRIGGERS],
    "# duelo: vida chequeada cada tick (se corta antes de morir)",
    f"execute if score #mode so_ar matches 10 run function {NS}:mode/pvp/tick",
    f"execute if score #beat so_ar matches 10 run function {NS}:lib/pads",
    f"execute if score #beat so_ar matches 20.. run function {NS}:lib/pads",
    f"execute if score #beat so_ar matches 20.. run function {NS}:lib/second",
    "execute if score #beat so_ar matches 20.. run scoreboard players set #beat so_ar 0",
])
FIGHT = "1..8"  # modos de desafío PvE (9 = preparación, 10 = duelo PvP)
F("lib/second", [
    "# Zona: quien sale (o muere y reaparece afuera) pierde marcas y kit; quien entra volando queda marcado.",
    f"execute as {ZONE} at @s unless dimension minecraft:overworld run function {NS}:lib/leave",
    f"execute as {ZONE} at @s unless entity @s[{ZONE_BOX}] run function {NS}:lib/leave",
    f"execute as @a[tag=!so_ar_zone,{ZONE_BOX}] at @s if dimension minecraft:overworld run function {NS}:lib/enter_zone",
    "# Muertes: cortan la racha.",
    f"execute as @a[scores={{so_ar_death=1..}}] run function {NS}:lib/died",
    "# Participantes: quienes están dentro del foso.",
    "tag @a remove so_ar_in",
    f"execute as @a[tag=so_ar_zone,{PIT_BOX}] run tag @s add so_ar_in",
    "# Kits prestados tirados al piso: se borran (no se exportan).",
    f"kill @e[type=minecraft:item,{ZONE_BOX},nbt={{Item:{{components:{{\"minecraft:custom_data\":{{so_arena_loan:1b}}}}}}}}]",
    f"function {NS}:lib/trash",
    f"function {NS}:lib/donations",
    f"execute if score #mode so_ar matches 9 run function {NS}:lib/stage_second",
    f"execute if score #mode so_ar matches 1 run function {NS}:mode/practice/second",
    f"execute if score #mode so_ar matches 2 run function {NS}:mode/caza/second",
    f"execute if score #mode so_ar matches 3 run function {NS}:mode/defensa/second",
    f"execute if score #mode so_ar matches 4 run function {NS}:mode/caza2/second",
    f"execute if score #mode so_ar matches 5 run function {NS}:mode/rey/second",
    f"execute if score #mode so_ar matches 6 run function {NS}:mode/jefes/second",
    f"execute if score #mode so_ar matches 7 run function {NS}:mode/asedio/second",
    f"execute if score #mode so_ar matches 10 run function {NS}:mode/pvp/second",
    f"execute if score #mode so_ar matches {FIGHT} if score #mut_n so_ar matches 1 run effect give {IN} minecraft:darkness 3 0 true",
    f"execute if score #mode so_ar matches 1..8 if score #anticamp so_ar matches 1 run function {NS}:lib/anticamp",
    f"execute if score #mode so_ar matches 10 run function {NS}:lib/anticamp",
    f"execute if score #mode so_ar matches {FIGHT} unless entity {IN} run function {NS}:lib/vacio",
    f"execute if score #mode so_ar matches {FIGHT} run function {NS}:lib/board",
    f"execute if score #playing so_ar matches 1 run function {NS}:lib/music_second",
    f"execute if score #exit so_ar matches 1 run function {NS}:lib/exit_second",
    f"execute if score #mode so_ar matches 0 if score #exit so_ar matches 0 as @a[tag=so_ar_zone,tag=!so_ar_in,tag=!so_ar_spec] run title @s actionbar {T({'text': 'Menú: aldeanos, carteles, placas del piso o /trigger arena', 'color': 'gray'})}",
])
F("lib/died", [
    "scoreboard players reset @s so_ar_death",
    "execute if score @s so_ar_streak matches 1.. run tellraw @s " + T(PFX, {"text": "Moriste: tu racha de victorias vuelve a 0.", "color": "red", "bold": False}),
    "scoreboard players set @s so_ar_streak 0",
])

# ---------------------------------------------------------------- viaje
F("lib/go", [
    f"execute if score @s arena matches 2 run return run function {NS}:lib/volver",
    f'execute if score #enabled so_ar matches 0 run return run {say("@s", "La arena está desactivada por un administrador.", "red")}',
    f"execute if entity @s[tag=so_ar_zone] run return run function {NS}:lib/menu",
    f'execute unless dimension minecraft:overworld run return run {say("@s", "Solo podés viajar desde el mundo normal (no desde el Nether, el End ni las fases).", "red")}',
    "execute store result score @s so_ar_x run data get entity @s Pos[0]",
    "execute store result score @s so_ar_y run data get entity @s Pos[1]",
    "execute store result score @s so_ar_z run data get entity @s Pos[2]",
    "scoreboard players set @s so_ar_saved 1",
    f"tp @s {P(ARR)} 180 0",
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
    f"execute if score #playing so_ar matches 1 run function {NS}:lib/music_one",
])
F("lib/leave", [
    "tag @s remove so_ar_zone", "tag @s remove so_ar_in", "tag @s remove so_ar_pad",
    "tag @s remove so_ar_ready", "tag @s remove so_ar_win", "tag @s remove so_ar_pvpw",
    f"clear @s {LOAN}",
    "tag @s remove so_ar_loan",
    "execute if entity @s[tag=so_ar_spec] run effect clear @s minecraft:invisibility",
    "tag @s remove so_ar_spec",
    "execute if entity @s[tag=so_ar_gm,gamemode=adventure] run gamemode survival @s",
    "tag @s remove so_ar_gm",
    "stopsound @s record",
    "scoreboard players reset @s so_ar_air",
])
F("lib/volver", [
    f'execute unless entity @s[tag=so_ar_zone] run return run {say("@s", "Este comando solo funciona dentro del Coliseo. Para ir: /trigger arena", "red")}',
    f"execute if score #mode so_ar matches {FIGHT} if entity @s[tag=so_ar_in] run function {NS}:lib/abandono",
    f"execute if score #mode so_ar matches 10 if entity @s[tag=so_ar_pvp] run function {NS}:mode/pvp/lose",
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
    "# Huyó en pleno desafío: pierde recompensa, kit y racha. El resto sigue peleando.",
    "title @s times 0 60 20",
    f'title @s title {T({"text": "¡ABANDONASTE,", "color": "red", "bold": True}, {"text": " CAGÓN!", "color": "dark_red", "bold": True})}',
    "playsound minecraft:entity.villager.no master @s ~ ~ ~ 1 0.7",
    "scoreboard players set @s so_ar_streak 0",
    say(ZONE, "Un gladiador abandonó el desafío.", "red"),
])
F("lib/menu", [f"dialog show @s {NS}:main", f"function {NS}:lib/chat_main"])


# ---------------------------------------------------------------- menú del chat (Java)
def link(label, cmd, color, tip):
    return {"text": label, "color": color, "click_event": {"action": "run_command", "command": cmd},
            "hover_event": {"action": "show_text", "value": tip}}


CONTRACTS = [  # (n, nombre corto, nombre, bloques mínimos, descripción)
    (1, "Caza", "Caza: 15 bajas objetivo", 400, "15 objetivos en tandas, con apoyo mixto según tu fase."),
    (2, "Oleadas", "Oleadas dobles", 400, "3 oleadas, cada una más dura."),
    (3, "Defensa", "Defensa del Núcleo", 2501, "2 minutos. Cebo vivo: todos van al núcleo. Te damos barricadas."),
    (4, "Rey", "Rey de la Colina", 400, "Aguantá 90 s dentro del círculo de luz central."),
    (5, "Asedio", "Asedio Volador", 2501, "Phantoms y vexes: arco, ballesta y escudo."),
    (6, "Duelo", "Duelo de Campeones", 3334, "3 minijefes seguidos, 10 s de respiro entre cada uno."),
    (7, "Jefes", "Desafío de Jefes", 6667, "5 jefes de tu fase en cadena. Botín de jefe."),
]


def fmt(n):
    return f"{n:,}".replace(",", ".")


F("lib/chat_main", [
    f"tellraw @s {T({'text': '━━━ Coliseo VorNeX ━━━', 'color': 'gold', 'bold': True})}",
    f"tellraw @s {T({'text': ' Práctica: ', 'color': 'gray'}, *[x for t in range(1, 5) for x in (link(f'[T{t}]', f'/trigger arena_pr set {t}', 'yellow', f'Tier {t} con kit prestado'), link(f'[T{t}+propio] ', f'/trigger arena_pr set {t + 10}', 'gold', f'Tier {t} con tu equipo'))])}",
    f"tellraw @s {T({'text': ' Contratos: ', 'color': 'gray'}, *[link(f'[{s}] ', f'/trigger arena_con set {n}', 'aqua', f'{name} ({fmt(b)}+): {d}') for n, s, name, b, d in CONTRACTS])}",
    f"tellraw @s {T({'text': ' Música: ', 'color': 'gray'}, *[link(f'[{name}] ', f'/trigger arena_dj set {n}', 'light_purple', f'Tema de entrada: {name}') for n, _, name, _ in SONGS], link('[Azar]', '/trigger arena_dj set 8', 'dark_purple', 'Tema al azar'))}",
    f"tellraw @s {T({'text': ' Mutadores (x2 botín): ', 'color': 'gray'}, link('[Niebla] ', '/trigger arena_mut set 1', 'dark_gray', 'Oscuridad constante'), link('[Furia] ', '/trigger arena_mut set 2', 'red', 'Monstruos con Velocidad II'), link('[Vampirismo] ', '/trigger arena_mut set 3', 'dark_red', 'Monstruos con Regeneración II'), link('[Quitar]', '/trigger arena_mut set 4', 'gray', 'Sin mutadores'))}",
    f"tellraw @s {T({'text': ' ', 'color': 'gray'}, link('[Unirse] ', '/trigger arena_con set 9', 'green', 'Entrar al desafío en curso'), link('[Tribunas] ', '/trigger arena_ver', 'aqua', 'Mirar desde las gradas (invisible)'), link('[Duelo PvP] ', '/trigger arena_pvp set 1', 'red', 'Retar o aceptar un duelo amistoso'), link('[Mi rango] ', '/trigger levelrank', 'gray', 'Rango y racha'), link('[Volver a la isla]', '/trigger volver', 'red', 'Salir (si hay desafío: abandono)'))}",
])

# ---------------------------------------------------------------- placas del piso
PADS = [(CX - 3, "pad_pr", "Práctica", "yellow"), (CX - 1, "pad_con", "Contratos", "light_blue"),
        (CX + 1, "pad_join", "Unirse", "lime"), (CX + 3, "pad_back", "Volver", "red")]
PAD_Z = LZ0 + 9


def at_cell(p):
    return f"x={p[0]},y={p[1]},z={p[2]},dx=0,dy=0,dz=0"


F("lib/pads", [
    "execute as @a[tag=so_ar_pad] at @s unless block ~ ~ ~ #minecraft:pressure_plates run tag @s remove so_ar_pad",
    *[f"execute as @a[tag=so_ar_zone,tag=!so_ar_pad,x={x},y=96,z={PAD_Z},dx=0,dy=0,dz=0] run function {NS}:lib/{fn}" for x, fn, _, _ in PADS],
    f"execute if score #mode so_ar matches 9 as @a[tag=so_ar_ready,tag=!so_ar_pad,{at_cell(START_PLATE)}] run function {NS}:lib/pad_start",
    f"execute if score #mode so_ar matches 0 as @a[tag=so_ar_zone,tag=!so_ar_pad,{at_cell(EXIT_PLATE)}] run function {NS}:lib/pad_exit",
])
F("lib/pad_pr", ["tag @s add so_ar_pad", f"dialog show @s {NS}:practice", f"function {NS}:lib/chat_main", "playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.4"])
F("lib/pad_con", ["tag @s add so_ar_pad", f"dialog show @s {NS}:contracts", f"function {NS}:lib/chat_main", "playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.4"])
F("lib/pad_join", ["tag @s add so_ar_pad", f"function {NS}:lib/join"])
F("lib/pad_back", ["tag @s add so_ar_pad", f"function {NS}:lib/volver"])
F("lib/pad_start", ["tag @s add so_ar_pad", f"function {NS}:lib/go_fight"])
F("lib/pad_exit", [
    "tag @s add so_ar_pad",
    f"clear @s {LOAN}", "tag @s remove so_ar_loan",
    f"tp @s {REWARD[0] - 1} 96 {REWARD[2] + 2} 0 0",
    "playsound minecraft:block.iron_door.open master @s ~ ~ ~ 1 1",
    say("@s", "Saliste por el portón. Tu cofre de recompensa está en el pedestal (podés dejar ahí lo que no quieras).", "green"),
])

# ---------------------------------------------------------------- interacciones (aldeanos, campana)
INTER = [  # (id, x, y, z, ancho, alto, acciones)
    ("main", CX, 96, LZ1 - 2, 1.0, 2.1, [f"function {NS}:lib/menu"]),
    ("pr", CX - 7, 96, LZ0 + 4, 1.0, 2.1, [f"dialog show @s {NS}:practice", f"function {NS}:lib/chat_main"]),
    ("con", CX + 7, 96, LZ0 + 4, 1.0, 2.1, [f"dialog show @s {NS}:contracts", f"function {NS}:lib/chat_main"]),
    ("med", CX + 6, 96, LZ0 + 15, 1.0, 2.1, [f"function {NS}:lib/medic"]),
    ("bell", BELL[0], 96, BELL[2], 1.1, 1.1, [f"function {NS}:lib/bell"]),
    ("dj", JUKE[0], 96, JUKE[2], 1.1, 1.1, [f"dialog show @s {NS}:dj"]),
]
MENU_VILLAGERS = [("main", "Guía del Coliseo", "gold"), ("pr", "Maestro de Armas", "yellow"),
                  ("con", "Comandante de Contratos", "aqua"), ("med", "Médica de Campaña", "light_purple")]
for nid, x, y, z, w, h, acts in INTER:
    W(f"data/{NS}/advancement/npc/{nid}.json", {
        "criteria": {"click": {"trigger": "minecraft:player_interacted_with_entity", "conditions": {
            "entity": [{"condition": "minecraft:entity_properties", "entity": "this",
                        "predicate": {"nbt": f"{{Tags:[\"so_ar_npc_{nid}\"]}}"}}]}}},
        "rewards": {"function": f"{NS}:npc/{nid}"}})
    F(f"npc/{nid}", [f"advancement revoke @s only {NS}:npc/{nid}",
                     *(["playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1"] if nid not in ("bell", "dj") else []), *acts])

NEGATIVE = ["poison", "wither", "weakness", "slowness", "mining_fatigue", "nausea", "blindness", "hunger", "darkness", "levitation", "unluck"]
F("lib/medic", [
    "# Médica de campaña: cura, alimenta y quita efectos negativos. Gratis.",
    f'execute if score #mode so_ar matches {FIGHT} if entity @s[tag=so_ar_in] run return run {say("@s", "No puedo atenderte en pleno combate.", "red")}',
    "effect give @s minecraft:instant_health 1 10 true",
    "effect give @s minecraft:saturation 1 20 true",
    *[f"effect clear @s minecraft:{e}" for e in NEGATIVE],
    "playsound minecraft:block.brewing_stand.brew master @s ~ ~ ~ 1 1.2",
    "particle minecraft:heart ~ ~2 ~ 0.4 0.3 0.4 0 6",
    say("@s", "Médica: vida y comida al máximo, efectos negativos fuera. ¡A la arena!", "light_purple"),
])


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

# ---------------------------------------------------------------- rango y racha
F("lib/rank", [
    "# Rangos ocultos: solo se ven con /trigger levelrank.",
    "scoreboard players operation #c so_ar = @s so_ar_rank",
    "execute unless score #c so_ar matches 0.. run scoreboard players set #c so_ar 0",
    "execute unless score @s so_ar_streak matches 0.. run scoreboard players set @s so_ar_streak 0",
    *[f'execute if score #c so_ar matches {rng} run tellraw @s {T(PFX, {"text": "Rango: ", "color": "gray", "bold": False}, {"text": n, "color": c, "bold": True}, {"text": " · Contratos cumplidos: ", "color": "gray", "bold": False}, {"score": {"name": "#c", "objective": "so_ar"}, "color": "white"})}'
      for rng, n, c in [("..2", "Recluta (C)", "white"), ("3..5", "Veterano (B)", "green"), ("6..9", "Élite (A)", "aqua"), ("10..", "Leyenda (S)", "gold")]],
    f'tellraw @s {T(PFX, {"text": "Racha de victorias sin morir: ", "color": "gray", "bold": False}, {"score": {"name": "@s", "objective": "so_ar_streak"}, "color": "yellow", "bold": True}, {"text": " (cofre extra a las 3, 5 y desde 10)", "color": "dark_gray", "bold": False})}',
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
TIERS = [
    (1, "Novato", ["zombie", "skeleton", "spider", "husk"], 0),
    (2, "Veterano", ["zombie_armor", "skeleton_armor", "piglin", "cave_spider", "slime_big"], 3334),
    (3, "Élite", ["vindicator", "pillager", "witch", "drowned_trident", "spider_big"], 7501),
    (4, "Maestro", ["enderman", "breeze", "zombie_ominous", "skeleton_ominous", "bogged", "wither_skeleton"], 15000),
]


def spawn(m, t=0):
    return f'function {NS}:lib/spawn {{m:"{m}",t:{t}}}'


def spawn_boss(b):
    return f'function {NS}:lib/spawn_boss {{b:"{b}"}}'


def busy_guard():
    return [
        f'execute unless entity @s[tag=so_ar_zone] run return run {say("@s", "Primero entrá al Coliseo con /trigger arena.", "red")}',
        f'execute if score #exit so_ar matches 1 run return run {say("@s", "El foso se está despejando. Esperá unos segundos (o salí por el portón).", "red")}',
        f'execute unless score #mode so_ar matches 0 run return run {say("@s", "Ya hay un desafío en curso. Podés unirte con el botón Unirse.", "red")}',
    ]


F("lib/start_pr", [
    f"execute if score @s arena_pr matches 20 run return run function {NS}:npc_menu_pr",
    *busy_guard(),
    f"function {NS}:lib/blocks",
    "scoreboard players operation #tier so_ar = @s arena_pr",
    "execute if score #tier so_ar matches 11..14 run scoreboard players remove #tier so_ar 10",
    "scoreboard players set #loan so_ar 1",
    "execute if score @s arena_pr matches 11..14 run scoreboard players set #loan so_ar 0",
    f'execute unless score #tier so_ar matches 1..4 run return run {say("@s", "Opción de práctica inválida.", "red")}',
    *[f'execute if score #tier so_ar matches {t} unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches {thr}.. run return run {say("@s", f"El Tier {n} se desbloquea a los {fmt(thr)} bloques.", "red")}'
      for t, n, _, thr in TIERS if thr > 0],
    f"execute if score #loan so_ar matches 1 run function {NS}:lib/kit",
    f'execute if score #loan so_ar matches 0 run {say("@s", "Entrás con tu propio equipo: si morís, tus cosas quedan en el foso.", "yellow")}',
    "scoreboard players set #ptype so_ar 1",
    *[f'execute if score #tier so_ar matches {t} run data modify storage so_arenas:b n set value "Práctica · Tier {t} {n}"' for t, n, _, _ in TIERS],
    f"function {NS}:lib/prepare",
])
KIT = {
    1: ["stone_sword", "leather_helmet", "leather_chestplate", "leather_leggings", "leather_boots", ("bread", 8)],
    2: ["iron_sword", "iron_chestplate", "leather_helmet", "leather_leggings", "bow", ("arrow", 24), ("bread", 8)],
    3: ["diamond_sword", "iron_helmet", "iron_chestplate", "iron_leggings", "iron_boots", "shield", "bow", ("arrow", 32), ("golden_apple", 2)],
    4: ["diamond_sword", "diamond_helmet", "diamond_chestplate", "iron_leggings", "iron_boots", "shield", "crossbow", ("arrow", 48), ("golden_apple", 3)],
}
F("lib/kit", [
    "# Kit prestado: todo lleva so_arena_loan y se borra al salir, terminar o tirarlo.",
    *[f'execute if score #tier so_ar matches {t} run give @s {(i if isinstance(i, str) else i[0])}[{LOAN_C}] {1 if isinstance(i, str) else i[1]}'
      for t, items in KIT.items() for i in items],
    "tag @s add so_ar_loan",
    say("@s", "Kit prestado entregado. Se retira solo al terminar o salir.", "yellow"),
])
F("lib/kit_def", [
    "# Barricadas de Defensa: se pueden poner sobre cualquier bloque (modo aventura) y se borran al limpiar el foso.",
    f"give @s minecraft:oak_planks[{LOAN_C},{ANYBLOCK}] 48",
    f"give @s minecraft:cobblestone_wall[{LOAN_C},{ANYBLOCK}] 24",
    "tag @s add so_ar_loan",
    say("@s", "Barricadas prestadas: tablas y muros. Armá defensas alrededor del Núcleo.", "dark_purple"),
])
F("lib/enter_pit", [
    f"tp @s {P(PIT_IN)} 180 0",
    "tag @s add so_ar_in",
    "effect give @s minecraft:resistance 3 3 true",
    "playsound minecraft:item.trident.thunder master @s ~ ~ ~ 0.6 1.2",
])
F("lib/join", [
    f'execute unless entity @s[tag=so_ar_zone] run return run {say("@s", "Primero entrá al Coliseo con /trigger arena.", "red")}',
    f'execute if score #mode so_ar matches 0 run return run {say("@s", "No hay ningún desafío en curso. Elegí una práctica o un contrato.", "gray")}',
    f'execute if score #mode so_ar matches 10 run return run {say("@s", "Hay un duelo PvP: miralo desde las tribunas.", "gray")}',
    f'execute if entity @s[tag=so_ar_in] run return run {say("@s", "Ya estás en el foso.", "gray")}',
    f'execute if entity @s[tag=so_ar_ready] run return run {say("@s", "Ya estás en el túnel de preparación.", "gray")}',
    f"execute if score #mode so_ar matches 9 run return run function {NS}:lib/stage_in",
    f"function {NS}:lib/enter_pit",
    f"bossbar set {NS}:fight players {IN}",
    say(ZONE, "¡Un gladiador más se suma al desafío!", "green"),
])

# ---------------------------------------------------------------- preparación en el túnel
F("lib/prepare", [
    "scoreboard players set #mode so_ar 9",
    "scoreboard players set #st so_ar 0",
    f"function {NS}:lib/stage_in",
    f"dialog show @s {NS}:dj",
    say(ZONE, "Un gladiador se prepara en el túnel. ¡Pueden unirse antes de la campana!", "gold"),
])
F("lib/stage_in", [
    f"tp @s {P(STAGE)} 180 0",
    "tag @s add so_ar_ready",
    "effect give @s minecraft:resistance 3 4 true",
    "playsound minecraft:block.iron_door.close master @s ~ ~ ~ 1 0.8",
    f'title @s title {T({"text": "Túnel de gladiadores", "color": "gold", "bold": True})}',
    f'title @s subtitle {T({"text": "Elegí tu tema y tocá la campana", "color": "yellow"})}',
    say("@s", "Elegí la música (carteles, tocadiscos o chat), activá mutadores si querés y tocá la CAMPANA o pisá la placa del portón. En 30 s arranca sola.", "yellow"),
    f"tellraw @s {T({'text': ' Música: ', 'color': 'gray'}, *[link(f'[{name}] ', f'/trigger arena_dj set {n}', 'light_purple', name) for n, _, name, _ in SONGS], link('[Azar] ', '/trigger arena_dj set 8', 'dark_purple', 'Al azar'), link('[¡COMENZAR!]', '/trigger arena_con set 30', 'green', 'Tocar la campana'))}",
])
F("lib/stage_second", [
    "scoreboard players add #st so_ar 1",
    f"execute unless entity @a[tag=so_ar_ready] run return run function {NS}:lib/stage_cancel",
    "scoreboard players set #left so_ar 30",
    "scoreboard players operation #left so_ar -= #st so_ar",
    f"title @a[tag=so_ar_ready] actionbar {T({'text': 'Tocá la campana · arranca solo en ', 'color': 'yellow'}, {'score': {'name': '#left', 'objective': 'so_ar'}, 'color': 'white', 'bold': True}, {'text': ' s', 'color': 'yellow'})}",
    f"execute if score #st so_ar matches 30.. run function {NS}:lib/go_fight",
])
F("lib/stage_cancel", [
    "scoreboard players set #mode so_ar 0",
    say(ZONE, "Preparación cancelada: nadie quedó en el túnel.", "gray"),
    f"execute as {ZONE} run clear @s {LOAN}",
])
F("lib/bell", [
    "playsound minecraft:block.bell.use master @a[tag=so_ar_zone] ~ ~ ~ 2 1",
    f"execute unless score #mode so_ar matches 9 run return run title @s actionbar {T({'text': 'La campana suena cuando hay un desafío preparado.', 'color': 'gray'})}",
    f"execute unless entity @s[tag=so_ar_ready] run return run title @s actionbar {T({'text': 'Solo los gladiadores del túnel pueden tocarla.', 'color': 'gray'})}",
    f"function {NS}:lib/go_fight",
])
F("lib/go_fight", [
    "execute unless score #mode so_ar matches 9 run return 0",
    "scoreboard players set #mode so_ar 0",
    "# mutadores activos",
    "scoreboard players operation #mutc so_ar = #mut_n so_ar",
    "scoreboard players operation #mutc so_ar += #mut_f so_ar",
    "scoreboard players operation #mutc so_ar += #mut_v so_ar",
    f"function {NS}:lib/music_pick",
    f"function {NS}:lib/gate_pit_open",
    f"function {NS}:lib/judges_salute",
    "title @a[tag=so_ar_zone] times 5 50 15",
    f"title @a[tag=so_ar_zone] title {T({'text': '¡Que empiece la batalla!', 'color': 'gold', 'bold': True})}",
    f"execute if score #mutc so_ar matches 1.. run title @a[tag=so_ar_zone] subtitle {T({'text': 'Mutadores activos: botín doble', 'color': 'red'})}",
    "execute as @a[tag=so_ar_zone] at @s run playsound minecraft:block.bell.resonate master @s ~ ~ ~ 1 0.8",
    f"execute as @a[tag=so_ar_ready] run function {NS}:lib/enter_pit",
    "tag @a remove so_ar_ready",
    f"function {NS}:lib/refill",
    f"execute if score #ptype so_ar matches 1 run function {NS}:mode/practice/start",
    f"execute if score #ptype so_ar matches 2 run function {NS}:lib/con_begin",
    f"function {NS}:lib/music_play",
    f"schedule function {NS}:lib/gate_pit_close 60t",
])

# ---------------------------------------------------------------- portones, jueces, tablero
GATE_PIT = f"{CX - 3} 96 {TZ0} {CX + 3} 100 {TZ0}"
GATE_LOBBY = f"{CX - 3} 96 {LZ0} {CX + 3} 100 {LZ0}"
F("lib/gate_pit_open", [f"fill {GATE_PIT} minecraft:air replace minecraft:iron_bars",
                        f"playsound minecraft:block.piston.extend master @a[tag=so_ar_zone] {CX} 98 {TZ0} 2 0.6",
                        f"particle minecraft:cloud {CX} 98 {TZ0} 3 2 0.3 0.02 40 force"])
F("lib/gate_pit_close", [f"fill {GATE_PIT} minecraft:iron_bars replace minecraft:air",
                         f"playsound minecraft:block.piston.contract master @a[tag=so_ar_zone] {CX} 98 {TZ0} 2 0.6"])
F("lib/gates_open", [f"function {NS}:lib/gate_pit_open", f"fill {GATE_LOBBY} minecraft:air replace minecraft:iron_bars",
                     f"particle minecraft:wax_on {CX} 98 {LZ0} 3 2 0.3 0 30 force",
                     f"playsound minecraft:block.iron_door.open master @a[tag=so_ar_zone] {CX} 98 {LZ0} 2 0.7"])
F("lib/gates_close", [f"fill {GATE_PIT} minecraft:iron_bars replace minecraft:air", f"fill {GATE_LOBBY} minecraft:iron_bars replace minecraft:air"])
JUDGES = [(CX - 2, JUDGE_Z), (CX, JUDGE_Z), (CX + 2, JUDGE_Z)]
F("lib/judges_salute", [
    f"effect give @e[tag=so_ar_judge,{ZONE_BOX}] minecraft:glowing 6 0 true",
    *[f"particle minecraft:totem_of_undying {x} 111 {z} 0.4 0.6 0.4 0.4 40 force" for x, z in JUDGES],
    f"particle minecraft:firework {CX} 112 {JUDGE_Z + 3} 3 1 1 0.15 80 force",
])
F("lib/board", [
    "execute store result storage so_arenas:b w int 1 run scoreboard players get #wave so_ar",
    "execute store result storage so_arenas:b a int 1 if entity @e[tag=so_ar_mob]",
    "execute store result storage so_arenas:b t int 1 run scoreboard players get #t so_ar",
    f"function {NS}:lib/board_set with storage so_arenas:b",
])
F("lib/board_set", [
    f'$data modify entity @e[tag=so_ar_board,limit=1,{ZONE_BOX}] text set value {{text:"",extra:[{{text:"⚔ $(n)\\n",color:"gold",bold:true}},{{text:"Oleada $(w) · Enemigos $(a) · $(t) s",color:"white"}}]}}'])
F("lib/board_idle", [
    f'data modify entity @e[tag=so_ar_board,limit=1,{ZONE_BOX}] text set value {{text:"",extra:[{{text:"⚔ Coliseo VorNeX\\n",color:"gold",bold:true}},{{text:"Esperando gladiadores",color:"gray"}}]}}'])

# ---------------------------------------------------------------- música
F("lib/dj", [
    f'execute unless entity @s[tag=so_ar_zone] run return run {say("@s", "La música se elige dentro del Coliseo.", "red")}',
    "execute if score @s arena_dj matches 1..7 run scoreboard players operation #song so_ar = @s arena_dj",
    "execute if score @s arena_dj matches 8 run scoreboard players set #song so_ar 0",
    *[f'execute if score @s arena_dj matches {n} run {say(ZONE, f"♪ Tema elegido: {name}", "light_purple")}' for n, _, name, _ in SONGS],
    f'execute if score @s arena_dj matches 8 run {say(ZONE, "♪ Tema al azar: la campana tira los dados.", "light_purple")}',
    "execute at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.5",
    f"execute if score #playing so_ar matches 1 if score #song so_ar matches 1.. run function {NS}:lib/music_play",
])
F("lib/music_pick", [
    "# Disco puesto en el tocadiscos del túnel > elección por cartel/menú > azar (solo temas épicos).",
    *[f'execute if block {P(JUKE)} minecraft:jukebox{{RecordItem:{{id:"minecraft:music_disc_{sid}"}}}} run scoreboard players set #song so_ar {n}' for n, sid, _, _ in SONGS],
    f"execute if data block {P(JUKE)} RecordItem run function {NS}:lib/juke_pop",
    "execute unless score #song so_ar matches 1..7 store result score #song so_ar run random value 1..7",
])
F("lib/juke_pop", [
    "# Devuelve el disco al piso del túnel (no desaparece) y apaga el tocadiscos para no duplicar la música.",
    f'summon minecraft:item {JUKE[0]} 97.2 {JUKE[2] + 1} {{Tags:["so_ar_disc"],Age:-32768s,PickupDelay:10s,Item:{{id:"minecraft:stone",count:1}}}}',
    f"data modify entity @e[type=minecraft:item,tag=so_ar_disc,limit=1] Item set from block {P(JUKE)} RecordItem",
    "tag @e[type=minecraft:item,tag=so_ar_disc] remove so_ar_disc",
    f"setblock {P(JUKE)} minecraft:air",
    f"setblock {P(JUKE)} minecraft:jukebox",
])
F("lib/music_play", [
    "stopsound @a[tag=so_ar_zone] record",
    "scoreboard players set #mt so_ar 0",
    "scoreboard players set #playing so_ar 1",
    f"execute as {ZONE} run function {NS}:lib/music_one",
    *[f'execute if score #song so_ar matches {n} run title @a[tag=so_ar_zone] actionbar {T({"text": f"♪ Suena: {name}", "color": "light_purple"})}' for n, _, name, _ in SONGS],
])
F("lib/music_one", [
    "# A todo volumen en todo el estadio (volumen mínimo 1 fuera del alcance).",
    *[f"execute if score #song so_ar matches {n} run playsound minecraft:music_disc.{sid} record @s {CX} 100 {CZ} 4 1 1" for n, sid, _, _ in SONGS],
])
F("lib/music_second", [
    "scoreboard players add #mt so_ar 1",
    *[f"execute if score #song so_ar matches {n} if score #mt so_ar matches {d}.. run function {NS}:lib/music_play" for n, _, _, d in SONGS],
])
F("lib/music_stop", ["stopsound @a[tag=so_ar_zone] record", "scoreboard players set #playing so_ar 0", "scoreboard players set #song so_ar 0"])

# ---------------------------------------------------------------- mutadores
MUTS = [(1, "mut_n", "Niebla de Oscuridad"), (2, "mut_f", "Furia Monstruosa"), (3, "mut_v", "Vampirismo")]
F("lib/mut", [
    f'execute unless entity @s[tag=so_ar_zone] run return run {say("@s", "Los mutadores se eligen dentro del Coliseo.", "red")}',
    f'execute if score #mode so_ar matches {FIGHT} run return run {say("@s", "Los mutadores se eligen antes de la campana.", "red")}',
    *[l for n, k, name in MUTS for l in (
        f"execute if score @s arena_mut matches {n} store success score #tmp so_ar if score #{k} so_ar matches 0",
        f"execute if score @s arena_mut matches {n} run scoreboard players operation #{k} so_ar = #tmp so_ar",
        f'execute if score @s arena_mut matches {n} if score #{k} so_ar matches 1 run {say(ZONE, f"Mutador ACTIVADO: {name} (botín doble).", "red")}',
        f'execute if score @s arena_mut matches {n} if score #{k} so_ar matches 0 run {say(ZONE, f"Mutador desactivado: {name}.", "gray")}')],
    *[f"execute if score @s arena_mut matches 4 run scoreboard players set #{k} so_ar 0" for _, k, _ in MUTS],
    f'execute if score @s arena_mut matches 4 run {say(ZONE, "Mutadores quitados.", "gray")}',
    "execute at @s run playsound minecraft:block.enchantment_table.use master @s ~ ~ ~ 1 1",
])

# ---------------------------------------------------------------- tribunas (espectador)
SPEC_POS = None  # se define en la construcción (fila alta, lado este)
F("lib/ver_dummy", ["# reemplazado más abajo"])

# ---------------------------------------------------------------- práctica
F("mode/practice/start", [
    "scoreboard players set #mode so_ar 1",
    "scoreboard players set #wave so_ar 0", "scoreboard players set #t so_ar 0", "scoreboard players set #anticamp so_ar 1",
    "scoreboard players operation #rew so_ar = #tier so_ar",
    f'bossbar set {NS}:fight name {T({"text": "Práctica", "color": "yellow"})}',
    f"bossbar set {NS}:fight color yellow", f"bossbar set {NS}:fight max 2", f"bossbar set {NS}:fight value 0",
    f"bossbar set {NS}:fight players {IN}", f"bossbar set {NS}:fight visible true",
    say(ZONE, "La práctica comienza: 2 oleadas. ¡Golpeá, esquivá y sobreviví!", "yellow"),
    f"function {NS}:mode/practice/wave",
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

# ---------------------------------------------------------------- contratos
PHASES = [
    (0, ["zombie", "husk", "skeleton", "spider"], ["skeleton", "spider"]),
    (3334, ["zombie_armor", "piglin", "bogged", "cave_spider"], ["witch", "skeleton_armor"]),
    (7501, ["vindicator", "pillager", "witch", "drowned_trident"], ["spider_big", "skeleton_ominous"]),
    (15000, ["zombie_ominous", "breeze", "bogged", "enderman"], ["wither_skeleton", "skeleton_ominous"]),
]
# Defensa: solo mobs que van a pegar cuerpo a cuerpo (los esqueletos no persiguen aldeanos)
DEF_MOBS = [["zombie", "husk", "zombie", "baby_zombie", "zombie_villager"],
            ["zombie_armor", "husk", "piglin", "zombie_escort", "baby_zombie", "zombified_piglin"],
            ["vindicator", "zombie_armor", "vindicator", "zombie_escort", "piglin_brute", "baby_zombie"],
            ["zombie_ominous", "vindicator", "piglin_brute", "zombie_ominous", "zoglin", "vindicator"]]
AIR_MOBS = [["phantom", "phantom", "vex"], ["phantom", "phantom", "phantom_big", "vex"],
            ["phantom_big", "phantom_big", "vex", "vex", "phantom"], ["phantom_big", "phantom_big", "vex", "vex", "breeze", "phantom"]]
AIR_BOSS = [None, "espectro_alfa", "espectro_alfa", "espectro_alfa"]
DUEL = [["rey_zombi", "slime_rey", "comandante"], ["capitan", "piglin_bruto", "bruja_madre"],
        ["caballero", "caudillo_bruto", "archimago"], ["devastador", "senor_end", "heraldo_ominoso"]]
RUSH = [["rey_zombi", "comandante", "slime_rey", "arana_colosal", "zombi_gigante"],
        ["capitan", "piglin_bruto", "jinete_oseo", "bruja_madre", "golem_furioso"],
        ["caballero", "archimago", "caudillo_bruto", "bestia_nether", "invocador"],
        ["senor_llamas", "senor_end", "heraldo_ominoso", "devastador", "zombi_gigante"]]


def phase_cond(i, pre="execute"):
    c = f"{pre} if score #blk so_ar matches {PHASES[i][0]}.."
    if i < len(PHASES) - 1:
        c += f" unless score #blk so_ar matches {PHASES[i + 1][0]}.."
    return c


def by_phase(build, pre="execute"):
    out = []
    for i, (thr, tg, sup) in enumerate(PHASES):
        out += [f"{phase_cond(i, pre)} run {c}" for c in build(tg, sup)]
    return out


def by_idx(lists, fn, pre="execute"):
    out = []
    for i, lst in enumerate(lists):
        out += [f"{phase_cond(i, pre)} run {c}" for c in fn(lst)]
    return out


F("lib/start_con", [
    f"execute if score @s arena_con matches 20 run return run function {NS}:npc_menu_con",
    f"execute if score @s arena_con matches 9 run return run function {NS}:lib/join",
    f"execute if score @s arena_con matches 30 run return run function {NS}:lib/bell",
    *busy_guard(),
    f"function {NS}:lib/blocks",
    f"execute unless score @s arena_con matches 1..{len(CONTRACTS)} run return run {say('@s', 'Contrato inválido.', 'red')}",
    *[f'execute if score @s arena_con matches {n} unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches {b}.. run return run {say("@s", f"{name} se desbloquea a los {fmt(b)} bloques. Mientras, probá la práctica.", "red")}' for n, _, name, b, _ in CONTRACTS],
    "scoreboard players operation #con so_ar = @s arena_con",
    "scoreboard players set #ptype so_ar 2",
    *[f'execute if score #con so_ar matches {n} run data modify storage so_arenas:b n set value "{name}"' for n, _, name, _, _ in CONTRACTS],
    f"function {NS}:lib/prepare",
])
F("lib/con_begin", [
    f"function {NS}:lib/blocks",
    "scoreboard players set #t so_ar 0", "scoreboard players set #wave so_ar 0",
    "scoreboard players set #spawned so_ar 0", "scoreboard players set #anticamp so_ar 1",
    "scoreboard players set #rew so_ar 10",
    f"bossbar set {NS}:fight players {IN}", f"bossbar set {NS}:fight visible true",
    f"execute if score #con so_ar matches 1 run function {NS}:mode/caza/start",
    f"execute if score #con so_ar matches 2 run function {NS}:mode/caza2/start",
    f"execute if score #con so_ar matches 3 run function {NS}:mode/defensa/start",
    f"execute if score #con so_ar matches 4 run function {NS}:mode/rey/start",
    f"execute if score #con so_ar matches 5 run function {NS}:mode/asedio/start",
    "execute if score #con so_ar matches 6 run scoreboard players set #jt so_ar 1",
    "execute if score #con so_ar matches 7 run scoreboard players set #jt so_ar 2",
    f"execute if score #con so_ar matches 6..7 run function {NS}:mode/jefes/start",
])
# caza
F("mode/caza/start", [
    "scoreboard players set #mode so_ar 2",
    f'bossbar set {NS}:fight name {T({"text": "Caza: objetivos restantes", "color": "aqua"})}',
    f"bossbar set {NS}:fight color blue", f"bossbar set {NS}:fight max 15", f"bossbar set {NS}:fight value 15",
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
    "scoreboard players operation #wave so_ar = #spawned so_ar",
    f"title {IN} actionbar {T({'text': 'Caza · quedan ', 'color': 'aqua'}, {'score': {'name': '#left', 'objective': 'so_ar'}, 'color': 'white', 'bold': True}, {'text': ' objetivos', 'color': 'gray'})}",
    f"execute if score #t so_ar matches 3.. if score #left so_ar matches ..0 run return run function {NS}:lib/win_contract",
    f"execute if score #alive so_ar matches ..1 if score #spawned so_ar matches ..10 run function {NS}:mode/caza/batch",
    "scoreboard players operation #m so_ar = #t so_ar", "scoreboard players operation #m so_ar %= #twentyfive so_ar",
    *by_phase(lambda tg, sup: [spawn(m) for m in sup], pre="execute if score #m so_ar matches 0"),
    f"execute if score #t so_ar matches 420.. run function {NS}:lib/fail",
])
# oleadas dobles
F("mode/caza2/start", [
    "scoreboard players set #mode so_ar 4",
    f'bossbar set {NS}:fight name {T({"text": "Oleadas dobles", "color": "aqua"})}',
    f"bossbar set {NS}:fight color blue", f"bossbar set {NS}:fight max 3", f"bossbar set {NS}:fight value 0",
    say(ZONE, "Contrato: superá 3 oleadas, cada una más dura.", "aqua"),
    f"function {NS}:mode/caza2/wave",
])
F("mode/caza2/wave", [
    "scoreboard players add #wave so_ar 1",
    f"execute store result bossbar {NS}:fight value run scoreboard players get #wave so_ar",
    *[l for w in (1, 2, 3) for l in by_phase(lambda tg, sup: [spawn(m) for m in tg + sup[:1]], pre=f"execute if score #wave so_ar matches {w}..")],
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
# defensa del núcleo: cebo vivo + barricadas
F("mode/defensa/start", [
    f"setblock {CX} 96 {CZ} minecraft:crying_obsidian",
    f'summon minecraft:villager {CX}.5 97 {CZ}.5 {{Tags:["so_ar_bait","so_ar_mob_keep"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,active_effects:[{{id:"minecraft:invisibility",amplifier:0b,duration:-1,show_particles:0b}}]}}',
    "scoreboard players set #mode so_ar 3", "scoreboard players set #hp so_ar 100", "scoreboard players set #anticamp so_ar 0",
    f"bossbar set {NS}:fight color purple", f"bossbar set {NS}:fight max 100", f"bossbar set {NS}:fight value 100",
    f'bossbar set {NS}:fight name {T({"text": "Núcleo", "color": "dark_purple"})}',
    f"execute as {IN} run function {NS}:lib/kit_def",
    say(ZONE, "Contrato: protegé el Núcleo 2 minutos. ¡Los monstruos van directo a él! Usá las barricadas. Acá la altura está permitida.", "dark_purple"),
    f"function {NS}:mode/defensa/wave",
])
F("mode/defensa/wave", [
    "scoreboard players add #wave so_ar 1",
    "execute store result score #alive so_ar if entity @e[tag=so_ar_mob]",
    f"execute if score #alive so_ar matches 30.. run return 0",
    *by_idx(DEF_MOBS, lambda lst: [spawn(m) for m in lst]),
    f"execute if score #wave so_ar matches 4.. run {spawn('zombie')}",
    f"execute if score #wave so_ar matches 6.. run {spawn('zombie_armor')}",
    f"execute as {IN} at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 0.9",
])
F("mode/defensa/second", [
    "scoreboard players add #t so_ar 1",
    f"execute positioned {CX}.5 96 {CZ}.5 store result score #near so_ar if entity @e[tag=so_ar_mob,distance=..3.5]",
    "scoreboard players operation #hp so_ar -= #near so_ar",
    f"execute if score #near so_ar matches 1.. run particle minecraft:damage_indicator {CX}.5 97.5 {CZ}.5 0.4 0.4 0.4 0.1 6 force",
    f"execute if score #near so_ar matches 1.. run playsound minecraft:block.anvil.land master {IN} {CX} 97 {CZ} 0.4 1.6",
    f"execute store result bossbar {NS}:fight value run scoreboard players get #hp so_ar",
    f"title {IN} actionbar {T({'text': 'Núcleo: ', 'color': 'dark_purple'}, {'score': {'name': '#hp', 'objective': 'so_ar'}, 'color': 'white', 'bold': True}, {'text': '% · tiempo: ', 'color': 'gray'}, {'score': {'name': '#t', 'objective': 'so_ar'}, 'color': 'white'}, {'text': '/120 s', 'color': 'gray'})}",
    f"execute if score #hp so_ar matches ..0 run return run function {NS}:lib/fail",
    f"execute if score #t so_ar matches 120.. run return run function {NS}:lib/win_contract",
    "scoreboard players operation #m so_ar = #t so_ar", "scoreboard players operation #m so_ar %= #fifteen so_ar",
    f"execute if score #m so_ar matches 0 run function {NS}:mode/defensa/wave",
])
# rey de la colina
RING = [(CX + 0.5 + 4 * math.cos(a * math.pi / 8), CZ + 0.5 + 4 * math.sin(a * math.pi / 8)) for a in range(16)]
F("mode/rey/start", [
    "scoreboard players set #mode so_ar 5", "scoreboard players set #hold so_ar 0",
    f"bossbar set {NS}:fight color yellow", f"bossbar set {NS}:fight max 90", f"bossbar set {NS}:fight value 0",
    f'bossbar set {NS}:fight name {T({"text": "Rey de la Colina: dominio", "color": "gold"})}',
    say(ZONE, "Contrato: quedate dentro del círculo de luz central 90 s. Si salís, el contador se frena.", "gold"),
    f"function {NS}:mode/rey/wave",
])
F("mode/rey/wave", [
    "scoreboard players add #wave so_ar 1",
    "execute store result score #alive so_ar if entity @e[tag=so_ar_mob]",
    "execute if score #alive so_ar matches 25.. run return 0",
    *by_phase(lambda tg, sup: [spawn(m) for m in tg[:3] + sup[:1]]),
    f"execute as {IN} at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 1.2",
])
F("mode/rey/second", [
    "scoreboard players add #t so_ar 1",
    *[f"particle minecraft:end_rod {x:.2f} 96.3 {z:.2f} 0 0.4 0 0.01 2 force" for x, z in RING],
    f"particle minecraft:glow {CX}.5 97 {CZ}.5 0.3 1.5 0.3 0 10 force",
    f"execute positioned {CX}.5 96 {CZ}.5 if entity @a[tag=so_ar_in,distance=..4.5] run scoreboard players add #hold so_ar 1",
    f"execute store result bossbar {NS}:fight value run scoreboard players get #hold so_ar",
    "scoreboard players operation #wave so_ar = #hold so_ar",
    f"title {IN} actionbar {T({'text': 'Dominio: ', 'color': 'gold'}, {'score': {'name': '#hold', 'objective': 'so_ar'}, 'color': 'white', 'bold': True}, {'text': '/90 s (quedate en el círculo)', 'color': 'gray'})}",
    f"execute if score #hold so_ar matches 90.. run return run function {NS}:lib/win_contract",
    "scoreboard players operation #m so_ar = #t so_ar", "scoreboard players operation #m so_ar %= #ten so_ar",
    f"execute if score #m so_ar matches 0 run function {NS}:mode/rey/wave",
    f"execute if score #t so_ar matches 300.. run function {NS}:lib/fail",
])
# asedio volador
F("mode/asedio/start", [
    "scoreboard players set #mode so_ar 7",
    f'bossbar set {NS}:fight name {T({"text": "Asedio Volador", "color": "aqua"})}',
    f"bossbar set {NS}:fight color blue", f"bossbar set {NS}:fight max 3", f"bossbar set {NS}:fight value 0",
    say(ZONE, "Contrato: el cielo ataca. 3 oleadas de phantoms y vexes. ¡Arco, ballesta y escudo!", "aqua"),
    f"function {NS}:mode/asedio/wave",
])
F("mode/asedio/wave", [
    "scoreboard players add #wave so_ar 1",
    f"execute store result bossbar {NS}:fight value run scoreboard players get #wave so_ar",
    *by_idx(AIR_MOBS, lambda lst: [spawn(m) for m in lst]),
    *by_idx(AIR_MOBS, lambda lst: [spawn(m) for m in lst[:2]], pre="execute if score #wave so_ar matches 2.."),
    *by_idx(AIR_BOSS, lambda b: [spawn_boss(b)] if b else [], pre="execute if score #wave so_ar matches 3"),
    f"execute as {IN} at @s run playsound minecraft:entity.phantom.swoop master @s ~ ~ ~ 1 0.8",
])
F("mode/asedio/second", [
    "scoreboard players add #t so_ar 1",
    "execute store result score #alive so_ar if entity @e[tag=so_ar_mob]",
    f"title {IN} actionbar {T({'text': 'Asedio · oleada ', 'color': 'aqua', 'bold': True}, {'score': {'name': '#wave', 'objective': 'so_ar'}, 'color': 'white'}, {'text': '/3 · enemigos: ', 'color': 'gray'}, {'score': {'name': '#alive', 'objective': 'so_ar'}, 'color': 'white'})}",
    f"execute if score #t so_ar matches 3.. if score #alive so_ar matches 0 if score #wave so_ar matches 3.. run return run function {NS}:lib/win_contract",
    f"execute if score #t so_ar matches 3.. if score #alive so_ar matches 0 if score #wave so_ar matches 1..2 run function {NS}:mode/asedio/wave",
    f"execute if score #t so_ar matches 480.. run function {NS}:lib/fail",
])
# duelo de campeones (jt=1, 3 minijefes, 10 s de respiro) / desafío de jefes (jt=2, 5 jefes, 5 s)
F("mode/jefes/start", [
    "scoreboard players set #mode so_ar 6", "scoreboard players set #champ so_ar 0", "scoreboard players set #rest so_ar 0",
    "execute if score #jt so_ar matches 1 run scoreboard players set #cmax so_ar 3",
    "execute if score #jt so_ar matches 2 run scoreboard players set #cmax so_ar 5",
    "execute if score #jt so_ar matches 2 run scoreboard players set #rew so_ar 11",
    f"bossbar set {NS}:fight color red",
    f'execute if score #jt so_ar matches 1 run {say(ZONE, "Duelo de Campeones: 3 minijefes seguidos con escoltas. 10 s de respiro entre cada uno.", "red")}',
    f'execute if score #jt so_ar matches 2 run {say(ZONE, "Desafío de Jefes: 5 jefes de tu fase en cadena. ¡Botín de jefe!", "red")}',
    f"function {NS}:mode/jefes/next",
])
F("mode/jefes/next", [
    "scoreboard players add #champ so_ar 1",
    "scoreboard players operation #wave so_ar = #champ so_ar",
    *[l for k in range(3) for l in by_idx(DUEL, lambda lst, k=k: [spawn_boss(lst[k])], pre=f"execute if score #jt so_ar matches 1 if score #champ so_ar matches {k + 1}")],
    *by_phase(lambda tg, sup: [spawn(m) for m in sup], pre="execute if score #jt so_ar matches 1"),
    *[l for k in range(5) for l in by_idx(RUSH, lambda lst, k=k: [spawn_boss(lst[k])], pre=f"execute if score #jt so_ar matches 2 if score #champ so_ar matches {k + 1}")],
    f'title {IN} title {T({"text": "Campeón ", "color": "red", "bold": True}, {"score": {"name": "#champ", "objective": "so_ar"}, "color": "white"}, {"text": "/", "color": "gray"}, {"score": {"name": "#cmax", "objective": "so_ar"}, "color": "white"})}',
    f"execute as {IN} at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.5 1.4",
])
F("mode/jefes/second", [
    "scoreboard players add #t so_ar 1",
    f"execute as @e[tag=so_ar_boss,limit=1] store result bossbar {NS}:fight value run data get entity @s Health",
    f"execute if entity @e[tag=so_ar_boss] run title {IN} actionbar {T({'text': 'Campeón ', 'color': 'red'}, {'score': {'name': '#champ', 'objective': 'so_ar'}, 'color': 'white', 'bold': True}, {'text': '/', 'color': 'gray'}, {'score': {'name': '#cmax', 'objective': 'so_ar'}, 'color': 'white'})}",
    f"execute if entity @e[tag=so_ar_boss] run return run execute if score #t so_ar matches 600.. run function {NS}:lib/fail",
    "execute if score #champ so_ar >= #cmax so_ar run kill @e[tag=so_ar_mob]",
    f"execute if score #champ so_ar >= #cmax so_ar run return run function {NS}:lib/win_contract",
    "scoreboard players add #rest so_ar 1",
    f"bossbar set {NS}:fight value 0",
    f"title {IN} actionbar {T({'text': '¡Campeón caído! Respiro: ', 'color': 'green'}, {'score': {'name': '#rest', 'objective': 'so_ar'}, 'color': 'white', 'bold': True}, {'text': ' s', 'color': 'green'})}",
    "execute if score #rest so_ar matches 1 run " + say(ZONE, "¡Campeón derrotado! Respirá: viene el siguiente.", "green"),
    f"execute if score #jt so_ar matches 1 if score #rest so_ar matches 10.. run function {NS}:mode/jefes/rest_done",
    f"execute if score #jt so_ar matches 2 if score #rest so_ar matches 5.. run function {NS}:mode/jefes/rest_done",
    f"execute if score #t so_ar matches 600.. run function {NS}:lib/fail",
])
F("mode/jefes/rest_done", ["scoreboard players set #rest so_ar 0", f"function {NS}:mode/jefes/next"])

# ---------------------------------------------------------------- victoria / derrota / limpieza
F("lib/win_practice", [
    f"title {IN} title {T({'text': '¡Victoria!', 'color': 'green', 'bold': True})}",
    say(ZONE, "Práctica superada.", "green"),
    f"function {NS}:lib/victory",
])
F("lib/win_contract", [
    f"scoreboard players add {IN} so_ar_rank 1",
    f"title {IN} title {T({'text': '¡Contrato cumplido!', 'color': 'green', 'bold': True})}",
    say(ZONE, "¡Contrato cumplido! Botellas de XP, esmeraldas y más.", "green"),
    f"function {NS}:lib/victory",
])
F("lib/victory", [
    "tag @a remove so_ar_win",
    f"tag {IN} add so_ar_win",
    f"function {NS}:lib/music_stop",
    f"function {NS}:lib/celebrar",
    f"function {NS}:lib/judges_salute",
    f"function {NS}:lib/end_fight",
    "scoreboard players add @a[tag=so_ar_win] so_ar_streak 1",
    f"function {NS}:lib/reward_chest",
    f"function {NS}:lib/gates_open",
    "scoreboard players set #exit so_ar 1", "scoreboard players set #ext so_ar 60",
    f'bossbar set {NS}:fight name {T({"text": "Portón abierto · el foso se limpia en", "color": "green"})}',
    f"bossbar set {NS}:fight color green", f"bossbar set {NS}:fight max 60", f"bossbar set {NS}:fight value 60",
    f"bossbar set {NS}:fight players {ZONE}", f"bossbar set {NS}:fight visible true",
    f"title @a[tag=so_ar_win] subtitle {T({'text': 'Salí por el portón: tu cofre te espera en el lobby', 'color': 'yellow'})}",
    say(ZONE, "Los portones están abiertos 60 s. Festejen, junten lo que quieran y salgan por el túnel (o pisen la placa dorada).", "green"),
])
REWARD_BLOCKS = ["minecraft:chest[facing=west]", "minecraft:trapped_chest[facing=west]", "minecraft:barrel[facing=up]",
                 "minecraft:copper_chest[facing=west]", "minecraft:exposed_copper_chest[facing=west]",
                 "minecraft:weathered_copper_chest[facing=west]", "minecraft:oxidized_copper_chest[facing=west]"]
F("lib/reward_chest", [
    "# Contenedor estético al azar en el pedestal del lobby (el anterior se reemplaza).",
    f"execute store result score #r so_ar run random value 0..{len(REWARD_BLOCKS) - 1}",
    f"setblock {P(REWARD)} minecraft:air",
    *[f"execute if score #r so_ar matches {i} run setblock {P(REWARD)} {b}" for i, b in enumerate(REWARD_BLOCKS)],
    f"execute as @a[tag=so_ar_win] run function {NS}:lib/reward_one",
    f"particle minecraft:happy_villager {REWARD[0]}.5 97 {REWARD[2]}.5 0.4 0.4 0.4 0 20 force",
])
F("lib/reward_one", [
    *[f"execute if score #rew so_ar matches {t} run loot insert {P(REWARD)} loot {NS}:practice_t{t}" for t in range(1, 5)],
    f"execute if score #rew so_ar matches 10 run loot insert {P(REWARD)} loot {NS}:contract",
    f"execute if score #rew so_ar matches 11 run loot insert {P(REWARD)} loot {NS}:boss",
    "# mutadores: botín doble",
    *[f"execute if score #mutc so_ar matches 1.. if score #rew so_ar matches {t} run loot insert {P(REWARD)} loot {NS}:practice_t{t}" for t in range(1, 5)],
    f"execute if score #mutc so_ar matches 1.. if score #rew so_ar matches 10 run loot insert {P(REWARD)} loot {NS}:contract",
    f"execute if score #mutc so_ar matches 1.. if score #rew so_ar matches 11 run loot insert {P(REWARD)} loot {NS}:boss",
    "# racha",
    f"execute if score @s so_ar_streak matches 3 run loot insert {P(REWARD)} loot {NS}:streak",
    f"execute if score @s so_ar_streak matches 5 run loot insert {P(REWARD)} loot {NS}:streak",
    f"execute if score @s so_ar_streak matches 10.. run loot insert {P(REWARD)} loot {NS}:streak",
    f'execute if score @s so_ar_streak matches 3 run {say(ZONE, "¡Racha de 3 victorias! Cofre extra.", "gold")}',
    f'execute if score @s so_ar_streak matches 5 run {say(ZONE, "¡Racha de 5 victorias! Cofre extra.", "gold")}',
    f'execute if score @s so_ar_streak matches 10.. run {say(ZONE, "¡Racha legendaria! Cofre extra.", "gold")}',
])
F("lib/fail", [say(ZONE, "Desafío perdido: sin recompensa.", "red"), f"function {NS}:lib/defeat"])
F("lib/vacio", [say(ZONE, "El desafío terminó: ya no quedaba nadie en el foso.", "gray"), f"function {NS}:lib/defeat"])
F("lib/defeat", [
    f"function {NS}:lib/music_stop",
    f"execute as {ZONE} at @s run playsound minecraft:entity.wither.death master @s ~ ~ ~ 0.4 1.6",
    f"title {IN} title {T({'text': 'Derrota', 'color': 'dark_red', 'bold': True})}",
    f"scoreboard players set {IN} so_ar_streak 0",
    f"function {NS}:lib/end_fight",
    "scoreboard players set #exit so_ar 1", "scoreboard players set #ext so_ar 3",
])
F("lib/end_fight", [
    "# Fin de combate: mobs al vacío (sin drops), cebo, núcleo y barra.",
    "tp @e[tag=so_ar_mob] -5000 -300 -5000",
    "kill @e[tag=so_ar_mob]",
    f"kill @e[tag=so_ar_bait,{ZONE_BOX}]",
    f"setblock {CX} 96 {CZ} minecraft:air",
    f"bossbar set {NS}:fight visible false",
    "scoreboard players set #mode so_ar 0", "scoreboard players set #wave so_ar 0",
    "scoreboard players set #t so_ar 0", "scoreboard players set #anticamp so_ar 1",
    "scoreboard players reset @a so_ar_air",
])
F("lib/exit_second", [
    "scoreboard players remove #ext so_ar 1",
    f"execute if score #ext so_ar matches 4.. store result bossbar {NS}:fight value run scoreboard players get #ext so_ar",
    f"execute if score #ext so_ar matches ..0 run function {NS}:lib/close_pit",
])
F("lib/close_pit", [
    "# Cierre: todos al lobby, kits fuera, foso limpio, portones cerrados.",
    f"execute as @a[tag=so_ar_zone,{PIT_BOX}] run tp @s {P(ARR)} 180 0",
    f"execute as @a[tag=so_ar_zone,{TUNNEL_BOX}] run tp @s {P(ARR)} 180 0",
    f"execute as {ZONE} run clear @s {LOAN}",
    "tag @a remove so_ar_loan", "tag @a remove so_ar_in", "tag @a remove so_ar_win", "tag @a remove so_ar_ready",
    f"function {NS}:lib/reset_pit",
    f"function {NS}:lib/gates_close",
    f"function {NS}:lib/board_idle",
    f"bossbar set {NS}:fight visible false",
    "scoreboard players set #exit so_ar 0",
    *[f"scoreboard players set #{k} so_ar 0" for _, k, _ in MUTS],
    say(ZONE, "Foso limpio y portones cerrados. Otro desafío, o /trigger volver para ir a la isla.", "gray"),
])


# reset del foso: geometría del óvalo
def zr(dx, r):
    a = 1 - (dx / (AX * r)) ** 2
    return int(BZ * r * math.sqrt(a)) if a >= 0 else -1


FLOOR_MIX = ["minecraft:sandstone", "minecraft:smooth_sandstone", "minecraft:coarse_dirt", "minecraft:packed_mud"]
FLOOR_LIGHTS = [(CX + dx, CZ + dz) for dx in range(-24, 25, 6) for dz in range(-28, 29, 7)
                if (dx / (AX * R_RESET)) ** 2 + (dz / (BZ * R_RESET)) ** 2 < 0.85 and (dx, dz) != (0, 0)]
reset = [
    "# Limpieza quirúrgica: SOLO el óvalo interior del foso (no toca muro, labio, gradas, túnel ni lobby).",
    f"kill @e[type=minecraft:item,{PIT_FLOOR_BOX}]",
    f"kill @e[type=minecraft:experience_orb,{PIT_FLOOR_BOX}]",
    f"kill @e[type=#minecraft:arrows,{PIT_BOX}]",
]
for dx in range(-AX, AX + 1):
    zb = zr(dx, R_RESET)
    if zb < 0: continue
    x = CX + dx
    reset.append(f"fill {x} 96 {CZ - zb} {x} 120 {CZ + zb} minecraft:air")
    reset.append(f"fill {x} {G} {CZ - zb} {x} {G} {CZ + zb} {FLOOR_MIX[(dx // 3) % len(FLOOR_MIX)]}")
reset += [f"setblock {x} {G} {z} minecraft:ochre_froglight" for x, z in FLOOR_LIGHTS]
F("lib/reset_pit", reset)

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
F("lib/spawn_boss", [
    "$data modify storage so_arenas:tmp b set value \"$(b)\"",
    "execute store result storage so_arenas:tmp a int 1 run random value 0..359",
    "execute store result storage so_arenas:tmp d int 1 run random value 8..14",
    f"function {NS}:lib/spawn_boss_at with storage so_arenas:tmp",
    "scoreboard players set #tg so_ar 0",
    f"execute as @e[tag=so_ev_mob,{MOB_BOX}] run function {NS}:lib/claim",
    "execute unless entity @e[tag=so_ev_boss] run bossbar set so_events:boss visible false",
])
F("lib/spawn_boss_at", [f'$execute positioned {CX} 96 {CZ} rotated $(a) 0 positioned ^ ^ ^$(d) run function so_events:api/boss {{id:"$(b)"}}'])
F("lib/claim", [
    "tag @s add so_ar_mob",
    "tag @s remove so_ev_mob",
    "execute if score #tg so_ar matches 1 run tag @s add so_ar_target",
    f"execute if entity @s[tag=so_ev_boss] run function {NS}:lib/claim_boss",
    "execute if score #mut_f so_ar matches 1 run effect give @s minecraft:speed infinite 1 true",
    "execute if score #mut_v so_ar matches 1 run effect give @s minecraft:regeneration infinite 1 true",
])
F("lib/claim_boss", [
    "tag @s remove so_ev_boss",
    "tag @s add so_ar_boss",
    f"execute store result bossbar {NS}:fight max run data get entity @s Health",
    f"execute store result bossbar {NS}:fight value run data get entity @s Health",
    f'bossbar set {NS}:fight name [{{"text":"Campeón: ","color":"red","bold":true}},{{"selector":"@e[tag=so_ar_boss,limit=1]"}}]',
])

# ---------------------------------------------------------------- torres / festejo / anticamping
TOWERS = []
for k in range(8):
    ang = math.pi / 8 + k * math.pi / 4
    TOWERS.append((CX + round(AX * 0.965 * math.cos(ang)), CZ + round(BZ * 0.965 * math.sin(ang))))
FW = '{{LifeTime:{lt},FireworksItem:{{id:"minecraft:firework_rocket",count:1,components:{{"minecraft:fireworks":{{flight_duration:1b,explosions:[{{shape:"large_ball",colors:[I;16750848,16711680,16776960],has_trail:1b,has_twinkle:1b}}]}}}}}}}}'
F("lib/celebrar", [
    "# Fuegos artificiales desde las 8 torres y el palco + fanfarria.",
    *[f"summon minecraft:firework_rocket {x} {TOP_Y + 3} {z} {FW.format(lt=20 + 4 * i)}" for i, (x, z) in enumerate(TOWERS)],
    f"summon minecraft:firework_rocket {CX} 116 {JUDGE_Z + 2} {FW.format(lt=30)}",
    f"execute as {ZONE} at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1",
    f"execute as {ZONE} at @s run playsound minecraft:item.goat_horn.sound.1 master @s ~ ~ ~ 1 1",
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

# ---------------------------------------------------------------- duelo PvP
F("lib/pvp", [
    f'execute unless entity @s[tag=so_ar_zone] run return run {say("@s", "Los duelos se hacen dentro del Coliseo.", "red")}',
    f"execute if score @s arena_pvp matches 2 run return run function {NS}:mode/pvp/cancel",
    *busy_guard()[1:],
    f"execute if entity @a[tag=so_ar_pvpw,tag=!so_ar_me] unless entity @s[tag=so_ar_pvpw] run return run function {NS}:mode/pvp/start",
    f'execute if entity @s[tag=so_ar_pvpw] run return run {say("@s", "Ya estás esperando rival. Cancelar: /trigger arena_pvp set 2", "gray")}',
    "tag @s add so_ar_pvpw",
    f'tellraw {ZONE} [{json.dumps(PFX)},{{"selector":"@s","color":"red"}},{{"text":" busca un duelo amistoso. ","color":"yellow","bold":false}},{json.dumps(link("[ACEPTAR]", "/trigger arena_pvp set 1", "green", "Batirse a duelo (sin perder cosas: termina a los 3 corazones)"))}]',
])
F("mode/pvp/cancel", ["tag @s remove so_ar_pvpw", say("@s", "Duelo cancelado.", "gray")])
F("mode/pvp/start", [
    "tag @a[tag=so_ar_pvpw,limit=1] add so_ar_pvp",
    "tag @s add so_ar_pvp",
    "tag @a remove so_ar_pvpw",
    "scoreboard players set #mode so_ar 10", "scoreboard players set #t so_ar 0", "scoreboard players set #anticamp so_ar 1",
    f"tp @a[tag=so_ar_pvp,tag=!so_ar_me,limit=1] {P(PIT_IN2)} 0 0",
    f"execute as @a[tag=so_ar_pvp] unless entity @s[{PIT_BOX}] run tp @s {P(PIT_IN)} 180 0",
    "tag @a[tag=so_ar_pvp] add so_ar_in",
    "effect give @a[tag=so_ar_pvp] minecraft:instant_health 1 5 true",
    "effect give @a[tag=so_ar_pvp] minecraft:resistance infinite 0 true",
    "title @a[tag=so_ar_zone] times 5 40 10",
    f"title @a[tag=so_ar_zone] title {T({'text': '¡Duelo!', 'color': 'red', 'bold': True})}",
    f"title @a[tag=so_ar_zone] subtitle {T({'text': 'Pierde quien baje a 3 corazones', 'color': 'gray'})}",
    f'tellraw {ZONE} [{json.dumps(PFX)},{{"text":"Duelo amistoso: ","color":"red","bold":false}},{{"selector":"@a[tag=so_ar_pvp]","color":"white"}}]',
    "execute store result score #song so_ar run random value 1..7",
    f"function {NS}:lib/music_play",
    f"function {NS}:lib/judges_salute",
])
F("mode/pvp/tick", [
    "execute as @a[tag=so_ar_pvp] store result score @s so_ar_hp run data get entity @s Health",
    f"execute as @a[tag=so_ar_pvp,scores={{so_ar_hp=..6}},limit=1] run function {NS}:mode/pvp/lose",
])
F("mode/pvp/second", [
    "scoreboard players add #t so_ar 1",
    f"execute as @a[tag=so_ar_pvp] unless entity @s[{PIT_BOX}] run function {NS}:mode/pvp/lose",
    f"execute if score #mode so_ar matches 10 unless entity @a[tag=so_ar_pvp] run function {NS}:mode/pvp/end",
    f"execute if score #t so_ar matches 300.. run function {NS}:mode/pvp/draw",
])
F("mode/pvp/lose", [
    "execute unless score #mode so_ar matches 10 run return 0",
    "tag @s remove so_ar_pvp",
    "effect give @s minecraft:instant_health 1 10 true",
    "effect clear @s minecraft:resistance",
    f'tellraw {ZONE} [{json.dumps(PFX)},{{"selector":"@a[tag=so_ar_pvp]","color":"gold","bold":true}},{{"text":" gana el duelo contra ","color":"yellow","bold":false}},{{"selector":"@s","color":"white"}}]',
    "title @a[tag=so_ar_pvp] title " + T({"text": "¡Ganaste el duelo!", "color": "gold", "bold": True}),
    f"function {NS}:lib/celebrar",
    f"function {NS}:mode/pvp/end",
])
F("mode/pvp/draw", [say(ZONE, "Duelo empatado por tiempo.", "gray"), f"function {NS}:mode/pvp/end"])
F("mode/pvp/end", [
    "effect give @a[tag=so_ar_pvp] minecraft:instant_health 1 10 true",
    "effect clear @a[tag=so_ar_pvp] minecraft:resistance",
    "tag @a remove so_ar_pvp",
    f"function {NS}:lib/music_stop",
    "scoreboard players set #mode so_ar 0",
    "scoreboard players set #exit so_ar 1", "scoreboard players set #ext so_ar 4",
])

# ---------------------------------------------------------------- diálogos
def act(cmd, label, tip=None, color=None, w=170):
    a = {"label": {"text": label} | ({"color": color} if color else {}), "width": w,
         "action": {"type": "minecraft:run_command", "command": cmd}}
    if tip: a["tooltip"] = {"text": tip, "color": "gray"}
    return a


def show(dialog, label, color, w=170):
    return {"label": {"text": label, "color": color}, "width": w, "action": {"type": "minecraft:show_dialog", "dialog": f"{NS}:{dialog}"}}


CLOSE = {"label": {"text": "✕ Cerrar", "color": "gray"}, "width": 170}
BACK = {"label": {"text": "« Volver"}, "width": 170, "action": {"type": "minecraft:show_dialog", "dialog": f"{NS}:main"}}


def dialog(name, title, color, body, actions, cols=2, w=170):
    W(f"data/{NS}/dialog/{name}.json", {
        "type": "minecraft:multi_action", "title": {"text": title, "color": color, "bold": True},
        **({"external_title": {"text": "Arena"}} if name == "main" else {}),
        "body": [{"type": "minecraft:plain_message", "contents": {"text": body, "color": "gray"}}],
        "columns": cols, "can_close_with_escape": True, "exit_action": CLOSE | {"width": w}, "pause": False,
        "actions": actions})


dialog("main", "Coliseo VorNeX", "gold",
       "Elegí desafío, música y mutadores. Después tocá la campana del túnel. Mercaderes y médica en el lobby.", [
           show("practice", "Práctica por tiers", "yellow"), show("contracts", "Contratos", "aqua"),
           show("dj", "Música de entrada", "light_purple"), show("mut", "Mutadores (x2 botín)", "red"),
           act("/trigger arena_con set 9", "Unirse al desafío", "Entrar si ya hay uno en curso o en preparación.", "green"),
           act("/trigger arena_ver", "Tribunas (espectador)", "Mirar invisible desde las gradas. Otra vez para bajar.", "aqua"),
           act("/trigger arena_pvp set 1", "Duelo PvP amistoso", "Retar o aceptar. Termina a los 3 corazones.", "red"),
           act("/trigger levelrank", "Ver mi rango y racha", "Se muestra en el chat.", "gray"),
           act("/trigger volver", "Volver a la isla", "Si hay desafío activo, cuenta como abandono.", "red"),
       ])
dialog("practice", "Práctica por tiers", "yellow",
       "El kit prestado se retira solo al terminar. Con equipo propio, si morís tus cosas quedan en el foso.",
       [x for t, n, mobs, thr in TIERS for x in (
           act(f"/trigger arena_pr set {t}", f"Tier {t} · {n} (kit)", f"Desde {fmt(thr)} bloques.", "yellow"),
           act(f"/trigger arena_pr set {t + 10}", f"Tier {t} · {n} (propio)", f"Desde {fmt(thr)} bloques.", "gold"))] + [BACK])
dialog("contracts", "Contratos", "aqua",
       "Un contrato por vez. Los enemigos escalan con tu fase. Cumplirlo sube tu rango oculto.",
       [act(f"/trigger arena_con set {n}", name, f"Desde {fmt(b)} bloques. {d}", "aqua", 250) for n, _, name, b, d in CONTRACTS] + [BACK | {"width": 250}],
       cols=1, w=250)
dialog("dj", "Música de entrada", "light_purple",
       "Elegí el tema que va a sonar en todo el estadio. También podés poner tu disco en el tocadiscos del túnel. Si no elegís, suena uno al azar.",
       [act(f"/trigger arena_dj set {n}", f"♪ {name}", None, "light_purple") for n, _, name, _ in SONGS] +
       [act("/trigger arena_dj set 8", "♪ Al azar", None, "dark_purple"),
        act("/trigger arena_con set 30", "¡Tocar la campana!", "Empieza el combate (solo desde el túnel).", "green"), BACK])
dialog("mut", "Mutadores", "red",
       "Cada mutador activo duplica el botín. Se eligen antes de la campana y se apagan al terminar.", [
           act("/trigger arena_mut set 1", "Niebla de Oscuridad", "Oscuridad constante en el foso.", "dark_gray"),
           act("/trigger arena_mut set 2", "Furia Monstruosa", "Monstruos con Velocidad II.", "red"),
           act("/trigger arena_mut set 3", "Vampirismo", "Monstruos con Regeneración II.", "dark_red"),
           act("/trigger arena_mut set 4", "Quitar todos", None, "gray"), BACK])

# ---------------------------------------------------------------- construcción
GRAD_MIX = ["minecraft:stone_bricks", "minecraft:polished_deepslate", "minecraft:cut_sandstone", "minecraft:smooth_sandstone"]
NROWS = 8


def row_r(i):
    return R_PITWALL + (R_GRADA - R_PITWALL) * i / NROWS


def band(x, dx, r0, r1, y0, y1, blk):
    za, zb = zr(dx, r0), zr(dx, r1)
    if zb < 0: return []
    if za < 0:
        return [f"fill {x} {y0} {CZ - zb} {x} {y1} {CZ + zb} {blk}"]
    if zb <= za: return []
    return [f"fill {x} {y0} {CZ - zb} {x} {y1} {CZ - za - 1} {blk}",
            f"fill {x} {y0} {CZ + za + 1} {x} {y1} {CZ + zb} {blk}"]


def in_band(dx, dz, r0, r1):
    za, zb = zr(dx, r0), zr(dx, r1)
    a = abs(dz)
    if zb < 0: return False
    if za < 0: return a <= zb
    return za < a <= zb


def grada_cell(deg, i):
    """Celda real de la fila i (misma geometría que band) cerca del ángulo dado. Devuelve (x, y_pie, z)."""
    rm = (row_r(i) + row_r(i + 1)) / 2
    dx = round(AX * rm * math.cos(math.radians(deg)))
    dz0 = round(BZ * rm * math.sin(math.radians(deg)))
    for d in (0, 1, -1, 2, -2, 3, -3):
        if in_band(dx, dz0 + d, row_r(i), row_r(i + 1)):
            return (CX + dx, 101 + i, CZ + dz0 + d)
    for e in (1, -1, 2, -2):
        for d in (0, 1, -1, 2, -2):
            if in_band(dx + e, dz0 + d, row_r(i), row_r(i + 1)):
                return (CX + dx + e, 101 + i, CZ + dz0 + d)
    return None


def facing_to_center(x, z):
    dx, dz = CX - x, CZ - z
    if abs(dx) > abs(dz): return "east" if dx > 0 else "west"
    return "south" if dz > 0 else "north"


def free_spot(deg):
    """Evita el túnel (sur) y el palco de jueces (norte)."""
    d = deg % 360
    return not (70 <= d <= 110 or 250 <= d <= 290)


steps = []
# 1-2: limpiar y base
cur = []
for dx in range(-AX, AX + 1):
    x, zb = CX + dx, zr(dx, 1.0)
    if zb < 0: continue
    cur.append(f"fill {x} 96 {CZ - zb} {x} {TOP_Y + 4} {CZ + zb} minecraft:air")
    cur.append(f"fill {x} 90 {CZ - zb} {x} 94 {CZ + zb} minecraft:deepslate_bricks")
    cur.append(f"fill {x} {G} {CZ - zb} {x} {G} {CZ + zb} {FLOOR_MIX[(dx // 3) % len(FLOOR_MIX)]}")
steps += [cur[:len(cur) // 2], cur[len(cur) // 2:]]
# 3: muro del foso, anillo, labio anti-arañas, baranda y luces empotradas
cur = []
for dx in range(-AX, AX + 1):
    x = CX + dx
    cur += band(x, dx, R_PIT - 0.03, R_PIT, G, G, "minecraft:chiseled_sandstone")
    cur += band(x, dx, R_PIT, R_PITWALL, G, 99, "minecraft:polished_blackstone_bricks")
    if dx % 6 == 3:
        cur += band(x, dx, R_PIT, R_PITWALL, 98, 98, "minecraft:pearlescent_froglight")
    cur += band(x, dx, R_LIP, R_PIT, 99, 99, "minecraft:smooth_sandstone_slab[type=top]")
    cur += band(x, dx, R_PIT, R_PITWALL, 100, 100, "minecraft:polished_blackstone_brick_wall")
cur += [f"setblock {x} {G} {z} minecraft:ochre_froglight" for x, z in FLOOR_LIGHTS]
steps.append(cur)
# 4-5: gradas + tiras de luz
cur = []
for i in range(NROWS):
    for dx in range(-AX, AX + 1):
        cur += band(CX + dx, dx, row_r(i), row_r(i + 1), G, 100 + i, GRAD_MIX[i % len(GRAD_MIX)])
for i in (1, 3, 5, 7):
    for dx in range(-AX, AX + 1):
        if dx % 6 == 0:
            cur += band(CX + dx, dx, row_r(i), row_r(i + 1), 100 + i, 100 + i,
                        "minecraft:ochre_froglight" if i % 4 == 1 else "minecraft:pearlescent_froglight")
steps += [cur[:len(cur) // 2], cur[len(cur) // 2:]]
# 6: muralla
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
# 7: terraza exterior (piso, aire, baranda) + plaza del lobby — antes que las torres
cur = []
TFLOOR = ["minecraft:smooth_sandstone", "minecraft:cut_sandstone"]
for dx in range(-int(AX * TR) - 1, int(AX * TR) + 2):
    x = CX + dx
    cur += band(x, dx, R_WALL + 0.03, TR, 96, 112, "minecraft:air")
    cur += band(x, dx, R_WALL - 0.01, TR, G, G, TFLOOR[(dx // 4) % 2])
    cur += band(x, dx, 1.105, 1.12, G, G, "minecraft:chiseled_sandstone")
    cur += band(x, dx, TR - 0.035, TR, 96, 96, "minecraft:sandstone_wall")
PZ0, PZ1, PXH = CZ + 52, LZ1 + 8, 22
cur += [f"fill {CX - PXH + 1} 96 {PZ0} {CX + PXH - 1} 112 {PZ1 - 1} minecraft:air",
        f"fill {CX - PXH} {G} {PZ0} {CX + PXH} {G} {PZ1} minecraft:smooth_sandstone",
        f"fill {CX - PXH + 2} {G} {LZ1 + 3} {CX + PXH - 2} {G} {LZ1 + 3} minecraft:chiseled_sandstone",
        f"fill {CX - PXH} 96 {CZ + 55} {CX - PXH} 96 {PZ1} minecraft:sandstone_wall",
        f"fill {CX + PXH} 96 {CZ + 55} {CX + PXH} 96 {PZ1} minecraft:sandstone_wall",
        f"fill {CX - PXH} 96 {PZ1} {CX + PXH} 96 {PZ1} minecraft:sandstone_wall"]
steps.append(cur)
# 8: torres (+ luz interior invisible para que no aparezcan mobs adentro)
cur = []
for tx, tz in TOWERS:
    cur += [f"fill {tx - 2} {G} {tz - 2} {tx + 2} {TOP_Y} {tz + 2} minecraft:polished_tuff",
            f"fill {tx - 1} 96 {tz - 1} {tx + 1} {TOP_Y - 1} {tz + 1} minecraft:air",
            f"fill {tx} 97 {tz} {tx} {TOP_Y - 2} {tz} minecraft:light[level=15]",
            f"fill {tx - 3} {TOP_Y + 1} {tz - 3} {tx + 3} {TOP_Y + 1} {tz + 3} minecraft:cut_sandstone",
            f"fill {tx - 1} {TOP_Y + 2} {tz - 1} {tx + 1} {TOP_Y + 2} {tz + 1} minecraft:glowstone"]
steps.append(cur)

# 9: palco de jueces, faroles, cofres de cohetes, cestas de donación, tocadiscos cerca del foso
cur = []
JB = (CX - 5, CX + 5, JUDGE_Z - 4, JUDGE_Z + 3)   # x0, x1, z0, z1
cur += [f"fill {JB[0]} {G} {JB[2]} {JB[1]} 108 {JB[3]} minecraft:polished_deepslate",
        f"fill {JB[0]} 109 {JB[2]} {JB[1]} 115 {JB[3]} minecraft:air",
        f"fill {JB[0] - 1} 116 {JB[2] - 1} {JB[1] + 1} 116 {JB[3] + 1} minecraft:polished_blackstone_bricks",
        f"fill {JB[0] - 1} 117 {JB[3] + 1} {JB[1] + 1} 117 {JB[3] + 1} minecraft:polished_blackstone_brick_slab",
        f"fill {JB[0]} 109 {JB[2]} {JB[1]} 115 {JB[2]} minecraft:polished_blackstone_bricks",
        f"fill {JB[0] + 1} 109 {JB[2] + 1} {JB[1] - 1} 109 {JB[3] - 1} minecraft:red_carpet",
        f"fill {JB[0]} 109 {JB[3]} {JB[1]} 109 {JB[3]} minecraft:polished_blackstone_brick_wall",
        f"setblock {CX} 112 {JB[2] + 1} minecraft:gold_block",
        f"setblock {CX} 113 {JB[2] + 1} minecraft:bell[attachment=floor,facing=south]"]
for px in (JB[0], JB[1]):
    cur += [f"fill {px} 109 {JB[3]} {px} 115 {JB[3]} minecraft:chiseled_sandstone",
            f"setblock {px} 113 {JB[3] + 1} minecraft:red_wall_banner[facing=south]",
            f"setblock {px} 110 {JB[3] + 1} minecraft:lantern" if False else f"setblock {px} 115 {JB[3] + 1} minecraft:soul_lantern[hanging=true]"]
for lx in (CX - 3, CX, CX + 3):
    cur.append(f"setblock {lx} 115 {JUDGE_Z} minecraft:lantern[hanging=true]")
cur.append(f"setblock {CX + 4} 109 {JB[2] + 1} minecraft:jukebox")
DECO_JUKES = [(CX + 4, 109, JB[2] + 1)]
# faroles en la fila alta y sobre la muralla
for k in range(12):
    deg = 15 + 30 * k
    if not free_spot(deg): continue
    c = grada_cell(deg, 7)
    if c:
        cur += [f"setblock {c[0]} {c[1]} {c[2]} minecraft:polished_blackstone_brick_wall",
                f"setblock {c[0]} {c[1] + 1} {c[2]} minecraft:lantern"]
for k in range(16):
    a = math.radians(k * 22.5 + 11.25)
    x, z = CX + round(AX * 0.965 * math.cos(a)), CZ + round(BZ * 0.965 * math.sin(a))
    cur.append(f"setblock {x} 128 {z} minecraft:soul_lantern")
# cofres de cobre con cohetes (fila alta)
ROCKET_CHESTS = []
for deg in (0, 45, 135, 180, 225, 315):
    c = grada_cell(deg, 7)
    if c:
        ROCKET_CHESTS.append(c)
        cur.append(f"setblock {c[0]} {c[1]} {c[2]} minecraft:copper_chest[facing={facing_to_center(c[0], c[2])}]")
# cestas de apoyo (fila 0)
HOPPERS = []
for deg in (30, 150, 210, 330):
    c = grada_cell(deg, 0)
    if c:
        HOPPERS.append(c)
        cur.append(f"setblock {c[0]} {c[1]} {c[2]} minecraft:hopper[facing=down]")
# tocadiscos junto al foso (fila 0, este y oeste)
for deg in (0, 180):
    c = grada_cell(deg, 0)
    if c:
        cur.append(f"setblock {c[0]} {c[1]} {c[2]} minecraft:jukebox")
        DECO_JUKES.append(c)
steps.append(cur)

# 10: decoración de la terraza (fuentes, pérgolas, árboles, glorietas con tocadiscos, faroles)
cur = []
RM = 1.11


def tpos(deg, r=RM):
    a = math.radians(deg)
    return CX + round(AX * r * math.cos(a)), CZ + round(BZ * r * math.sin(a))


def in_plaza(x, z):
    return abs(x - CX) <= PXH + 2 and z >= PZ0 - 3


for k in range(24):
    deg = 7.5 + 15 * k
    x, z = tpos(deg, TR - 0.06)
    if in_plaza(x, z): continue
    lan = "minecraft:lantern" if k % 2 else "minecraft:soul_lantern"
    cur += [f"fill {x} 96 {z} {x} 97 {z} minecraft:polished_deepslate_wall", f"setblock {x} 98 {z} {lan}"]
FEATURES = ["fountain", "pergola", "tree", "gazebo"]
for k in range(8):
    deg = 22.5 + 45 * k
    fx, fz = tpos(deg)
    if in_plaza(fx, fz): continue
    kind = FEATURES[k % 4]
    if kind == "fountain":
        cur += [f"fill {fx - 2} 96 {fz - 2} {fx + 2} 96 {fz + 2} minecraft:mossy_stone_bricks",
                f"fill {fx - 1} 96 {fz - 1} {fx + 1} 96 {fz + 1} minecraft:water",
                f"setblock {fx} {G} {fz} minecraft:sea_lantern",
                f"setblock {fx} 96 {fz} minecraft:chiseled_stone_bricks",
                f"setblock {fx} 97 {fz} minecraft:water",
                *[f"setblock {fx + a} 97 {fz + b} minecraft:lantern" for a, b in ((-2, -2), (2, -2), (-2, 2), (2, 2))]]
    elif kind == "pergola":
        cur += [*[f"fill {fx + a} 96 {fz + b} {fx + a} 98 {fz + b} minecraft:stripped_birch_log" for a, b in ((-2, -2), (2, -2), (-2, 2), (2, 2))],
                f"fill {fx - 2} 99 {fz - 2} {fx + 2} 99 {fz + 2} minecraft:flowering_azalea_leaves[persistent=true]",
                f"setblock {fx} 98 {fz} minecraft:lantern[hanging=true]",
                f"fill {fx - 1} 96 {fz - 1} {fx + 1} 96 {fz - 1} minecraft:birch_stairs[facing=north]",
                f"fill {fx - 1} 96 {fz + 1} {fx + 1} 96 {fz + 1} minecraft:birch_stairs[facing=south]"]
    elif kind == "tree":
        cur += [f"fill {fx - 2} {G} {fz - 2} {fx + 2} {G} {fz + 2} minecraft:moss_block",
                f"fill {fx - 2} 99 {fz - 2} {fx + 2} 100 {fz + 2} minecraft:cherry_leaves[persistent=true]",
                f"fill {fx - 1} 101 {fz - 1} {fx + 1} 101 {fz + 1} minecraft:cherry_leaves[persistent=true]",
                f"fill {fx} 96 {fz} {fx} 100 {fz} minecraft:cherry_log",
                *[f"setblock {fx + a} 96 {fz + b} minecraft:{fl}" for (a, b), fl in zip(((-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, 2)),
                                                                                     ("allium", "cornflower", "oxeye_daisy", "azure_bluet", "lily_of_the_valley", "poppy"))]]
    else:
        cur += [*[f"fill {fx + a} 96 {fz + b} {fx + a} 99 {fz + b} minecraft:chiseled_sandstone" for a, b in ((-2, -2), (2, -2), (-2, 2), (2, 2))],
                f"fill {fx - 2} 100 {fz - 2} {fx + 2} 100 {fz + 2} minecraft:smooth_sandstone_slab",
                f"setblock {fx} 96 {fz} minecraft:jukebox",
                f"setblock {fx} 99 {fz} minecraft:lantern[hanging=true]",
                f"fill {fx - 1} {G} {fz - 1} {fx + 1} {G} {fz + 1} minecraft:moss_block",
                f"setblock {fx} {G} {fz} minecraft:smooth_sandstone"]
        DECO_JUKES.append((fx, 96, fz))
# jardineras pequeñas entre medio
for k in range(8):
    deg = 45 * k
    x, z = tpos(deg, 1.065)
    if in_plaza(x, z): continue
    cur += [f"fill {x - 1} {G} {z - 1} {x + 1} {G} {z + 1} minecraft:moss_block",
            f"setblock {x} 96 {z} minecraft:flowering_azalea",
            f"setblock {x - 1} 96 {z} minecraft:azalea", f"setblock {x + 1} 96 {z} minecraft:azalea"]
# plaza: faroles, bancos y jardineras junto a las puertas del lobby
for x, z in ((CX - PXH + 2, LZ1 + 6), (CX + PXH - 2, LZ1 + 6), (CX - PXH + 2, PZ0 + 4), (CX + PXH - 2, PZ0 + 4),
             (CX - 14, LZ0 + 14), (CX + 14, LZ0 + 14)):
    cur += [f"fill {x} 96 {z} {x} 98 {z} minecraft:polished_deepslate_wall", f"setblock {x} 99 {z} minecraft:lantern"]
for sx in (-1, 1):
    bx = CX + sx * 17
    cur += [f"fill {bx - 1} {G} {LZ1 + 1} {bx + 1} {G} {LZ1 + 5} minecraft:moss_block",
            f"setblock {bx} 96 {LZ1 + 2} minecraft:flowering_azalea", f"setblock {bx} 96 {LZ1 + 4} minecraft:flowering_azalea",
            f"fill {bx - 3} 96 {LZ0 + 2} {bx - 3} 96 {LZ0 + 5} minecraft:spruce_stairs[facing=east]" if sx > 0 else
            f"fill {bx + 3} 96 {LZ0 + 2} {bx + 3} 96 {LZ0 + 5} minecraft:spruce_stairs[facing=west]"]
steps.append(cur)


# 11: túnel, lobby abierto, DJ, campana, pedestal, tacho, carteles, placas
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
cur += [f"fill {CX - 4} {G} {TZ0} {CX + 4} 101 {LZ0} minecraft:stone_bricks",
        f"fill {CX - 3} 96 {TZ0} {CX + 3} 100 {LZ0} minecraft:air",
        f"fill {CX - 3} {G} {TZ0} {CX + 3} {G} {LZ0} minecraft:polished_deepslate",
        f"fill {CX} {G} {TZ0 + 1} {CX} {G} {LZ0 - 1} minecraft:red_terracotta",
        f"fill {GATE_PIT} minecraft:iron_bars"]
for tz in range(TZ0 + 4, LZ0, 6):
    cur.append(f"setblock {CX} 100 {tz} minecraft:lantern[hanging=true]")
for tz in range(TZ0 + 2, LZ0, 4):  # luces empotradas en las paredes del túnel
    cur += [f"setblock {CX - 4} 99 {tz} minecraft:ochre_froglight", f"setblock {CX + 4} 99 {tz} minecraft:ochre_froglight"]
# lobby (núcleo seguro) con techo de vidrio y arcos hacia la plaza
cur += [f"fill {CX - LX} {G} {LZ0} {CX + LX} 105 {LZ1} minecraft:stone_bricks hollow",
        f"fill {CX - LX + 1} {G} {LZ0 + 1} {CX + LX - 1} {G} {LZ1 - 1} minecraft:polished_deepslate",
        f"fill {CX - LX + 1} 105 {LZ0 + 1} {CX + LX - 1} 105 {LZ1 - 1} minecraft:tinted_glass",
        f"fill {CX - LX} 105 {LZ0} {CX + LX} 105 {LZ0} minecraft:chiseled_sandstone",
        f"fill {CX - LX} 105 {LZ1} {CX + LX} 105 {LZ1} minecraft:chiseled_sandstone",
        f"fill {CX - 3} 96 {LZ0} {CX + 3} 100 {LZ0} minecraft:air",
        f"fill {GATE_LOBBY} minecraft:iron_bars",
        f"fill {CX} {G} {LZ0 + 1} {CX} {G} {LZ1 - 1} minecraft:red_terracotta",
        f"fill {CX - LX} 96 {LZ0 + 16} {CX - LX} 98 {LZ0 + 18} minecraft:air",
        f"fill {CX + LX} 96 {LZ0 + 16} {CX + LX} 98 {LZ0 + 18} minecraft:air",
        f"fill {CX - LX} 99 {LZ0 + 16} {CX - LX} 99 {LZ0 + 18} minecraft:chiseled_stone_bricks",
        f"fill {CX + LX} 99 {LZ0 + 16} {CX + LX} 99 {LZ0 + 18} minecraft:chiseled_stone_bricks",
        f"fill {CX - 1} 96 {LZ1} {CX + 1} 98 {LZ1} minecraft:air",
        f"fill {CX - 1} 99 {LZ1} {CX + 1} 99 {LZ1} minecraft:chiseled_stone_bricks"]
for lx in (CX - 6, CX, CX + 6):
    for lz in (LZ0 + 5, LZ0 + 12, LZ1 - 4):
        cur.append(f"setblock {lx} 104 {lz} minecraft:lantern[hanging=true]")
for lz in range(LZ0 + 3, LZ1, 4):
    cur += [f"setblock {CX - LX} 102 {lz} minecraft:ochre_froglight", f"setblock {CX + LX} 102 {lz} minecraft:ochre_froglight"]
# pedestal de recompensa y tacho de descarte
cur += [f"setblock {REWARD[0]} {G} {REWARD[2]} minecraft:chiseled_quartz_block",
        f"setblock {P(REWARD)} minecraft:chest[facing=west]",
        f"setblock {TRASH[0]} {G} {TRASH[2]} minecraft:magma_block",
        f"setblock {P(TRASH)} minecraft:cauldron",
        f"setblock {TRASH[0] - 1} 96 {TRASH[2]} minecraft:oak_wall_sign[facing=west]" if False else
        f"setblock {TRASH[0]} 96 {TRASH[2] + 1} minecraft:oak_sign[rotation=8]{sign_snbt(['Tacho de', ('descarte', 'dark_red'), 'tirá acá la', 'basura: se quema'])}"]
# placas del lobby
for x, fn, label, col in PADS:
    cur += [f"setblock {x} {G} {PAD_Z} minecraft:{col}_concrete",
            f"setblock {x} 96 {PAD_Z} minecraft:light_weighted_pressure_plate",
            f"setblock {x} 96 {PAD_Z - 1} minecraft:oak_sign[rotation=0]{sign_snbt(['Pisá la placa', (label, 'dark_blue'), '(o tocá el cartel)'], {'pad_pr': '/trigger arena_pr set 20', 'pad_con': '/trigger arena_con set 20', 'pad_join': '/trigger arena_con set 9', 'pad_back': '/trigger volver'}[fn])}"]
# muro oeste: práctica (y98 kit, y97 propio) + utilidades (y99)
for idx, (t, n, _, thr) in enumerate(TIERS):
    z = LZ0 + 6 + idx * 3
    cur.append(f"setblock {CX - LX + 1} 98 {z} minecraft:oak_wall_sign[facing=east]{sign_snbt([f'Práctica T{t}', (n, 'dark_green'), 'kit prestado', f'{thr} bloques+'], f'/trigger arena_pr set {t}')}")
    cur.append(f"setblock {CX - LX + 1} 97 {z} minecraft:oak_wall_sign[facing=east]{sign_snbt([f'Práctica T{t}', (n, 'dark_red'), 'equipo propio', ''], f'/trigger arena_pr set {t + 10}')}")
WEST_UP = [("Desafío", ("Unirse", "dark_green"), "", "/trigger arena_con set 9"),
           ("Espectador", ("Tribunas", "dark_aqua"), "(otra vez: bajar)", "/trigger arena_ver"),
           ("Reto extra", ("Mutadores", "dark_red"), "botín x2", "/trigger arena_mut set 0"),
           ("Amistoso", ("Duelo PvP", "dark_red"), "retar / aceptar", "/trigger arena_pvp set 1")]
for idx, (a, b, c, cmd) in enumerate(WEST_UP):
    cur.append(f"setblock {CX - LX + 1} 99 {LZ0 + 6 + idx * 3} minecraft:oak_wall_sign[facing=east]{sign_snbt([a, b, c], cmd)}")
# muro este: 7 contratos (y98 x4, y97 x3) + utilidades (y99)
for idx, (n, s, name, b, d) in enumerate(CONTRACTS):
    y = 98 if idx < 4 else 97
    z = LZ0 + 6 + (idx % 4) * 3
    cur.append(f"setblock {CX + LX - 1} {y} {z} minecraft:oak_wall_sign[facing=west]{sign_snbt(['Contrato', (name[:15], 'dark_aqua'), f'{b} bloques+'], f'/trigger arena_con set {n}')}")
EAST_UP = [("Tu rango", ("Ver rango", "dark_gray"), "y racha", "/trigger levelrank"),
           ("Salir", ("Volver a isla", "dark_red"), "", "/trigger volver"),
           ("Menú", ("Abrir menú", "gold"), "", "/trigger arena")]
for idx, (a, b, c, cmd) in enumerate(EAST_UP):
    cur.append(f"setblock {CX + LX - 1} 99 {LZ0 + 6 + idx * 3} minecraft:oak_wall_sign[facing=west]{sign_snbt([a, b, c], cmd)}")
cur.append(f"setblock {CX + LX - 1} 97 {LZ0 + 15} minecraft:oak_wall_sign[facing=west]{sign_snbt(['Tienda', ('Mercaderes', 'dark_green'), 'al fondo', ''])}")
for nid, name, color in MENU_VILLAGERS:
    x, z = [(i[1], i[3]) for i in INTER if i[0] == nid][0]
    cmd = {"main": "/trigger arena", "pr": "/trigger arena_pr set 20", "con": "/trigger arena_con set 20", "med": None}[nid]
    if not cmd: continue
    rot = 8 if z > LZ0 + 10 else 0
    dz = -1 if rot == 8 else 1
    cur.append(f"setblock {x} 96 {z + dz} minecraft:oak_sign[rotation={rot}]{sign_snbt([name[:15], ('Tocá acá', 'dark_blue'), 'o al aldeano'], cmd)}")
# estación DJ + campana + placa del portón + placa de salida
cur += [f"setblock {JUKE[0]} {G} {JUKE[2]} minecraft:gold_block",
        f"setblock {P(JUKE)} minecraft:jukebox",
        f"setblock {BELL[0]} {G} {BELL[2]} minecraft:gold_block",
        f"setblock {P(BELL)} minecraft:bell[attachment=floor,facing=west]",
        f"setblock {P(START_PLATE)} minecraft:polished_blackstone_pressure_plate",
        f"setblock {START_PLATE[0]} {G} {START_PLATE[2]} minecraft:chiseled_polished_blackstone",
        f"setblock {P(EXIT_PLATE)} minecraft:light_weighted_pressure_plate",
        f"setblock {EXIT_PLATE[0]} {G} {EXIT_PLATE[2]} minecraft:gold_block"]
for idx, (n, sid, name, _) in enumerate(SONGS + [(8, None, "Al azar", 0)]):
    cur.append(f"setblock {CX - 3} 97 {TZ0 + 5 + idx} minecraft:oak_wall_sign[facing=east]{sign_snbt(['Tema de entrada', ('♪ ' + name, 'dark_purple'), 'tocá para elegir', ''], f'/trigger arena_dj set {n}')}")
cur.append(f"setblock {CX - 3} 98 {TZ0 + 4} minecraft:oak_wall_sign[facing=east]{sign_snbt(['O poné tu disco', ('Tocadiscos', 'dark_purple'), 'acá abajo', ''])}")
for idx, (n, k, name) in enumerate(MUTS + [(4, None, "Quitar todos")]):
    cur.append(f"setblock {CX + 3} 97 {TZ0 + 6 + idx} minecraft:oak_wall_sign[facing=west]{sign_snbt(['Mutador x2', (name[:15], 'dark_red'), 'activar/quitar', ''], f'/trigger arena_mut set {n}')}")
cur.append(f"setblock {CX + 3} 98 {TZ0 + 4} minecraft:oak_wall_sign[facing=west]{sign_snbt(['¡Listo!', ('¡COMENZAR!', 'dark_green'), 'o tocá la campana', ''], '/trigger arena_con set 30')}")
steps.append(cur)

# arena_mut 0 desde el cartel del lobby abre el diálogo: trigger set 0 no dispara, usamos 20
for i, s in enumerate(steps):
    steps[i] = [l.replace("/trigger arena_mut set 0", "/trigger arena_mut set 20") for l in s]
_mut = open(os.path.join(ROOT, f"data/{NS}/function/lib/mut.mcfunction"), encoding="utf-8").read().splitlines()
F("lib/mut", [f"execute if score @s arena_mut matches 20 run return run dialog show @s {NS}:mut"] + _mut)

# ---------------------------------------------------------------- tribunas (espectador)
SPEC = grada_cell(0, 7)
F("lib/ver_dummy", ["# sin uso"])
os.remove(os.path.join(ROOT, f"data/{NS}/function/lib/ver_dummy.mcfunction"))
F("lib/ver", [
    f'execute unless entity @s[tag=so_ar_zone] run return run {say("@s", "Primero entrá al Coliseo con /trigger arena.", "red")}',
    f"execute if entity @s[tag=so_ar_spec] run return run function {NS}:lib/ver_off",
    f'execute if entity @s[tag=so_ar_in] if score #mode so_ar matches 1.. run return run {say("@s", "Estás peleando: no podés subir a las tribunas.", "red")}',
    f'execute if entity @s[tag=so_ar_ready] run return run {say("@s", "Estás en el túnel de preparación.", "red")}',
    "tag @s add so_ar_spec",
    f"tp @s {SPEC[0]} {SPEC[1]} {SPEC[2]} 90 15",
    "effect give @s minecraft:invisibility infinite 0 true",
    "effect give @s minecraft:resistance 30 4 true",
    say("@s", "Estás en las tribunas (invisible). Usá las cestas de apoyo para enviar ítems y los cofres de cobre para tirar cohetes. /trigger arena_ver para bajar.", "aqua"),
])
F("lib/ver_off", ["tag @s remove so_ar_spec", "effect clear @s minecraft:invisibility", f"tp @s {P(ARR)} 180 0",
                  say("@s", "De vuelta en el lobby.", "gray")])

# ---------------------------------------------------------------- cohetes, donaciones, tacho, tocadiscos
ROCKET = ('{{Slot:{s}b,id:"minecraft:firework_rocket",count:16,components:{{"minecraft:can_place_on":[{{}}],'
          '"minecraft:fireworks":{{flight_duration:2b,explosions:[{{shape:"{sh}",colors:[I;{c}],has_twinkle:1b,has_trail:1b}}]}}}}}}')
ROCKET_SETS = [("large_ball", "16711680,16776960"), ("star", "65535,16777215"), ("burst", "65280,16750848"), ("creeper", "16711935,255")]
F("lib/refill", [
    "# Cofres de cobre de las gradas: cohetes para festejar o apoyar (se pueden lanzar en modo aventura).",
    *[f"data modify block {x} {y} {z} Items set value [{','.join(ROCKET.format(s=i, sh=sh, c=c) for i, (sh, c) in enumerate(ROCKET_SETS))}]" for x, y, z in ROCKET_CHESTS],
])
F("lib/donations", [
    "# Cestas de apoyo: lo que un espectador tira en la tolva aparece junto a un luchador al azar.",
    *[f"execute if score #mode so_ar matches 1..8 if data block {x} {y} {z} Items[0] if entity {IN} run function {NS}:lib/donate {{x:{x},y:{y},z:{z}}}" for x, y, z in HOPPERS],
])
F("lib/donate", [
    '$execute as @a[tag=so_ar_in,limit=1,sort=random] at @s run summon minecraft:item ~ ~1.5 ~ {Tags:["so_ar_gift"],PickupDelay:10s,Motion:[0.0d,0.2d,0.0d],Item:{id:"minecraft:stone",count:1}}',
    "$data modify entity @e[type=minecraft:item,tag=so_ar_gift,limit=1] Item set from block $(x) $(y) $(z) Items[0]",
    "data remove entity @e[type=minecraft:item,tag=so_ar_gift,limit=1] Item.Slot",
    "execute as @e[type=minecraft:item,tag=so_ar_gift] at @s run particle minecraft:totem_of_undying ~ ~ ~ 0.3 0.3 0.3 0.2 20 force",
    "execute as @e[type=minecraft:item,tag=so_ar_gift] at @s run playsound minecraft:entity.player.levelup master @a[distance=..20] ~ ~ ~ 0.6 1.6",
    "tag @e[type=minecraft:item,tag=so_ar_gift] remove so_ar_gift",
    "$data remove block $(x) $(y) $(z) Items[0]",
    f"execute as {ZONE} at @s run playsound minecraft:entity.villager.celebrate master @s ~ ~ ~ 0.6 1.1",
    say(ZONE, "¡Un espectador envía suministros al foso!", "green"),
])
F("lib/trash", [
    f"execute positioned {TRASH[0]} 96 {TRASH[2]} if entity @e[type=minecraft:item,dx=0,dy=1,dz=0] run particle minecraft:large_smoke {TRASH[0]}.5 97 {TRASH[2]}.5 0.2 0.2 0.2 0.01 10",
    f"execute positioned {TRASH[0]} 96 {TRASH[2]} if entity @e[type=minecraft:item,dx=0,dy=1,dz=0] run playsound minecraft:block.lava.extinguish master @a[distance=..12] ~ ~ ~ 0.6 1",
    f"execute positioned {TRASH[0]} 96 {TRASH[2]} run kill @e[type=minecraft:item,dx=0,dy=1,dz=0]",
    *[f"execute if score #playing so_ar matches 1 run particle minecraft:note {x}.5 {y + 1.2} {z}.5 0.3 0.2 0.3 1 2" for x, y, z in DECO_JUKES],
])


# ---------------------------------------------------------------- aldeanos, jueces, público, carteles flotantes
def villager(x, y, z, tags, name=None, color="gold", prof="none", typ="plains", yaw=0):
    nm = f',CustomNameVisible:1b,CustomName:{{text:"{name}",color:"{color}",bold:true}}' if name else ""
    return (f'summon minecraft:villager {x}.5 {y} {z}.5 {{Tags:[{tags}],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,'
            f'Rotation:[{yaw}f,0f],VillagerData:{{profession:"minecraft:{prof}",level:5,type:"minecraft:{typ}"}}{nm}}}')


def label(x, y, z, text, color, tags='"so_ar_npc"', scale=1.0):
    return (f'summon minecraft:text_display {x}.5 {y} {z}.5 {{Tags:[{tags}],billboard:"center",'
            f'transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[{scale}f,{scale}f,{scale}f]}},'
            f'text:{{text:"{text}",color:"{color}",bold:true}}}}')


PROFS = ["farmer", "librarian", "fletcher", "shepherd", "butcher", "cartographer", "mason", "toolsmith"]
TYPES = ["plains", "desert", "savanna", "taiga", "snow", "jungle", "swamp"]


def npc_summons():
    out = [f"kill @e[tag=so_ar_npc,{ZONE_BOX}]"]
    for nid, name, color in MENU_VILLAGERS:
        x, z = [(i[1], i[3]) for i in INTER if i[0] == nid][0]
        prof = {"main": "cartographer", "pr": "weaponsmith", "con": "armorer", "med": "cleric"}[nid]
        out.append(villager(x, 96, z, '"so_ar_npc"', name, color, prof, yaw=(0 if z < LZ0 + 10 else 180)).replace(f"{x}.5 96 {z}.5", f"{x} 96 {z}"))
    for nid, x, y, z, w, h, _ in INTER:
        cx, cz = (f"{x}.5", f"{z}.5") if nid in ("bell", "dj") else (str(x), str(z))
        out.append(f'summon minecraft:interaction {cx} {y} {cz} {{Tags:["so_ar_npc","so_ar_npc_{nid}"],width:{w}f,height:{h}f,response:1b}}')
    for name, color, x, z, offers in TRADERS:
        out.append(f'summon minecraft:wandering_trader {x} 96 {z} {{Tags:["so_ar_npc"],NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,DespawnDelay:0,CustomNameVisible:1b,CustomName:{{text:"{name}",color:"{color}",bold:true}},Offers:{{Recipes:[{",".join(offers)}]}}}}')
    for i, (x, z) in enumerate(JUDGES):
        out.append(villager(x, 109, z, '"so_ar_npc","so_ar_judge"', ["Juez Áureo", "Juez Supremo", "Jueza Carmesí"][i], "gold", "cleric" if i == 1 else "librarian", "desert"))
    k = 0
    for deg in range(10, 360, 20):
        if not free_spot(deg) or deg in (30, 150, 210, 330): continue
        c = grada_cell(deg, 3 + (k % 3))
        if not c: continue
        yaw = (math.degrees(math.atan2(-(CX - c[0]), (CZ - c[2]))) + 360) % 360
        out.append(villager(c[0], c[1], c[2], '"so_ar_npc","so_ar_fan"', None, prof=PROFS[k % len(PROFS)], typ=TYPES[k % len(TYPES)], yaw=round(yaw)))
        k += 1
    out.append(label(CX, 118, JUDGE_Z + 3, "Coliseo VorNeX", "gold", '"so_ar_npc","so_ar_board"', 2.5))
    out += [label(x, y + 1, z, "Cesta de apoyo", "green", scale=0.7) for x, y, z in HOPPERS]
    out += [label(REWARD[0], 97.4, REWARD[2], "Cofre de recompensa", "gold", scale=0.6),
            label(TRASH[0], 97.4, TRASH[2], "Tacho de descarte", "red", scale=0.6),
            label(JUKE[0], 97.4, JUKE[2], "♪ DJ", "light_purple", scale=0.7),
            label(BELL[0], 97.4, BELL[2], "Campana de inicio", "gold", scale=0.7)]
    return out


N = len(steps)
for i, s in enumerate(steps):
    F(f"admin/build_{i + 1:02d}", [f"# coliseo: paso {i + 1}/{N}"] + s)
FL = f"{CX - 60} {CZ - 70} {CX + 60} {LZ1 + 14}"
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
    f"function {NS}:lib/refill",
    f"function {NS}:lib/board_idle",
    f"forceload remove {FL}",
    say("@a", "¡El Coliseo VorNeX está listo! Entrá con /trigger arena.", "green"),
    "execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1",
])
F("admin/npcs", [*npc_summons(), f"function {NS}:lib/refill", f"function {NS}:lib/board_idle", say("@s", "Aldeanos, jueces, público y carteles recolocados.", "green")])
F("npc_menu_pr", [f"dialog show @s {NS}:practice", f"function {NS}:lib/chat_main"])
F("npc_menu_con", [f"dialog show @s {NS}:contracts", f"function {NS}:lib/chat_main"])

# ---------------------------------------------------------------- admin
F("admin/help", [f"tellraw @s {T({'text': h, 'color': 'gold' if i == 0 else 'gray'})}" for i, h in enumerate([
    f"SO Arenas {VER} — ayuda admin",
    "Construir: /trigger arena (o volá a -5000 100 -5000) y /function so_arenas:admin/build",
    "Recolocar aldeanos/jueces/público: /function so_arenas:admin/npcs",
    "Limpiar el foso a mano: /function so_arenas:admin/reset_pit",
    "/function so_arenas:admin/status | stop | enable | disable",
    "Probar todo: /function so_arenas:admin/test",
    "Jugadores: /trigger arena, volver, levelrank, arena_ver (tribunas), arena_pvp (duelo)",
])])
F("admin/test", [
    f"tellraw @s {T({'text': '━━━ SO Arenas · Modo prueba ━━━', 'color': 'gold', 'bold': True})}",
    f"tellraw @s {T({'text': 'Como admin entrás a todo sin importar los bloques. Fase simulada para los enemigos:', 'color': 'gray'})}",
    f"tellraw @s {T(*[link(f'[{n}] ', f'/function so_arenas:admin/fase_{i}', 'aqua', f'Simular {v} bloques') for i, (n, v) in enumerate([('Fase 1', 0), ('Fase 2', 3500), ('Fase 3', 8000), ('Fase 4', 16000)])], link('[Real]', '/function so_arenas:admin/fase_real', 'gray', 'Usar los bloques reales'))}",
    f"tellraw @s {T({'text': ' Práctica: ', 'color': 'gray'}, *[link(f'[T{t}] ', f'/trigger arena_pr set {t}', 'yellow', f'Tier {t} con kit') for t in range(1, 5)])}",
    f"tellraw @s {T({'text': ' Contratos: ', 'color': 'gray'}, *[link(f'[{s}] ', f'/trigger arena_con set {n}', 'aqua', name) for n, s, name, _, _ in CONTRACTS])}",
    f"tellraw @s {T(link('[Campana: empezar ya] ', '/trigger arena_con set 30', 'gold', 'Saltar la espera del túnel'), link('[Ganar ya] ', '/function so_arenas:admin/win', 'green', 'Forzar victoria'), link('[Perder] ', '/function so_arenas:admin/lose', 'red', 'Forzar derrota'), link('[Detener]', '/function so_arenas:admin/stop', 'red', 'Cancelar y limpiar'))}",
    f"tellraw @s {T(link('[Probar donación] ', '/function so_arenas:admin/test_gift', 'green', 'Pone una manzana dorada en una cesta'), link('[Racha +2] ', '/scoreboard players add @s so_ar_streak 2', 'yellow', 'Para probar el cofre de racha'), link('[Limpiar foso]', '/function so_arenas:admin/reset_pit', 'gray', 'Solo ítems y bloques del óvalo interior'))}",
    f"tellraw @s {T({'text': 'Primero entrá con /trigger arena. Duelo PvP: necesitás 2 jugadores.', 'color': 'dark_gray'})}",
])
for i, v in enumerate([0, 3500, 8000, 16000]):
    F(f"admin/fase_{i}", [f"scoreboard players set #fake so_ar {v}", say("@s", f"Fase simulada: {v} bloques.", "aqua")])
F("admin/fase_real", ["scoreboard players reset #fake so_ar", say("@s", "Usando bloques reales.", "gray")])
F("admin/win", [
    f"execute if score #mode so_ar matches 1 run return run function {NS}:lib/win_practice",
    f"execute if score #mode so_ar matches 2..8 run return run function {NS}:lib/win_contract",
    say("@s", "No hay desafío en curso (si estás en el túnel, tocá la campana primero).", "gray"),
])
F("admin/lose", [f"execute if score #mode so_ar matches 1..8 run return run function {NS}:lib/fail", say("@s", "No hay desafío en curso.", "gray")])
F("admin/test_gift", [f"item replace block {HOPPERS[0][0]} {HOPPERS[0][1]} {HOPPERS[0][2]} container.0 with minecraft:golden_apple 2",
                      say("@s", "Manzanas en la cesta de apoyo: aparecen junto a un luchador si hay desafío.", "green")])
F("admin/reset_pit", [f"function {NS}:lib/reset_pit", say("@s", "Foso limpio (solo ítems/flechas y bloques del óvalo interior).", "gray")])
F("admin/status", [f"function {NS}:lib/blocks",
    f"tellraw @s {T(PFX, {'text': 'modo=', 'color': 'gray', 'bold': False}, {'score': {'name': '#mode', 'objective': 'so_ar'}, 'color': 'white'}, {'text': '  salida=', 'color': 'gray'}, {'score': {'name': '#exit', 'objective': 'so_ar'}, 'color': 'white'}, {'text': '  bloques=', 'color': 'gray'}, {'score': {'name': '#blk', 'objective': 'so_ar'}, 'color': 'white'}, {'text': '  tema=', 'color': 'gray'}, {'score': {'name': '#song', 'objective': 'so_ar'}, 'color': 'white'}, {'text': '  activo=', 'color': 'gray'}, {'score': {'name': '#enabled', 'objective': 'so_ar'}, 'color': 'white'})}"])
F("admin/stop", [f"function {NS}:lib/music_stop", "tag @a remove so_ar_pvp", f"function {NS}:lib/end_fight", f"function {NS}:lib/close_pit", say("@a", "Desafío del coliseo detenido por un administrador.", "gray")])
F("admin/enable", ["scoreboard players set #enabled so_ar 1", say("@s", "Arena activada.", "green")])
F("admin/disable", [f"function {NS}:admin/stop", "scoreboard players set #enabled so_ar 0", say("@s", "Arena desactivada.", "red")])
F("uninstall", [f"function {NS}:admin/stop", f"bossbar remove {NS}:fight",
    *[f"scoreboard objectives remove {o}" for o in ["so_ar", *TRIGGERS, *OBJS, "so_ar_death"]],
    say("@s", "so_arenas desinstalado (el coliseo queda en el mundo). Quitá el datapack y hacé /reload.", "gray")])

W("README.md", f"""# so_arenas {VER} — el Coliseo VorNeX

Zona en **-5000 100 -5000** (Overworld). Enemigos y jefes de `so_events:api/*` (sin duplicar mobs).

## Instalar / actualizar
1. Borrá la carpeta vieja `so-arenas` de `world/datapacks` y poné la nueva. `/reload`.
2. **Reconstruí** (hay terraza, palco, luces y túnel nuevos): `/trigger arena` y `/function so_arenas:admin/build` ({N} pasos, ~{2 + N // 2} s).
3. Si algún aldeano se pierde: `/function so_arenas:admin/npcs`.

## Flujo de un desafío
1. Elegís práctica o contrato (aldeanos, carteles, placas del piso, diálogo o chat).
2. Vas al **túnel de gladiadores**: elegís el tema (carteles, diálogo, chat o poniendo tu disco en el tocadiscos), activás mutadores y tocás la **campana**, el cartel ¡COMENZAR! o la placa del portón. A los 30 s arranca sola. Sin elección suena un tema épico al azar (Pigstep, Otherside, Creator, Relic, Precipice, Strad, Chirp).
3. Los jueces saludan, se abre la reja y la música suena en todo el estadio.
4. **Victoria**: cohetes, fanfarria, portones abiertos 60 s y un **cofre de recompensa** (cofre, cofre trampa, barril o cofre de cobre al azar) en el pedestal del lobby. Salís a pie por el túnel o pisando la placa dorada. Después el foso se limpia solo.
5. **Derrota / abandono**: sin recompensa, el foso se limpia a los 3 s.

## Limpieza segura
Solo se borran ítems, flechas y orbes del piso del foso, y bloques dentro del óvalo interior (barricadas). Nunca se tocan muros, labio anti-arañas, gradas, túnel, lobby, tocadiscos ni terraza.

## Desafíos
- Práctica Tier I–IV (0 / 3.334 / 7.501 / 15.000 bloques), con kit prestado o equipo propio.
- Contratos: {", ".join(f"{name} ({fmt(b)}+)" for _, _, name, b, _ in CONTRACTS)}.
- Mutadores (botín doble): Niebla de Oscuridad, Furia Monstruosa, Vampirismo.
- Racha: ganar sin morir; cofre extra a las 3, 5 y desde 10. Se ve con `/trigger levelrank`.
- Duelo PvP amistoso (`/trigger arena_pvp`): termina a los 3 corazones. Requiere PvP activado en el servidor.

## Estadio
- Lobby con techo de vidrio, arcos hacia una plaza y una terraza que rodea el coliseo: fuentes, pérgolas, cerezos, glorietas con tocadiscos, jardineras y faroles.
- Palco de jueces (norte) con tablero en vivo, público en las gradas, cofres de cobre con cohetes, cestas de apoyo (lo que tirás aparece junto a un luchador), médica de campaña, tacho de descarte.
- `/trigger arena_ver`: subir/bajar de las tribunas como espectador invisible.
""")

# ---------------------------------------------------------------- zip
os.makedirs("/mnt/documents", exist_ok=True)
out = f"/mnt/documents/so_arenas-{VER}.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for d, _, files in os.walk(ROOT):
        for f in files:
            full = os.path.join(d, f); z.write(full, os.path.relpath(full, ROOT))
print("ok", out, "pasos", N, "cofres", len(ROCKET_CHESTS), "cestas", len(HOPPERS), "jukes", len(DECO_JUKES), "spec", SPEC)
