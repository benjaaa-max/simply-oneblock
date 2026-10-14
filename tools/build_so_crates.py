#!/usr/bin/env python3
"""Genera el datapack so_crates v2 (Templo de las Bóvedas + Forja de Llaves).
Uso: python3 tools/build_so_crates.py
Fuente única de verdad: nunca editar los .mcfunction / .json generados a mano.
"""
import json, pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent / "datapacks/so-crates"
VERSION = "2.0"
CX, FY, CZ = 5000, 100, 5000           # centro del templo; FY = cota del suelo (se pisa en FY+1)
ISLAND = (0, 65, 0)                    # regreso si no hay posición guardada
X0, X1, Z0, Z1 = 4970, 5030, 4980, 5020  # caja exterior del templo
TOP = 118                              # última fila de muro (techo en TOP+1)
OLD = (4983, 193, 4983, 5017, 206, 5017)  # plataforma vieja v1 (Y=200) a limpiar
ARRIVE = (5000.5, FY + 1, 5012.5)
PORTAL_Z = 5018                        # placa de regreso (x 4999..5001)

if ROOT.exists():
    shutil.rmtree(ROOT)


def w(path, text):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def fn(name, lines): w(f"data/so_crates/function/{name}.mcfunction", "\n".join(lines))
def js(path, obj): w(path, json.dumps(obj, ensure_ascii=False, indent=2))


# ================================================================ llaves
# Simply OneBlock: custom_name EXACTO en string plano (sus cámaras/bóvedas comparan 1:1).
SIMPLY = [  # (id, nombre exacto, item, tier, nombre del crate)
    ("cemetery", "Cemetery Key", "trial_key", 1, "Cripta del Cementerio"),
    ("graveyard", "Graveyard Key", "trial_key", 1, "Camposanto"),
    ("ossuary", "Ossuary Key", "trial_key", 1, "Osario"),
    ("old_tower", "Old Tower Key", "trial_key", 1, "Torre Antigua"),
    ("pyramid", "Pyramid Key", "trial_key", 2, "Pirámide del Desierto"),
    ("rusty", "Rusty Mineshaft Key", "trial_key", 2, "Mina Oxidada"),
    ("treasure", "Treasure Room", "trial_key", 2, "Sala del Tesoro"),
    ("deep", "Deep_Key", "trial_key", 2, "Las Profundidades"),
    ("elder", "Elder Guardian Key", "ominous_trial_key", 3, "Guardián Anciano"),
    ("to_the_end", "To the End", "trial_key", 3, "Hacia el End"),
    ("warden", "Warden_Key", "ominous_trial_key", 3, "Guarida del Warden"),
    ("wither", "Wither Arena", "ominous_trial_key", 3, "Arena del Wither"),
]
SK = {s[0]: s for s in SIMPLY}
OURS = [  # (id, nombre, color, item, crate)
    ("builder", "Llave del Arquitecto", "aqua", "trial_key", "Crate del Constructor"),
    ("nature", "Llave Silvestre", "green", "trial_key", "Crate de la Naturaleza"),
    ("miner", "Llave Subterránea", "gray", "trial_key", "Crate del Minero"),
    ("combat", "Llave de Batalla", "red", "trial_key", "Crate de Combate"),
    ("mystic", "Llave Abisal", "dark_purple", "ominous_trial_key", "Crate Místico"),
    ("legend", "Llave del Vacío", "gold", "ominous_trial_key", "Crate Legendario"),
]
OK = {k[0]: k for k in OURS}


def our_snbt(k):
    _, name, color, _, crate = k
    return (f'{{"minecraft:custom_name":{{text:"{name}",color:"{color}",italic:false}},'
            f'"minecraft:lore":[{{text:"Abre: {crate}",color:"gray",italic:false}}]}}')


def our_give(k):
    _, name, color, _, crate = k
    return (f'[custom_name={{text:"{name}",color:"{color}",italic:false}},'
            f'lore=[{{text:"Abre: {crate}",color:"gray",italic:false}}]]')


def our_json(k):
    _, name, color, _, crate = k
    return {"minecraft:custom_name": {"text": name, "color": color, "italic": False},
            "minecraft:lore": [{"text": f"Abre: {crate}", "color": "gray", "italic": False}]}


# Fragmento de Llave: MISMO formato que so_arenas (echo_shard + custom_data so_key_frag).
FRAG_COMP = {"minecraft:custom_name": {"text": "Fragmento de Llave", "color": "light_purple", "italic": False},
             "minecraft:lore": [{"text": "Juntá varios para forjar una llave de crate", "color": "gray", "italic": False}],
             "minecraft:custom_data": "{so_key_frag:1b}"}
FRAG_GIVE = ('echo_shard[custom_name={text:"Fragmento de Llave",color:"light_purple",italic:false},'
             'lore=[{text:"Juntá varios para forjar una llave de crate",color:"gray",italic:false}],'
             'custom_data={so_key_frag:1b}]')

# ================================================================ helpers de botín
def it(name, w_=1, lo=1, hi=1, extra=None):
    e = {"type": "minecraft:item", "name": f"minecraft:{name}", "weight": w_}
    f = []
    if hi > 1 or lo > 1:
        f.append({"function": "minecraft:set_count", "count": {"min": lo, "max": hi} if hi != lo else lo})
    f += extra or []
    if f:
        e["functions"] = f
    return e


def lv(name, w_, lo, hi):  # encantamiento aleatorio por niveles
    return it(name, w_, extra=[{"function": "minecraft:enchant_with_levels", "levels": {"min": lo, "max": hi}}])


def pot(w_, p, kind="potion"):
    return it(kind, w_, extra=[{"function": "minecraft:set_potion", "id": f"minecraft:{p}"}])


def tipped(w_, p, lo, hi):
    return it("tipped_arrow", w_, lo, hi, extra=[{"function": "minecraft:set_potion", "id": f"minecraft:{p}"}])


def ebook(w_, ench, level):
    return it("enchanted_book", w_, extra=[{"function": "minecraft:set_enchantments",
                                             "enchantments": {f"minecraft:{ench}": level}}])


def gear(name, w_, enchs, lore=None, color="gold"):
    f = [{"function": "minecraft:set_enchantments", "enchantments": {f"minecraft:{k}": v for k, v in enchs.items()}}]
    if lore:
        f.append({"function": "minecraft:set_lore", "mode": "replace_all",
                  "lore": [{"text": lore, "color": color, "italic": False}]})
    return it(name, w_, extra=f)


def ilegal(kind, name, color, effs, w_):
    return it(kind, w_, extra=[{"function": "minecraft:set_components", "components": {
        "minecraft:potion_contents": {"custom_color": color, "custom_effects": [
            {"id": f"minecraft:{e}", "amplifier": a, "duration": d, "show_icon": True} for e, a, d in effs]},
        "minecraft:item_name": {"text": name, "color": "light_purple"},
        "minecraft:lore": [{"text": "✦ Poción prohibida ✦", "color": "dark_purple", "italic": False}]}}])


def skey(sid, w_):
    _, nm, item, _, _ = SK[sid]
    return it(item, w_, extra=[{"function": "minecraft:set_components", "components": {"minecraft:custom_name": nm}}])


def okey(kid, w_):
    return it(OK[kid][3], w_, extra=[{"function": "minecraft:set_components", "components": our_json(OK[kid])}])


def frag(w_, lo, hi):
    return it("echo_shard", w_, lo, hi, extra=[{"function": "minecraft:set_components", "components": FRAG_COMP}])


def empty(w_): return {"type": "minecraft:empty", "weight": w_}
def pool(entries, rolls=1): return {"rolls": rolls, "entries": [e for e in entries if e.get("weight", 1) > 0]}
def table(*pools): return {"type": "minecraft:vault", "pools": list(pools)}


# ---------------------------------------------------------------- pociones prohibidas
ELIXIR = lambda w_: ilegal("potion", "Elixir del Minero Veloz", 0xF2D13A, [("haste", 9, 3600)], w_)
TITAN = lambda w_: ilegal("potion", "Tónico de Titán", 0x8B1A1A, [("strength", 9, 1200)], w_)
VITAL = lambda w_: ilegal("potion", "Esencia Vital", 0xFF5FA2, [("regeneration", 9, 300)], w_)
MILAGRO = lambda w_: ilegal("splash_potion", "Poción de Milagro", 0xFF3355, [("instant_health", 4, 1), ("regeneration", 9, 300)], w_)
PESTE = lambda w_: ilegal("splash_potion", "Frasco de Peste Oscura", 0x2E7D32, [("poison", 9, 300)], w_)
JUICIO = lambda w_: ilegal("splash_potion", "Frasco del Juicio", 0x2A0033, [("instant_damage", 9, 1)], w_)

# ---------------------------------------------------------------- equipo de élite
MAXE = {
    "sword": {"sharpness": 5, "sweeping_edge": 3, "fire_aspect": 2, "looting": 3, "unbreaking": 3, "mending": 1},
    "pickaxe": {"efficiency": 5, "fortune": 3, "unbreaking": 3, "mending": 1},
    "axe": {"efficiency": 5, "sharpness": 5, "unbreaking": 3, "mending": 1},
    "shovel": {"efficiency": 5, "unbreaking": 3, "mending": 1},
    "hoe": {"efficiency": 5, "fortune": 3, "unbreaking": 3, "mending": 1},
    "helmet": {"protection": 4, "respiration": 3, "aqua_affinity": 1, "unbreaking": 3, "mending": 1},
    "chestplate": {"protection": 4, "unbreaking": 3, "mending": 1},
    "leggings": {"protection": 4, "swift_sneak": 3, "unbreaking": 3, "mending": 1},
    "boots": {"protection": 4, "feather_falling": 4, "depth_strider": 3, "unbreaking": 3, "mending": 1},
    "bow": {"power": 5, "punch": 2, "flame": 1, "infinity": 1, "unbreaking": 3},
    "crossbow": {"quick_charge": 3, "multishot": 1, "unbreaking": 3, "mending": 1},
    "trident": {"loyalty": 3, "impaling": 5, "channeling": 1, "unbreaking": 3, "mending": 1},
    "mace": {"density": 5, "wind_burst": 3, "unbreaking": 3, "mending": 1},
}
SOLO = {"bow", "crossbow", "trident", "mace"}  # sin versión de netherita/diamante


def near(e):  # "casi al máximo": un nivel menos y sin Reparación
    return {k: max(1, v - 1) for k, v in e.items() if k != "mending"}


def elite(kinds, w_max=12, w_near=20, w_dia=30, w_empty=38):
    """Pool de 1 tirada: netherita al máximo (~12%), netherita casi al máximo (~20%), diamante full (~30%)."""
    n, out = len(kinds), []
    for k in kinds:
        mat = (lambda m: k) if k in SOLO else (lambda m: f"{m}_{k}")
        out.append(gear(mat("netherite"), w_max, MAXE[k], "✦ Forja Suprema ✦", "light_purple"))
        out.append(gear(mat("netherite"), w_near, near(MAXE[k]), "✧ Forja Superior ✧", "aqua"))
        out.append(gear(mat("diamond"), w_dia, MAXE[k], "◆ Forja Maestra ◆", "blue"))
    return pool(out + [empty(w_empty * n)])


# ---------------------------------------------------------------- libros
BOOKS = [("sharpness", 5), ("protection", 4), ("efficiency", 5), ("fortune", 3), ("looting", 3), ("unbreaking", 3),
         ("power", 5), ("feather_falling", 4), ("depth_strider", 3), ("sweeping_edge", 3), ("respiration", 3),
         ("fire_aspect", 2), ("smite", 5), ("bane_of_arthropods", 5), ("blast_protection", 4), ("fire_protection", 4),
         ("projectile_protection", 4), ("thorns", 3), ("swift_sneak", 3), ("soul_speed", 3), ("riptide", 3),
         ("loyalty", 3), ("impaling", 5), ("quick_charge", 3), ("piercing", 4), ("density", 5), ("breach", 4),
         ("wind_burst", 3), ("lure", 3), ("luck_of_the_sea", 3), ("frost_walker", 2), ("punch", 2), ("knockback", 2)]
SINGLE = ["mending", "silk_touch", "infinity", "aqua_affinity", "flame", "channeling", "multishot"]
BOOK_T1 = pool([lv("book", 1, 5, 15)])
BOOK_T2 = pool([ebook(2, e, m - 1) for e, m in BOOKS] + [lv("book", 6, 22, 30)])
BOOK_T3 = pool([ebook(2, e, m) for e, m in BOOKS] + [ebook(2, e, 1) for e in SINGLE if e != "mending"] + [ebook(1, "mending", 1)])

# ---------------------------------------------------------------- pools por tier (12 Simply)
MAIN = {
    1: [it("bread", 5, 16, 32), it("cooked_beef", 5, 12, 24), it("cooked_porkchop", 3, 12, 24), it("baked_potato", 3, 16, 32),
        it("torch", 4, 32, 64), it("arrow", 4, 32, 64), it("iron_ingot", 6, 12, 24), it("gold_ingot", 4, 8, 16),
        it("emerald", 5, 6, 16), it("coal", 4, 16, 32), it("lapis_lazuli", 3, 12, 24), it("redstone", 3, 16, 32),
        it("experience_bottle", 4, 8, 16), it("golden_carrot", 2, 8, 16), it("oak_log", 3, 16, 32), it("water_bucket", 1),
        it("lava_bucket", 1), it("saddle", 1), it("name_tag", 1), it("shield", 2), it("ender_pearl", 1, 1, 3),
        pot(3, "healing"), pot(2, "swiftness"), pot(2, "strength"), pot(2, "regeneration"), pot(2, "fire_resistance"),
        pot(1, "night_vision"), pot(1, "water_breathing"), pot(2, "healing", "splash_potion"),
        lv("iron_sword", 3, 5, 12), lv("iron_pickaxe", 3, 5, 12), lv("iron_axe", 2, 5, 12), lv("iron_shovel", 1, 5, 12),
        lv("iron_helmet", 2, 5, 12), lv("iron_chestplate", 2, 5, 12), lv("iron_leggings", 2, 5, 12), lv("iron_boots", 2, 5, 12),
        lv("bow", 2, 5, 12), lv("crossbow", 1, 5, 12), lv("diamond_sword", 1, 5, 10), lv("diamond_pickaxe", 1, 5, 10),
        lv("diamond_chestplate", 1, 5, 10)],
    2: [it("golden_apple", 4, 4, 8), it("ender_pearl", 4, 6, 12), it("experience_bottle", 5, 16, 32), it("golden_carrot", 4, 16, 32),
        it("iron_ingot", 4, 16, 32), it("gold_ingot", 3, 16, 32), it("obsidian", 3, 8, 16), it("emerald", 4, 12, 24),
        it("lapis_lazuli", 3, 16, 32), it("blaze_rod", 2, 4, 8), it("spectral_arrow", 2, 16, 32), it("arrow", 2, 64),
        it("cooked_beef", 3, 24, 48), it("iron_block", 1, 2, 4), it("slime_ball", 1, 4, 8), it("wind_charge", 2, 8, 16),
        pot(3, "strength"), pot(1, "long_strength"), pot(3, "regeneration"), pot(1, "long_regeneration"),
        pot(2, "fire_resistance"), pot(1, "long_fire_resistance"), pot(2, "strong_healing"),
        pot(2, "strong_healing", "splash_potion"), pot(1, "strong_swiftness"), pot(1, "turtle_master"), pot(1, "slow_falling"),
        lv("diamond_sword", 2, 20, 30), lv("diamond_pickaxe", 2, 20, 30), lv("diamond_axe", 1, 20, 30),
        lv("diamond_shovel", 1, 20, 30), lv("diamond_helmet", 2, 20, 30), lv("diamond_chestplate", 2, 20, 30),
        lv("diamond_leggings", 2, 20, 30), lv("diamond_boots", 2, 20, 30), lv("bow", 2, 20, 30),
        lv("crossbow", 1, 20, 30), lv("trident", 1, 20, 30), it("shield", 1)],
    3: [lv("netherite_sword", 2, 3, 8), lv("netherite_pickaxe", 2, 3, 8), lv("netherite_axe", 2, 3, 8), lv("netherite_shovel", 1, 3, 8),
        lv("netherite_helmet", 2, 3, 8), lv("netherite_chestplate", 2, 3, 8), lv("netherite_leggings", 2, 3, 8),
        lv("netherite_boots", 2, 3, 8), it("netherite_ingot", 2, 1, 3), it("netherite_scrap", 3, 2, 4),
        it("crying_obsidian", 3, 12, 24), it("totem_of_undying", 3), it("golden_apple", 4, 8, 16),
        it("enchanted_golden_apple", 1), pot(3, "strong_healing", "splash_potion"), pot(3, "strong_strength"),
        pot(2, "long_regeneration"), pot(2, "strong_regeneration"), it("heart_of_the_sea", 1),
        it("netherite_upgrade_smithing_template", 2), it("shulker_shell", 2, 2, 4), it("ender_eye", 2, 8, 16),
        it("experience_bottle", 4, 32, 64), it("diamond_block", 1, 1, 3), it("ancient_debris", 2, 2, 4),
        it("end_crystal", 1, 1, 2), it("ender_pearl", 3, 8, 16), it("blaze_rod", 2, 8, 16), it("emerald_block", 2, 4, 8)],
}
GUARANTEED = {1: pool([it("diamond", 1, 2, 4)]), 2: pool([it("diamond", 1, 8, 16)]), 3: pool([it("diamond", 1, 16, 32)])}
BOOKP = {1: BOOK_T1, 2: BOOK_T2, 3: BOOK_T3}
THEME = {
    "cemetery": [it("bone_meal", 4, 16, 32), it("bone_block", 3, 8, 16), it("soul_lantern", 3, 4, 8), it("soul_torch", 3, 16, 32),
                 it("white_candle", 2, 4, 8), it("pumpkin", 2, 4, 8), it("skeleton_skull", 1)],
    "graveyard": [it("jack_o_lantern", 3, 4, 8), it("cobweb", 2, 4, 8), it("white_candle", 2, 8, 16), it("lantern", 3, 8, 16),
                  it("milk_bucket", 2), it("golden_carrot", 3, 8, 16), it("zombie_head", 1)],
    "ossuary": [it("bone", 4, 16, 32), it("bone_block", 3, 16, 32), it("arrow", 3, 32, 64), lv("bow", 2, 8, 15),
                it("skeleton_skull", 1), it("spectral_arrow", 2, 8, 16)],
    "old_tower": [it("bookshelf", 3, 4, 8), it("book", 3, 8, 16), it("lectern", 2), it("spyglass", 2), it("lantern", 3, 8, 16),
                  it("ladder", 3, 16, 32), it("chiseled_bookshelf", 2, 2, 4), it("enchanting_table", 1)],
    "pyramid": [it("sand", 3, 32, 64), it("sandstone", 3, 32, 64), it("tnt", 3, 4, 8), it("gold_ingot", 3, 8, 16),
                it("golden_apple", 2, 1, 2), it("cactus", 2, 8, 16), it("dune_armor_trim_smithing_template", 1)],
    "rusty": [it("rail", 3, 32, 64), it("powered_rail", 3, 8, 16), it("minecart", 2), it("raw_iron", 3, 16, 32),
              it("raw_copper", 3, 16, 32), it("torch", 3, 64), it("tnt", 2, 4, 8)],
    "treasure": [it("gold_block", 3, 2, 4), it("emerald", 4, 16, 32), it("diamond", 3, 3, 6), it("golden_apple", 3, 2, 4),
                 it("heart_of_the_sea", 1), it("nautilus_shell", 2, 2, 4), it("emerald_block", 1, 1, 3)],
    "deep": [it("prismarine_shard", 3, 16, 32), it("prismarine_crystals", 3, 16, 32), it("sea_lantern", 3, 8, 16),
             it("nautilus_shell", 2, 2, 4), it("kelp", 2, 32, 64), pot(2, "long_water_breathing"), it("turtle_helmet", 1),
             it("trident", 1)],
    "elder": [it("sponge", 3, 2, 6), it("prismarine_bricks", 3, 32, 64), it("dark_prismarine", 3, 32, 64),
              it("sea_lantern", 3, 16, 32), it("heart_of_the_sea", 2), it("conduit", 1), it("tide_armor_trim_smithing_template", 1)],
    "to_the_end": [it("ender_pearl", 3, 8, 16), it("ender_eye", 3, 6, 12), it("end_stone_bricks", 2, 32, 64),
                   it("purpur_block", 2, 32, 64), it("shulker_shell", 2, 2, 4), it("end_rod", 2, 8, 16),
                   it("chorus_fruit", 2, 16, 32), it("dragon_breath", 2, 2, 4), it("spire_armor_trim_smithing_template", 1)],
    "warden": [it("sculk", 3, 32, 64), it("echo_shard", 2, 2, 4), it("sculk_catalyst", 2, 1, 2), it("sculk_sensor", 2, 2, 4),
               it("calibrated_sculk_sensor", 1, 1, 2), ebook(1, "swift_sneak", 3), it("music_disc_otherside", 1),
               it("disc_fragment_5", 2, 2, 4), it("silence_armor_trim_smithing_template", 1)],
    "wither": [it("soul_sand", 3, 16, 32), it("wither_skeleton_skull", 2), it("nether_bricks", 2, 32, 64),
               it("blaze_rod", 3, 8, 16), it("magma_cream", 2, 8, 16), it("ghast_tear", 2, 2, 4), it("quartz", 3, 32, 64),
               it("nether_star", 1)],
}
T1K, T2K, T3K = ([s[0] for s in SIMPLY if s[3] == t] for t in (1, 2, 3))
CHAIN = {  # llaves en cadena (más que nada en las 12 Simply)
    1: [skey(k, 2) for k in T1K] + [skey(k, 1) for k in T2K] + [okey("builder", 1), okey("nature", 1), empty(22)],
    2: [skey(k, 2) for k in T2K] + [skey(k, 1) for k in T3K] + [okey(k, 1) for k in ("builder", "nature", "miner", "combat")] + [empty(24)],
    3: [skey(k, 2) for k in T3K] + [okey("miner", 2), okey("combat", 2), okey("mystic", 1), okey("legend", 1), empty(26)],
}
FRAGP = {1: pool([frag(30, 1, 2), empty(70)]), 2: pool([frag(35, 1, 2), empty(65)]), 3: pool([frag(40, 1, 3), empty(60)])}

LOOT = {}
for sid, _, _, t, _ in SIMPLY:
    LOOT[f"oneblock/{sid}"] = table(pool(MAIN[t], rolls=5), GUARANTEED[t], pool(THEME[sid], rolls=2), BOOKP[t],
                                    pool(CHAIN[t]), FRAGP[t])

# ---------------------------------------------------------------- 6 crates especiales (más OP y temáticas)
SFRAG = lambda p, lo, hi: pool([frag(p, lo, hi), empty(100 - p)])
LOOT["builder"] = table(pool([
    it(b, 3, 48, 64) for b in ("cherry_planks", "mangrove_planks", "bamboo_planks", "dark_oak_planks", "spruce_planks",
                               "quartz_block", "smooth_quartz", "quartz_bricks", "polished_blackstone_bricks", "deepslate_tiles",
                               "deepslate_bricks", "calcite", "tuff_bricks", "mud_bricks", "stone_bricks", "glass", "white_concrete",
                               "gray_concrete", "black_concrete", "terracotta", "smooth_stone", "polished_andesite",
                               "prismarine_bricks", "purpur_block", "copper_block", "white_wool", "moss_block")
] + [it("sea_lantern", 4, 32, 64), it("lantern", 4, 32, 64), it("scaffolding", 4, 64), it("end_rod", 2, 16, 32),
     it("white_glazed_terracotta", 2, 32, 64), it("cyan_glazed_terracotta", 2, 32, 64), it("glowstone", 2, 32, 64),
     it("chain", 2, 32, 64), it("oxidized_cut_copper", 2, 32, 64), it("light_blue_stained_glass", 2, 32, 64),
     it("bookshelf", 1, 16, 32), it("item_frame", 1, 16, 32), it("flower_pot", 1, 16, 32)], rolls=6),
    pool([gear("diamond_axe", 3, MAXE["axe"], "◆ Forja Maestra ◆", "blue"), gear("diamond_shovel", 3, MAXE["shovel"], "◆ Forja Maestra ◆", "blue"),
          gear("diamond_pickaxe", 3, {"efficiency": 5, "silk_touch": 1, "unbreaking": 3, "mending": 1}, "◆ Forja Maestra ◆", "blue"),
          gear("netherite_pickaxe", 1, {"efficiency": 5, "silk_touch": 1, "unbreaking": 3, "mending": 1}, "✦ Forja Suprema ✦", "light_purple"),
          it("shulker_box", 1), empty(9)]),
    pool([it("emerald", 1, 8, 16)]),
    pool([okey("builder", 2), okey("nature", 1), okey("miner", 1), empty(10)]), SFRAG(40, 1, 3))

EGGS = ("cow", "sheep", "chicken", "pig", "bee", "horse", "rabbit", "goat", "mooshroom", "fox", "axolotl", "frog",
        "llama", "donkey", "camel", "armadillo", "wolf", "cat", "parrot", "turtle")
LOOT["nature"] = table(
    pool([it(f"{e}_spawn_egg", 2, 2, 4) for e in EGGS] + [it("sniffer_egg", 1, 1, 2), it("turtle_egg", 1, 2, 4)], rolls=3),
    pool([it("bone_meal", 5, 64), it("honey_bottle", 3, 16), it("honeycomb", 3, 16, 32), it("wind_charge", 3, 16, 32),
          it("sugar_cane", 3, 32, 64), it("bamboo", 3, 32, 64), it("cactus", 2, 16, 32), it("nether_wart", 3, 32, 64),
          it("wheat_seeds", 3, 32, 64), it("melon_seeds", 2, 16, 32), it("pumpkin_seeds", 2, 16, 32), it("cocoa_beans", 2, 16, 32),
          it("carrot", 2, 32, 64), it("potato", 2, 32, 64), it("beetroot_seeds", 2, 32, 64), it("sweet_berries", 2, 32, 64),
          it("glow_berries", 2, 32, 64), it("moss_block", 2, 32, 64), it("grass_block", 2, 32, 64), it("dirt", 2, 64),
          it("podzol", 2, 32, 64), it("mycelium", 1, 16, 32), it("mud", 1, 32, 64), it("hay_block", 2, 16, 32),
          it("golden_carrot", 3, 32, 64), it("cherry_sapling", 2, 8, 16), it("mangrove_propagule", 2, 8, 16),
          it("oak_sapling", 2, 8, 16), it("birch_sapling", 2, 8, 16), it("spruce_sapling", 2, 8, 16),
          it("jungle_sapling", 2, 8, 16), it("dark_oak_sapling", 2, 8, 16), it("acacia_sapling", 2, 8, 16),
          it("pale_oak_sapling", 1, 8, 16), it("azalea", 1, 4, 8), it("flowering_azalea", 1, 4, 8),
          it("crimson_fungus", 1, 4, 8), it("warped_fungus", 1, 4, 8), it("water_bucket", 2), it("lead", 2, 4, 8),
          it("name_tag", 2, 2, 4), it("saddle", 1, 1, 2), it("brush", 1), it("composter", 1, 2, 4), it("beehive", 1)], rolls=6),
    pool([gear("netherite_hoe", 1, MAXE["hoe"], "✦ Hoz Silvestre ✦", "green"), gear("diamond_hoe", 3, MAXE["hoe"], "◆ Forja Maestra ◆", "blue"),
          gear("diamond_axe", 2, MAXE["axe"], "◆ Forja Maestra ◆", "blue"), VITAL(2), it("golden_apple", 2, 4, 8), empty(8)]),
    pool([okey("nature", 2), okey("builder", 1), okey("miner", 1), empty(10)]), SFRAG(40, 1, 3))

LOOT["miner"] = table(
    pool([it("iron_block", 4, 8, 16), it("gold_block", 3, 8, 12), it("diamond_block", 2, 2, 6), it("emerald_block", 2, 4, 8),
          it("redstone_block", 3, 16, 32), it("lapis_block", 3, 16, 32), it("coal_block", 3, 16, 32), it("copper_block", 3, 16, 32),
          it("raw_iron_block", 3, 8, 16), it("raw_gold_block", 2, 4, 8), it("raw_copper_block", 2, 8, 16), it("tnt", 3, 32),
          it("ancient_debris", 2, 2, 6), it("amethyst_block", 2, 16, 32), it("torch", 3, 64), it("rail", 2, 64),
          it("powered_rail", 2, 16, 32), it("obsidian", 2, 16, 32), it("diamond", 3, 8, 16), it("netherite_scrap", 1, 2, 4),
          it("quartz_block", 2, 16, 32), it("glowstone", 2, 16, 32), it("lantern", 2, 16, 32), it("water_bucket", 1)], rolls=6),
    elite(["pickaxe", "shovel", "axe", "pickaxe"]),
    pool([ELIXIR(4), pot(2, "long_night_vision"), it("golden_apple", 2, 4, 8), empty(6)]),
    pool([okey("miner", 2), okey("combat", 1), okey("mystic", 1), empty(12)]), SFRAG(45, 1, 3))

LOOT["combat"] = table(
    pool([it("arrow", 4, 64), it("spectral_arrow", 3, 32, 64), tipped(3, "strong_harming", 16, 32), tipped(2, "strong_poison", 16, 32),
          tipped(2, "slowness", 16, 32), it("golden_apple", 4, 8, 16), it("enchanted_golden_apple", 1, 1, 2), it("totem_of_undying", 2),
          it("ender_pearl", 3, 16), it("firework_rocket", 3, 32, 64), it("wind_charge", 2, 16, 32), it("shield", 2),
          it("cooked_beef", 3, 32, 64), it("golden_carrot", 3, 32, 64), it("experience_bottle", 3, 32, 64),
          pot(3, "strong_healing", "splash_potion"), pot(3, "strong_strength"), pot(2, "long_strength"),
          pot(2, "strong_regeneration"), pot(2, "long_fire_resistance"), pot(2, "strong_swiftness"),
          pot(1, "strong_turtle_master"), pot(2, "strong_harming", "splash_potion"), it("obsidian", 1, 16, 32),
          it("end_crystal", 1, 2, 4), it("respawn_anchor", 1), it("glowstone", 1, 16, 32)], rolls=6),
    elite(["sword", "bow", "crossbow", "helmet", "chestplate", "leggings", "boots", "axe"]),
    pool([TITAN(3), MILAGRO(3), PESTE(2), JUICIO(2), VITAL(2), empty(8)]),
    pool([okey("combat", 2), okey("miner", 1), okey("mystic", 1), empty(12)]), SFRAG(45, 1, 3))

TRIMS = ("silence", "eye", "ward", "vex", "rib", "spire", "snout", "tide", "host", "raiser", "shaper", "wayfinder", "flow",
         "bolt", "sentry", "dune", "coast", "wild")
LOOT["mystic"] = table(
    pool([it("netherite_upgrade_smithing_template", 4, 1, 2)] + [it(f"{t}_armor_trim_smithing_template", 1) for t in TRIMS] +
         [it("heart_of_the_sea", 2, 1, 2), it("nautilus_shell", 2, 4, 8), it("blaze_rod", 3, 16), it("ghast_tear", 3, 4, 8),
          it("ender_pearl", 3, 16), it("ender_eye", 3, 8, 16), it("shulker_shell", 2, 2, 4), it("dragon_breath", 2, 4, 8),
          it("experience_bottle", 4, 32, 64), it("lapis_block", 2, 8, 16), it("crying_obsidian", 2, 16, 32),
          it("amethyst_block", 2, 16, 32), it("end_crystal", 1, 1, 2), it("nether_wart", 2, 32, 64), it("magma_cream", 2, 8, 16),
          it("echo_shard", 1, 2, 4), it("totem_of_undying", 1), it("enchanted_golden_apple", 1)], rolls=6),
    pool([ebook(1, "mending", 1)]),
    BOOK_T3,
    elite(["helmet", "chestplate", "leggings", "boots", "trident", "sword", "pickaxe"]),
    pool([ELIXIR(2), TITAN(2), MILAGRO(2), PESTE(1), JUICIO(1), VITAL(2), empty(8)]),
    pool([okey("mystic", 2), okey("legend", 1), empty(12)]), SFRAG(50, 1, 3))

LOOT["legend"] = table(
    pool([it("heavy_core", 2), it("netherite_ingot", 4, 2, 4), it("beacon", 2), it("totem_of_undying", 4),
          it("enchanted_golden_apple", 4, 2, 3), it("shulker_shell", 3, 4), it("nether_star", 2, 1, 2),
          it("netherite_upgrade_smithing_template", 3, 2), it("diamond_block", 4, 4, 8), it("emerald_block", 3, 8, 16),
          it("netherite_block", 1), it("dragon_breath", 2, 8, 16), it("end_crystal", 2, 2, 4), it("conduit", 1),
          it("experience_bottle", 3, 64), it("trident", 1), it("heart_of_the_sea", 2, 1, 2), it("golden_apple", 3, 16, 32),
          it("silence_armor_trim_smithing_template", 1), it("music_disc_pigstep", 1), it("music_disc_otherside", 1)], rolls=5),
    elite(["sword", "pickaxe", "axe", "helmet", "chestplate", "leggings", "boots", "bow", "crossbow", "trident", "mace"],
          w_max=16, w_near=24, w_dia=30, w_empty=30),
    elite(["sword", "pickaxe", "helmet", "chestplate", "leggings", "boots"], w_max=10, w_near=18, w_dia=30, w_empty=42),
    BOOK_T3,
    pool([ELIXIR(2), TITAN(2), MILAGRO(2), PESTE(1), JUICIO(1), VITAL(2), empty(6)]),
    # Única fuente de Élitra de TODO el sistema: casi rota (20% de durabilidad), sin encantar, ~7%.
    pool([it("elytra", 7, extra=[{"function": "minecraft:set_damage", "damage": 0.2}]), empty(93)]),
    pool([okey("legend", 1), okey("mystic", 2), empty(14)]), SFRAG(50, 2, 4))

for name, t in LOOT.items():
    js(f"data/so_crates/loot_table/{name}.json", t)
assert "elytra" not in json.dumps({k: v for k, v in LOOT.items() if k != "legend"}), "Élitra fuera del Crate Legendario"

# ================================================================ construcción
def text_display(x, y, z, parts, scale=1.0):
    t = ",".join(parts)
    return (f'summon minecraft:text_display {x} {y} {z} {{Tags:["so_cr_txt"],billboard:"center",shadow:1b,'
            f'background:1073741824,text:[{t}],transformation:{{left_rotation:[0f,0f,0f,1f],'
            f'right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[{scale}f,{scale}f,{scale}f]}}}}')


def tc(text, color, bold=False):
    b = ",bold:true" if bold else ""
    return f'{{text:"{text}",color:"{color}"{b}}}'


NL = '"\\n"'
STARS = {1: "★☆☆", 2: "★★☆", 3: "★★★"}
TIERCOL = {1: "green", 2: "yellow", 3: "red"}

s1 = [  # estructura
    "# so_crates v2 · paso 1: estructura del templo",
    f"fill {OLD[0]} {OLD[1]} {OLD[2]} {OLD[3]} {OLD[4]} {OLD[5]} minecraft:air",
    f"fill {X0} {FY-1} {Z0} {X1} {FY-1} {Z1} minecraft:polished_deepslate",
    f"fill {X0+1} {FY} {Z0+1} {X1-1} {FY} {Z1-1} minecraft:polished_blackstone_bricks",
]
for a, b in ((FY + 1, 109), (110, TOP)):
    s1.append(f"fill {X0+1} {a} {Z0+1} {X1-1} {b} {Z1-1} minecraft:air")
for (xa, za, xb, zb) in ((X0, Z0, X1, Z0), (X0, Z1, X1, Z1), (X0, Z0, X0, Z1), (X1, Z0, X1, Z1)):
    s1 += [f"fill {xa} {FY} {za} {xb} {TOP} {zb} minecraft:deepslate_bricks",
           f"fill {xa} {FY} {za} {xb} {FY+1} {zb} minecraft:polished_blackstone",
           f"fill {xa} {TOP-1} {za} {xb} {TOP-1} {zb} minecraft:chiseled_deepslate"]
# ventanales y columnas en los muros largos
for x in range(X0 + 3, X1 - 2, 6):
    for z in (Z0, Z1):
        s1.append(f"fill {x} {FY+4} {z} {x+1} {FY+13} {z} minecraft:purple_stained_glass")
    for z in (Z0 + 1, Z1 - 1):
        s1.append(f"fill {x-1} {FY+1} {z} {x-1} {TOP-2} {z} minecraft:polished_blackstone_bricks")
        s1.append(f"setblock {x-1} {TOP-2} {z} minecraft:gilded_blackstone")
for z in range(Z0 + 4, Z1 - 3, 6):
    for x in (X0, X1):
        s1.append(f"fill {x} {FY+4} {z} {x} {FY+13} {z+1} minecraft:purple_stained_glass")
# techo + capa de losas (evita spawns hostiles) + tragaluz central de vidrio
s1 += [f"fill {X0} {TOP+1} {Z0} {X1} {TOP+1} {Z1} minecraft:deepslate_tiles",
       f"fill {X0} {TOP+2} {Z0} {X1} {TOP+2} {Z1} minecraft:deepslate_tile_slab[type=bottom]",
       f"fill 4994 {TOP+1} 4992 5006 {TOP+1} 5008 minecraft:glass",
       f"fill 4994 {TOP+2} 4992 5006 {TOP+2} 5008 minecraft:air"]
# arcadas que separan alas y atrio
for ax in (4990, 5010):
    s1.append(f"fill {ax} {TOP-3} {Z0+1} {ax} {TOP-3} {Z1-1} minecraft:polished_blackstone_bricks")
    for z in range(Z0 + 3, Z1 - 1, 5):
        s1 += [f"fill {ax} {FY+1} {z} {ax} {TOP-4} {z} minecraft:polished_blackstone_bricks",
               f"setblock {ax} {FY+1} {z} minecraft:chiseled_polished_blackstone",
               f"setblock {ax} {TOP-4} {z} minecraft:gilded_blackstone",
               f"setblock {ax} {TOP-4} {z+2} minecraft:lantern[hanging=true]"]
# suelo: pasillo central, luz empotrada (sin oscuridad = sin mobs)
s1 += [f"fill 4999 {FY} {Z0+1} 5001 {FY} {Z1-1} minecraft:polished_deepslate",
       f"fill 5000 {FY} {Z0+1} 5000 {FY} {Z1-1} minecraft:chiseled_polished_blackstone"]
for x in range(X0 + 3, X1 - 1, 5):
    for z in range(Z0 + 3, Z1 - 1, 5):
        s1.append(f"setblock {x} {FY} {z} minecraft:sea_lantern")
# lámparas colgantes (cadenas) en las tres naves
for x in (4980, 5000, 5020):
    for z in (4988, 5000, 5012):
        s1 += [f"fill {x} {TOP-3} {z} {x} {TOP} {z} minecraft:chain",
               f"setblock {x} {TOP-4} {z} minecraft:lantern[hanging=true]"]
s1.append("schedule function so_crates:build/s2 10t")
fn("build/s1", s1)

# ---------------------------------------------------------------- paso 2: alas y bóvedas
VAULTS = []  # (x,y,z,facing,key_snbt,loot,ominous)
s2 = ["# so_crates v2 · paso 2: pabellones y altares"]
TIERMAT = {1: ("mossy_stone_bricks", "oxidized_cut_copper", "chiseled_stone_bricks", "lantern"),
           2: ("smooth_sandstone", "cut_sandstone", "chiseled_sandstone", "lantern"),
           3: ("polished_blackstone", "crying_obsidian", "gilded_blackstone", "soul_lantern")}
TROW = {1: 4985, 2: 5000, 3: 5015}
TNAME = {1: "Pabellón I · Llaves Iniciales", 2: "Pabellón II · Llaves del Explorador", 3: "Pabellón III · Llaves Ancestrales"}
labels = []
for t, row in TROW.items():
    floor, back, chis, lamp = TIERMAT[t]
    s2 += [f"fill 4971 {FY} {row-2} 4989 {FY} {row+3} minecraft:{floor}",
           f"fill 4972 {FY+1} {row-1} 4988 {FY+4} {row-1} minecraft:{back}",
           f"fill 4972 {FY+5} {row-1} 4988 {FY+5} {row-1} minecraft:{chis}"]
    labels.append(text_display(4980.5, FY + 8, row - 0.4, [tc(f"◆ {TNAME[t]} ◆", TIERCOL[t], True)], 1.4))
    for i, sid in enumerate([s[0] for s in SIMPLY if s[3] == t]):
        _, nm, item, _, crate = SK[sid]
        x = 4974 + 4 * i
        s2 += [f"setblock {x} {FY} {row} minecraft:{chis}",
               f"fill {x-1} {FY+1} {row-1} {x+1} {FY+3} {row-1} minecraft:{chis}",
               f"setblock {x} {FY+6} {row-1} minecraft:{lamp}"]
        comp = f'{{"minecraft:custom_name":"{nm}"}}'
        VAULTS.append((x, FY + 1, row, "south", f'{{id:"minecraft:{item}",count:1,components:{comp}}}',
                       f"oneblock/{sid}", item.startswith("ominous")))
        labels.append(text_display(x + 0.5, FY + 3.3, row + 0.5,
                                   [tc(crate, "gold", True), NL, tc(nm, "gray"), NL, tc(STARS[t], TIERCOL[t])], 0.8))

ALT = {  # tema: (base, pilar, remate)
    "builder": ("smooth_quartz", "quartz_pillar", "sea_lantern"),
    "nature": ("moss_block", "oak_log", "flowering_azalea_leaves"),
    "miner": ("polished_deepslate", "deepslate_diamond_ore", "lantern"),
    "combat": ("red_nether_bricks", "nether_bricks", "shroomlight"),
    "mystic": ("purpur_block", "purpur_pillar", "amethyst_block"),
    "legend": ("gilded_blackstone", "crying_obsidian", "gold_block"),
}
APOS = {"builder": (5016, 4987), "nature": (5025, 4987), "miner": (5016, 5000),
        "combat": (5025, 5000), "mystic": (5016, 5013), "legend": (5025, 5013)}
MINER_ORES = ["deepslate_iron_ore", "deepslate_gold_ore", "deepslate_diamond_ore", "deepslate_emerald_ore"]
for k in OURS:
    kid, name, color, item, crate = k
    ax, az = APOS[kid]
    base, pil, top = ALT[kid]
    s2 += [f"fill {ax-2} {FY+1} {az-2} {ax+2} {FY+1} {az+2} minecraft:{base}",
           f"setblock {ax-3} {FY+1} {az} minecraft:polished_blackstone_brick_stairs[facing=east]"]
    for n, (dx, dz) in enumerate(((-2, -2), (2, -2), (-2, 2), (2, 2))):
        p = MINER_ORES[n] if kid == "miner" else pil
        s2 += [f"fill {ax+dx} {FY+2} {az+dz} {ax+dx} {FY+4} {az+dz} minecraft:{p}",
               f"setblock {ax+dx} {FY+5} {az+dz} minecraft:{top}"]
        if kid in ("mystic", "legend"):
            s2.append(f"setblock {ax+dx} {FY+6} {az+dz} minecraft:end_rod")
    VAULTS.append((ax, FY + 2, az, "west", f'{{id:"minecraft:{item}",count:1,components:{our_snbt(k)}}}',
                   kid, item.startswith("ominous")))
    labels.append(text_display(ax + 0.5, FY + 4.4, az + 0.5,
                               [tc(crate, color, True), NL, tc(name, "gray"), NL, tc("✦ ESPECIAL ✦", "light_purple")], 0.9))

reset = []
for x, y, z, face, keysnbt, loot, omin in VAULTS:
    o = "true" if omin else "false"
    s2.append(f'setblock {x} {y} {z} minecraft:vault[facing={face},ominous={o}]'
              f'{{config:{{key_item:{keysnbt},loot_table:"so_crates:{loot}"}}}} replace')
    reset.append(f"data modify block {x} {y} {z} server_data.rewarded_players set value []")
s2.append("schedule function so_crates:build/s3 10t")
fn("build/s2", s2)

# ---------------------------------------------------------------- paso 3: atrio, forja, portal y entidades
FORGE = [(4, T1K, "skey"), (6, T2K + ["builder", "nature"], None), (9, T3K + ["miner", "combat", "mystic"], None), (12, ["legend"], None)]


def sell_snbt(kid):
    if kid in SK:
        _, nm, item, _, _ = SK[kid]
        return f'{{id:"minecraft:{item}",count:1,components:{{"minecraft:custom_name":"{nm}"}}}}'
    return f'{{id:"minecraft:{OK[kid][3]}",count:1,components:{our_snbt(OK[kid])}}}'


recipes = []
for cost, kids, _ in FORGE:
    for kid in kids:
        recipes.append(f'{{buy:{{id:"minecraft:echo_shard",count:{cost},components:{{"minecraft:custom_data":{{so_key_frag:1b}}}}}},'
                       f'sell:{sell_snbt(kid)},maxUses:999999,uses:0,xp:0,rewardExp:0b,priceMultiplier:0f,demand:0,specialPrice:0}}')
FZ = 4986
s3 = ["# so_crates v2 · paso 3: atrio, forja y regreso",
      "kill @e[type=minecraft:text_display,tag=so_cr_txt]",
      "kill @e[type=minecraft:villager,tag=so_cr_npc]",
      # forja (norte del atrio)
      f"fill 4993 {FY} {Z0+1} 5007 {FY} {FZ+3} minecraft:polished_deepslate",
      f"fill 4993 {FY+1} {Z0+1} 5007 {FY+5} {Z0+1} minecraft:polished_blackstone_bricks",
      f"fill 4996 {FY+2} {Z0+1} 5004 {FY+4} {Z0+1} minecraft:gilded_blackstone",
      f"fill 4998 {FY+2} {Z0+1} 5002 {FY+3} {Z0+1} minecraft:magma_block",
      f"setblock 4997 {FY+1} {FZ} minecraft:anvil[facing=east]",
      f"setblock 5003 {FY+1} {FZ} minecraft:smithing_table",
      f"setblock 4996 {FY+1} {FZ-2} minecraft:blast_furnace[facing=south,lit=true]",
      f"setblock 5004 {FY+1} {FZ-2} minecraft:lava_cauldron",
      f"setblock 4995 {FY+1} {FZ} minecraft:grindstone[face=floor,facing=east]",
      f"setblock 5005 {FY+1} {FZ} minecraft:chain",
      f"setblock 5005 {FY+2} {FZ} minecraft:lantern",
      f"setblock 4995 {FY+2} {FZ} minecraft:lantern",
      # corazón del atrio
      f"fill 4997 {FY} 4997 5003 {FY} 5003 minecraft:chiseled_polished_blackstone",
      f"fill 4998 {FY} 4998 5002 {FY} 5002 minecraft:gilded_blackstone",
      f"fill 5000 {FY+1} 5000 5000 {FY+3} 5000 minecraft:crying_obsidian",
      f"setblock 5000 {FY+4} 5000 minecraft:amethyst_cluster",
      f"setblock 4998 {FY+1} 4998 minecraft:end_rod", f"setblock 5002 {FY+1} 4998 minecraft:end_rod",
      f"setblock 4998 {FY+1} 5002 minecraft:end_rod", f"setblock 5002 {FY+1} 5002 minecraft:end_rod",
      # portal de regreso (sur)
      f"fill 4998 {FY+1} {PORTAL_Z+1} 5002 {FY+5} {PORTAL_Z+1} minecraft:crying_obsidian",
      f"fill 4999 {FY+1} {PORTAL_Z+1} 5001 {FY+4} {PORTAL_Z+1} minecraft:purple_stained_glass",
      f"fill 4999 {FY} {PORTAL_Z} 5001 {FY} {PORTAL_Z} minecraft:crying_obsidian",
      f"fill 4999 {FY+1} {PORTAL_Z} 5001 {FY+1} {PORTAL_Z} minecraft:light_weighted_pressure_plate",
      (f'summon minecraft:villager 5000.5 {FY+1} {FZ+0.5} {{Tags:["so_cr_npc"],NoAI:1b,Invulnerable:1b,'
       f'PersistenceRequired:1b,Silent:1b,Rotation:[0f,0f],CustomNameVisible:1b,'
       f'CustomName:{{text:"⚒ Herrero de Bóvedas",color:"gold",bold:true}},'
       f'VillagerData:{{profession:"minecraft:toolsmith",level:5,type:"minecraft:plains"}},'
       f'Offers:{{Recipes:[{",".join(recipes)}]}}}}'),
      text_display(5000.5, FY + 7.5, Z0 + 1.6, [tc("⚒ FORJA DE LLAVES ⚒", "gold", True), NL,
                                                tc("Cambiá Fragmentos de Llave por la llave que necesites", "gray"), NL,
                                                tc("4 → Pabellón I · 6 → Pabellón II + Arquitecto/Silvestre", "green"), NL,
                                                tc("9 → Pabellón III + Subterránea/Batalla/Abisal · 12 → Vacío", "yellow")], 1.0),
      text_display(5000.5, FY + 12, 5000.5, [tc("✦ TEMPLO DE LAS BÓVEDAS ✦", "light_purple", True)], 3.0),
      text_display(4990.5, FY + 9, 5000.5, [tc("◀ Ala Oeste", "gold", True), NL, tc("Bóvedas Simply OneBlock", "gray")], 1.3),
      text_display(5010.5, FY + 9, 5000.5, [tc("Ala Este ▶", "gold", True), NL, tc("Bóvedas Especiales", "gray")], 1.3),
      text_display(5000.5, FY + 6.3, PORTAL_Z + 0.5, [tc("« Volver a la isla", "green", True), NL,
                                                      tc("pisá la placa o usá /trigger isla", "gray")], 1.1),
      ] + labels + [
      "forceload remove 4960 4970 5040 5030",
      f'tellraw @a[tag=oneblock_admin] [{{"text":"[SO Crates] ","color":"gold"}},{{"text":"Templo construido: {len(VAULTS)} bóvedas + Forja.","color":"green"}}]',
]
fn("build/s3", s3)
fn("admin/build", [
    "# Construye el Templo de las Bóvedas (no hace falta estar cerca: forzamos la carga de chunks).",
    "execute in minecraft:overworld run forceload add 4960 4970 5040 5030",
    'tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Construyendo el templo en 3 pasos (~2 s)...","color":"yellow"}]',
    "schedule function so_crates:build/s1 20t",
])
fn("lib/reset_vaults", ["# Vacía la lista de premiados: canje ilimitado mientras tengas llaves"] + reset)

# ================================================================ lógica
ZONE = f"x={X0-1},y={FY-5},z={Z0-1},dx={X1-X0+2},dy=30,dz={Z1-Z0+2}"
w("data/minecraft/tags/function/load.json", json.dumps({"values": ["so_crates:load"]}))
w("data/minecraft/tags/function/tick.json", json.dumps({"values": ["so_crates:tick"]}))
js("pack.mcmeta", {"pack": {"description": f"Simply OneBlock Expansion - Crates v{VERSION} (/trigger crates)",
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
    f'tellraw @a[tag=oneblock_admin] [{{"text":"[SO Crates v{VERSION}] ","color":"gold"}},{{"text":"cargado. Ayuda: /function so_crates:admin/help","color":"gray"}}]',
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
    f"execute in minecraft:overworld as @a[tag=so_cr_in,x=4999,y={FY+1},z={PORTAL_Z},dx=2,dy=1,dz=0] at @s run function so_crates:lib/back",
    "scoreboard players add #r so_crates 1",
    "execute if score #r so_crates matches 2.. if entity @a[tag=so_cr_now] in minecraft:overworld run function so_crates:lib/reset_vaults",
    "execute if score #r so_crates matches 2.. run scoreboard players set #r so_crates 0",
    "tag @a remove so_cr_now",
])
fn("lib/enter", [
    "tag @s add so_cr_in",
    "execute unless entity @s[tag=oneblock_admin] if entity @s[gamemode=survival] run tag @s add so_cr_gm",
    "execute unless entity @s[tag=oneblock_admin] run gamemode adventure @s",
    'title @s actionbar {"text":"✦ Templo de las Bóvedas ✦","color":"light_purple"}',
    'execute if entity @s[tag=oneblock_admin,gamemode=!adventure] run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"⚠ Estás en el templo. ","color":"yellow"},{"text":"[Pasar a Aventura]","color":"green","underlined":true,"click_event":{"action":"run_command","command":"/gamemode adventure"},"hover_event":{"action":"show_text","value":"Clic para cambiar a modo aventura"}}]',
])
fn("lib/leave", [
    "tag @s remove so_cr_in",
    "execute if entity @s[tag=so_cr_gm,gamemode=adventure] run gamemode survival @s",
    "tag @s remove so_cr_gm",
])
fn("lib/go", [
    'execute unless dimension minecraft:overworld run return run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Solo podés viajar desde el mundo normal (no desde el Nether, el End ni las dimensiones de fase).","color":"red"}]',
    'execute if entity @s[tag=so_cr_in] run return run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Ya estás en el templo. Para volver: /trigger isla","color":"yellow"}]',
    "execute store result score @s so_cr_x run data get entity @s Pos[0]",
    "execute store result score @s so_cr_y run data get entity @s Pos[1]",
    "execute store result score @s so_cr_z run data get entity @s Pos[2]",
    "scoreboard players set @s so_cr_saved 1",
    f"tp @s {ARRIVE[0]} {ARRIVE[1]} {ARRIVE[2]} 180 0",
    "playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1",
    'tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Bienvenido al Templo de las Bóvedas. Oeste: llaves Simply · Este: especiales · Norte: Forja de Llaves. Volver: ","color":"green"},{"text":"/trigger isla","color":"yellow","click_event":{"action":"run_command","command":"/trigger isla"}}]',
])
fn("lib/back", [
    'execute unless entity @s[tag=so_cr_in] run return run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Este comando solo funciona dentro del templo de Crates.","color":"red"}]',
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

# ================================================================ admin
for sid, nm, item, _, _ in SIMPLY:
    fn(f"give/{sid}", [f'give @s minecraft:{item}[custom_name="{nm}"] 1'])
for k in OURS:
    fn(f"give/{k[0]}", [f"give @s minecraft:{k[3]}{our_give(k)} 1"])
fn("give/fragments", [f"give @s minecraft:{FRAG_GIVE} 16"])
fn("admin/give_all_keys", [f"function so_crates:give/{s[0]}" for s in SIMPLY] + [f"function so_crates:give/{k[0]}" for k in OURS])
fn("admin/test", ["function so_crates:admin/give_all_keys", "function so_crates:give/fragments", "function so_crates:give/fragments",
                  "execute in minecraft:overworld run tp @s 5000.5 101 4990.5 180 0",
                  'tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Kit de prueba: 18 llaves + 32 fragmentos. Probá la Forja (adelante) y las bóvedas.","color":"green"}]'])
fn("admin/goto", [f"execute in minecraft:overworld run tp @s {ARRIVE[0]} {ARRIVE[1]} {ARRIVE[2]} 180 0"])
fn("admin/enable", ["scoreboard players set #enabled so_crates 1", 'tellraw @s {"text":"[SO Crates] activado","color":"green"}'])
fn("admin/disable", ["scoreboard players set #enabled so_crates 0", 'tellraw @s {"text":"[SO Crates] desactivado (/trigger crates no hace nada)","color":"red"}'])
fn("admin/status", [
    f'tellraw @s [{{"text":"[SO Crates v{VERSION}] ","color":"gold"}},{{"text":"activo: ","color":"gray"}},{{"score":{{"name":"#enabled","objective":"so_crates"}},"color":"white"}}]',
    f'tellraw @s [{{"text":"Templo: {CX} {FY} {CZ} (overworld) · bóvedas: {len(VAULTS)} · forja: {len(recipes)} tratos","color":"gray"}}]',
    'tellraw @s [{"text":"Jugadores en el templo: ","color":"gray"},{"selector":"@a[tag=so_cr_in]"}]',
])
fn("admin/help", [
    f'tellraw @s {{"text":"══ SO Crates v{VERSION} · admin ══","color":"gold","bold":true}}',
    'tellraw @s {"text":"/function so_crates:admin/build → construye el templo (borra la plataforma vieja de Y=200)","color":"gray"}',
    'tellraw @s {"text":"/function so_crates:admin/goto · admin/test (18 llaves + 32 fragmentos)","color":"gray"}',
    'tellraw @s {"text":"/function so_crates:admin/give_all_keys · give/<llave> · give/fragments","color":"gray"}',
    'tellraw @s {"text":"/function so_crates:admin/status · enable · disable · uninstall","color":"gray"}',
    'tellraw @s {"text":"Jugadores: /trigger crates (ir) · /trigger isla o placa del portal (volver)","color":"gray"}',
])
fn("uninstall", [
    "execute as @a[tag=so_cr_in] run function so_crates:lib/leave",
    *[f"scoreboard objectives remove {o}" for o in ["so_crates", "crates", "isla", "so_cr_x", "so_cr_y", "so_cr_z", "so_cr_saved"]],
    "data remove storage so_crates:tmp x",
    'tellraw @s {"text":"[SO Crates] desinstalado. Quitá la carpeta del datapack y /reload. El templo queda construido.","color":"yellow"}',
])

# ================================================================ readme
w("README.md", f"""# SO Crates (so_crates) v{VERSION} · Templo de las Bóvedas

## Instalación (admin)
1. Reemplazá la carpeta `so-crates` en `world/datapacks/` y `/reload`.
2. `/function so_crates:admin/build` (construye el templo en {CX} {FY} {CZ}; borra la plataforma vieja de Y=200).
3. `/function so_crates:admin/test` → 18 llaves + 32 Fragmentos de Llave para probar todo.

## Recorrido
- Llegada (`/trigger crates`) al centro del templo. Volver: `/trigger isla` o pisar la placa del portal sur.
- **Ala Oeste:** 12 bóvedas de las llaves Simply OneBlock en 3 pabellones (★ iniciales, ★★ explorador, ★★★ ancestrales).
- **Ala Este:** 6 altares temáticos de las llaves especiales (Constructor, Naturaleza, Minero, Combate, Místico, Legendario).
- **Norte:** Forja de Llaves con el Herrero de Bóvedas (comercio de aldeano, igual en Java y Bedrock):
  4 fragmentos → llave Pabellón I · 6 → Pabellón II, Arquitecto, Silvestre · 9 → Pabellón III, Subterránea, Batalla, Abisal · 12 → Llave del Vacío.
- Carteles reemplazados por textos 3D flotantes. Canje ilimitado mientras tengas llaves.

## Botín
- Pabellón I: comida, hierro/oro, 2–4 diamantes garantizados, equipo de hierro/diamante con encantamientos I–II, libros I–III.
- Pabellón II: 8–16 diamantes garantizados, manzanas doradas, perlas, equipo de diamante III–IV, libros a un nivel del máximo.
- Pabellón III: 16–32 diamantes garantizados, netherita con encantamientos I–II, tótems, libros al máximo.
- Cada bóveda Simply tiene un pool temático propio y puede soltar otras llaves (cadena) y Fragmentos de Llave (30–40%).
- Especiales: cantidades grandes temáticas, equipo de élite (netherita al máximo ~12%, casi al máximo ~20%, diamante full ~30%)
  y pociones prohibidas (Haste X, Fuerza X, Regeneración X, Milagro: Curación V, Peste: Veneno X, Juicio: Daño X).
- **Élitra:** solo en el Crate Legendario, ~7%, sin encantar y con 20% de durabilidad. Ninguna otra tabla la tiene.
""")
print(f"OK so_crates v{VERSION}: {len(VAULTS)} bóvedas, {len(LOOT)} tablas, {len(recipes)} tratos de forja")
