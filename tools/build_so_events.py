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

# ---------------------------------------------------------------- mobs (v2: todo suma)
def it(item, **ench):
    if not ench:
        return f'{{id:"minecraft:{item}",count:1}}'
    e = ",".join(f'"minecraft:{k}":{v}' for k, v in ench.items())
    return f'{{id:"minecraft:{item}",count:1,components:{{"minecraft:enchantments":{{{e}}}}}}}'

def eq(**slots):
    parts = [f"{k}:{v if v.startswith('{') else it(v)}" for k, v in slots.items()]
    drops = ",".join(f"{k}:0.0f" for k in slots)
    return f"equipment:{{{','.join(parts)}}},drop_chances:{{{drops}}}"

def attrs(**a):
    return "attributes:[" + ",".join(f'{{id:"minecraft:{k}",base:{v}d}}' for k, v in a.items()) + "]"

def rider(eid, nbt):
    return f'Passengers:[{{id:"minecraft:{eid}",{nbt}}}]'

FX = lambda *ids: "active_effects:[" + ",".join(f'{{id:"minecraft:{i}",amplifier:0b,duration:-1,show_particles:1b}}' for i in ids) + "]"
BASE = 'Tags:["so_ev_mob"],PersistenceRequired:1b'
GOLEM = 'Tags:["so_ev_mob","so_ev_golem"],PersistenceRequired:1b'
GOLD = lambda p: it(p, protection=2, unbreaking=1)
LEATH = lambda p: it(p, protection=1, unbreaking=3)
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
    # --- horda zombi
    "zombie_villager": ("zombie_villager", BASE),
    "drowned": ("drowned", BASE),
    "baby_zombie": ("zombie", f"{BASE},IsBaby:1b"),
    "zombie_horseman": ("zombie_horse", f'{BASE},' + rider("zombie",
        f'{BASE},CustomNameVisible:1b,CustomName:{{text:"Jinete Zombi",color:"dark_green"}},{attrs(max_health=40)},Health:40f,'
        f'{eq(head="iron_helmet", chest="iron_chestplate", mainhand="iron_spear")}')),
    "chicken_jockey": ("chicken", f'{BASE},IsChickenJockey:1b,' + rider("zombie",
        f'{BASE},IsBaby:1b,CustomName:{{text:"Escolta Dorada",color:"gold"}},'
        f'{eq(head=GOLD("golden_helmet"), chest=GOLD("golden_chestplate"), legs=GOLD("golden_leggings"), feet=GOLD("golden_boots"), mainhand=it("wooden_sword", sharpness=1))}')),
    # --- slimes que si pegan (mediano con escala de bebe)
    "slime_mini": ("slime", f"{BASE},Size:1,{attrs(scale=0.5, attack_damage=3)}"),
    # --- acorazada
    "witch": ("witch", BASE),
    "enderman": ("enderman", BASE),
    "creeper": ("creeper", BASE),
    "zombie_escort": ("zombie", f'{BASE},CustomName:{{text:"Escolta de Cuero",color:"gray"}},'
        f'{eq(head=LEATH("leather_helmet"), chest=LEATH("leather_chestplate"), legs=LEATH("leather_leggings"), feet=LEATH("leather_boots"), mainhand="iron_sword")}'),
    # --- nether
    "piglin": ("piglin", f"{BASE},IsImmuneToZombification:1b,{eq(mainhand='golden_sword')}"),
    "piglin_crossbow": ("piglin", f"{BASE},IsImmuneToZombification:1b,{eq(mainhand='crossbow')}"),
    # --- end
    "endermite": ("endermite", BASE),
    "shulker": ("shulker", BASE),
    # --- artropodos
    "cave_spider": ("cave_spider", BASE),
    "spider_big": ("spider", f"{BASE},{attrs(scale=2, max_health=32)},Health:32f"),
    "spider_jockey": ("spider", f"{BASE}," + rider("skeleton", f"{BASE},{eq(mainhand='bow')}")),
    # --- marina
    "drowned_trident": ("drowned", f"{BASE},{eq(mainhand='trident')}"),
    # --- ominosa (estilo trial chambers)
    "breeze": ("breeze", BASE),
    "bogged": ("bogged", f"{BASE},{eq(mainhand='bow')}"),
    "zombie_ominous": ("zombie", f"{BASE},{FX('speed', 'resistance')},{eq(head='chainmail_helmet', mainhand='stone_sword')}"),
    "skeleton_ominous": ("skeleton", f"{BASE},{FX('speed', 'strength')},{eq(head='chainmail_helmet', mainhand='bow')}"),
    # --- tormenta de huesos
    "stray": ("stray", f"{BASE},{eq(mainhand='bow')}"),
    "skeleton_horseman": ("skeleton_horse", f"{BASE}," + rider("skeleton", f"{BASE},{eq(head='iron_helmet', mainhand='bow')}")),
    # --- rebelion de golems
    "iron_golem": ("iron_golem", GOLEM),
    # --- v3: ilusion sombria
    "illusioner": ("illusioner", f"{BASE},{eq(mainhand='bow')}"),
    "vex": ("vex", f"{BASE},{eq(mainhand='iron_sword')}"),
    "evoker": ("evoker", BASE),
    "ravager": ("ravager", BASE),
    # --- v3: bastion
    "piglin_brute": ("piglin_brute", f"{BASE},IsImmuneToZombification:1b,{eq(mainhand='golden_axe')}"),
    # --- v3: oscuridad (sombras invisibles y rapidas)
    "sombra": ("zombie", f'{BASE},CustomName:{{text:"Sombra",color:"dark_gray"}},{FX("invisibility", "speed")},{eq(mainhand="stone_sword")}'),
    "acechador": ("husk", f'{BASE},CustomName:{{text:"Acechador del Abismo",color:"dark_aqua"}},{FX("speed", "resistance")},{eq(head="chainmail_helmet", mainhand="iron_sword")}'),
    # --- v3: pesadilla alada (sin quemarse de dia; mob_griefing esta apagado en el evento)
    "phantom": ("phantom", f"{BASE},{FX('fire_resistance')}"),
    "phantom_big": ("phantom", f"{BASE},{FX('fire_resistance')},{attrs(scale=1.6, max_health=30)},Health:30f"),
    "bat_bomber": ("bat", f"{BASE}," + rider("creeper", f'{BASE},Fuse:25,ExplosionRadius:2b,CustomName:{{text:"Murciélago Bomba",color:"red"}}')),
    # --- v3: pantano e infierno
    "blaze_fast": ("blaze", f"{BASE},{FX('speed', 'strength')}"),
    "zombified_piglin": ("zombified_piglin", f"{GOLEM},{eq(mainhand='golden_sword')}"),
    "zoglin": ("zoglin", BASE),
    # --- v4: elite (eclipse e invasiones alfa)
    "elite_zombie": ("zombie", f"{BASE},{FX('speed', 'strength', 'resistance')},"
        f"{eq(head='netherite_helmet', chest='netherite_chestplate', legs='netherite_leggings', feet='netherite_boots', mainhand=it('netherite_sword', sharpness=2))}"),
    "elite_skeleton": ("skeleton", f"{BASE},{FX('speed', 'resistance')},"
        f"{eq(head='netherite_helmet', chest='netherite_chestplate', mainhand=it('bow', power=3, punch=1))}"),
    "elite_spider": ("spider", f"{BASE},{FX('speed', 'strength')},{attrs(scale=1.4, max_health=40)},Health:40f"),
    "elite_vex": ("vex", f"{BASE},{FX('strength')},{eq(mainhand=it('iron_sword', sharpness=3))}"),
    # --- v4: caravana perdida
    "llama_caravan": ("llama", 'Tags:["so_ev_llama"],PersistenceRequired:1b,ChestedHorse:1b,Tame:1b,'
        'CustomNameVisible:1b,CustomName:{text:"Llama de la Caravana",color:"gold"}'),
    "saqueador_caravana": ("pillager", f"{BASE},{eq(mainhand='crossbow')},PatrolLeader:0b"),
    # --- v4.1: jinete del eclipse (araña élite montada por esqueleto wither)
    "eclipse_rider": ("spider", f"{BASE},{FX('speed', 'resistance')},{attrs(scale=1.3, max_health=40)},Health:40f," + rider("wither_skeleton",
        f"{BASE},{FX('fire_resistance')},{eq(head='netherite_helmet', chest='netherite_chestplate', mainhand=it('netherite_sword', sharpness=3))}")),
}
for name, (eid, nbt) in MOBS.items():
    F(f"mob/{name}", [f"summon minecraft:{eid} ~ ~ ~ {{{nbt}}}", "scoreboard players set #ok so_ev 1"])

# Warden: memoria de excavación bloqueada (no puede enterrarse ni desaparecer).
WARDEN_BRAIN = 'Brain:{memories:{"minecraft:dig_cooldown":{value:{},ttl:1200000L}}}'
F("lib/warden_keep", ['data modify entity @s Brain.memories."minecraft:dig_cooldown" set value {value:{},ttl:1200000L}'])


def boss(name, eid, hp, label, color, extra="", att=None, mount=None, tags='"so_ev_mob","so_ev_boss"'):
    a = {"max_health": hp, "knockback_resistance": 0.6, **(att or {})}
    core = (f'Tags:[{tags}],PersistenceRequired:1b,CustomNameVisible:1b,'
            f'CustomName:{{text:"{label}",color:"{color}",bold:true}},{attrs(**a)},Health:{hp}f' + (f",{extra}" if extra else ""))
    summon = (f"summon minecraft:{mount} ~ ~ ~ {{{BASE},{rider(eid, core)}}}" if mount
              else f"summon minecraft:{eid} ~ ~ ~ {{{core}}}")
    F(f"boss/{name}", [summon, "scoreboard players set #ok so_ev 1",
        f"bossbar set {NS}:boss name {T({'text': label, 'color': color, 'bold': True})}",
        f"bossbar set {NS}:boss max {hp}", f"bossbar set {NS}:boss value {hp}",
        f"bossbar set {NS}:boss players @a", f"bossbar set {NS}:boss visible true",
        "playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3",
        say("@a", f"¡Apareció {label}!", "red")])

DIA = lambda p: it(p, protection=1, thorns=1)
BOSSES = {
    "rey_zombi": dict(eid="zombie", hp=120, label="Rey Zombi", color="dark_green",
        extra=eq(head="golden_helmet", chest="iron_chestplate", mainhand=it("iron_sword", sharpness=2))),
    "zombi_gigante": dict(eid="zombie", hp=200, label="Zombi Colosal", color="dark_green", att={"scale": 2},
        extra=eq(head=DIA("diamond_helmet"), chest=DIA("diamond_chestplate"), legs=DIA("diamond_leggings"), feet=DIA("diamond_boots"), mainhand="diamond_sword")),
    "slime_rey": dict(eid="slime", hp=64, label="Slime Rey", color="green", extra="Size:5"),
    "comandante": dict(eid="skeleton", hp=110, label="Comandante Óseo", color="white",
        extra=eq(head="diamond_helmet", chest="iron_chestplate", mainhand="bow")),
    "capitan": dict(eid="vindicator", hp=130, label="Capitán Saqueador", color="dark_red",
        extra=eq(head="white_banner", mainhand=it("diamond_axe", sharpness=1))),
    "devastador": dict(eid="ravager", hp=150, label="Devastador", color="dark_red"),
    "caballero": dict(eid="wither_skeleton", hp=160, label="Caballero del Nether", color="dark_purple",
        extra=eq(head="netherite_helmet", mainhand=it("netherite_sword", sharpness=2))),
    "piglin_bruto": dict(eid="piglin_brute", hp=120, label="Bruto del Nether", color="gold",
        extra="IsImmuneToZombification:1b," + eq(mainhand=it("golden_axe", sharpness=2))),
    "senor_end": dict(eid="enderman", hp=160, label="Señor del End", color="light_purple", att={"scale": 1.6}),
    "arana_colosal": dict(eid="spider", hp=220, label="Araña Colosal", color="dark_red", att={"scale": 5, "attack_damage": 8}),
    "guardian_abismo": dict(eid="guardian", hp=60, label="Guardián del Abismo", color="aqua"),
    "heraldo_ominoso": dict(eid="breeze", hp=120, label="Heraldo Ominoso", color="dark_aqua", att={"scale": 1.8}),
    "jinete_oseo": dict(eid="skeleton", hp=130, label="Jinete Óseo", color="white", mount="skeleton_horse",
        extra=eq(head="diamond_helmet", chest="iron_chestplate", mainhand=it("bow", power=2))),
    "golem_furioso": dict(eid="iron_golem", hp=140, label="Gólem Furioso", color="gray",
        tags='"so_ev_mob","so_ev_boss","so_ev_golem"'),
    # --- v3
    "archimago": dict(eid="illusioner", hp=140, label="Archimago Espectral", color="dark_blue", att={"scale": 1.4},
        extra=eq(mainhand=it("bow", power=3))),
    "caudillo_bruto": dict(eid="piglin_brute", hp=180, label="Caudillo Bruto", color="gold",
        extra="IsImmuneToZombification:1b," + eq(chest="netherite_chestplate", mainhand=it("golden_axe", sharpness=3))),
    "guardian_oscuro": dict(eid="warden", hp=180, label="Guardián de la Oscuridad", color="dark_aqua",
        att={"attack_damage": 10, "knockback_resistance": 1}, extra=WARDEN_BRAIN),
    "espectro_alfa": dict(eid="phantom", hp=100, label="Espectro Alfa", color="dark_gray", att={"scale": 3},
        extra=FX("fire_resistance")),
    "guardian_anciano": dict(eid="elder_guardian", hp=120, label="Guardián Anciano", color="aqua"),
    "bruja_madre": dict(eid="witch", hp=150, label="Gran Bruja Madre", color="dark_purple", att={"scale": 1.5},
        extra=FX("resistance")),
    "senor_llamas": dict(eid="blaze", hp=160, label="Señor de las Llamas", color="gold", att={"scale": 2.5}),
    "bestia_nether": dict(eid="zoglin", hp=180, label="Bestia del Nether", color="red", att={"scale": 1.8}),
    "invocador": dict(eid="evoker", hp=120, label="Invocador Supremo", color="dark_red", mount="ravager"),
    # --- v4.1: jefe final de la caravana
    "caudillo_saqueador": dict(eid="pillager", hp=160, label="Caudillo Saqueador", color="red", mount="ravager",
        extra=eq(head="iron_helmet", chest="iron_chestplate", mainhand=it("crossbow", piercing=2))),
}
for n, kw in BOSSES.items():
    boss(n, **kw)

# ---------------------------------------------------------------- spawn seguro (radio 6-14; 3-7 junto al OneBlock)
F("lib/spawn", [
    "# $(mob): mob/, boss/ o npc/. Busca suelo con 2 de aire (nunca en el vacío).",
    "scoreboard players set #ok so_ev 0",
    "$data modify storage so_events:tmp mob set value \"$(mob)\"",
    *(["function so_events:lib/spawn_roll", "execute if score #ok so_ev matches 0 run function so_events:lib/spawn_try with storage so_events:tmp"] * 6),
    "execute if score #ok so_ev matches 0 run function so_events:lib/spawn_here with storage so_events:tmp",
])
F("lib/spawn_roll", [
    "execute store result storage so_events:tmp a int 1 run random value 0..359",
    "execute if score #near so_ev matches 1 store result storage so_events:tmp d int 1 run random value 3..7",
    "execute unless score #near so_ev matches 1 store result storage so_events:tmp d int 1 run random value 6..14",
])
F("lib/spawn_try", ["$execute rotated $(a) 0 positioned ^ ^ ^$(d) if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:$(mob)"])
F("lib/spawn_here", [
    "$execute if score #near so_ev matches 1 positioned ~2 ~ ~ run function so_events:$(mob)",
    "$execute unless score #near so_ev matches 1 run function so_events:$(mob)"])

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
    # v3: extra por nivel de invasion
    "reward_t2": [2, [item("iron_ingot", 6, 8, 16), item("gold_ingot", 5, 6, 12), item("diamond", 4, 2, 4), item("emerald", 6, 12, 20)]],
    "reward_t3": [3, [item("diamond", 6, 3, 6), item("emerald", 6, 20, 32), item("netherite_scrap", 3, 1, 2), item("golden_apple", 3, 2, 3),
                      item("enchanted_golden_apple", 1), item("totem_of_undying", 2)]],
    # v3: eventos activos
    "runner": [4, [item("emerald", 8, 8, 16), item("experience_bottle", 8, 8, 16), item("gold_ingot", 3, 4, 8), item("diamond", 1, 1, 2)]],
    # v4: eventos nuevos
    "meteor": [2, [item("iron_ingot", 6, 2, 6), item("gold_ingot", 5, 2, 5), item("coal", 5, 4, 10), item("obsidian", 3, 2, 4),
                   item("emerald", 3, 1, 3), item("experience_bottle", 3, 2, 6), item("diamond", 2)]],
    "gold_fever": [1, [item("gold_nugget", 7, 3, 9), item("gold_ingot", 3, 1, 2), item("raw_gold", 2, 1, 3)]],
    "mimic_treasure": [3, [item("emerald", 6, 6, 14), item("diamond", 5, 2, 5), item("golden_apple", 3, 1, 2),
                           item("netherite_scrap", 2), item("totem_of_undying", 1), item("enchanted_golden_apple", 1)]],
    "caravan": [3, [item("emerald", 6, 6, 14), item("iron_ingot", 5, 6, 12), item("golden_carrot", 4, 4, 8),
                    item("experience_bottle", 4, 4, 10), item("lead", 3, 1, 2), item("diamond", 2, 1, 3), item("name_tag", 2)]],
    "reward_alpha": [3, [item("emerald", 6, 16, 28), item("diamond", 5, 3, 6), item("netherite_scrap", 4, 1, 2),
                         item("totem_of_undying", 3), item("enchanted_golden_apple", 2)]],
}
# v4.1: pools variados (libros, pociones, equipo encantado, rarezas) que se suman a cada tabla.
def book(w, lv):
    return {"type": "minecraft:item", "name": "minecraft:book", "weight": w,
            "functions": [{"function": "minecraft:enchant_with_levels", "levels": lv}]}
def gear(name, w, lv):
    return {"type": "minecraft:item", "name": f"minecraft:{name}", "weight": w,
            "functions": [{"function": "minecraft:enchant_with_levels", "levels": lv}]}
def pot(kind, pid, w, n=1):
    e = {"type": "minecraft:item", "name": f"minecraft:{kind}", "weight": w,
         "functions": [{"function": "minecraft:set_potion", "id": f"minecraft:{pid}"}]}
    if n > 1: e["functions"].append({"function": "minecraft:set_count", "count": {"min": 1, "max": n}})
    return e
POTS = [pot("potion", "strong_strength", 3), pot("potion", "strong_swiftness", 3), pot("potion", "strong_regeneration", 3),
        pot("potion", "long_slow_falling", 2), pot("potion", "strong_turtle_master", 2), pot("potion", "long_fire_resistance", 2),
        pot("splash_potion", "strong_healing", 3, 3), pot("potion", "long_night_vision", 2)]
COMMON = [book(4, 15), *POTS[:3], item("wind_charge", 3, 4, 10), item("ender_pearl", 3, 2, 4), item("firework_rocket", 3, 8, 16),
          item("amethyst_shard", 2, 4, 10), item("glow_berries", 2, 6, 12), item("saddle", 1), item("name_tag", 2),
          item("slime_ball", 2, 3, 8), item("blaze_rod", 2, 2, 5), item("nautilus_shell", 1), item("sponge", 1, 1, 3),
          gear("iron_pickaxe", 2, 15), gear("bow", 2, 15), item("cooked_beef", 2, 8, 16)]
RARE = [book(6, 30), *POTS, item("shulker_shell", 3, 1, 2), item("totem_of_undying", 3), item("heart_of_the_sea", 1),
        item("ender_eye", 3, 2, 6), item("netherite_upgrade_smithing_template", 2), item("trial_key", 2),
        item("breeze_rod", 2, 2, 4), item("echo_shard", 1, 1, 2), item("ancient_debris", 2), item("enchanted_golden_apple", 1),
        gear("diamond_pickaxe", 2, 30), gear("diamond_sword", 2, 30), gear("diamond_chestplate", 2, 30), gear("crossbow", 2, 25),
        *[item(f"{t}_armor_trim_smithing_template", 1) for t in ("sentry", "vex", "wild", "coast", "dune", "ward", "silence", "spire")]]
LOOT["meteor"][1] += [item("crying_obsidian", 4, 2, 6), item("ghast_tear", 2, 1, 2), item("netherite_scrap", 2), item("quartz", 4, 6, 16),
                      item("magma_cream", 3, 2, 6), item("ancient_debris", 1), item("blaze_powder", 3, 2, 6)]
LOOT["caravan"][1] += [item("saddle", 3), item("hay_block", 4, 2, 6), item("golden_apple", 3, 1, 3), item("lead", 2, 2, 4),
                       gear("iron_shovel", 2, 20), gear("iron_axe", 2, 20), item("cake", 2), item("bundle", 2), item("spyglass", 2), item("compass", 2)]
LOOT["mimic_junk"] = [4, [item("rotten_flesh", 8, 4, 12), item("bone", 6, 2, 6), item("dirt", 6, 4, 16), item("spider_eye", 5, 1, 4),
                          item("poisonous_potato", 4, 1, 3), item("stick", 4, 2, 8), item("dead_bush", 3), item("string", 3, 1, 3)]]
LOOT["reward_eclipse"] = [4, [item("netherite_ingot", 3), item("netherite_scrap", 6, 2, 4), item("totem_of_undying", 5), book(6, 30),
                              item("enchanted_golden_apple", 3), item("netherite_upgrade_smithing_template", 3), item("shulker_shell", 4, 2, 4),
                              gear("netherite_sword", 1, 30), gear("diamond_helmet", 3, 30), item("heart_of_the_sea", 2), item("elytra", 1),
                              item("dragon_breath", 2, 2, 4), item("echo_shard", 3, 2, 4)]]
EXTRA = {"rain": (COMMON, 1), "supply": (COMMON, 2), "reward_small": (COMMON, 2), "runner": (COMMON, 2), "meteor": (COMMON, 1),
         "caravan": (COMMON, 2), "reward_big": (RARE, 2), "reward_t2": (RARE, 1), "reward_t3": (RARE, 2),
         "mimic_treasure": (RARE, 3), "reward_alpha": (RARE, 3), "reward_eclipse": (RARE, 3)}
for n, (rolls, entries) in LOOT.items():
    pools = [{"rolls": rolls, "entries": entries}]
    if n in EXTRA: pools.append({"rolls": EXTRA[n][1], "entries": EXTRA[n][0]})
    W(f"data/{NS}/loot_table/{n}.json", {"type": "minecraft:chest", "pools": pools})

# avance invisible que detecta golpes al fugitivo
W(f"data/{NS}/advancement/hit.json", {"criteria": {"hit": {"trigger": "minecraft:player_hurt_entity", "conditions": {"entity": [
    {"condition": "minecraft:entity_properties", "entity": "this", "predicate": {"nbt": "{Tags:[\"so_ev_runner\"]}"}}]}}},
    "rewards": {"function": f"{NS}:hit"}})

# ---------------------------------------------------------------- nucleo
F("load", [
    "scoreboard objectives add so_ev dummy",
    "scoreboard objectives add evento trigger",
    "scoreboard objectives add evento_diario trigger",
    "scoreboard objectives add so_ev_win dummy", "scoreboard objectives add so_ev_inv dummy", "scoreboard objectives add so_ev_pos dummy",
    "execute unless score #streak so_ev matches 0.. run scoreboard players set #streak so_ev 0",
    "execute unless score #alpha_force so_ev matches 0..1 run scoreboard players set #alpha_force so_ev 0",
    "execute unless score #enabled so_ev matches 0..1 run scoreboard players set #enabled so_ev 1",
    "execute unless score #auto so_ev matches 0..1 run scoreboard players set #auto so_ev 1",
    "execute unless score #every so_ev matches 1.. run scoreboard players set #every so_ev 400",
    "execute unless score #min so_ev matches 0.. run scoreboard players set #min so_ev 300",
    "execute unless score #mine_goal so_ev matches 1.. run scoreboard players set #mine_goal so_ev 150",
    "execute unless score #active so_ev matches 0.. run scoreboard players set #active so_ev 0",
    "execute unless score #bless_on so_ev matches 0..1 run scoreboard players set #bless_on so_ev 1",
    "execute unless score #bless_every so_ev matches 1.. run scoreboard players set #bless_every so_ev 200",
    "execute unless score #bless_next so_ev matches 0.. run scoreboard players set #bless_next so_ev 0",
    f"bossbar add {NS}:ev {T({'text': 'Evento'})}",
    f"bossbar add {NS}:boss {T({'text': 'Jefe'})}",
    f"bossbar set {NS}:ev color yellow", f"bossbar set {NS}:boss color red",
    f"tellraw @a[tag=oneblock_admin] {T({'text': '[SO Events] ', 'color': 'gold'}, {'text': 'cargado. Ayuda: /function so_events:admin/help', 'color': 'gray'})}",
])
F("tick", [
    f"execute as @a[scores={{evento=1..}}] run function {NS}:lib/info",
    f"execute as @a[scores={{evento_diario=1..}}] run function {NS}:lib/diary",
    "scoreboard players reset @a evento", "scoreboard players enable @a evento",
    "scoreboard players reset @a evento_diario", "scoreboard players enable @a evento_diario",
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
    f"execute if score #enabled so_ev matches 1 if score #bless_on so_ev matches 1 run function {NS}:bless/check",
    f"execute if score #active so_ev matches 1 run function {NS}:event/rain/second",
    f"execute if score #active so_ev matches 3 run function {NS}:event/mining/second",
    f"execute if score #active so_ev matches 4 run function {NS}:event/trader/second",
    f"execute if score #active so_ev matches 5 run function {NS}:event/invasion/second",
    f"execute if score #active so_ev matches 6 run function {NS}:event/dark/second",
    f"execute if score #active so_ev matches 7 run function {NS}:event/runner/second",
    f"execute if score #active so_ev matches 8 run function {NS}:event/mana/second",
    f"execute if score #active so_ev matches 9 run function {NS}:event/altar/second",
    f"execute if score #active so_ev matches 10 run function {NS}:event/meteor/second",
    f"execute if score #active so_ev matches 11 run function {NS}:event/gold/second",
    f"execute if score #active so_ev matches 12 run function {NS}:event/mimic/second",
    f"execute if score #active so_ev matches 13 run function {NS}:event/caravan/second",
    f"execute if score #active so_ev matches 14 run function {NS}:event/eclipse/second",
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
    "execute store result score #r so_ev run random value 1..14",
    "# Noche oscura desde la fase 5 (1668 bloques); eclipse solo post-Nether (9000 bloques).",
    "execute if score #r so_ev matches 6 if score #blk so_ev matches ..1667 run scoreboard players set #r so_ev 1",
    "execute if score #r so_ev matches 14 if score #blk so_ev matches ..8999 run scoreboard players set #r so_ev 2",
    f"execute if score #r so_ev matches 1 run function {NS}:event/rain/start",
    f"execute if score #r so_ev matches 2 run function {NS}:event/supply/start",
    f"execute if score #r so_ev matches 3 run function {NS}:event/mining/start",
    f"execute if score #r so_ev matches 4 run function {NS}:event/trader/start",
    f"execute if score #r so_ev matches 5 run function {NS}:event/invasion/start",
    f"execute if score #r so_ev matches 6 run function {NS}:event/dark/start",
    f"execute if score #r so_ev matches 7 run function {NS}:event/runner/start",
    f"execute if score #r so_ev matches 8 run function {NS}:event/mana/start",
    f"execute if score #r so_ev matches 9 run function {NS}:event/altar/start",
    f"execute if score #r so_ev matches 10 run function {NS}:event/meteor/start",
    f"execute if score #r so_ev matches 11 run function {NS}:event/gold/start",
    f"execute if score #r so_ev matches 12 run function {NS}:event/mimic/start",
    f"execute if score #r so_ev matches 13 run function {NS}:event/caravan/start",
    f"execute if score #r so_ev matches 14 run function {NS}:event/eclipse/start",
])
F("lib/begin", [
    "# Comun a todo evento: participantes, alerta, temporizador y nivel (1 <5000, 2 <10000, 3 desde 10000).",
    "tag @a remove so_ev_in", NEAR,
    "scoreboard players set #t so_ev 0",
    "scoreboard players set #tier so_ev 1",
    "execute if score #blk so_ev matches 5000.. run scoreboard players set #tier so_ev 2",
    "execute if score #blk so_ev matches 10000.. run scoreboard players set #tier so_ev 3",
    f"bossbar set {NS}:ev players {IN}", f"bossbar set {NS}:ev visible true",
    "playsound minecraft:block.bell.use master @a ~ ~ ~ 1 0.8",
])
F("lib/tier_up", [
    "# Refuerza a los mobs nuevos del evento segun #tier (vida, daño, armadura, velocidad).",
    "tag @e[tag=so_ev_mob,tag=!so_ev_t] add so_ev_tn",
    "execute if score #tier so_ev matches 2 as @e[tag=so_ev_tn] run function so_events:lib/tier_2",
    "execute if score #tier so_ev matches 3.. as @e[tag=so_ev_tn] run function so_events:lib/tier_3",
    "execute if score #tier so_ev matches 2.. as @e[tag=so_ev_tn,tag=so_ev_boss,limit=1] store result bossbar so_events:boss max run attribute @s minecraft:max_health get",
    "tag @e[tag=so_ev_tn] add so_ev_t", "tag @e[tag=so_ev_tn] remove so_ev_tn",
])
for lv, (hp, dmg, arm, tough, spd) in {2: (0.5, 0.3, 4, 0, 0.1), 3: (1.0, 0.6, 8, 4, 0.15)}.items():
    F(f"lib/tier_{lv}", [
        f"attribute @s minecraft:max_health modifier add so_events:tier {hp} add_multiplied_base",
        f"attribute @s minecraft:attack_damage modifier add so_events:tier {dmg} add_multiplied_base",
        f"attribute @s minecraft:armor modifier add so_events:tier {arm} add_value",
        *([f"attribute @s minecraft:armor_toughness modifier add so_events:tier {tough} add_value"] if tough else []),
        f"attribute @s minecraft:movement_speed modifier add so_events:tier {spd} add_multiplied_base",
        "data modify entity @s Health set value 4096f",
    ])
F("lib/cleanup", [
    "# Limpieza total: mobs al vacío (sin drops), barras, marcas y regla de griefing.",
    "tp @e[tag=so_ev_mob] 0 -300 0", "kill @e[tag=so_ev_mob]",
    "kill @e[tag=so_ev_altar]", "kill @e[tag=so_ev_mimic]", "kill @e[tag=so_ev_llama]",
    "scoreboard players set #alpha so_ev 0", "scoreboard players set #mimic so_ev 0",
    f"bossbar set {NS}:ev visible false", f"bossbar set {NS}:boss visible false",
    "execute if score #mg_saved so_ev matches 1 if score #mg_prev so_ev matches 1 run gamerule mob_griefing true",
    "scoreboard players set #mg_saved so_ev 0",
    "effect clear @a[tag=so_ev_in] minecraft:darkness",
    "tag @a remove so_ev_in",
    "scoreboard players set #active so_ev 0", "scoreboard players set #t so_ev 0",
    "scoreboard players set #stage so_ev 0", "scoreboard players set #wave so_ev 0",
    "scoreboard players set #hits so_ev 0", "scoreboard players set #paid so_ev 0",
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
    f"execute if score #active so_ev matches 7 run tellraw @s {T(PFX, {'text': 'Caza del fugitivo: golpes ', 'color': 'gold', 'bold': False}, {'score': {'name': '#hits', 'objective': 'so_ev'}, 'color': 'white'}, {'text': '/5', 'color': 'gray'})}",
    f"execute if score #active so_ev matches 8 run tellraw @s {T(PFX, {'text': 'Tormenta de maná: juntá los orbes.', 'color': 'aqua', 'bold': False})}",
    f"execute if score #active so_ev matches 9 run tellraw @s {T(PFX, {'text': 'Altar: tributo ', 'color': 'yellow', 'bold': False}, {'score': {'name': '#paid', 'objective': 'so_ev'}, 'color': 'white'}, {'text': '/32 (piedra o troncos)', 'color': 'gray'})}",
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
    "scoreboard players add @a[tag=so_ev_in] so_ev_win 1", "scoreboard players add @a[tag=so_ev_in] so_ev_pos 1",
    f"function {NS}:lib/streak_up",
    say("@a", "¡Desafío superado! Recompensa entregada a los participantes.", "green"),
    "execute as @a[tag=so_ev_in] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1", f"function {NS}:lib/cleanup"])
F("event/mining/fail", [f"function {NS}:lib/streak_reset", say("@a", "Se acabó el tiempo del desafío de minería.", "gray"), f"function {NS}:lib/cleanup"])

# ---------------------------------------------------------------- 4 mercaderes especiales (5 min, junto al OneBlock)
def sell_raw(raw, buy, bc, uses):
    return f'{{buy:{{id:"minecraft:{buy}",count:{bc}}},sell:{raw},maxUses:{uses}}}'
def offer(buy, bc, sell, sc, uses):
    return sell_raw(f'{{id:"minecraft:{sell}",count:{sc}}}', buy, bc, uses)
def potion(p, price, uses=3):
    return sell_raw(f'{{id:"minecraft:splash_potion",count:1,components:{{"minecraft:potion_contents":{{potion:"minecraft:{p}"}}}}}}', "emerald", price, uses)

# 1 Misterioso: catalogo fijo (v1)
FIXED = ",".join([offer("emerald", 10, "diamond", 1, 4), offer("emerald", 6, "golden_apple", 1, 3), offer("emerald", 4, "ender_pearl", 2, 4),
                  offer("emerald", 8, "experience_bottle", 16, 3), offer("emerald", 16, "netherite_scrap", 1, 1), offer("emerald", 12, "heart_of_the_sea", 1, 1),
                  offer("diamond", 2, "emerald", 24, 4), offer("emerald", 20, "totem_of_undying", 1, 1)])
# pools: se eligen 8 al azar sin repetir
POOLS = {
    "alq": [potion(p, c) for p, c in [("healing", 4), ("strong_healing", 7), ("regeneration", 6), ("strong_regeneration", 9), ("swiftness", 4),
            ("strong_swiftness", 6), ("strength", 6), ("strong_strength", 9), ("fire_resistance", 6), ("night_vision", 4), ("leaping", 4),
            ("invisibility", 6), ("slow_falling", 5), ("water_breathing", 5), ("turtle_master", 8), ("harming", 5), ("strong_harming", 8),
            ("poison", 4), ("strong_poison", 6), ("weakness", 4), ("slowness", 4), ("infested", 5), ("oozing", 5), ("weaving", 5), ("wind_charged", 5)]],
    "arm": [offer("emerald", 24, "netherite_upgrade_smithing_template", 1, 1)] +
           [offer("emerald", c, f"{t}_armor_trim_smithing_template", 1, 1) for t, c in [("sentry", 10), ("dune", 10), ("coast", 10), ("wild", 10),
            ("ward", 14), ("eye", 14), ("vex", 14), ("tide", 10), ("snout", 12), ("rib", 12), ("spire", 14), ("wayfinder", 10), ("shaper", 10),
            ("silence", 18), ("raiser", 10), ("host", 10), ("flow", 12), ("bolt", 12)]],
    "min": [offer("emerald", 12, "diamond", 1, 4), offer("emerald", 15, "netherite_scrap", 1, 2), offer("emerald", 29, "netherite_ingot", 1, 1),
            offer("emerald", 6, "iron_ingot", 8, 4), offer("emerald", 8, "gold_ingot", 8, 4), offer("emerald", 5, "redstone", 32, 4),
            offer("emerald", 5, "lapis_lazuli", 16, 4), offer("emerald", 4, "coal", 32, 4), offer("emerald", 4, "copper_ingot", 16, 4),
            offer("emerald", 4, "quartz", 8, 4), offer("emerald", 5, "amethyst_shard", 8, 4), offer("emerald", 46, "diamond", 4, 1)],
}
TRADERS = {  # tipo: (nombre, color, pool)
    1: ("Mercader Misterioso", "aqua", None),
    2: ("Alquimista Errante", "light_purple", "alq"),
    3: ("Armero de la Corte", "gold", "arm"),
    4: ("Minero Ambulante", "gray", "min"),
}
F("load_offers", [f"data modify storage {NS}:offers {k} set value [{','.join(v)}]" for k, v in POOLS.items()])
for k, (label, color, pool) in TRADERS.items():
    rec = FIXED if pool is None else ""
    lines = [f'summon minecraft:wandering_trader ~ ~ ~ {{Tags:["so_ev_mob","so_ev_new"],Invulnerable:1b,NoAI:1b,PersistenceRequired:1b,CustomNameVisible:1b,'
             f'CustomName:{{text:"{label}",color:"{color}",bold:true}},Offers:{{Recipes:[{rec}]}}}}', "scoreboard players set #ok so_ev 1"]
    if pool:
        lines += [f"data modify storage {NS}:tmp pool set from storage {NS}:offers {pool}"] + [f"function {NS}:lib/offer_pick"] * 8
    lines += ["particle minecraft:happy_villager ~ ~1 ~ 0.5 1 0.5 0 20", "tag @e[tag=so_ev_new] remove so_ev_new"]
    F(f"npc/trader_{k}", lines)
F("lib/offer_pick", [f"execute store result score #len so_ev run data get storage {NS}:tmp pool",
    "scoreboard players remove #len so_ev 1",
    f"execute if score #len so_ev matches 1.. store result storage {NS}:tmp max int 1 run scoreboard players get #len so_ev",
    f"execute if score #len so_ev matches 1.. run function {NS}:lib/offer_take with storage {NS}:tmp"])
F("lib/offer_take", [f"$execute store result storage {NS}:tmp i int 1 run random value 0..$(max)",
    f"function {NS}:lib/offer_move with storage {NS}:tmp"])
F("lib/offer_move", [f"$data modify entity @e[tag=so_ev_new,limit=1] Offers.Recipes append from storage {NS}:tmp pool[$(i)]",
    f"$data remove storage {NS}:tmp pool[$(i)]"])

F("event/trader/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 4",
    f"execute store result score #ttype so_ev run random value 1..{len(TRADERS)}",
    f"execute if score #force_trader so_ev matches 1..{len(TRADERS)} run scoreboard players operation #ttype so_ev = #force_trader so_ev",
    "scoreboard players set #force_trader so_ev 0",
    f"bossbar set {NS}:ev max 300", f"bossbar set {NS}:ev color blue",
    *[f"execute if score #ttype so_ev matches {k} run bossbar set {NS}:ev name {T({'text': v[0], 'color': v[1]})}" for k, v in TRADERS.items()],
    "scoreboard players set #near so_ev 1",
    *[f'execute if score #ttype so_ev matches {k} in minecraft:overworld positioned 0 65 0 run function {NS}:lib/spawn {{mob:"npc/trader_{k}"}}' for k in TRADERS],
    "scoreboard players set #near so_ev 0",
    *[f"execute if score #ttype so_ev matches {k} run tellraw @a {T(PFX, {'text': v[0], 'color': v[1], 'bold': True}, {'text': ' llegó junto al OneBlock por 5 minutos.', 'color': 'aqua', 'bold': False})}" for k, v in TRADERS.items()]])
F("event/trader/second", ["scoreboard players add #t so_ev 1",
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    f"execute if score #t so_ev matches 300.. run tellraw @a {T(PFX, {'text': 'El mercader se fue.', 'color': 'gray', 'bold': False})}",
    f"execute if score #t so_ev matches 300.. run function {NS}:lib/cleanup"])

# ---------------------------------------------------------------- 5 invasion: cuenta atras, 3 oleadas, jefe(s) + escoltas
INV = {  # tipo: (nombre, color, oleadas, etapa final, bloques minimos)
    1: ("Horda de zombis", "dark_green", [["husk", "zombie", "zombie_villager"], ["husk", "zombie", "zombie", "baby_zombie", "drowned"],
        ["zombie", "husk", "zombie_armor", "baby_zombie", "zombie_villager", "zombie_horseman"]],
        ["boss/rey_zombi", "boss/zombi_gigante", "mob/chicken_jockey", "mob/chicken_jockey"], 0),
    2: ("Ataque de slimes", "green", [["slime", "slime", "slime_mini", "slime_mini"], ["slime", "slime_big", "slime_mini", "slime_mini"],
        ["slime_big", "slime_big", "slime", "slime_mini", "slime_mini"]], ["boss/slime_rey"], 0),
    3: ("Oleada acorazada", "gray", [["zombie_armor", "skeleton", "zombie_armor"], ["zombie_armor", "skeleton_armor", "spider", "skeleton"],
        ["zombie_armor", "zombie_armor", "skeleton_armor", "skeleton_armor", "spider", "witch", "witch", "enderman", "creeper", "creeper"]],
        ["boss/comandante", "mob/zombie_escort", "mob/zombie_escort"], 2501),
    4: ("Raid de saqueadores", "dark_red", [["pillager", "pillager", "pillager"], ["pillager", "pillager", "vindicator", "vindicator"],
        ["vindicator", "pillager", "vindicator", "pillager", "vindicator"]], ["boss/capitan", "boss/devastador", "mob/witch"], 2501),
    5: ("Invasión del Nether", "dark_purple", [["magma_cube", "blaze", "piglin"], ["blaze", "wither_skeleton", "piglin", "piglin_crossbow"],
        ["wither_skeleton", "blaze", "magma_cube", "piglin", "piglin"]], ["boss/caballero", "boss/piglin_bruto"], 6667),
    6: ("Invasión del End", "light_purple", [["enderman", "endermite", "endermite"], ["enderman", "enderman", "endermite", "shulker"],
        ["enderman", "enderman", "shulker", "endermite", "endermite"]], ["boss/senor_end"], 10000),
    7: ("Plaga de artrópodos", "dark_red", [["spider", "cave_spider", "cave_spider"], ["spider_big", "spider", "cave_spider", "spider_jockey"],
        ["spider_big", "spider_big", "cave_spider", "cave_spider", "spider_jockey"]], ["boss/arana_colosal"], 1500),
    8: ("Asedio marino", "aqua", [["drowned", "drowned", "drowned_trident"], ["drowned", "drowned_trident", "drowned_trident", "drowned"],
        ["drowned_trident", "drowned_trident", "drowned", "drowned", "drowned_trident"]], ["boss/guardian_abismo"] * 3, 4000),
    9: ("Prueba ominosa", "dark_aqua", [["zombie_ominous", "bogged", "breeze"], ["skeleton_ominous", "zombie_ominous", "breeze", "bogged"],
        ["breeze", "breeze", "zombie_ominous", "skeleton_ominous", "bogged"]], ["boss/heraldo_ominoso", "mob/breeze"], 5000),
    10: ("Tormenta de huesos", "white", [["skeleton", "stray", "bogged"], ["skeleton", "stray", "bogged", "wither_skeleton"],
        ["skeleton_horseman", "skeleton_horseman", "stray", "bogged", "wither_skeleton"]], ["boss/jinete_oseo"], 2501),
    11: ("Rebelión de gólems", "gray", [["iron_golem"], ["iron_golem"], ["iron_golem"]], ["boss/golem_furioso"] * 3, 5000),
    12: ("Ilusionismo oscuro", "dark_aqua", [["illusioner", "vex", "vex"], ["illusioner", "evoker", "vex", "vex"],
        ["evoker", "evoker", "illusioner", "vex", "vex"]], ["boss/archimago", "mob/vex"], 8000),
    13: ("Asalto del Bastión", "gold", [["piglin_brute", "zombified_piglin"], ["piglin_brute", "piglin_brute", "zoglin"],
        ["piglin_brute", "piglin_brute", "zoglin", "zombified_piglin", "zombified_piglin"]], ["boss/caudillo_bruto", "mob/piglin_brute"], 9500),
    14: ("Caza del Warden", "dark_blue", [["sombra", "acechador"], ["sombra", "sombra", "acechador"],
        ["sombra", "sombra", "acechador", "acechador"]], ["boss/guardian_oscuro"], 12000),
    15: ("Enjambre del cielo", "dark_gray", [["phantom", "phantom"], ["phantom", "phantom_big", "bat_bomber"],
        ["phantom_big", "phantom", "bat_bomber", "bat_bomber", "phantom"]], ["boss/espectro_alfa", "mob/phantom_big"], 7000),
    16: ("Marea anciana", "aqua", [["drowned_trident", "drowned", "drowned"], ["drowned_trident", "drowned_trident", "drowned", "drowned"],
        ["drowned_trident", "drowned_trident", "drowned", "drowned", "drowned"]], ["boss/guardian_anciano", "boss/guardian_anciano", "mob/drowned_trident"], 9000),
    17: ("Aquelarre de brujas", "dark_purple", [["witch", "witch"], ["witch", "witch", "creeper"],
        ["witch", "witch", "witch", "creeper", "creeper"]], ["boss/bruja_madre", "mob/witch", "mob/witch"], 3500),
    18: ("Furia de llamas", "red", [["blaze_fast", "magma_cube"], ["blaze_fast", "blaze_fast", "magma_cube"],
        ["blaze_fast", "blaze_fast", "magma_cube", "magma_cube", "blaze_fast"]], ["boss/senor_llamas", "mob/blaze_fast"], 11000),
    19: ("Horda zombificada", "dark_green", [["zombified_piglin", "zombified_piglin"], ["zombified_piglin", "zoglin", "zombified_piglin"],
        ["zoglin", "zoglin", "zombified_piglin", "zombified_piglin", "zombified_piglin"]], ["boss/bestia_nether", "mob/zoglin", "mob/zoglin"], 8500),
    20: ("Vanguardia del Mal", "dark_red", [["vindicator", "pillager", "pillager"], ["vindicator", "vindicator", "evoker", "ravager"],
        ["vindicator", "vindicator", "evoker", "evoker", "ravager"]], ["boss/invocador", "mob/vindicator", "mob/vindicator"], 13000),
}
TIER = {1: "", 2: " [Nivel II]", 3: " [Nivel III]"}
N = len(INV)
F("event/invasion/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 5",
    "execute if score #force_tier so_ev matches 1..3 run scoreboard players operation #tier so_ev = #force_tier so_ev",
    "scoreboard players set #force_tier so_ev 0",
    "scoreboard players set #stage so_ev 0", "scoreboard players set #wave so_ev 0", f"function {NS}:lib/no_grief",
    f"execute unless score #force_type so_ev matches 1..{N} run function so_events:event/invasion/pick",
    f"execute if score #force_type so_ev matches 1..{N} run scoreboard players operation #type so_ev = #force_type so_ev",
    "scoreboard players set #force_type so_ev 0",
    "# Invasión alfa: 10% de chance (o forzada por admin).",
    "execute store result score #alpha so_ev run random value 1..10",
    "execute if score #alpha_force so_ev matches 1 run scoreboard players set #alpha so_ev 1",
    "execute if score #alpha so_ev matches 2.. run scoreboard players set #alpha so_ev 0",
    f"bossbar set {NS}:ev color red", f"bossbar set {NS}:ev max 10",
    *[f"execute if score #type so_ev matches {k} if score #tier so_ev matches {t} run bossbar set {NS}:ev name {T({'text': '¡' + v[0] + '!' + ts, 'color': v[1], 'bold': True})}" for k, v in INV.items() for t, ts in TIER.items()],
    *[f"execute if score #type so_ev matches {k} if score #tier so_ev matches {t} run tellraw @a {T(PFX, {'text': '¡ALERTA! ' + v[0] + ts + ' en 10 segundos. Defiendan la isla.', 'color': 'red', 'bold': True})}" for k, v in INV.items() for t, ts in TIER.items()],
    f"execute if score #tier so_ev matches 2.. run tellraw @a {T(PFX, {'text': 'La isla ya es fuerte: los invasores vienen reforzados y la recompensa es mayor.', 'color': 'gold', 'bold': False})}",
    "playsound minecraft:event.raid.horn master @a ~ ~ ~ 1 1"])
F("event/invasion/pick", ["# Elige al azar entre los tipos ya desbloqueados por bloques minados.",
    "scoreboard players set #tries so_ev 0", f"function {NS}:event/invasion/pick_try"])
F("event/invasion/pick_try", ["scoreboard players add #tries so_ev 1",
    f"execute store result score #type so_ev run random value 1..{N}",
    "scoreboard players set #ok so_ev 1",
    *[f"execute if score #type so_ev matches {k} unless score #blk so_ev matches {v[4]}.. run scoreboard players set #ok so_ev 0" for k, v in INV.items() if v[4] > 0],
    f"execute if score #ok so_ev matches 0 if score #tries so_ev matches ..40 run function {NS}:event/invasion/pick_try",
    "execute if score #ok so_ev matches 0 run scoreboard players set #type so_ev 1"])
F("event/invasion/second", ["scoreboard players add #t so_ev 1", NEAR, f"bossbar set {NS}:ev players {IN}",
    f"execute if score #stage so_ev matches 0 run function {NS}:event/invasion/countdown",
    f"execute if score #stage so_ev matches 1 run function {NS}:event/invasion/waves",
    f"execute if score #stage so_ev matches 2 unless entity @e[tag=so_ev_boss] run function {NS}:event/invasion/win",
    "# Golems enfurecidos: un roce minimo atribuido al jugador mas cercano los vuelve hostiles.",
    "scoreboard players operation #m so_ev = #t so_ev", "scoreboard players operation #m so_ev %= #five so_ev",
    f"execute if score #m so_ev matches 0 as @e[tag=so_ev_golem] at @s if entity {IN.replace(']', ',distance=..32]')} run damage @s 0.01 minecraft:player_attack by @p[tag=so_ev_in]",
    "# Warden: se renueva el bloqueo de excavación y un golpe real del jugador más cercano le sube la ira al tope.",
    f"execute as @e[tag=so_ev_boss,type=minecraft:warden] run function {NS}:lib/warden_keep",
    f"execute if score #m so_ev matches 0 as @e[tag=so_ev_boss,type=minecraft:warden] at @s if entity @a[tag=so_ev_in,distance=..48] run damage @s 0.1 minecraft:player_attack by @p[tag=so_ev_in]",
    "# Invasión alfa: aura del jefe.",
    "execute if score #alpha so_ev matches 1 as @e[tag=so_ev_boss] at @s run particle minecraft:soul_fire_flame ~ ~1 ~ 0.4 0.6 0.4 0.02 12",
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
    "# Nivel III: la oleada final suma la primera como refuerzo.",
    *[f"execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches {k} run function {NS}:event/invasion/w_{k}_1" for k in INV],
    f"function {NS}:lib/tier_up",
    f"execute if score #wave so_ev matches 1..3 run title {IN} title {T({'text': 'Oleada ', 'color': 'red', 'bold': True}, {'score': {'name': '#wave', 'objective': 'so_ev'}, 'color': 'white'})}",
    "execute if score #wave so_ev matches 1..3 run playsound minecraft:entity.zombie.ambient hostile @a[tag=so_ev_in] ~ ~ ~ 1 0.7"])
for k, v in INV.items():
    for w, mobs in enumerate(v[2], 1):
        F(f"event/invasion/w_{k}_{w}", [spawn(m) for m in mobs])
    F(f"event/invasion/boss_{k}", [f'execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function {NS}:lib/spawn {{mob:"{e}"}}' for e in v[3]])
F("event/invasion/waves", [
    "scoreboard players add #wt so_ev 1",
    "execute store result score #alive so_ev if entity @e[tag=so_ev_mob]",
    f"title {IN} actionbar {T({'text': 'Enemigos restantes: ', 'color': 'red'}, {'score': {'name': '#alive', 'objective': 'so_ev'}, 'color': 'white', 'bold': True})}",
    f"execute if score #alive so_ev matches 0 if score #wt so_ev matches 3.. run function {NS}:event/invasion/next",
    f"execute if score #wt so_ev matches 90.. run function {NS}:event/invasion/next"])
F("event/invasion/boss", ["scoreboard players set #stage so_ev 2",
    *[f"execute if score #type so_ev matches {k} run function {NS}:event/invasion/boss_{k}" for k in INV],
    f"function {NS}:lib/tier_up",
    "# Versión alfa: jefe con aura, refuerzos de la primera oleada y anuncio especial.",
    *[f"execute if score #alpha so_ev matches 1 if score #type so_ev matches {k} run function {NS}:event/invasion/w_{k}_1" for k in INV],
    "execute if score #alpha so_ev matches 1 run function so_events:lib/tier_up",
    "execute if score #alpha so_ev matches 1 as @e[tag=so_ev_boss] run effect give @s minecraft:resistance infinite 1 true",
    "execute if score #alpha so_ev matches 1 as @e[tag=so_ev_boss] run effect give @s minecraft:strength infinite 0 true",
    f"execute if score #alpha so_ev matches 1 run title {IN} title {T({'text': '¡JEFE ALFA!', 'color': 'dark_purple', 'bold': True})}",
    f"execute if score #alpha so_ev matches 1 run tellraw @a {T(PFX, {'text': '¡Es una invasión ALFA! El jefe viene con aura y refuerzos; la recompensa es mucho mayor.', 'color': 'dark_purple', 'bold': True})}",
    f"execute unless score #alpha so_ev matches 1 run title {IN} title {T({'text': '¡JEFE INVASOR!', 'color': 'dark_red', 'bold': True})}"])
F("event/invasion/win", [f"execute as {IN} run loot give @s loot {NS}:reward_big",
    f"execute if score #tier so_ev matches 2 as {IN} run loot give @s loot {NS}:reward_t2",
    f"execute if score #tier so_ev matches 3.. as {IN} run loot give @s loot {NS}:reward_t3",
    f"execute if score #alpha so_ev matches 1 as {IN} run loot give @s loot {NS}:reward_alpha",
    "scoreboard players add @a[tag=so_ev_in] so_ev_win 1", "scoreboard players add @a[tag=so_ev_in] so_ev_inv 1",
    f"function {NS}:lib/streak_up",
    say("@a", "¡Invasión derrotada! Cada defensor recibió su recompensa.", "green"),
    f"title {IN} title {T({'text': '¡Victoria!', 'color': 'green', 'bold': True})}",
    "execute as @a[tag=so_ev_in] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1", f"function {NS}:lib/cleanup"])
F("event/invasion/fail", [f"function {NS}:lib/streak_reset",
    say("@a", "La invasión se retiró sin vencedores. No hubo recompensa.", "gray"), f"function {NS}:lib/cleanup"])

# ---------------------------------------------------------------- 6 noche oscura (90 s): oleadas de 5, final de 10
DARK = ["zombie", "skeleton", "spider", "witch", "blaze"]
F("event/dark/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 6", f"function {NS}:lib/no_grief",
    f"bossbar set {NS}:ev name {T({'text': 'Noche oscura', 'color': 'dark_purple'})}", f"bossbar set {NS}:ev max 90", f"bossbar set {NS}:ev color purple",
    f"title {IN} title {T({'text': 'Noche oscura', 'color': 'dark_purple', 'bold': True})}",
    say("@a", "La oscuridad cubre la plataforma. Sobrevivan 90 segundos.", "dark_purple")])
F("event/dark/second", ["scoreboard players add #t so_ev 1", NEAR,
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    f"effect give {IN} minecraft:darkness 3 0 true",
    "scoreboard players operation #m so_ev = #t so_ev", "scoreboard players operation #m so_ev %= #twenty so_ev",
    f"execute if score #m so_ev matches 1 if score #t so_ev matches ..80 run function {NS}:event/dark/spawn",
    f"execute if score #t so_ev matches 81 run function {NS}:event/dark/final",
    f"execute if score #t so_ev matches 90.. run function {NS}:event/dark/end"])
F("event/dark/spawn", [spawn(m) for m in DARK] + [f"function {NS}:lib/tier_up"])
F("event/dark/final", [*[spawn(m) for m in DARK for _ in (0, 1)], f"function {NS}:lib/tier_up",
    f"title {IN} title {T({'text': '¡Oleada final!', 'color': 'dark_purple', 'bold': True})}"])
F("event/dark/end", [f"execute as {IN} run loot give @s loot {NS}:reward_small",
    "scoreboard players add @a[tag=so_ev_in] so_ev_win 1", "scoreboard players add @a[tag=so_ev_in] so_ev_inv 1",
    f"function {NS}:lib/streak_up",
    say("@a", "Amaneció. Los sobrevivientes recibieron una recompensa.", "green"), f"function {NS}:lib/cleanup"])
# ---------------------------------------------------------------- v3: bendiciones del bloque (cada 200 bloques)
BLESS = [
    ("prisa_minera", "haste", 9, 300, "Prisa Minera X", "5 minutos", "gold"),
    ("regeneracion", "regeneration", 2, 60, "Regeneración III", "60 segundos", "light_purple"),
    ("fuerza", "strength", 4, 60, "Fuerza V", "60 segundos", "red"),
    ("velocidad", "speed", 1, 120, "Velocidad II", "2 minutos", "aqua"),
    ("absorcion", "absorption", 8, 180, "Absorción IX", "3 minutos", "yellow"),
]
F("bless/check", [
    "# Se activa cuando los bloques minados avanzan #bless_every (200) desde #bless_next.",
    "execute positioned 0 64 0 store result score #n so_ev if entity @a[distance=..64,gamemode=!spectator]",
    "execute if score #n so_ev matches 0 run return 0",
    "scoreboard players operation #diff so_ev = #blk so_ev",
    "scoreboard players operation #diff so_ev -= #bless_next so_ev",
    "execute if score #diff so_ev matches ..-1 run scoreboard players operation #bless_next so_ev = #blk so_ev",
    "execute if score #diff so_ev matches ..-1 run return 0",
    "execute if score #diff so_ev matches 200.. run scoreboard players operation #bless_next so_ev = #blk so_ev",
    f"execute if score #diff so_ev matches 200.. run execute store result score #r so_ev run random value 1..{len(BLESS)}",
    f"execute if score #diff so_ev matches 200.. run function {NS}:admin/bless",
])
F("admin/bless", [
    f"execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run function {NS}:bless/give",
    say("@s", "Bendición entregada a la isla.", "green"),
])
F("bless/give", [
    *[f'execute if score #r so_ev matches {i} run effect give @s minecraft:{fx} {dur} {amp} true'
      for i, (_, fx, amp, dur, _, _, _) in enumerate(BLESS, 1)],
    f'execute if score #r so_ev matches ..0 run effect give @s minecraft:haste 300 9 true',
    *[f'execute if score #r so_ev matches {i} run title @s actionbar {T(PFX, {"text": "Bendición: " + n, "color": c, "bold": True}, {"text": " (" + d + ")", "color": "gray"})}'
      for i, (_, _, _, _, n, d, c) in enumerate(BLESS, 1)],
    f'execute if score #r so_ev matches ..0 run title @s actionbar {T(PFX, {"text": "Bendición: Prisa Minera X", "color": "gold", "bold": True}, {"text": " (5 minutos)", "color": "gray"})}',
    "playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.6",
    "particle minecraft:end_rod ~ ~1 ~ 0.4 0.6 0.4 0.03 20",
])

# ---------------------------------------------------------------- v3: caza del fugitivo (60 s, 5 golpes)
F("event/runner/start", [
    f"function {NS}:lib/begin", "scoreboard players set #active so_ev 7", "scoreboard players set #hits so_ev 0",
    f'bossbar set {NS}:ev name {T({"text": "Caza del fugitivo", "color": "gold"})}',
    f"bossbar set {NS}:ev max 60", f"bossbar set {NS}:ev color yellow",
    "execute store result score #kind so_ev run random value 1..2",
    f'execute if score #kind so_ev matches 1 as @a[tag=so_ev_in,limit=1,sort=random] at @s run summon minecraft:chicken ~ ~ ~ {{Tags:["so_ev_mob","so_ev_runner"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{{text:"Pollo Dorado",color:"gold",bold:true}},active_effects:[{{id:"minecraft:speed",amplifier:1b,duration:-1,show_particles:1b}}],attributes:[{{id:"minecraft:movement_speed",base:0.42}}]}}',
    f'execute if score #kind so_ev matches 2 as @a[tag=so_ev_in,limit=1,sort=random] at @s run summon minecraft:fox ~ ~ ~ {{Tags:["so_ev_mob","so_ev_runner"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{{text:"Zorro Místico",color:"light_purple",bold:true}},active_effects:[{{id:"minecraft:speed",amplifier:1b,duration:-1,show_particles:1b}}],attributes:[{{id:"minecraft:movement_speed",base:0.6}}]}}',
    *[f"execute if score #kind so_ev matches {k} run tellraw @a {T(PFX, {'text': ('¡El Pollo Dorado apareció!' if k == 1 else '¡El Zorro Místico apareció!') + ' Golpeenlo 5 veces en 60 segundos.', 'color': 'gold', 'bold': True})}" for k in (1, 2)],
    "execute as @e[tag=so_ev_runner,limit=1] at @s run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 1 1.6",
])
F("event/runner/second", [
    "scoreboard players add #t so_ev 1",
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    f"execute as @e[tag=so_ev_runner,limit=1] at @s run particle minecraft:end_rod ~ ~0.5 ~ 0.2 0.2 0.2 0.02 6",
    f"execute as @e[tag=so_ev_runner,limit=1] at @s run title @a[tag=so_ev_in,distance=..40] actionbar {T({'text': 'Golpes: ', 'color': 'gold'}, {'score': {'name': '#hits', 'objective': 'so_ev'}, 'color': 'white', 'bold': True}, {'text': '/5', 'color': 'gray'})}",
    f"execute unless entity @e[tag=so_ev_runner] run function {NS}:event/runner/fail",
    f"execute if score #t so_ev matches 60.. run function {NS}:event/runner/fail",
])
F("hit", [
    f"advancement revoke @s only {NS}:hit",
    "scoreboard players add #hits so_ev 1",
    f'execute if score #hits so_ev matches 5.. run function {NS}:event/runner/win',
    f'execute unless score #hits so_ev matches 5.. run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.2',
])
F("event/runner/win", [
    f"execute as @e[tag=so_ev_runner,limit=1] at @s run loot spawn ~ ~ ~ loot {NS}:runner",
    f"execute as @e[tag=so_ev_runner,limit=1] at @s run particle minecraft:firework ~ ~0.5 ~ 0.3 0.3 0.3 0.1 60",
    f'title {IN} title {T({"text": "¡Atraparon al fugitivo!", "color": "gold", "bold": True})}',
    say("@a", "¡El fugitivo cayó! Esmeraldas, botellas de XP y oro en el piso.", "gold"),
    "kill @e[tag=so_ev_runner]",
    "scoreboard players add @a[tag=so_ev_in] so_ev_win 1", "scoreboard players add @a[tag=so_ev_in] so_ev_pos 1",
    f"function {NS}:lib/streak_up",
    f"function {NS}:lib/cleanup",
])
F("event/runner/fail", [
    f'title {IN} title {T({"text": "¡Se escapó!", "color": "gray", "bold": True})}',
    say("@a", "El fugitivo escapó con su tesoro.", "gray"),
    f"function {NS}:lib/streak_reset",
    f"function {NS}:lib/cleanup",
])

# ---------------------------------------------------------------- v3: tormenta de maná (45 s, orbes cada 3 s)
F("event/mana/start", [
    f"function {NS}:lib/begin", "scoreboard players set #active so_ev 8",
    f'bossbar set {NS}:ev name {T({"text": "Tormenta de maná", "color": "aqua"})}',
    f"bossbar set {NS}:ev max 45", f"bossbar set {NS}:ev color blue",
    say("@a", "¡Tormenta de maná! Corran: los orbes de experiencia caen por 45 segundos.", "aqua"),
])
F("event/mana/second", [
    "scoreboard players add #t so_ev 1",
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    "scoreboard players operation #m so_ev = #t so_ev", "scoreboard players operation #m so_ev %= #three so_ev",
    f"execute if score #m so_ev matches 0 run function {NS}:event/mana/burst",
    f"execute if score #t so_ev matches 45.. run function {NS}:event/mana/end",
])
F("event/mana/end", [
    "scoreboard players add @a[tag=so_ev_in] so_ev_win 1", "scoreboard players add @a[tag=so_ev_in] so_ev_pos 1",
    f"function {NS}:lib/streak_up",
    f"function {NS}:lib/cleanup",
])
F("event/mana/burst", [
    f"execute as @a[tag=so_ev_in,limit=3] at @s run function {NS}:lib/orbs",
    f"execute as @a[tag=so_ev_in,limit=3] at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.4",
])
F("lib/orbs", [
    "execute store result storage so_events:tmp dx int 1 run random value -6..6",
    "execute store result storage so_events:tmp dz int 1 run random value -6..6",
    "function so_events:lib/orb_spawn with storage so_events:tmp",
])
F("lib/orb_spawn", ["$execute positioned ~ ~4 ~ run summon minecraft:experience_orb ~$(dx) ~ ~$(dz) {Value:6}"])

# ---------------------------------------------------------------- v3: altar del sacrificio (90 s, tributo de 32 cobblestone o 16 troncos)
F("event/altar/start", [
    f"function {NS}:lib/begin", "scoreboard players set #active so_ev 9",
    "scoreboard players set #paid so_ev 0", "scoreboard players set #need so_ev 32",
    f'bossbar set {NS}:ev name {T({"text": "Altar del sacrificio", "color": "gold"})}',
    f"bossbar set {NS}:ev max 90", f"bossbar set {NS}:ev color yellow",
    "scoreboard players set #near so_ev 1",
    f'execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function {NS}:event/altar/place',
    "scoreboard players set #near so_ev 0",
    say("@a", "El Altar del Sacrificio apareció. Tirenle encima 32 bloques de piedra o 16 troncos para bendecir la isla.", "gold"),
])
F("event/altar/place", [
    "execute positioned ~4 ~ ~ run function so_events:lib/altar_at",
])
F("lib/altar_at", [
    'execute if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air run summon minecraft:block_display ~ ~0.5 ~ {Tags:["so_ev_altar"],block_state:{Name:"minecraft:end_portal_frame"},brightness:{sky:15,block:0},glowing:1b}',
    'execute if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air run particle minecraft:flame ~ ~1 ~ 0.2 0.3 0.2 0.02 20',
])
F("event/altar/second", [
    "scoreboard players add #t so_ev 1",
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    f"execute as @e[tag=so_ev_altar,limit=1] at @s run particle minecraft:end_rod ~ ~1.2 ~ 0.2 0.4 0.2 0.02 8",
    f"execute as @e[tag=so_ev_altar,limit=1] at @s run function {NS}:event/altar/take",
    f"execute if score #t so_ev matches 45.. run title {IN} actionbar {T({'text': '¡Tributo al altar: 32 piedra o 16 troncos!', 'color': 'gold', 'bold': True})}",
    f"execute if score #paid so_ev matches 32.. run function {NS}:event/altar/win",
    f"execute if score #t so_ev matches 90.. run function {NS}:event/altar/fail",
])
W(f"data/{NS}/tags/item/altar_tribute.json", {"values": [
    *[f"minecraft:{b}" for b in ("cobblestone", "stone", "deepslate", "cobbled_deepslate", "andesite", "diorite", "granite",
                                 "tuff", "blackstone", "calcite", "mossy_cobblestone", "netherrack", "end_stone")],
    "#minecraft:logs"]})
F("event/altar/take", [
    "# 'if items' sí acepta tags de ítem (las NBT con # no funcionan).",
    f"execute as @e[type=minecraft:item,distance=..3.5] if items entity @s contents #{NS}:altar_tribute run function {NS}:event/altar/add",
])
F("event/altar/add", [
    "execute store result score #cnt so_ev run data get entity @s Item.count 1",
    "scoreboard players operation #paid so_ev += #cnt so_ev",
    "particle minecraft:soul_fire_flame ~ ~0.3 ~ 0.2 0.2 0.2 0.05 12",
    "playsound minecraft:block.respawn_anchor.charge master @a ~ ~ ~ 0.8 1.4",
    "kill @s",
    f"title {IN} actionbar {T({'text': 'Tributo: ', 'color': 'gold'}, {'score': {'name': '#paid', 'objective': 'so_ev'}, 'color': 'white', 'bold': True}, {'text': ' / 32', 'color': 'gold'})}",
])
F("event/altar/win", [
    f'title {IN} title {T({"text": "¡Altar satisfecho!", "color": "gold", "bold": True})}',
    f"execute as @a[tag=so_ev_in] at @s run summon minecraft:lightning_bolt ~ ~ ~ {{visual_only:1b}}",
    f"execute as {IN} run effect give @s minecraft:haste 180 1 true",
    f"execute as {IN} run effect give @s minecraft:regeneration 180 1 true",
    say("@a", "El altar premió a la isla: Prisa II y Regeneración II por 3 minutos.", "gold"),
    "scoreboard players add @a[tag=so_ev_in] so_ev_win 1", "scoreboard players add @a[tag=so_ev_in] so_ev_pos 1",
    f"function {NS}:lib/streak_up",
    f"function {NS}:lib/cleanup",
])
F("event/altar/fail", [
    say("@a", "El altar no recibió su tributo y se apagó.", "gray"),
    f"function {NS}:lib/cleanup",
])

# ---------------------------------------------------------------- v4: racha de eventos (multiplicador de recompensa)
F("lib/streak_up", [
    "scoreboard players add #streak so_ev 1",
    "# Bonus: 1 rollo extra de reward_small por cada 2 de racha (tope 3).",
    "execute if score #streak so_ev matches 2..3 as @a[tag=so_ev_in] run loot give @s loot so_events:reward_small",
    "execute if score #streak so_ev matches 4..5 as @a[tag=so_ev_in] run loot give @s loot so_events:reward_small",
    "execute if score #streak so_ev matches 4..5 as @a[tag=so_ev_in] run loot give @s loot so_events:reward_small",
    "execute if score #streak so_ev matches 6.. as @a[tag=so_ev_in] run loot give @s loot so_events:reward_small",
    "execute if score #streak so_ev matches 6.. as @a[tag=so_ev_in] run loot give @s loot so_events:reward_small",
    "execute if score #streak so_ev matches 6.. as @a[tag=so_ev_in] run loot give @s loot so_events:reward_small",
    f"execute if score #streak so_ev matches 2.. run tellraw @a {T(PFX, {'text': 'Racha de eventos: x', 'color': 'gold', 'bold': False}, {'score': {'name': '#streak', 'objective': 'so_ev'}, 'color': 'white', 'bold': True}, {'text': ' — recompensa mejorada.', 'color': 'gold'})}",
])
F("lib/streak_reset", [
    f"execute if score #streak so_ev matches 2.. run tellraw @a {T(PFX, {'text': 'La racha de eventos se perdió.', 'color': 'gray', 'bold': False})}",
    "scoreboard players set #streak so_ev 0",
])

# ---------------------------------------------------------------- v4: diario de eventos (/trigger evento_diario)
F("lib/diary", [
    f"tellraw @s {T({'text': '—— Diario de eventos ——', 'color': 'gold', 'bold': True})}",
    f"tellraw @s {T({'text': 'Eventos ganados: ', 'color': 'gray'}, {'score': {'name': '@s', 'objective': 'so_ev_win'}, 'color': 'white', 'bold': True})}",
    f"tellraw @s {T({'text': 'Invasiones derrotadas: ', 'color': 'gray'}, {'score': {'name': '@s', 'objective': 'so_ev_inv'}, 'color': 'red'})}",
    f"tellraw @s {T({'text': 'Eventos positivos completados: ', 'color': 'gray'}, {'score': {'name': '@s', 'objective': 'so_ev_pos'}, 'color': 'green'})}",
    f"tellraw @s {T({'text': 'Racha actual de la isla: x', 'color': 'gray'}, {'score': {'name': '#streak', 'objective': 'so_ev'}, 'color': 'gold'})}",
])

# ---------------------------------------------------------------- v4: 10 lluvia de meteoritos (60 s)
F("event/meteor/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 10", f"function {NS}:lib/no_grief",
    f"bossbar set {NS}:ev name {T({'text': 'Lluvia de meteoritos', 'color': 'red'})}", f"bossbar set {NS}:ev max 60", f"bossbar set {NS}:ev color red",
    f"title {IN} title {T({'text': '¡Lluvia de meteoritos!', 'color': 'red', 'bold': True})}",
    say("@a", "¡Meteoritos caen sobre la isla durante 60 segundos! Cada cráter deja botín... si te animás a acercarte.", "red")])
F("event/meteor/second", ["scoreboard players add #t so_ev 1", NEAR,
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    "scoreboard players operation #m so_ev = #t so_ev", "scoreboard players operation #m so_ev %= #three so_ev",
    f"execute if score #m so_ev matches 0 as @a[tag=so_ev_in,limit=3] at @s run function {NS}:event/meteor/burst",
    f"execute if score #t so_ev matches 60.. run function {NS}:event/meteor/end"])
F("event/meteor/burst", [
    "execute store result storage so_events:tmp dx int 1 run random value -10..10",
    "execute store result storage so_events:tmp dz int 1 run random value -10..10",
    f"function {NS}:event/meteor/fall with storage {NS}:tmp",
])
F("event/meteor/fall", [
    "$execute positioned ~$(dx) ~ ~$(dz) over motion_blocking_no_leaves run summon minecraft:falling_block ~ ~14 ~ {BlockState:{Name:\"minecraft:magma_block\"},Time:1,Tags:[\"so_ev_meteor\"]}",
    "$execute positioned ~$(dx) ~ ~$(dz) over motion_blocking_no_leaves run particle minecraft:flame ~ ~2 ~ 0.3 1 0.3 0.02 30",
    "$execute positioned ~$(dx) ~ ~$(dz) over motion_blocking_no_leaves run loot spawn ~ ~1 ~ loot so_events:meteor",
    "$execute positioned ~$(dx) ~ ~$(dz) over motion_blocking_no_leaves run playsound minecraft:entity.generic.explode master @a ~ ~ ~ 0.7 1.2",
])
F("event/meteor/end", [
    "scoreboard players add @a[tag=so_ev_in] so_ev_win 1", "scoreboard players add @a[tag=so_ev_in] so_ev_pos 1",
    f"function {NS}:lib/streak_up",
    say("@a", "La lluvia de meteoritos terminó. Revisen los cráteres.", "green"), f"function {NS}:lib/cleanup"])

# ---------------------------------------------------------------- v4: 11 fiebre del oro (60 s)
F("event/gold/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 11",
    f"bossbar set {NS}:ev name {T({'text': 'Fiebre del oro', 'color': 'gold'})}", f"bossbar set {NS}:ev max 60", f"bossbar set {NS}:ev color yellow",
    f"title {IN} title {T({'text': '¡Fiebre del oro!', 'color': 'gold', 'bold': True})}",
    say("@a", "¡El OneBlock brilla! Durante 60 segundos el oro brota de la isla.", "gold")])
F("event/gold/second", ["scoreboard players add #t so_ev 1", NEAR,
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    "scoreboard players operation #m so_ev = #t so_ev", "scoreboard players operation #m so_ev %= #two so_ev",
    f"execute if score #m so_ev matches 0 as {IN} at @s run loot spawn ~ ~1 ~ loot {NS}:gold_fever",
    f"execute if score #m so_ev matches 0 as {IN} at @s run particle minecraft:happy_villager ~ ~2 ~ 1 0.5 1 0 8",
    f"execute as {IN} at @s run particle minecraft:end_rod ~ ~1.5 ~ 0.6 0.4 0.6 0.01 3",
    f"execute if score #t so_ev matches 60.. run function {NS}:event/gold/end"])
F("event/gold/end", [
    "scoreboard players add @a[tag=so_ev_in] so_ev_win 1", "scoreboard players add @a[tag=so_ev_in] so_ev_pos 1",
    f"function {NS}:lib/streak_up",
    say("@a", "La fiebre del oro se calmó.", "gold"), f"function {NS}:lib/cleanup"])

# ---------------------------------------------------------------- v4: 12 espejismo (2 cofres gemelos: uno tesoro, otro trampa)
for adv, tbl, fn in (("mimic", "mimic_treasure", "mimic_open"), ("mimic_junk", "mimic_junk", "mimic_trap_open")):
    W(f"data/{NS}/advancement/{adv}.json", {"criteria": {"open": {"trigger": "minecraft:player_generates_container_loot",
        "conditions": {"loot_table": f"{NS}:{tbl}"}}}, "rewards": {"function": f"{NS}:{fn}"}})
F("event/mimic/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 12", "scoreboard players set #mimic so_ev 0",
    f"bossbar set {NS}:ev name {T({'text': 'Espejismo: elegí un cofre', 'color': 'light_purple'})}", f"bossbar set {NS}:ev max 120", f"bossbar set {NS}:ev color purple",
    "execute store result score #side so_ev run random value 1..2",
    f"execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function {NS}:event/mimic/place",
    f"title {IN} title {T({'text': 'Espejismo', 'color': 'light_purple', 'bold': True})}",
    f"title {IN} subtitle {T({'text': 'Dos cofres gemelos... solo uno es real', 'color': 'gray'})}",
    say("@a", "Dos cofres gemelos aparecieron junto a vos. Uno guarda un tesoro, el otro es una trampa. Abrí solo uno: tenés 2 minutos.", "light_purple")])
_REAL = 'setblock ~ ~ ~ minecraft:chest[facing=north]{LootTable:"so_events:mimic_treasure"}'
_FAKE = 'setblock ~ ~ ~ minecraft:chest[facing=north]{LootTable:"so_events:mimic_junk"}'
F("event/mimic/place", [
    *[f"execute if score #side so_ev matches {s} positioned ~{dx} ~ ~2 if block ~ ~ ~ #minecraft:air run {blk}"
      for s, dx, blk in ((1, 2, _REAL), (1, -2, _FAKE), (2, 2, _FAKE), (2, -2, _REAL))],
    *[f'execute positioned ~{dx} ~ ~2 if block ~ ~ ~ minecraft:chest run summon minecraft:marker ~ ~ ~ {{Tags:["so_ev_mimic","{t}"]}}'
      for dx, t in ((2, "so_ev_mim_a"), (-2, "so_ev_mim_b"))],
    "execute if score #side so_ev matches 1 as @e[tag=so_ev_mim_a] run tag @s add so_ev_mim_real",
    "execute if score #side so_ev matches 2 as @e[tag=so_ev_mim_b] run tag @s add so_ev_mim_real",
    "tag @e[tag=so_ev_mimic,tag=!so_ev_mim_real] add so_ev_mim_fake",
    "execute as @e[tag=so_ev_mimic] at @s run particle minecraft:witch ~ ~0.5 ~ 0.3 0.3 0.3 0.02 20",
    "execute as @e[tag=so_ev_mimic] at @s run playsound minecraft:block.amethyst_block.chime master @a ~ ~ ~ 1 0.6",
])
F("event/mimic/second", ["scoreboard players add #t so_ev 1", NEAR,
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    f"execute if score #mimic so_ev matches 0 as @e[tag=so_ev_mimic] at @s run particle minecraft:witch ~ ~0.7 ~ 0.3 0.3 0.3 0.01 4",
    f"execute if score #mimic so_ev matches 0 as @e[tag=so_ev_mimic] at @s run particle minecraft:enchant ~ ~1.2 ~ 0.3 0.3 0.3 0.5 6",
    "# Antitrampa: romper el cofre también cuenta como elegirlo.",
    f"execute if score #mimic so_ev matches 0 as @e[tag=so_ev_mim_real] at @s unless block ~ ~ ~ minecraft:chest run function {NS}:event/mimic/treasure",
    f"execute if score #mimic so_ev matches 0 as @e[tag=so_ev_mim_fake] at @s unless block ~ ~ ~ minecraft:chest run function {NS}:event/mimic/trap",
    f"execute if score #mimic so_ev matches 1 run function {NS}:event/mimic/end",
    "# Trampa: el evento sigue hasta derrotar a los vexes.",
    f"execute if score #mimic so_ev matches 2 run title {IN} actionbar {T({'text': '¡Derrotá a los vexes y phantoms de la trampa!', 'color': 'red', 'bold': True})}",
    f"execute if score #mimic so_ev matches 2 unless entity @e[tag=so_ev_mob] run function {NS}:event/mimic/trap_win",
    f"execute if score #t so_ev matches 120.. run function {NS}:event/mimic/vanish"])
F("mimic_open", [
    f"advancement revoke @s only {NS}:mimic",
    f"execute if score #active so_ev matches 12 if score #mimic so_ev matches 0 run function {NS}:event/mimic/treasure",
])
F("mimic_trap_open", [
    f"advancement revoke @s only {NS}:mimic_junk",
    f"execute if score #active so_ev matches 12 if score #mimic so_ev matches 0 run function {NS}:event/mimic/trap",
])
F("event/mimic/treasure", [
    "scoreboard players set #mimic so_ev 1",
    "execute as @e[tag=so_ev_mim_real] at @s run particle minecraft:firework ~ ~1 ~ 0.4 0.4 0.4 0.05 40",
    "execute as @e[tag=so_ev_mim_real] at @s run playsound minecraft:ui.toast.challenge_complete master @a ~ ~ ~ 1 1",
    "execute as @e[tag=so_ev_mim_fake] at @s run particle minecraft:large_smoke ~ ~0.5 ~ 0.3 0.4 0.3 0.02 30",
    "execute as @e[tag=so_ev_mim_fake] at @s run playsound minecraft:entity.illusioner.mirror_move master @a ~ ~ ~ 1 1",
    "execute as @e[tag=so_ev_mim_fake] at @s run setblock ~ ~ ~ minecraft:air",
    say("@a", "¡Elegiste bien! El cofre era un tesoro de verdad y su gemelo se desvaneció en humo.", "gold")])
F("event/mimic/trap", [
    "scoreboard players set #mimic so_ev 2",
    "execute as @e[tag=so_ev_mim_real] at @s run particle minecraft:large_smoke ~ ~0.5 ~ 0.3 0.4 0.3 0.02 30",
    "execute as @e[tag=so_ev_mim_real] at @s run setblock ~ ~ ~ minecraft:air",
    "execute as @e[tag=so_ev_mim_fake] at @s run playsound minecraft:event.raid.horn hostile @a ~ ~ ~ 1 1.4",
    "execute as @e[tag=so_ev_mim_fake] at @s run playsound minecraft:entity.vex.charge hostile @a ~ ~ ~ 1 0.8",
    "execute as @e[tag=so_ev_mim_fake] at @s run particle minecraft:soul ~ ~1 ~ 0.4 0.4 0.4 0.05 30",
    *["execute as @e[tag=so_ev_mim_fake,limit=1] at @s positioned ~ ~1 ~ run function so_events:mob/elite_vex"] * 3,
    *["execute as @e[tag=so_ev_mim_fake,limit=1] at @s positioned ~ ~6 ~ run function so_events:mob/phantom"] * 2,
    say("@a", "¡Era una trampa! El cofre solo tenía chatarra y salen vexes espectrales con phantoms. ¡Derrotalos!", "red")])
F("event/mimic/trap_win", [
    f"execute as {IN} run loot give @s loot {NS}:reward_small",
    say("@a", "Sobreviviste a la trampa del espejismo. Algo es algo.", "green"),
    f"function {NS}:event/mimic/end"])
F("event/mimic/end", [
    "scoreboard players add @a[tag=so_ev_in] so_ev_win 1", "scoreboard players add @a[tag=so_ev_in] so_ev_pos 1",
    f"function {NS}:lib/streak_up", f"function {NS}:lib/cleanup"])
F("event/mimic/vanish", [
    "execute if score #mimic so_ev matches 0 as @e[tag=so_ev_mimic] at @s run setblock ~ ~ ~ minecraft:air",
    "execute as @e[tag=so_ev_mimic] at @s run particle minecraft:large_smoke ~ ~0.5 ~ 0.3 0.4 0.3 0.02 20",
    say("@a", "El espejismo se desvaneció.", "gray"), f"function {NS}:lib/cleanup"])

# ---------------------------------------------------------------- v4: 13 caravana perdida (3 min, defender las llamas)
F("event/caravan/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 13", f"function {NS}:lib/no_grief",
    f"bossbar set {NS}:ev name {T({'text': 'Caravana perdida', 'color': 'gold'})}", f"bossbar set {NS}:ev max 120", f"bossbar set {NS}:ev color yellow",
    "scoreboard players set #near so_ev 1",
    f'execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function {NS}:lib/spawn {{mob:"mob/llama_caravan"}}',
    f'execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function {NS}:lib/spawn {{mob:"mob/llama_caravan"}}',
    f'execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function {NS}:lib/spawn {{mob:"mob/llama_caravan"}}',
    "scoreboard players set #near so_ev 0",
    f"title {IN} title {T({'text': '¡Caravana perdida!', 'color': 'gold', 'bold': True})}",
    say("@a", "Una caravana de llamas cargadas llegó a la isla. ¡Saqueadores las persiguen! Defendé al menos una por 3 minutos.", "gold")])
F("event/caravan/second", ["scoreboard players add #t so_ev 1", NEAR,
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    "execute store result score #llamas so_ev if entity @e[tag=so_ev_llama]",
    f"execute if score #t so_ev matches 15 run function {NS}:event/caravan/wave",
    f"execute if score #t so_ev matches 45 run function {NS}:event/caravan/wave",
    f"execute if score #t so_ev matches 75 run function {NS}:event/caravan/wave",
    f"execute if score #t so_ev matches 90 run function {NS}:event/caravan/boss",
    "# Los saqueadores lastiman a la llama más cercana cada 5 s.",
    "scoreboard players operation #m so_ev = #t so_ev", "scoreboard players operation #m so_ev %= #five so_ev",
    "execute if score #m so_ev matches 0 as @e[tag=so_ev_mob,tag=!so_ev_llama] at @s if entity @e[tag=so_ev_llama,distance=..16] run damage @e[tag=so_ev_llama,limit=1,sort=nearest] 2 minecraft:mob_attack by @s",
    f"execute if score #llamas so_ev matches 0 run function {NS}:event/caravan/fail",
    "# Victoria a los 120 s, pero solo si el caudillo ya cayó.",
    f"execute if score #t so_ev matches 120.. unless entity @e[tag=so_ev_boss] run function {NS}:event/caravan/win",
    "# Si el caudillo se resiste demasiado, la caravana se rinde a los 240 s.",
    f"execute if score #t so_ev matches 240.. run function {NS}:event/caravan/fail"])
F("event/caravan/wave", [
    spawn("saqueador_caravana"), spawn("saqueador_caravana"), spawn("pillager"), spawn("vindicator"),
    f"function {NS}:lib/tier_up",
    f"title {IN} actionbar {T({'text': '¡Saqueadores atacan la caravana!', 'color': 'red', 'bold': True})}"])
F("event/caravan/boss", [
    f'execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function {NS}:lib/spawn {{mob:"boss/caudillo_saqueador"}}',
    "playsound minecraft:event.raid.horn hostile @a ~ ~ ~ 1 0.8",
    f"title {IN} title {T({'text': '¡El Caudillo Saqueador!', 'color': 'red', 'bold': True})}",
    f"title {IN} subtitle {T({'text': 'Derrotalo para salvar la caravana', 'color': 'gray'})}",
    say("@a", "¡El Caudillo Saqueador llegó montado en su devastador! Derrotalo para asegurar la caravana.", "red")])
F("event/caravan/win", [
    f"execute as {IN} run loot give @s loot {NS}:caravan",
    "# Por cada llama viva, un rollo extra de cargamento para la isla.",
    f"execute as @e[tag=so_ev_llama] at @s run loot spawn ~ ~1 ~ loot {NS}:caravan",
    "scoreboard players add @a[tag=so_ev_in] so_ev_win 1", "scoreboard players add @a[tag=so_ev_in] so_ev_pos 1",
    f"function {NS}:lib/streak_up",
    f"title {IN} title {T({'text': '¡Caravana a salvo!', 'color': 'green', 'bold': True})}",
    say("@a", "La caravana sobrevivió y les deja su cargamento. Las llamas se quedan en la isla como mascotas.", "green"),
    "# Las llamas dejan de ser del evento: el limpiador ya no las toca.",
    "execute as @e[tag=so_ev_llama] at @s run particle minecraft:heart ~ ~1.8 ~ 0.4 0.3 0.4 0 6",
    "execute as @e[tag=so_ev_llama] run data merge entity @s {PersistenceRequired:1b,Tame:1b,CustomName:{text:\"Llama de la Isla\",color:\"gold\"}}",
    "tag @e[tag=so_ev_llama] add so_ev_saved", "tag @e[tag=so_ev_llama] remove so_ev_mob", "tag @e[tag=so_ev_llama] remove so_ev_llama",
    f"function {NS}:lib/cleanup"])
F("event/caravan/fail", [
    f"function {NS}:lib/streak_reset",
    say("@a", "Los saqueadores acabaron con la caravana. No quedó nada que rescatar.", "gray"), f"function {NS}:lib/cleanup"])

# ---------------------------------------------------------------- v4: 14 eclipse (90 s, élite, botín legendario; desde 9000 bloques)
ECLIPSE = ["elite_zombie", "elite_skeleton", "elite_spider", "elite_vex", "witch", "eclipse_rider"]
F("event/eclipse/start", [f"function {NS}:lib/begin", "scoreboard players set #active so_ev 14", f"function {NS}:lib/no_grief",
    f"bossbar set {NS}:ev name {T({'text': 'Eclipse', 'color': 'dark_purple', 'bold': True})}", f"bossbar set {NS}:ev max 90", f"bossbar set {NS}:ev color purple",
    f"title {IN} title {T({'text': '¡ECLIPSE!', 'color': 'dark_purple', 'bold': True})}",
    f"title {IN} subtitle {T({'text': 'Sobreviví 90 segundos a la élite', 'color': 'light_purple'})}",
    f"execute as {IN} at @s run playsound minecraft:entity.wither.spawn hostile @s ~ ~ ~ 0.8 0.6",
    say("@a", "Un eclipse cubre la isla. Jinetes y enemigos de élite cada 15 s: sobrevivan 90 segundos por un botín legendario.", "dark_purple")])
F("event/eclipse/second", ["scoreboard players add #t so_ev 1", NEAR,
    f"execute store result bossbar {NS}:ev value run scoreboard players get #t so_ev",
    f"effect give {IN} minecraft:darkness 3 0 true",
    f"execute as {IN} at @s run particle minecraft:reverse_portal ~ ~1 ~ 4 2 4 0.02 20",
    "scoreboard players operation #m so_ev = #t so_ev", "scoreboard players operation #m so_ev %= #fifteen so_ev",
    f"execute if score #m so_ev matches 1 if score #t so_ev matches ..80 run function {NS}:event/eclipse/spawn",
    f"execute if score #t so_ev matches 81 run function {NS}:event/eclipse/final",
    f"execute if score #t so_ev matches 90.. run function {NS}:event/eclipse/end"])
F("event/eclipse/spawn", [spawn(m) for m in ECLIPSE] + [f"function {NS}:lib/tier_up"])
F("event/eclipse/final", [*[spawn(m) for m in ECLIPSE for _ in (0, 1)], f"function {NS}:lib/tier_up",
    f"title {IN} title {T({'text': '¡Oleada final del eclipse!', 'color': 'dark_purple', 'bold': True})}"])
F("event/eclipse/end", [f"execute as {IN} run loot give @s loot {NS}:reward_eclipse",
    f"execute as {IN} run loot give @s loot {NS}:reward_big",
    "scoreboard players add @a[tag=so_ev_in] so_ev_win 1", "scoreboard players add @a[tag=so_ev_in] so_ev_inv 1",
    f"function {NS}:lib/streak_up",
    f"execute as {IN} at @s run summon minecraft:firework_rocket ~ ~1 ~ {{LifeTime:30,FireworksItem:{{id:\"minecraft:firework_rocket\",count:1,components:{{\"minecraft:fireworks\":{{explosions:[{{shape:\"large_ball\",colors:[I;11141290,16777215],has_trail:1b}}]}}}}}}}}",
    say("@a", "El eclipse terminó. Los sobrevivientes recibieron el botín legendario del eclipse.", "green"), f"function {NS}:lib/cleanup"])


lines = open(os.path.join(ROOT, f"data/{NS}/function/load.mcfunction"), encoding="utf-8").read()
W(f"data/{NS}/function/load.mcfunction", lines + "scoreboard players set #twenty so_ev 20\nscoreboard players set #five so_ev 5\nscoreboard players set #near so_ev 0\n"
  + "scoreboard players set #three so_ev 3\nscoreboard players set #two so_ev 2\nscoreboard players set #fifteen so_ev 15\n" + f"function {NS}:load_offers\n")


# ---------------------------------------------------------------- API para so_arenas
F("api/boss", ["# Uso: execute positioned X Y Z run function so_events:api/boss {id:\"rey_zombi\"}", "$function so_events:boss/$(id)"])
F("api/mob", ["# Uso: execute positioned X Y Z run function so_events:api/mob {id:\"husk\"}", "$function so_events:mob/$(id)"])
F("api/cleanup", [f"function {NS}:lib/cleanup"])
# ---------------------------------------------------------------- admin
EVS = {"lluvia": "rain", "suministro": "supply", "mineria": "mining", "mercader": "trader", "invasion": "invasion", "oscuridad": "dark",
       "duende": "runner", "mana": "mana", "altar": "altar", "meteoritos": "meteor", "oro": "gold", "espejismo": "mimic",
       "caravana": "caravan", "eclipse": "eclipse"}
for es, en in EVS.items():
    F(f"admin/start_{es}", [f"function {NS}:lib/blocks", f"execute unless score #active so_ev matches 0 run function {NS}:lib/cleanup",
                            f"function {NS}:event/{en}/start"])
for k in INV:
    F(f"admin/start_invasion_{k}", [f"scoreboard players set #force_type so_ev {k}", f"function {NS}:admin/start_invasion"])
for k in TRADERS:
    F(f"admin/start_mercader_{k}", [f"scoreboard players set #force_trader so_ev {k}", f"function {NS}:admin/start_mercader"])
for lv in (1, 2, 3):
    F(f"admin/start_invasion_nivel_{lv}", [f"scoreboard players set #force_tier so_ev {lv}", f"function {NS}:admin/start_invasion"])
for i in range(1, 6):
    F(f"admin/bless_{i}", [f"scoreboard players set #r so_ev {i}", f"function {NS}:admin/bless"])
F("admin/alpha_on", ["scoreboard players set #alpha_force so_ev 1", say("@s", "Próximas invasiones SIEMPRE alfa: ON.", "green")])
F("admin/alpha_off", ["scoreboard players set #alpha_force so_ev 0", say("@s", "Invasiones alfa forzadas: OFF (vuelve el 10% al azar).", "red")])
F("admin/bless_on", ["scoreboard players set #bless_on so_ev 1", say("@s", "Bendiciones cada 200 bloques: ON.", "green")])
F("admin/bless_off", ["scoreboard players set #bless_on so_ev 0", say("@s", "Bendiciones cada 200 bloques: OFF.", "red")])
F("admin/stop", [f"function {NS}:lib/cleanup", say("@a", "Evento detenido por un administrador.", "gray")])
F("admin/enable", ["scoreboard players set #enabled so_ev 1", say("@s", "Eventos activados.", "green")])
F("admin/disable", [f"function {NS}:lib/cleanup", "scoreboard players set #enabled so_ev 0", say("@s", "Eventos desactivados.", "red")])
F("admin/auto_on", ["scoreboard players set #auto so_ev 1", say("@s", "Eventos automáticos por bloques: ON.", "green")])
F("admin/auto_off", ["scoreboard players set #auto so_ev 0", say("@s", "Eventos automáticos por bloques: OFF.", "red")])
F("admin/status", [f"function {NS}:lib/blocks",
    f"tellraw @s {T(PFX, {'text': 'activo=', 'color': 'gray', 'bold': False}, {'score': {'name': '#active', 'objective': 'so_ev'}, 'color': 'white'}, {'text': '  bloques=', 'color': 'gray'}, {'score': {'name': '#blk', 'objective': 'so_ev'}, 'color': 'white'}, {'text': '  próximo=', 'color': 'gray'}, {'score': {'name': '#next', 'objective': 'so_ev'}, 'color': 'white'}, {'text': '  cada=', 'color': 'gray'}, {'score': {'name': '#every', 'objective': 'so_ev'}, 'color': 'white'})}"])
INV_LIST = ", ".join(f"{k} {v[0].lower()}" for k, v in INV.items())
HELP = ["SO Events v4 — ayuda admin",
        "/function so_events:admin/start_<lluvia|suministro|mineria|mercader|invasion|oscuridad|duende|mana|altar>",
        f"/function so_events:admin/start_invasion_<1..{N}>",
        "/function so_events:admin/start_invasion_nivel_<1|2|3>  (invasión al azar con nivel forzado)",
        "/function so_events:admin/start_<meteoritos|oro|espejismo|caravana|eclipse>  (eventos v4)",
        "/function so_events:admin/alpha_on | alpha_off  (forzar invasiones alfa)",
        "/function so_events:admin/bless | bless_<1..5> | bless_on | bless_off",
        "  1 prisa X 5 min, 2 regeneración III 60 s, 3 fuerza V 60 s, 4 velocidad II 2 min, 5 absorción IX 3 min",
        f"  {INV_LIST}",
        "/function so_events:admin/start_mercader_<1..4>  (1 misterioso, 2 alquimista, 3 armero, 4 minero)",
        "/function so_events:admin/stop | status | enable | disable | auto_on | auto_off",
        "/scoreboard players set #every so_ev 400   (bloques entre eventos)",
        "/scoreboard players set #min so_ev 300     (primer evento posible)",
        "/scoreboard players set #mine_goal so_ev 150",
        "/scoreboard players set #bless_every so_ev 200   (bloques entre bendiciones)",
        "Jugadores: /trigger evento  (estado del evento actual)  ·  /trigger evento_diario  (estadísticas)"]
F("admin/help", [f"tellraw @s {T({'text': h, 'color': 'gold' if i == 0 else 'gray'})}" for i, h in enumerate(HELP)])
F("uninstall", [f"function {NS}:lib/cleanup", f"bossbar remove {NS}:ev", f"bossbar remove {NS}:boss",
                "scoreboard objectives remove so_ev", "scoreboard objectives remove evento",
                "scoreboard objectives remove evento_diario", "scoreboard objectives remove so_ev_win",
                "scoreboard objectives remove so_ev_inv", "scoreboard objectives remove so_ev_pos",
                f"data remove storage {NS}:offers alq", f"data remove storage {NS}:offers arm", f"data remove storage {NS}:offers min",
                say("@s", "so_events desinstalado. Quitá el datapack y hacé /reload.", "gray")])

INV_ROWS = "\n".join(f"| {k} | {v[0]} | {v[4]} | {', '.join(x.split('/')[1] for x in v[3])} |" for k, v in INV.items())
W("README.md", f"""# so_events v4 — lo que pasa en la isla

Eventos automáticos cada `#every` bloques minados (por defecto 400, el primero desde 300), solo si hay alguien en la isla (64 bloques alrededor de 0 64 0).

| Evento | Duración | Qué pasa |
|---|---|---|
| Lluvia de recursos | 60 s | Caen materiales sobre los jugadores |
| Suministro | instantáneo | Cae un paquete de botín sobre cada jugador |
| Desafío de minería | 3 min | Romper `#mine_goal` bloques entre todos |
| Mercader especial | 5 min | Aparece a 3-7 bloques del OneBlock (uno de 4 mercaderes) |
| Invasión | hasta 7 min | Alerta, cuenta atrás, 3 oleadas y jefe(s) con escoltas |
| Noche oscura | 90 s | Oscuridad + oleadas de 5 mobs cada 20 s y final de 10 |
| Caza del fugitivo | 60 s | Pollo Dorado o Zorro Místico veloz: 5 golpes y suelta esmeraldas y XP |
| Tormenta de maná | 45 s | Grietas en el aire disparan orbes de experiencia cada 3 s |
| Altar del sacrificio | 90 s | Tiren cerca (3 bloques) 32 piedra de cualquier tipo o troncos: Prisa II + Regeneración II 3 min para todos |
| Lluvia de meteoritos | 60 s | Cráteres de magma con botín caen cerca de los jugadores cada 3 s |
| Fiebre del oro | 60 s | El oro brota de la isla cada 2 s |
| Espejismo | 2 min | Dos cofres gemelos: uno es tesoro, el otro chatarra + vexes espectrales |
| Caravana perdida | 3 min | Defendé las llamas cargadas de los saqueadores; sobrevive al menos una |
| Eclipse | 90 s | Jinetes y enemigos de élite con oscuridad; botín legendario (desde 9.000 bloques) |

## Sistemas v4
- **Racha de eventos**: cada evento ganado sube la racha de la isla; desde x2 da rollos extra de recompensa (tope 3). Fallar la reinicia.
- **Invasión alfa**: 10% de chance (o `admin/alpha_on`); jefe con aura y refuerzos, recompensa `reward_alpha`.
- **Diario**: `/trigger evento_diario` muestra eventos ganados, invasiones derrotadas y positivos completados.

## Mercaderes
1. Misterioso: siempre las mismas 8 ofertas.
2. Alquimista: 8 pociones arrojadizas al azar (positivas y negativas).
3. Armero de la Corte: 8 al azar entre plantilla de netherita y ornamentos.
4. Minero: 8 minerales al azar, ~1.2x más caro.

## Niveles de invasión
Nivel I hasta 4.999 bloques, II desde 5.000 y III desde 10.000: más vida, daño, armadura y velocidad,
y la oleada final de nivel III trae refuerzos. Recompensa extra en II y III.

## Invasiones (tipo | nombre | desde bloques | final)
| # | Invasión | Desde | Jefes / escoltas |
|---|---|---|---|
{INV_ROWS}

Los mobs aparecen a 6-14 bloques del jugador sobre suelo firme (6 intentos; si no hay suelo, junto al jugador).
`mob_griefing` se desactiva durante el evento y se restaura al final; limpieza total al terminar.

Para `so_arenas`: `function so_events:api/boss {{id:"zombi_gigante"}}`, `api/mob {{id:"husk"}}`, `api/cleanup`.
Ayuda admin: `/function so_events:admin/help`. Jugadores: `/trigger evento`.
""")

# ---------------------------------------------------------------- zip (raiz limpia)
os.makedirs("/mnt/documents", exist_ok=True)
out = "/mnt/documents/so_events-v4.1.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for d, _, files in os.walk(ROOT):
        for f in files:
            full = os.path.join(d, f); z.write(full, os.path.relpath(full, ROOT))
print("ok", out)
