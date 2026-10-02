#!/usr/bin/env python3
"""Generador de so_quests v2 (misiones individuales, logros, metas de la isla y diarias).
Edita las listas de abajo (nombres, objetivos, recompensas) y vuelve a ejecutar:
    python3 tools/build_so_quests.py
Salida: datapacks/so-quests/
"""
import json, os, shutil

OUT = os.path.join(os.path.dirname(__file__), "..", "datapacks", "so-quests")
NS = "so_quests"

def E(n): return [("emerald", n)]

# ---------- condiciones ----------
# ("blocks", n)                     -> bloques minados del OneBlock (compartido)
# ("stat", criterio, objetivo, div) -> estadistica vanilla del jugador (div: 100 para cm->bloques)
# ("adv", id)                       -> advancement concedido
# ("score", objetivo, n)            -> marcador externo (puente con so_shop)
# ("deliver", item, n)              -> entrega con confirmacion (se quita al reclamar)

CATS = {
    1: ("Fases y progreso", "gold"),
    2: ("Recolección y fabricación", "green"),
    3: ("Combate y exploración", "red"),
    4: ("Logros de Minecraft", "aqua"),
    5: ("Metas de la Isla", "light_purple"),
    6: ("Diarias", "yellow"),
}

def M(c, s): return ("stat", f"minecraft.mined:minecraft.{s}", c, 1)
def C(c, s): return ("stat", f"minecraft.crafted:minecraft.{s}", c, 1)
def P(c, s): return ("stat", f"minecraft.used:minecraft.{s}", c, 1)
def K(c, s): return ("stat", f"minecraft.killed:minecraft.{s}", c, 1)
def U(c, s, d=1): return ("stat", f"minecraft.custom:minecraft.{s}", c * d, d)

# (id, categoria, nombre, icono, condicion, recompensas)
QUESTS = [
    # --- Fases y progreso ---
    (101, 1, "Primeros pasos", "grass_block", ("blocks", 100), E(4)),
    (102, 1, "Bajo tierra", "stone", ("blocks", 500), E(8)),
    (103, 1, "Mil golpes", "iron_pickaxe", ("blocks", 1000), E(12)),
    (104, 1, "Isla en marcha", "oak_sapling", ("blocks", 2500), E(16) + [("experience_bottle", 8)]),
    (105, 1, "Cinco mil", "diamond_pickaxe", ("blocks", 5000), E(24)),
    (106, 1, "Veterano del bloque", "obsidian", ("blocks", 7500), E(32)),
    (107, 1, "Diez mil", "netherite_scrap", ("blocks", 10000), E(40)),
    (108, 1, "Leyenda de la isla", "end_stone", ("blocks", 12500), E(48)),
    (109, 1, "Maestría OneBlock", "nether_star", ("blocks", 15000), E(64) + [("totem_of_undying", 1)]),
    (110, 1, "Primera visita a la tienda", "lantern", ("score", "so_shop_seen", 1), E(2)),
    (111, 1, "Cliente fiel", "emerald", ("score", "so_shop_buys", 10), E(10)),
    (112, 1, "Primer trueque", "emerald_block", ("adv", f"{NS}:trade/any"), E(4)),
    (113, 1, "Trato en la llanura", "wheat", ("adv", f"{NS}:trade/mercader_de_la_llanura"), E(6)),
    (114, 1, "El buzo del abismo", "sponge", ("adv", f"{NS}:trade/buzo_mercante"), E(10)),
    (115, 1, "Pacto en el Inframundo", "quartz", ("adv", f"{NS}:trade/comerciante_infernal"), E(14)),
    (116, 1, "Saqueador de tumbas", "bone", ("adv", f"{NS}:trade/saqueador_de_tumbas"), E(18)),
    (117, 1, "Trato con el maestro", "nether_star", ("adv", f"{NS}:trade/maestro_del_oneblock"), E(32)),
    # --- Recoleccion y fabricacion ---
    (201, 2, "Cantero", "stone", M(500, "stone"), E(6)),
    (202, 2, "Carbonero", "coal_ore", M(100, "coal_ore"), E(6)),
    (203, 2, "Herrero en ciernes", "iron_ore", M(64, "iron_ore"), E(8)),
    (204, 2, "Cobre a montones", "copper_ore", M(64, "copper_ore"), E(6)),
    (205, 2, "Fiebre del oro", "gold_ore", M(32, "gold_ore"), E(10)),
    (206, 2, "Brillo azul", "diamond_ore", M(16, "diamond_ore"), E(16)),
    (207, 2, "Esmeraldas en bruto", "emerald_ore", M(5, "emerald_ore"), E(12)),
    (208, 2, "Leñador", "oak_log", M(128, "oak_log"), E(6)),
    (209, 2, "Restos antiguos", "ancient_debris", M(4, "ancient_debris"), E(24)),
    (210, 2, "Que se haga la luz", "torch", C(128, "torch"), E(4)),
    (211, 2, "Pico de hierro", "iron_pickaxe", C(1, "iron_pickaxe"), E(4)),
    (212, 2, "Pico de diamante", "diamond_pickaxe", C(1, "diamond_pickaxe"), E(10)),
    (213, 2, "Panadero", "bread", C(32, "bread"), E(6)),
    (214, 2, "Biblioteca", "bookshelf", C(8, "bookshelf"), E(8)),
    (215, 2, "Yunque propio", "anvil", C(1, "anvil"), E(8)),
    (216, 2, "Granjero", "wheat_seeds", P(64, "wheat_seeds"), E(4)),
    (217, 2, "Abono", "bone_meal", P(64, "bone_meal"), E(4)),
    (218, 2, "Manzana dorada", "golden_apple", C(1, "golden_apple"), E(8)),
    # --- Combate y exploracion ---
    (301, 3, "Cazador de zombis", "rotten_flesh", K(50, "zombie"), E(8)),
    (302, 3, "Rompehuesos", "bone", K(50, "skeleton"), E(8)),
    (303, 3, "Aracnofobia", "string", K(30, "spider"), E(6)),
    (304, 3, "Antiexplosivos", "gunpowder", K(25, "creeper"), E(8)),
    (305, 3, "Mirada perdida", "ender_pearl", K(15, "enderman"), E(12)),
    (306, 3, "Bomberos", "blaze_rod", K(10, "blaze"), E(12)),
    (307, 3, "Esqueletos oscuros", "coal", K(10, "wither_skeleton"), E(16)),
    (308, 3, "Pegajoso", "slime_ball", K(20, "slime"), E(6)),
    (309, 3, "Guerrero", "iron_sword", U(300, "mob_kills"), E(16)),
    (310, 3, "Caminante", "leather_boots", U(10000, "walk_one_cm", 100), E(6)),
    (311, 3, "Nadador", "kelp", U(2000, "swim_one_cm", 100), E(6)),
    (312, 3, "Pescador", "fishing_rod", U(20, "fish_caught"), E(6)),
    (313, 3, "Criador", "wheat", U(30, "animals_bred"), E(6)),
    (314, 3, "Comerciante", "emerald", U(25, "traded_with_villager"), E(10)),
    (315, 3, "Escalador", "ladder", U(500, "climb_one_cm", 100), E(4)),
]

# Logros vanilla con recompensa extra: (id, advancement, nombre, icono, recompensas)
ADVS = [
    (401, "story/mine_stone", "Edad de piedra", "wooden_pickaxe", E(1)),
    (402, "story/upgrade_tools", "Mejora", "stone_pickaxe", E(2)),
    (403, "story/smelt_iron", "Edad del hierro", "iron_ingot", E(3)),
    (404, "story/obtain_armor", "Vístete", "iron_chestplate", E(4)),
    (405, "story/lava_bucket", "Ponte caliente", "lava_bucket", E(4)),
    (406, "story/iron_tools", "¿No es pico de hierro?", "iron_pickaxe", E(4)),
    (407, "story/deflect_arrow", "Hoy no, gracias", "shield", E(4)),
    (408, "story/form_obsidian", "Desafío de hielo", "obsidian", E(6)),
    (409, "story/mine_diamond", "¡Diamantes!", "diamond", E(8)),
    (410, "story/enter_the_nether", "Más profundo", "flint_and_steel", E(10)),
    (411, "story/shiny_gear", "Cúbreme de diamantes", "diamond_chestplate", E(12)),
    (412, "story/enchant_item", "Encantador", "enchanting_table", E(8)),
    (413, "story/cure_zombie_villager", "Doctor zombi", "golden_apple", E(16)),
    (414, "story/follow_ender_eye", "Ojo espía", "ender_eye", E(16)),
    (415, "story/enter_the_end", "¿El fin?", "end_stone", E(20)),
    (416, "nether/find_fortress", "Una terrible fortaleza", "nether_bricks", E(10)),
    (417, "nether/obtain_blaze_rod", "En llamas", "blaze_rod", E(8)),
    (418, "nether/get_wither_skull", "Esqueleto espeluznante", "wither_skeleton_skull", E(16)),
    (419, "nether/summon_wither", "Altura máxima", "nether_star", E(32)),
    (420, "nether/brew_potion", "Cervecería local", "brewing_stand", E(6)),
    (421, "end/kill_dragon", "Libera el End", "dragon_head", E(48)),
    (422, "end/find_end_city", "El final del juego", "purpur_block", E(24)),
    (423, "adventure/kill_a_mob", "Cazador de monstruos", "iron_sword", E(2)),
    (424, "adventure/trade", "¡Buen trato!", "emerald", E(2)),
    (425, "adventure/totem_of_undying", "Más allá de la tumba", "totem_of_undying", E(16)),
    (426, "husbandry/plant_seed", "Un lugar con semillas", "wheat_seeds", E(1)),
    (427, "husbandry/breed_an_animal", "Los pájaros y las abejas", "wheat", E(2)),
    (428, "husbandry/tame_an_animal", "Mejores amigos", "bone", E(4)),
]

# Metas de la Isla (grupales). (id, nombre, icono, criterio, objetivo, div, recompensas por jugador)
def GM(i, n, ic, s, t, r): return (i, n, ic, f"minecraft.mined:minecraft.{s}", t, 1, r)
def GP(i, n, ic, s, t, r): return (i, n, ic, f"minecraft.used:minecraft.{s}", t, 1, r)
def GC(i, n, ic, s, t, r): return (i, n, ic, f"minecraft.crafted:minecraft.{s}", t, 1, r)
def GK(i, n, ic, s, t, r): return (i, n, ic, f"minecraft.killed:minecraft.{s}", t, 1, r)
def GU(i, n, ic, s, t, d, r): return (i, n, ic, f"minecraft.custom:minecraft.{s}", t, d, r)
GROUPS = [
    GP(501, "Colocar 3000 de tierra", "dirt", "dirt", 3000, E(8)),
    GP(502, "Colocar 3000 de adoquín", "cobblestone", "cobblestone", 3000, E(8)),
    GP(503, "Colocar 2000 tablones de roble", "oak_planks", "oak_planks", 2000, E(8)),
    GM(504, "Minar 5000 de piedra", "stone", "stone", 5000, E(12)),
    GM(505, "Minar 1000 menas de carbón", "coal_ore", "coal_ore", 1000, E(10)),
    GM(506, "Minar 500 menas de hierro", "iron_ore", "iron_ore", 500, E(12)),
    GM(507, "Minar 800 menas de cobre", "copper_ore", "copper_ore", 800, E(10)),
    GM(508, "Minar 300 menas de oro", "gold_ore", "gold_ore", 300, E(12)),
    GM(509, "Minar 500 menas de redstone", "redstone_ore", "redstone_ore", 500, E(10)),
    GM(510, "Minar 300 menas de lapislázuli", "lapis_ore", "lapis_ore", 300, E(10)),
    GM(511, "Minar 150 menas de diamante", "diamond_ore", "diamond_ore", 150, E(20)),
    GM(512, "Romper 300 troncos de roble", "oak_log", "oak_log", 300, E(8)),
    GM(513, "Romper 300 troncos de abeto", "spruce_log", "spruce_log", 300, E(8)),
    GM(514, "Romper 300 troncos de abedul", "birch_log", "birch_log", 300, E(8)),
    GM(515, "Romper 300 troncos de jungla", "jungle_log", "jungle_log", 300, E(8)),
    GM(516, "Romper 300 troncos de acacia", "acacia_log", "acacia_log", 300, E(8)),
    GM(517, "Romper 300 troncos de roble oscuro", "dark_oak_log", "dark_oak_log", 300, E(8)),
    GM(518, "Romper 200 troncos de cerezo", "cherry_log", "cherry_log", 200, E(8)),
    GM(519, "Romper 200 troncos de mangle", "mangrove_log", "mangrove_log", 200, E(8)),
    GM(520, "Minar 3000 de netherrack", "netherrack", "netherrack", 3000, E(10)),
    GM(521, "Minar 1000 de arena", "sand", "sand", 1000, E(8)),
    GM(522, "Minar 500 de piedra del End", "end_stone", "end_stone", 500, E(12)),
    GC(523, "Fabricar 100 bloques de diamante", "diamond_block", "diamond_block", 100, E(32)),
    GC(524, "Fabricar 200 bloques de hierro", "iron_block", "iron_block", 200, E(16)),
    GC(525, "Fabricar 100 bloques de oro", "gold_block", "gold_block", 100, E(16)),
    GC(526, "Fabricar 2000 antorchas", "torch", "torch", 2000, E(8)),
    GC(527, "Hornear 500 panes", "bread", "bread", 500, E(10)),
    GK(528, "Derrotar 500 zombis", "zombie_head", "zombie", 500, E(12)),
    GK(529, "Derrotar 500 esqueletos", "skeleton_skull", "skeleton", 500, E(12)),
    GK(530, "Derrotar 300 creepers", "creeper_head", "creeper", 300, E(12)),
    GK(531, "Derrotar 200 endermen", "ender_pearl", "enderman", 200, E(16)),
    GU(532, "Derrotar 3000 monstruos", "netherite_sword", "mob_kills", 3000, 1, E(20)),
    GU(533, "Correr 50.000 bloques", "golden_boots", "sprint_one_cm", 50000, 100, E(12)),
    GU(534, "Volar 20.000 bloques", "phantom_membrane", "aviate_one_cm", 20000, 100, E(16)),
    GU(535, "Nadar 10.000 bloques", "trident", "swim_one_cm", 10000, 100, E(12)),
    GU(536, "Navegar 10.000 bloques", "oak_boat", "boat_one_cm", 10000, 100, E(10)),
]

# Diarias (se reinician cada dia de Minecraft, 24000 ticks)
DAILY = [
    (601, "Patrulla diaria", "iron_sword", ("stat", "minecraft.custom:minecraft.mob_kills", 20, 1), E(4)),
    (602, "Cantera diaria", "stone", ("stat", "minecraft.mined:minecraft.stone", 128, 1), E(4)),
    (603, "Entrega: 32 adoquines", "cobblestone", ("deliver", "cobblestone", 32), E(5)),
]

# ---------- utilidades ----------
files = {}
def W(path, content):
    files[path] = content if isinstance(content, str) else json.dumps(content, indent=2, ensure_ascii=False)
def F(name, lines): W(f"data/{NS}/function/{name}.mcfunction", "\n".join(lines) + "\n")
def T(*parts): return json.dumps(list(parts), ensure_ascii=False)
PFX = {"text": "[Misiones] ", "color": "gold"}

ES = {"emerald": "esmeraldas", "experience_bottle": "frascos de experiencia", "totem_of_undying": "tótem de la inmortalidad"}
def rew_text(r):
    return ", ".join(f"{n} {ES.get(it, it.replace('_', ' '))}" for it, n in r)

# Todas las misiones en formato comun: id, cat, nombre, icono, cond, rew, kind
ALL = []
for q in QUESTS: ALL.append(dict(id=q[0], cat=q[1], name=q[2], icon=q[3], cond=q[4], rew=q[5], kind="ind"))
for a in ADVS: ALL.append(dict(id=a[0], cat=4, name=a[2], icon=a[3], cond=("adv", "minecraft:" + a[1]), rew=a[4], kind="ind"))
for g in GROUPS: ALL.append(dict(id=g[0], cat=5, name=g[1], icon=g[2], crit=g[3], target=g[4], div=g[5], rew=g[6], kind="grp"))
for d in DAILY: ALL.append(dict(id=d[0], cat=6, name=d[1], icon=d[2], cond=d[3], rew=d[4], kind="day"))

objectives = ["sq dummy", "sq_group dummy", "sq_tmp dummy", "so_shop_seen dummy", "so_shop_buys dummy",
              "quests trigger", "quest_menu trigger", "quest_view trigger", "quest_claim trigger"]
check = []   # cada segundo
reset_day = []

def cond_desc(q):
    c = q.get("cond")
    if q["kind"] == "grp": return f"Meta compartida: {q['target']}"
    t = c[0]
    if t == "blocks": return f"Llegar a {c[1]} bloques minados del OneBlock"
    if t == "stat": return f"Objetivo: {c[2] // c[3]}" + (" bloques" if c[3] > 1 else "")
    if t == "adv": return "Conseguir el logro" if c[1].startswith("minecraft:") else "Comerciar con el mercader"
    if t == "score": return f"Objetivo: {c[2]}"
    if t == "deliver": return f"Entregar {c[2]} {c[1].replace('_', ' ')} (se quitan al reclamar)"

for q in ALL:
    i, kind = q["id"], q["kind"]
    s = f"sqs_{i}"; objectives.append(f"{s} dummy")
    ready_cmd = f"function {NS}:q/{i}/ready"
    give = [f"give @s minecraft:{it} {n}" for it, n in q["rew"]]
    done_msg = f"tellraw @s {T(PFX, {'text': 'Reclamaste ', 'color': 'green'}, {'text': q['name'], 'color': 'white'}, {'text': ' → ' + rew_text(q['rew']), 'color': 'gray'})}"
    snd = "playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.6 1.2"
    full = f"execute unless function {NS}:lib/space run return run tellraw @s {T(PFX, {'text': 'Inventario lleno: libera un espacio y vuelve a reclamar.', 'color': 'red'})}"
    back = {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": f"/trigger quest_menu set {q['cat']}"}}

    if kind == "grp":
        c = f"sqc_{i}"; objectives.append(f"{c} {q['crit']}")
        raw = f"#raw_{i}"; g = f"#g_{i}"
        check += [f"execute as @a[scores={{{c}=1..}}] run scoreboard players operation {raw} sq_group += @s {c}",
                  f"scoreboard players set @a[scores={{{c}=1..}}] {c} 0",
                  f"scoreboard players operation {g} sq_group = {raw} sq_group"]
        if q["div"] > 1: check.append(f"scoreboard players operation {g} sq_group /= #{q['div']} sq")
        check.append(f"execute unless score #done_{i} sq_group matches 1 if score {g} sq_group matches {q['target']}.. run {ready_cmd}")
        F(f"q/{i}/ready", ["scoreboard players set #done_" + str(i) + " sq_group 1",
                           f"tellraw @a {T(PFX, {'text': '¡Meta de la Isla completada! ', 'color': 'light_purple'}, {'text': q['name'], 'color': 'white'}, {'text': ' — todos pueden reclamar su parte con /trigger quests', 'color': 'gray'})}",
                           "execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.7 1"])
        prog = [{"score": {"name": g, "objective": "sq_group"}, "color": "yellow"}, {"text": f" / {q['target']}", "color": "gray"}]
        F(f"q/{i}/view", [
            f"execute if score #done_{i} sq_group matches 1 unless score @s {s} matches 2 run return run dialog show @s {NS}:claim_{i}",
            f"execute if score @s {s} matches 2 run return run tellraw @s {T(PFX, {'text': q['name'] + ': ya reclamaste tu parte.', 'color': 'gray'}, back)}",
            f"tellraw @s {T(PFX, {'text': q['name'] + ': ', 'color': 'white'}, *prog, back)}"])
        F(f"q/{i}/claim", [f"execute unless score #done_{i} sq_group matches 1 run return fail",
                           f"execute if score @s {s} matches 2 run return fail", full,
                           f"scoreboard players set @s {s} 2", *give, done_msg, snd])
    else:
        c = q["cond"]; t = c[0]; prog = []
        sel = f"@a[scores={{{s}=0}}]" if kind == "ind" else f"@a[scores={{{s}=0}}]"
        if t == "blocks":
            check.append(f"execute if score #blocks sq matches {c[1]}.. run {ready_cmd.replace('function', 'execute as ' + sel + ' run function')}")
            prog = [{"score": {"name": "#blocks", "objective": "sq"}, "color": "yellow"}, {"text": f" / {c[1]} bloques", "color": "gray"}]
        elif t == "stat":
            p = f"sqp_{i}"; objectives.append(f"{p} {c[1]}")
            check.append(f"execute as {sel} if score @s {p} matches {c[2]}.. run {ready_cmd}")
            if c[3] > 1:
                v = f"sqv_{i}"; objectives.append(f"{v} dummy")
                check.append(f"execute as @a run scoreboard players operation @s {v} = @s {p}")
                check.append(f"execute as @a run scoreboard players operation @s {v} /= #{c[3]} sq")
            else: v = p
            prog = [{"score": {"name": "@s", "objective": v}, "color": "yellow"}, {"text": f" / {c[2] // c[3]}", "color": "gray"}]
            if kind == "day": reset_day.append(f"scoreboard players reset * {p}")
        elif t == "adv":
            check.append(f"execute as @a[scores={{{s}=0}},advancements={{{c[1]}=true}}] run {ready_cmd}")
            prog = [{"text": "pendiente", "color": "yellow"}]
        elif t == "score":
            check.append(f"execute as {sel} if score @s {c[1]} matches {c[2]}.. run {ready_cmd}")
            prog = [{"score": {"name": "@s", "objective": c[1]}, "color": "yellow"}, {"text": f" / {c[2]}", "color": "gray"}]
        if t != "deliver":
            F(f"q/{i}/ready", [f"scoreboard players set @s {s} 1",
                               f"tellraw @s {T(PFX, {'text': '¡Misión lista para reclamar! ', 'color': 'green'}, {'text': q['name'], 'color': 'white'}, {'text': ' [Abrir]', 'color': 'aqua', 'click_event': {'action': 'run_command', 'command': f'/trigger quest_view set {i}'}})}",
                               "playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.7 1.6"])
            F(f"q/{i}/view", [
                f"execute if score @s {s} matches 1 run return run dialog show @s {NS}:claim_{i}",
                f"execute if score @s {s} matches 2 run return run tellraw @s {T(PFX, {'text': q['name'] + ': completada.', 'color': 'gray'}, back)}",
                f"tellraw @s {T(PFX, {'text': q['name'] + ': ', 'color': 'white'}, *prog, back)}"])
            F(f"q/{i}/claim", [f"execute unless score @s {s} matches 1 run return fail", full,
                               f"scoreboard players set @s {s} 2", *give, done_msg, snd])
        else:
            item, n = c[1], c[2]
            F(f"q/{i}/view", [
                f"execute if score @s {s} matches 2 run return run tellraw @s {T(PFX, {'text': q['name'] + ': ya entregada hoy.', 'color': 'gray'}, back)}",
                f"execute store result score @s sq_tmp run clear @s minecraft:{item} 0",
                f"execute if score @s sq_tmp matches {n}.. run return run dialog show @s {NS}:claim_{i}",
                f"tellraw @s {T(PFX, {'text': q['name'] + ': tienes ', 'color': 'white'}, {'score': {'name': '@s', 'objective': 'sq_tmp'}, 'color': 'yellow'}, {'text': f' / {n}', 'color': 'gray'}, back)}"])
            F(f"q/{i}/claim", [f"execute if score @s {s} matches 2 run return fail",
                               f"execute store result score @s sq_tmp run clear @s minecraft:{item} 0",
                               f"execute unless score @s sq_tmp matches {n}.. run return run tellraw @s {T(PFX, {'text': 'Te faltan objetos para entregar.', 'color': 'red'})}",
                               full, f"clear @s minecraft:{item} {n}",
                               f"scoreboard players set @s {s} 2", *give, done_msg, snd])
        if kind == "day": reset_day.append(f"scoreboard players set * {s} 0")

    # ventana de reclamo (confirmacion)
    body = [{"type": "minecraft:item", "item": {"id": f"minecraft:{q['icon']}", "count": 1},
             "description": {"contents": {"text": q["name"], "color": "white"}}},
            {"type": "minecraft:plain_message", "contents": {"text": cond_desc(q), "color": "gray"}},
            {"type": "minecraft:plain_message", "contents": {"text": "Recompensa: " + rew_text(q["rew"]), "color": "green"}}]
    W(f"data/{NS}/dialog/claim_{i}.json", {
        "type": "minecraft:confirmation", "title": {"text": "Reclamar recompensa", "color": "gold"},
        "body": body, "can_close_with_escape": True, "pause": False,
        "yes": {"label": {"text": "Entregar y reclamar" if q.get("cond", ("",))[0] == "deliver" else "Reclamar", "color": "green"},
                "action": {"type": "minecraft:run_command", "command": f"/trigger quest_claim set {i}"}},
        "no": {"label": {"text": "« Volver"}, "action": {"type": "minecraft:show_dialog", "dialog": f"{NS}:cat_{q['cat']}"}}})

# advancements de mercaderes (oneblock_adventure_traders)
def trade_adv(name, tag):
    W(f"data/{NS}/advancement/trade/{name}.json", {"criteria": {"c": {"trigger": "minecraft:villager_trade",
        "conditions": {"villager": {"nbt": "{Tags:[\"%s\"]}" % tag}}}}, "requirements": [["c"]]})
trade_adv("any", "oba_trader")
for t in ["mercader_de_la_llanura", "buzo_mercante", "comerciante_infernal", "saqueador_de_tumbas", "maestro_del_oneblock"]:
    trade_adv(t, f"oba_t_{t}")

# ---------- ventanas ----------
W(f"data/{NS}/dialog/main.json", {
    "type": "minecraft:multi_action", "title": {"text": "Misiones OneBlock", "color": "gold", "bold": True},
    "external_title": {"text": "Misiones"},
    "body": [{"type": "minecraft:plain_message", "contents": {"text": "Toca una misión para ver tu progreso o reclamarla.", "color": "gray"}}],
    "columns": 2, "can_close_with_escape": True, "pause": False,
    "actions": [{"label": {"text": n, "color": col}, "width": 150,
                 "action": {"type": "minecraft:run_command", "command": f"/trigger quest_menu set {k}"}} for k, (n, col) in CATS.items()]})
for k, (n, col) in CATS.items():
    acts = [{"label": {"text": q["name"], "color": col}, "width": 150,
             "tooltip": {"text": cond_desc(q) + "\nRecompensa: " + rew_text(q["rew"])},
             "action": {"type": "minecraft:run_command", "command": f"/trigger quest_view set {q['id']}"}}
            for q in ALL if q["cat"] == k]
    W(f"data/{NS}/dialog/cat_{k}.json", {
        "type": "minecraft:multi_action", "title": {"text": n, "color": col, "bold": True},
        "body": [{"type": "minecraft:plain_message", "contents": {"text": "Verde en el chat = lista para reclamar. Pasa el ratón para ver el objetivo.", "color": "gray"}}],
        "columns": 2, "can_close_with_escape": True, "pause": False, "actions": acts,
        "exit_action": {"label": {"text": "« Volver"}, "action": {"type": "minecraft:show_dialog", "dialog": f"{NS}:main"}}})

# ---------- funciones base ----------
F("load", ["# Crea marcadores (repetir no falla: Minecraft solo avisa que ya existen)",
           *[f"scoreboard objectives add {o}" for o in objectives],
           "scoreboard objectives add so_core dummy", "scoreboard objectives add ib_minedcount dummy",
           "execute unless score #enabled sq matches 0.. run scoreboard players set #enabled sq 1",
           "scoreboard players set #100 sq 100",
           f"tellraw @a[tag=oneblock_admin] {T(PFX, {'text': 'v2 cargado. /function so_quests:admin/help', 'color': 'gray'})}"])
F("lib/read_count", ["# so_core primero; si no existe, lectura autonoma de Simply OneBlock",
    "scoreboard players set #src sq 0",
    "execute if score #blocks so_core matches -2147483648.. run scoreboard players set #src sq 1",
    "execute if score #src sq matches 1 run scoreboard players operation #blocks sq = #blocks so_core",
    "execute if score #src sq matches 0 if score fake_player ib_minedcount matches -2147483648.. run scoreboard players set #src sq 2",
    "execute if score #src sq matches 2 run scoreboard players operation #blocks sq = fake_player ib_minedcount",
    "execute if score #src sq matches 0 run scoreboard players set #blocks sq 0"])
F("lib/space", [*[f"execute unless items entity @s container.{n} * run return 1" for n in range(36)], "return fail"])
F("lib/init_player", [f"execute unless score @s sqs_{q['id']} matches 0.. run scoreboard players set @s sqs_{q['id']} 0" for q in ALL if q["kind"] != "grp"]
  + ["tag @s add sq_init"])
F("lib/check", ["function so_quests:lib/read_count", *check])
F("lib/new_day", [*reset_day, f"tellraw @a {T(PFX, {'text': 'Nuevo día: las misiones diarias se reiniciaron.', 'color': 'yellow'})}"])
F("lib/view", ["$function so_quests:q/$(id)/view"])
F("lib/claim", ["$function so_quests:q/$(id)/claim"])
F("lib/open_cat", ["$dialog show @s so_quests:cat_$(id)"])
F("lib/h_open_cat", ["execute store result storage so_quests:tmp id int 1 run scoreboard players get @s quest_menu", "function so_quests:lib/open_cat with storage so_quests:tmp"])
F("lib/h_view", ["execute store result storage so_quests:tmp id int 1 run scoreboard players get @s quest_view", "function so_quests:lib/view with storage so_quests:tmp"])
F("lib/h_claim", ["execute store result storage so_quests:tmp id int 1 run scoreboard players get @s quest_claim", "function so_quests:lib/claim with storage so_quests:tmp"])
F("tick", [
    "execute unless score #enabled sq matches 1 run return 0",
    "execute as @a[tag=!sq_init] run function so_quests:lib/init_player",
    "scoreboard players add #t sq 1",
    "execute if score #t sq matches 20.. run function so_quests:lib/check",
    "execute if score #t sq matches 20.. run scoreboard players set #t sq 0",
    "scoreboard players add #day sq 1",
    "execute if score #day sq matches 24000.. run function so_quests:lib/new_day",
    "execute if score #day sq matches 24000.. run scoreboard players set #day sq 0",
    "execute as @a[scores={quests=1..}] at @s run dialog show @s so_quests:main",
    "scoreboard players reset @a quests", "scoreboard players enable @a quests",
    "execute as @a[scores={quest_menu=1..6}] at @s run function so_quests:lib/h_open_cat",
    "scoreboard players reset @a quest_menu", "scoreboard players enable @a quest_menu",
    "execute as @a[scores={quest_view=1..}] at @s run function so_quests:lib/h_view",
    "scoreboard players reset @a quest_view", "scoreboard players enable @a quest_view",
    "execute as @a[scores={quest_claim=1..}] at @s run function so_quests:lib/h_claim",
    "scoreboard players reset @a quest_claim", "scoreboard players enable @a quest_claim"])
F("admin/help", [f"tellraw @s {T(PFX, {'text': 'Admin: enable, disable, status, new_day, reset_me, set_group {id:501,value:100}, uninstall', 'color': 'gray'})}"])
F("admin/enable", ["scoreboard players set #enabled sq 1", f"tellraw @s {T(PFX, {'text': 'Activado', 'color': 'green'})}"])
F("admin/disable", ["scoreboard players set #enabled sq 0", f"tellraw @s {T(PFX, {'text': 'Desactivado', 'color': 'red'})}"])
F("admin/new_day", ["function so_quests:lib/new_day"])
F("admin/status", ["function so_quests:lib/read_count",
    f"tellraw @s {T(PFX, {'text': 'Fuente (1=so_core 2=Simply OneBlock 0=ninguna): ', 'color': 'gray'}, {'score': {'name': '#src', 'objective': 'sq'}, 'color': 'yellow'}, {'text': '  Bloques: ', 'color': 'gray'}, {'score': {'name': '#blocks', 'objective': 'sq'}, 'color': 'yellow'})}"])
F("admin/reset_me", [f"scoreboard players set @s sqs_{q['id']} 0" for q in ALL] + [f"tellraw @s {T(PFX, {'text': 'Tus misiones se reiniciaron.', 'color': 'yellow'})}"])
F("admin/set_group", ["$scoreboard players set #raw_$(id) sq_group $(value)", "$scoreboard players reset #done_$(id) sq_group"])
F("uninstall", [f"scoreboard objectives remove {o.split()[0]}" for o in objectives if not o.startswith("so_shop")]
  + ["tag @a remove sq_init", "datapack disable \"file/so-quests\"", "datapack disable \"file/so-quests.zip\""])

README2 = """\
=====================================================
 SO QUESTS v2 - Guia de objetivos sin especificacion
=====================================================

Este listado explica SOLO las misiones cuya ventana no dice
que hacer exactamente (muestran "Objetivo: N" sin mas).
Las que ya se explican solas (hitos de bloques, metas de la
isla y entregas) no estan aqui.

Recompensa: todas pagan en esmeraldas (E); el numero sale al
pasar el raton por la mision en el menu.

-----------------------------------------------------
 FASES Y PROGRESO (las unicas sin detalle)
-----------------------------------------------------
- Primera visita a la tienda: abre la tienda una vez con
  /trigger shop (solo abrirla cuenta, no hace falta comprar).
- Cliente fiel: hacer 10 compras en la tienda.
- Primer trueque: comerciar 1 vez con cualquier mercader.
- Trato en la llanura: comerciar con el Mercader de la
  Llanura (aparece a los 750 bloques).
- El buzo del abismo: comerciar con el Buzo Mercante
  (aparece a los 3.000 bloques).
- Pacto en el Inframundo: comerciar con el Comerciante
  Infernal (aparece a los 6.750 bloques).
- Saqueador de tumbas: comerciar con el Saqueador de Tumbas
  (aparece a los 9.000 bloques).
- Trato con el maestro: comerciar con el Maestro del
  OneBlock (aparece a los 15.000 bloques).

-----------------------------------------------------
 RECOLECCION Y FABRICACION
-----------------------------------------------------
- Cantero: picar 500 bloques de piedra.
- Carbonero: picar 100 menas de carbon.
- Herrero en ciernes: picar 64 menas de hierro.
- Cobre a montones: picar 64 menas de cobre.
- Fiebre del oro: picar 32 menas de oro.
- Brillo azul: picar 16 menas de diamante.
- Esmeraldas en bruto: picar 5 menas de esmeralda.
- Lenador: romper 128 troncos de roble.
- Restos antiguos: picar 4 restos antiguos (ancient debris).
- Que se haga la luz: fabricar 128 antorchas.
- Pico de hierro: fabricar 1 pico de hierro.
- Pico de diamante: fabricar 1 pico de diamante.
- Panadero: fabricar 32 panes.
- Biblioteca: fabricar 8 estanterias.
- Yunque propio: fabricar 1 yunque.
- Granjero: plantar 64 semillas de trigo.
- Abono: usar 64 polvos de hueso (hacer crecer cultivos).
- Manzana dorada: fabricar 1 manzana dorada.

-----------------------------------------------------
 COMBATE Y EXPLORACION
-----------------------------------------------------
- Cazador de zombis: derrotar 50 zombis.
- Rompehuesos: derrotar 50 esqueletos.
- Aracnofobia: derrotar 30 aranas.
- Antiexplosivos: derrotar 25 creepers.
- Mirada perdida: derrotar 15 endermen.
- Bomberos: derrotar 10 blazes.
- Esqueletos oscuros: derrotar 10 esqueletos del Wither.
- Pegajoso: derrotar 20 slimes (limas).
- Guerrero: derrotar 300 monstruos (de cualquier tipo).
- Caminante: caminar 10.000 bloques.
- Nadador: nadar 2.000 bloques.
- Pescador: pescar 20 peces (cania).
- Criador: criar 30 animales.
- Comerciante: comerciar 25 veces con aldeanos o mercaderes.
- Escalador: trepar 500 bloques (escaleras, enredaderas).

-----------------------------------------------------
 LOGROS DE MINECRAFT (cual es cada uno)
-----------------------------------------------------
- Edad de piedra: picar piedra nueva (con pico de madera).
- Mejora: fabricar una herramienta mejor (pico de piedra).
- Edad del hierro: fundir un lingote de hierro.
- Vestete: conseguir una pieza de armadura de hierro.
- Ponte caliente: llenar un balde con lava.
- No es pico de hierro?: fabricar un pico de hierro.
- Hoy no, gracias: detener una flecha con el escudo.
- Desafio de hielo: conseguir un bloque de obsidiana.
- Diamantes!: picar un diamante.
- Mas profundo: entrar al Nether.
- Cubreme de diamantes: llevar armadura completa de diamante.
- Encantador: encantar un objeto en la mesa de encantamientos.
- Doctor zombi: curar a un aldeano zombi.
- Ojo espia: lanzar y seguir un ojo de ender.
- El fin?: entrar al End.
- Una terrible fortaleza: entrar a una fortaleza del Nether.
- En llamas: conseguir una varilla de blaze.
- Esqueleto espeluznante: conseguir un craneo de esqueleto
  del Wither.
- Altura maxima: invocar al Wither.
- Cerveceria local: preparar una pocion.
- Libera el End: derrotar al dragon del End.
- El final del juego: encontrar una ciudad del End.
- Cazador de monstruos: derrotar a cualquier monstruo hostil.
- Buen trato!: comerciar con un aldeano.
- Mas alla de la tumba: evitar la muerte usando un totem de
  la inmortalidad.
- Un lugar con semillas: plantar una semilla.
- Los pajaros y las abejas: criar dos animales.
- Mejores amigos: domesticar un animal.

-----------------------------------------------------
 DIARIAS (sin detalle en la ventana)
-----------------------------------------------------
- Patrulla diaria: derrotar 20 monstruos en un dia.
- Cantera diaria: picar 128 bloques de piedra en un dia.

(Entrega: 32 adoquines si se explica sola: te quita los 32
 adoquines al reclamar.)

Nota: los logros de Minecraft ya conseguidos antes de
instalar el datapack SI cuentan: se pueden reclamar al
instante desde la seccion Logros.
"""

W("README-OBJETIVOS.md", README2)
W("data/minecraft/tags/function/load.json", {"values": [f"{NS}:load"]})
W("data/minecraft/tags/function/tick.json", {"values": [f"{NS}:tick"]})
W("pack.mcmeta", {"pack": {"description": "Simply OneBlock Expansion - Quests v2 (/trigger quests)", "min_format": [107, 1], "max_format": [107, 1]}})

if os.path.isdir(OUT): shutil.rmtree(OUT)
for p, c in files.items():
    fp = os.path.join(OUT, p); os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(c)
print(f"{len(files)} archivos | individuales {len(QUESTS)} | logros {len(ADVS)} | grupales {len(GROUPS)} | diarias {len(DAILY)}")
