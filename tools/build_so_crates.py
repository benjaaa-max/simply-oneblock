#!/usr/bin/env python3
"""Genera el datapack so_crates (zona de Crates con bóvedas vanilla de canje ilimitado).
Uso: python3 tools/build_so_crates.py
Editá CENTER, las llaves (KEYS / OUR_KEYS) y las tablas de botín (LOOT) y regenerá.
"""
import json, pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent / "datapacks/so-crates"
CX, CY, CZ = 5000, 200, 5000          # centro de la plataforma (Y = suelo + 1)
ISLAND = (0, 65, 0)                   # regreso si no hay posición guardada (bloque OneBlock 0 64 0)
R = 15                                # media anchura de la plataforma

if ROOT.exists():
    shutil.rmtree(ROOT)
D = ROOT / "data/so_crates"
FN, LT = D / "function", D / "loot_table"


def w(path, text):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def fn(name, lines): w(f"data/so_crates/function/{name}.mcfunction", "\n".join(lines))
def js(path, obj): w(path, json.dumps(obj, ensure_ascii=False, indent=2))


# ---------------------------------------------------------------- llaves
# Llaves de Simply OneBlock: nombre EXACTO (string plano), igual que sus vaults.
# tier 1 = barata (apuesta chica) ... 3 = cara (mejores probabilidades)
SIMPLY = [  # (id, nombre exacto, item, tier)
    ("cemetery", "Cemetery Key", "trial_key", 1), ("graveyard", "Graveyard Key", "trial_key", 1),
    ("ossuary", "Ossuary Key", "trial_key", 1), ("old_tower", "Old Tower Key", "trial_key", 1),
    ("pyramid", "Pyramid Key", "trial_key", 2), ("rusty", "Rusty Mineshaft Key", "trial_key", 2),
    ("treasure", "Treasure Room", "trial_key", 2), ("deep", "Deep_Key", "trial_key", 2),
    ("elder", "Elder Guardian Key", "ominous_trial_key", 3), ("warden", "Warden_Key", "ominous_trial_key", 3),
    ("wither", "Wither Arena", "ominous_trial_key", 3), ("to_the_end", "To the End", "trial_key", 3),
]
# Llaves propias de so_crates (nombre con color; la bóveda compara todo, por eso se usan iguales en todos lados)
OURS = [  # (id, nombre, color, item, crate)
    ("builder", "Llave del Arquitecto", "aqua", "trial_key", "Crate del Constructor"),
    ("miner", "Llave Subterránea", "gray", "trial_key", "Crate del Minero"),
    ("nature", "Llave Silvestre", "green", "trial_key", "Crate de la Naturaleza"),
    ("combat", "Llave de Batalla", "red", "trial_key", "Crate de Combate"),
    ("mystic", "Llave Abisal", "dark_purple", "ominous_trial_key", "Crate Místico"),
    ("legend", "Llave del Vacío", "gold", "ominous_trial_key", "Crate Legendario"),
]


def our_components_snbt(k):
    _, name, color, _, crate = k
    return (f'{{"minecraft:custom_name":{{text:"{name}",color:"{color}",italic:false}},'
            f'"minecraft:lore":[{{text:"Abre: {crate}",color:"gray",italic:false}}]}}')


def our_give_args(k):
    _, name, color, _, crate = k
    return (f'[custom_name={{text:"{name}",color:"{color}",italic:false}},'
            f'lore=[{{text:"Abre: {crate}",color:"gray",italic:false}}]]')


def our_components_json(k):
    _, name, color, _, crate = k
    return {"minecraft:custom_name": {"text": name, "color": color, "italic": False},
            "minecraft:lore": [{"text": f"Abre: {crate}", "color": "gray", "italic": False}]}


OK = {k[0]: k for k in OURS}

# ---------------------------------------------------------------- botín
def it(name, w_=1, lo=1, hi=1, extra=None):
    e = {"type": "minecraft:item", "name": f"minecraft:{name}", "weight": w_}
    f = []
    if hi > 1 or lo > 1:
        f.append({"function": "minecraft:set_count", "count": {"min": lo, "max": hi} if hi != lo else lo})
    if extra:
        f += extra
    if f:
        e["functions"] = f
    return e


def book(w_, ench=None):  # libro encantado aleatorio (opcional: lista de encantamientos)
    fx = {"function": "minecraft:enchant_randomly"}
    if ench:
        fx["options"] = [f"minecraft:{x}" for x in ench]
    return it("book", w_, extra=[fx])


def potion(w_, p, kind="potion"):
    return it(kind, w_, extra=[{"function": "minecraft:set_potion", "id": f"minecraft:{p}"}])


def key(kid, w_):
    k = OK[kid]
    return it(k[3], w_, extra=[{"function": "minecraft:set_components", "components": our_components_json(k)}])


def empty(w_): return {"type": "minecraft:empty", "weight": w_}
def pool(entries, rolls=1): return {"rolls": rolls, "entries": [e for e in entries if e.get("weight", 1) > 0]}
def table(*pools): return {"type": "minecraft:vault", "pools": list(pools)}


ANY_KEY = lambda w_: [key(k[0], w_) for k in OURS[:5]]

LOOT = {}
# OneBlock Crate: una bóveda por llave de Simply; el tier sube cantidades y chances.
for sid, _, _, t in SIMPLY:
    LOOT[f"oneblock/{sid}"] = table(
        pool([it("emerald", 10, t, 3 * t), it("emerald", 2 * t, 4 * t, 8 * t), empty(6 - t * 2)]),
        pool([it("iron_ingot", 6, 2, 6 * t), it("gold_ingot", 4, 2, 4 * t), it("cooked_beef", 5, 4, 12),
              it("golden_carrot", 3, 2, 6 * t), it("arrow", 4, 8, 24), it("experience_bottle", 3, 2, 6 * t),
              it("diamond", t, 1, t), book(t)], rolls=t),
        pool(ANY_KEY(1) + [key("legend", 1 if t == 3 else 0) if t == 3 else empty(0), empty(40 - 8 * t)]),
    )

LOOT["builder"] = table(pool([
    it("cherry_planks", 4, 32, 64), it("mangrove_planks", 4, 32, 64), it("bamboo_planks", 3, 32, 64),
    it("quartz_block", 4, 16, 48), it("smooth_quartz", 3, 16, 48), it("polished_blackstone_bricks", 3, 32, 64),
    it("deepslate_tiles", 3, 32, 64), it("sea_lantern", 3, 8, 24), it("lantern", 3, 8, 16),
    it("white_glazed_terracotta", 2, 16, 32), it("cyan_glazed_terracotta", 2, 16, 32),
    it("oxidized_cut_copper", 2, 16, 32), it("waxed_copper_block", 2, 8, 24), it("calcite", 3, 32, 64),
    it("tuff_bricks", 3, 32, 64), it("mud_bricks", 3, 32, 64), it("glass", 4, 32, 64),
    it("prismarine_bricks", 2, 16, 32), it("purpur_block", 1, 16, 32), it("end_rod", 2, 8, 16),
], rolls=3), pool([it("emerald", 1, 2, 6), key("builder", 1), empty(5)]))

LOOT["miner"] = table(pool([
    it("raw_iron", 6, 8, 24), it("raw_copper", 5, 16, 32), it("raw_gold", 4, 6, 16), it("coal", 5, 16, 32),
    it("lapis_lazuli", 4, 8, 24), it("redstone", 4, 16, 32), it("amethyst_shard", 3, 8, 16),
    it("diamond", 2, 1, 4), it("emerald", 2, 2, 6), it("iron_pickaxe", 2),
    book(2, ["efficiency", "fortune", "unbreaking"]),
], rolls=3), pool([key("miner", 1), key("mystic", 1), empty(10)]))

LOOT["nature"] = table(pool([
    it("cherry_sapling", 3, 2, 4), it("mangrove_propagule", 3, 2, 4), it("dark_oak_sapling", 3, 4, 8),
    it("jungle_sapling", 3, 2, 6), it("sugar_cane", 4, 4, 12), it("bamboo", 3, 4, 12), it("cactus", 3, 2, 6),
    it("nether_wart", 3, 4, 8), it("crimson_fungus", 2, 2, 4), it("warped_fungus", 2, 2, 4),
    it("melon_seeds", 3, 2, 6), it("pumpkin_seeds", 3, 2, 6), it("cocoa_beans", 3, 2, 6),
    it("honeycomb", 3, 4, 8), it("bone_meal", 4, 16, 32), it("cow_spawn_egg", 1), it("sheep_spawn_egg", 1),
    it("chicken_spawn_egg", 1), it("bee_spawn_egg", 1), it("pig_spawn_egg", 1),
], rolls=3), pool([key("nature", 1), empty(7)]))

LOOT["combat"] = table(pool([
    potion(4, "healing"), potion(3, "strength"), potion(3, "swiftness"), potion(2, "fire_resistance"),
    potion(2, "regeneration", "splash_potion"), it("ender_pearl", 3, 2, 6), it("arrow", 5, 16, 48),
    it("golden_apple", 3, 1, 3), it("iron_chestplate", 2), it("iron_sword", 2), it("shield", 2),
    it("crossbow", 1), it("spectral_arrow", 3, 8, 16),
    book(3, ["sharpness", "protection", "power", "smite", "projectile_protection"]),
], rolls=3), pool([key("combat", 1), key("legend", 1), empty(14)]))

LOOT["mystic"] = table(pool([
    it("blaze_rod", 5, 2, 6), it("ghast_tear", 3, 1, 3), it("ender_pearl", 4, 2, 6), it("magma_cream", 3, 2, 6),
    it("glowstone", 3, 8, 16), it("quartz", 4, 16, 32), it("shulker_shell", 2, 1, 2), it("ancient_debris", 1),
    it("crying_obsidian", 2, 4, 8), it("experience_bottle", 4, 8, 16), it("nether_wart", 3, 8, 16),
    book(3),
], rolls=3), pool([key("mystic", 1), key("legend", 1), empty(10)]))

LOOT["legend"] = table(
    pool([it("totem_of_undying", 3), it("enchanted_golden_apple", 2), it("diamond", 5, 3, 8),
          it("netherite_scrap", 2, 1, 2), it("heart_of_the_sea", 2), it("nether_star", 1),
          it("trident", 1), it("music_disc_pigstep", 1), it("emerald_block", 3, 2, 6),
          book(3, ["mending", "unbreaking", "looting", "fortune", "silk_touch"])], rolls=2),
    pool([it("emerald", 1, 8, 24)]),
)

for name, t in LOOT.items():
    js(f"data/so_crates/loot_table/{name}.json", t)

# ---------------------------------------------------------------- disposición de bóvedas
VAULTS = []  # (x, y, z, facing, key_item_snbt, loot, titulo, subtitulo, ominous)
for i, (sid, nm, item, t) in enumerate(SIMPLY):
    comp = f'{{"minecraft:custom_name":"{nm}"}}'
    VAULTS.append((CX - 11 + 2 * i, CY, CZ - 10, "south", f'{{id:"minecraft:{item}",count:1,components:{comp}}}',
                   f"oneblock/{sid}", "OneBlock Crate", nm, item.startswith("ominous")))
for i, k in enumerate(OURS):
    VAULTS.append((CX - 10 + 4 * i, CY, CZ + 10, "north",
                   f'{{id:"minecraft:{k[3]}",count:1,components:{our_components_snbt(k)}}}',
                   k[0], k[4], k[1], k[3].startswith("ominous")))

SIGN_ROT = {"south": 0, "north": 8}
x0, x1, z0, z1 = CX - R, CX + R, CZ - R, CZ + R
build = [
    "# Construye la zona de Crates. Párate en la zona antes (admin/goto) para que esté cargada.",
    f"fill {x0-1} {CY} {z0-1} {x1+1} {CY+4} {z1+1} minecraft:barrier hollow",
    f"fill {x0} {CY-1} {z0} {x1} {CY-1} {z1} minecraft:polished_blackstone_bricks",
    f"fill {x0} {CY} {z0} {x1} {CY+3} {z1} minecraft:air",
    f"fill {x0-1} {CY-2} {z0-1} {x1+1} {CY-2} {z1+1} minecraft:barrier",
]
for dx in range(-R + 2, R - 1, 5):
    for dz in range(-R + 2, R - 1, 5):
        build.append(f"setblock {CX+dx} {CY-1} {CZ+dz} minecraft:sea_lantern")
build.append(f"fill {CX-1} {CY-1} {CZ-1} {CX+1} {CY-1} {CZ+1} minecraft:gilded_blackstone")
reset = []
for x, y, z, face, keysnbt, loot, title, sub, omin in VAULTS:
    o = "true" if omin else "false"
    build.append(f'setblock {x} {y} {z} minecraft:vault[facing={face},ominous={o}]'
                 f'{{config:{{key_item:{keysnbt},loot_table:"so_crates:{loot}"}}}} replace')
    build.append(f'setblock {x} {y+1} {z} minecraft:dark_oak_sign[rotation={SIGN_ROT[face]}]'
                 f'{{is_waxed:1b,front_text:{{messages:["",{{text:"{title}",color:"gold",bold:true}},'
                 f'{{text:"{sub}",color:"dark_gray"}},""]}}}} replace')
    reset.append(f"data modify block {x} {y} {z} server_data.rewarded_players set value []")
build += [
    f'setblock {CX} {CY} {CZ+3} minecraft:dark_oak_sign[rotation=8]{{is_waxed:1b,front_text:{{messages:["",'
    f'{{text:"« Volver a la isla",color:"dark_green",bold:true,click_event:{{action:"run_command",command:"/trigger isla"}}}},'
    f'{{text:"(toca el cartel)",color:"gray"}},""]}}}} replace',
    f'tellraw @s [{{"text":"[SO Crates] ","color":"gold"}},{{"text":"Zona construida: {len(VAULTS)} bóvedas.","color":"green"}}]',
]
fn("admin/build", build)
fn("lib/reset_vaults", ["# Vacía la lista de jugadores premiados: canje ilimitado mientras tengas llaves"] + reset)

# ---------------------------------------------------------------- lógica
ZONE = f"x={x0-1},y={CY-6},z={z0-1},dx={2*R+2},dy=20,dz={2*R+2}"
w("data/minecraft/tags/function/load.json", json.dumps({"values": ["so_crates:load"]}))
w("data/minecraft/tags/function/tick.json", json.dumps({"values": ["so_crates:tick"]}))
js("pack.mcmeta", {"pack": {"description": "Simply OneBlock Expansion - Crates (/trigger crates)",
                            "min_format": [107, 1], "max_format": [107, 1]}})
fn("load", [
    "scoreboard objectives add so_crates dummy",
    "scoreboard objectives add crates trigger",
    "scoreboard objectives add isla trigger",
    "scoreboard objectives add so_cr_x dummy",
    "scoreboard objectives add so_cr_y dummy",
    "scoreboard objectives add so_cr_z dummy",
    "scoreboard objectives add so_cr_saved dummy",
    "execute unless score #enabled so_crates matches 0..1 run scoreboard players set #enabled so_crates 1",
    'tellraw @a[tag=oneblock_admin] [{"text":"[SO Crates] ","color":"gold"},{"text":"cargado. Ayuda: /function so_crates:admin/help","color":"gray"}]',
])
fn("tick", [
    "execute if score #enabled so_crates matches 1 as @a[scores={crates=1..}] at @s run function so_crates:lib/go",
    "execute if score #enabled so_crates matches 1 as @a[scores={isla=1..}] at @s run function so_crates:lib/back",
    "scoreboard players reset @a crates", "scoreboard players enable @a crates",
    "scoreboard players reset @a isla", "scoreboard players enable @a isla",
    "scoreboard players add #t so_crates 1",
    "execute if score #t so_crates matches 10.. run function so_crates:lib/zone",
])
fn("lib/zone", [
    "scoreboard players set #t so_crates 0",
    f"execute in minecraft:overworld run tag @a[{ZONE}] add so_cr_now",
    "execute as @a[tag=so_cr_now,tag=!so_cr_in] run function so_crates:lib/enter",
    "execute as @a[tag=so_cr_in,tag=!so_cr_now] run function so_crates:lib/leave",
    "scoreboard players add #r so_crates 1",
    "execute if score #r so_crates matches 2.. if entity @a[tag=so_cr_now] in minecraft:overworld run function so_crates:lib/reset_vaults",
    "execute if score #r so_crates matches 2.. run scoreboard players set #r so_crates 0",
    "tag @a remove so_cr_now",
])
fn("lib/enter", [
    "tag @s add so_cr_in",
    "execute unless entity @s[tag=oneblock_admin] if entity @s[gamemode=survival] run tag @s add so_cr_gm",
    "execute unless entity @s[tag=oneblock_admin] run gamemode adventure @s",
    'title @s actionbar {"text":"✦ Zona de Crates ✦","color":"gold"}',
    'execute if entity @s[tag=oneblock_admin,gamemode=!adventure] run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"⚠ Estás en la zona de Crates. ","color":"yellow"},{"text":"[Pasar a Aventura]","color":"green","underlined":true,"click_event":{"action":"run_command","command":"/gamemode adventure"},"hover_event":{"action":"show_text","value":"Clic para cambiar a modo aventura"}}]',
    "execute if entity @s[tag=oneblock_admin,gamemode=!adventure] at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 0.6 1.2",
])
fn("lib/leave", [
    "tag @s remove so_cr_in",
    "execute if entity @s[tag=so_cr_gm,gamemode=adventure] run gamemode survival @s",
    "tag @s remove so_cr_gm",
])
fn("lib/go", [
    'execute unless dimension minecraft:overworld run return run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Solo podés viajar desde el mundo normal (no desde el Nether, el End ni las dimensiones de fase).","color":"red"}]',
    'execute if entity @s[tag=so_cr_in] run return run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Ya estás en la zona de Crates. Para volver: /trigger isla","color":"yellow"}]',
    "execute store result score @s so_cr_x run data get entity @s Pos[0]",
    "execute store result score @s so_cr_y run data get entity @s Pos[1]",
    "execute store result score @s so_cr_z run data get entity @s Pos[2]",
    "scoreboard players set @s so_cr_saved 1",
    f"tp @s {CX} {CY} {CZ+5} 180 0",
    "playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1",
    'tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Bienvenido. Poné tu llave en la bóveda que la acepte. Para volver: ","color":"green"},{"text":"/trigger isla","color":"yellow","click_event":{"action":"run_command","command":"/trigger isla"}}]',
])
fn("lib/back", [
    'execute unless entity @s[tag=so_cr_in] run return run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Este comando solo funciona dentro de la zona de Crates.","color":"red"}]',
    "execute store result storage so_crates:tmp x int 1 run scoreboard players get @s so_cr_x",
    "execute store result storage so_crates:tmp y int 1 run scoreboard players get @s so_cr_y",
    "execute store result storage so_crates:tmp z int 1 run scoreboard players get @s so_cr_z",
    "execute if score @s so_cr_saved matches 1 run function so_crates:lib/back_tp with storage so_crates:tmp",
    f"execute unless score @s so_cr_saved matches 1 in minecraft:overworld run tp @s {ISLAND[0]} {ISLAND[1]} {ISLAND[2]}",
    "scoreboard players reset @s so_cr_saved",
    "function so_crates:lib/leave",
    "execute at @s run playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1",
])
fn("lib/back_tp", ["$execute in minecraft:overworld run tp @s $(x) $(y) $(z)"])

# ---------------------------------------------------------------- admin
for sid, nm, item, _ in SIMPLY:
    fn(f"give/{sid}", [f'give @s minecraft:{item}[custom_name="{nm}"] 1'])
for k in OURS:
    fn(f"give/{k[0]}", [f"give @s minecraft:{k[3]}{our_give_args(k)} 1"])
fn("admin/give_all_keys", [f"function so_crates:give/{s[0]}" for s in SIMPLY] + [f"function so_crates:give/{k[0]}" for k in OURS])
fn("admin/goto", [f"execute in minecraft:overworld run tp @s {CX} {CY+2} {CZ}"])
fn("admin/enable", ["scoreboard players set #enabled so_crates 1", 'tellraw @s {"text":"[SO Crates] activado","color":"green"}'])
fn("admin/disable", ["scoreboard players set #enabled so_crates 0", 'tellraw @s {"text":"[SO Crates] desactivado (/trigger crates no hace nada)","color":"red"}'])
fn("admin/status", [
    'tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"activo: ","color":"gray"},{"score":{"name":"#enabled","objective":"so_crates"},"color":"white"}]',
    f'tellraw @s [{{"text":"Zona: {CX} {CY} {CZ} (overworld) · bóvedas: {len(VAULTS)}","color":"gray"}}]',
    'tellraw @s [{"text":"Jugadores en la zona: ","color":"gray"},{"selector":"@a[tag=so_cr_in]"}]',
])
fn("admin/help", [
    'tellraw @s {"text":"══ SO Crates · admin ══","color":"gold","bold":true}',
    'tellraw @s {"text":"1) /function so_crates:admin/goto  → te lleva a la zona","color":"gray"}',
    'tellraw @s {"text":"2) /function so_crates:admin/build → construye plataforma y bóvedas","color":"gray"}',
    'tellraw @s {"text":"/function so_crates:admin/give_all_keys · give/<llave>","color":"gray"}',
    'tellraw @s {"text":"/function so_crates:admin/status · enable · disable · uninstall","color":"gray"}',
    'tellraw @s {"text":"Jugadores: /trigger crates (ir) · /trigger isla (volver)","color":"gray"}',
])
fn("uninstall", [
    "execute as @a[tag=so_cr_in] run function so_crates:lib/leave",
    *[f"scoreboard objectives remove {o}" for o in ["so_crates", "crates", "isla", "so_cr_x", "so_cr_y", "so_cr_z", "so_cr_saved"]],
    "data remove storage so_crates:tmp x",
    'tellraw @s {"text":"[SO Crates] desinstalado. Quitá la carpeta del datapack y /reload. La plataforma queda construida.","color":"yellow"}',
])

# ---------------------------------------------------------------- readme
simply_rows = "\n".join(f"- {nm} — nivel {t}" for _, nm, _, t in SIMPLY)
ours_rows = "\n".join(f"- {k[1]} → {k[4]}" for k in OURS)
w("README.md", f"""# SO Crates (so_crates) v0.1

Zona de Crates con bóvedas de Minecraft (vaults). Abrís con llave, la bóveda gira unos segundos y te tira el premio.
Canje ilimitado: mientras tengas llaves, podés abrir la misma bóveda las veces que quieras.

## Instalación (admin)
1. Copiá la carpeta `so-crates` a `world/datapacks/` y `/reload`.
2. `/function so_crates:admin/goto` (te lleva a {CX} {CY} {CZ} del mundo normal).
3. `/function so_crates:admin/build` (construye la plataforma con barreras y las {len(VAULTS)} bóvedas).

## Jugadores
- `/trigger crates` → viaja a la zona (solo desde el mundo normal). Guarda dónde estabas.
- `/trigger isla` o tocar el cartel "Volver a la isla" → regresa al lugar de donde viniste.
- Dentro de la zona se pasa a modo aventura (no se puede romper ni construir). Al salir vuelve a supervivencia.
- Admins (tag `oneblock_admin`): no se les cambia el modo; reciben un aviso con clic para pasar a aventura.

## OneBlock Crate (12 bóvedas, fila norte)
Una bóveda por cada llave de Simply OneBlock. Mayor nivel = más premios y mejores chances (y chance de Llave del Vacío en nivel 3).
{simply_rows}

## Crates temáticos (fila sur)
{ours_rows}

## Llaves para probar
`/function so_crates:admin/give_all_keys` o `/function so_crates:give/<id>` (cemetery, warden, builder, legend, ...).
La venta en la tienda se agrega en so_shop (próximo paso).

## Ajustes
Todo se edita en `tools/build_so_crates.py` (centro, botín, llaves) y se regenera.
""")
print("so_crates:", len(VAULTS), "bóvedas,", len(LOOT), "tablas de botín")
