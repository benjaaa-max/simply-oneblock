#!/usr/bin/env python3
"""so_shop v0.6 — catálogo completo (11 secciones + vender excedentes).

Regenera artículos, ventanas, menú de chat y despachadores a partir de CATALOG.
Conserva intactos init/tick/lib de lectura de progreso, cooldown y límite diario.
Uso: python3 tools/build_so_shop_catalog.py
"""
from pathlib import Path
import json, math, shutil

ROOT = Path(__file__).resolve().parent.parent / 'datapacks/so-shop'
NS = ROOT / 'data/so_shop'
FN, DLG = NS / 'function', NS / 'dialog'
MULT = {2: .95, 3: .92, 4: .88, 8: .82}


def J(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))


def ench(item, **e):
    return f'{item}[minecraft:enchantments={J({"minecraft:"+k: v for k, v in e.items()})}]'


def book(**e):
    return f'enchanted_book[minecraft:stored_enchantments={J({"minecraft:"+k: v for k, v in e.items()})}]'


def splash(p):
    return f'splash_potion[minecraft:potion_contents={{potion:"minecraft:{p}"}}]'


def crate_key(base, name, color, crate):
    return (f'{base}[custom_name={{text:"{name}",color:"{color}",italic:false}},'
            f'lore=[{{text:"Abre: {crate}",color:"gray",italic:false}}]]')


def simply_key(base, name):
    return f'{base}[minecraft:custom_name={J(name)}]'


# Artículo: (id, nombre, [(ítem, cantidad), ...], precio, bloques para desbloquear)
def one(iid, name, item, n, cost, unlock):
    return (iid, name, [(item, n)], cost, unlock)


SECTIONS = [
  (1, 'Bloques de construcción', 'green', [
    one(101, 'Tronco de roble x32', 'oak_log', 32, 4, 0),
    one(102, 'Tronco de abedul x32', 'birch_log', 32, 4, 0),
    one(103, 'Tronco de abeto x32', 'spruce_log', 32, 4, 0),
    one(104, 'Tronco de jungla x32', 'jungle_log', 32, 5, 500),
    one(105, 'Tronco de acacia x32', 'acacia_log', 32, 5, 500),
    one(106, 'Tronco de roble oscuro x32', 'dark_oak_log', 32, 5, 1000),
    one(107, 'Tronco de cerezo x32', 'cherry_log', 32, 6, 1500),
    one(108, 'Tronco de mangle x32', 'mangrove_log', 32, 6, 1500),
    one(109, 'Bloque de bambú x32', 'bamboo_block', 32, 5, 500),
    one(110, 'Tallo carmesí x32', 'crimson_stem', 32, 7, 6667),
    one(111, 'Tallo distorsionado x32', 'warped_stem', 32, 7, 6667),
    one(112, 'Ladrillos de piedra x64', 'stone_bricks', 64, 5, 500),
    one(113, 'Pizarra profunda pulida x64', 'polished_deepslate', 64, 6, 2500),
    one(114, 'Ladrillos x64', 'bricks', 64, 6, 1000),
    one(115, 'Bloque de cuarzo x32', 'quartz_block', 32, 10, 6667),
    one(116, 'Ladrillos del Nether x64', 'nether_bricks', 64, 6, 6667),
    one(117, 'Prismarina x32', 'prismarine', 32, 8, 4000),
    one(118, 'Ladrillos de piedra del End x32', 'end_stone_bricks', 32, 8, 8500),
    one(119, 'Bloque de púrpur x32', 'purpur_block', 32, 8, 8500),
    one(120, 'Cobre encerado x64', 'waxed_copper_block', 64, 10, 1500),
    one(121, 'Cobre expuesto encerado x64', 'waxed_exposed_copper', 64, 10, 1500),
    one(122, 'Cobre desgastado encerado x64', 'waxed_weathered_copper', 64, 10, 1500),
    one(123, 'Cobre oxidado encerado x64', 'waxed_oxidized_copper', 64, 10, 1500),
  ]),
  (2, 'Minerales e ingredientes', 'aqua', [
    one(201, 'Carbón x32', 'coal', 32, 4, 0),
    one(202, 'Lingote de cobre x32', 'copper_ingot', 32, 5, 500),
    one(203, 'Lingote de hierro x16', 'iron_ingot', 16, 6, 500),
    one(204, 'Lingote de oro x16', 'gold_ingot', 16, 8, 1500),
    one(205, 'Diamante x4', 'diamond', 4, 10, 3500),
    one(206, 'Fragmento de netherita x2', 'netherite_scrap', 2, 12, 6667),
    one(207, 'Lingote de netherita', 'netherite_ingot', 1, 24, 7500),
    one(208, 'Lapislázuli x32', 'lapis_lazuli', 32, 4, 1000),
    one(209, 'Fragmento de amatista x16', 'amethyst_shard', 16, 6, 2500),
    one(210, 'Polvo de piedra luminosa x32', 'glowstone_dust', 32, 6, 6667),
    one(211, 'Cuarzo del Nether x32', 'quartz', 32, 3, 6667),
    one(212, 'Pólvora x16', 'gunpowder', 16, 6, 2500),
    one(213, 'Perla de Ender x4', 'ender_pearl', 4, 8, 5000),
    one(214, 'Vara de breeze x2', 'breeze_rod', 2, 14, 7000),
  ]),
  (3, 'Herramientas, armas y armaduras', 'yellow', [
    one(301, 'Pico de hierro (Efic. III, Irromp. II)', ench('iron_pickaxe', efficiency=3, unbreaking=2), 1, 10, 500),
    one(302, 'Espada de hierro (Filo III)', ench('iron_sword', sharpness=3), 1, 8, 500),
    one(303, 'Hacha de hierro (Efic. III)', ench('iron_axe', efficiency=3), 1, 8, 500),
    one(304, 'Pala de hierro (Efic. III)', ench('iron_shovel', efficiency=3), 1, 6, 500),
    one(305, 'Pechera de hierro (Prot. II)', ench('iron_chestplate', protection=2), 1, 12, 1000),
    one(306, 'Pantalones de hierro (Prot. II)', ench('iron_leggings', protection=2), 1, 11, 1000),
    one(307, 'Pico de diamante (Efic. IV, Fortuna II)', ench('diamond_pickaxe', efficiency=4, fortune=2), 1, 24, 3500),
    one(308, 'Espada de diamante (Filo IV, Botín II)', ench('diamond_sword', sharpness=4, looting=2), 1, 22, 3500),
    one(309, 'Hacha de diamante (Efic. IV)', ench('diamond_axe', efficiency=4), 1, 20, 3500),
    one(310, 'Azada de diamante (Fortuna II)', ench('diamond_hoe', fortune=2), 1, 16, 3500),
    one(311, 'Pechera de diamante (Prot. III)', ench('diamond_chestplate', protection=3), 1, 28, 4000),
    one(312, 'Botas de diamante (Prot. III, Pluma III)', ench('diamond_boots', protection=3, feather_falling=3), 1, 22, 4000),
    one(313, 'Pico de netherita (Efic. V, Irromp. III)', ench('netherite_pickaxe', efficiency=5, unbreaking=3), 1, 55, 8500),
    one(314, 'Espada de netherita (Filo V, Fuego II)', ench('netherite_sword', sharpness=5, fire_aspect=2), 1, 50, 8500),
    one(315, 'Pechera de netherita (Prot. IV)', ench('netherite_chestplate', protection=4), 1, 55, 9000),
    one(316, 'Tijeras (Toque de seda)', ench('shears', silk_touch=1), 1, 12, 1000),
    one(317, 'Armadura de caballo de hierro', 'iron_horse_armor', 1, 14, 1500),
    one(318, 'Armadura de caballo de diamante', 'diamond_horse_armor', 1, 28, 4000),
    one(319, 'Arnés para Happy Ghast', 'white_harness', 1, 20, 5000),
  ]),
  (4, 'Bloques funcionales', 'gold', [
    one(401, 'Barril x4', 'barrel', 4, 4, 0),
    one(402, 'Cama roja', 'red_bed', 1, 4, 0),
    one(403, 'Soporte de armaduras x2', 'armor_stand', 2, 4, 0),
    one(404, 'Telar', 'loom', 1, 4, 0),
    one(405, 'Alto horno', 'blast_furnace', 1, 6, 500),
    one(406, 'Ahumador', 'smoker', 1, 5, 500),
    one(407, 'Cortapiedras', 'stonecutter', 1, 5, 500),
    one(408, 'Afilador', 'grindstone', 1, 6, 1000),
    one(409, 'Librería x8', 'bookshelf', 8, 8, 1000),
    one(410, 'Cofre de cobre encerado x2', 'waxed_copper_chest', 2, 8, 1500),
    one(411, 'Mesa de herrería', 'smithing_table', 1, 8, 2000),
    one(412, 'Yunque', 'anvil', 1, 16, 2500),
    one(413, 'Tocadiscos', 'jukebox', 1, 10, 2500),
    one(414, 'Atril', 'lectern', 1, 6, 1500),
    one(415, 'Mesa de encantamientos', 'enchanting_table', 1, 26, 3500),
    one(416, 'Cofre de Ender', 'ender_chest', 1, 12, 5000),
    one(417, 'Soporte para pociones', 'brewing_stand', 1, 12, 6667),
    one(418, 'Nexo de reaparición', 'respawn_anchor', 1, 24, 6667),
  ]),
  (5, 'Mecanismos y redstone', 'red', [
    one(501, 'Polvo de redstone x32', 'redstone', 32, 4, 500),
    one(502, 'Pistón x8', 'piston', 8, 6, 1000),
    one(503, 'Pistón pegajoso x8', 'sticky_piston', 8, 10, 1500),
    one(504, 'Observador x8', 'observer', 8, 8, 2000),
    one(505, 'Repetidor x8', 'repeater', 8, 4, 1000),
    one(506, 'Comparador x4', 'comparator', 4, 8, 6667),
    one(507, 'Tolva x4', 'hopper', 4, 12, 1500),
    one(508, 'Dispensador x4', 'dispenser', 4, 6, 1500),
    one(509, 'Soltador x4', 'dropper', 4, 4, 1000),
    one(510, 'Lámpara de redstone x8', 'redstone_lamp', 8, 6, 6667),
    one(511, 'Sensor de luz solar x2', 'daylight_detector', 2, 6, 6667),
    one(512, 'Diana x4', 'target', 4, 5, 1000),
    one(513, 'Bloque de slime x4', 'slime_block', 4, 8, 2500),
    one(514, 'Riel propulsor x8', 'powered_rail', 8, 8, 1500),
  ]),
  (6, 'Naturaleza y granja', 'dark_green', [
    one(601, 'Bloque de pasto x16', 'grass_block', 16, 4, 0),
    one(602, 'Podzol x16', 'podzol', 16, 5, 500),
    one(603, 'Micelio x16', 'mycelium', 16, 6, 1500),
    one(604, 'Bloque de musgo x16', 'moss_block', 16, 5, 1000),
    one(605, 'Nylium carmesí x16', 'crimson_nylium', 16, 6, 6667),
    one(606, 'Nylium distorsionado x16', 'warped_nylium', 16, 6, 6667),
    one(607, 'Estalactita puntiaguda x16', 'pointed_dripstone', 16, 6, 2000),
    one(608, 'Esponja x2', 'sponge', 2, 16, 4500),
    one(609, 'Obsidiana llorosa x8', 'crying_obsidian', 8, 12, 6667),
    (610, 'Pack de brotes (7 árboles x2)', [(s + '_sapling', 2) for s in
        ('oak', 'birch', 'spruce', 'jungle', 'acacia', 'dark_oak', 'cherry')], 6, 0),
    one(611, 'Propágulo de mangle x4', 'mangrove_propagule', 4, 4, 1000),
    (612, 'Hongos del Overworld x8', [('brown_mushroom', 4), ('red_mushroom', 4)], 4, 500),
    (613, 'Hongos del Nether x8', [('crimson_fungus', 4), ('warped_fungus', 4)], 6, 6667),
    one(614, 'Verruga del Nether x8', 'nether_wart', 8, 8, 6667),
    one(615, 'Caña de azúcar x8', 'sugar_cane', 8, 3, 0),
    one(616, 'Cactus x8', 'cactus', 8, 3, 500),
    one(617, 'Bambú x16', 'bamboo', 16, 4, 500),
    (618, 'Semillas surtidas x24', [(s, 4) for s in ('wheat_seeds', 'pumpkin_seeds', 'melon_seeds',
        'beetroot_seeds', 'carrot', 'potato')], 4, 0),
    one(619, 'Granos de cacao x8', 'cocoa_beans', 8, 4, 1000),
    one(620, 'Bayas dulces x8', 'sweet_berries', 8, 3, 500),
  ]),
  (7, 'Alimentos y pociones', 'light_purple', [
    one(701, 'Pan x32', 'bread', 32, 3, 0),
    one(702, 'Torta', 'cake', 1, 4, 0),
    one(703, 'Filete cocinado x16', 'cooked_beef', 16, 5, 500),
    one(704, 'Chuleta cocinada x16', 'cooked_porkchop', 16, 5, 500),
    one(705, 'Zanahoria dorada x16', 'golden_carrot', 16, 10, 2500),
    one(706, 'Manzana dorada x2', 'golden_apple', 2, 8, 3500),
    one(707, 'Manzana de Notch', 'enchanted_golden_apple', 1, 12, 6667),
    one(708, 'Arrojadiza: Curación II x2', splash('strong_healing'), 2, 8, 6667),
    one(709, 'Arrojadiza: Regeneración x2', splash('regeneration'), 2, 10, 6667),
    one(710, 'Arrojadiza: Fuerza II x2', splash('strong_strength'), 2, 10, 6667),
    one(711, 'Arrojadiza: Velocidad II x2', splash('strong_swiftness'), 2, 8, 6667),
    one(712, 'Arrojadiza: Caída lenta x2', splash('slow_falling'), 2, 8, 6667),
    one(713, 'Arrojadiza: Daño II x2', splash('strong_harming'), 2, 8, 6667),
    one(714, 'Arrojadiza: Debilidad x2', splash('weakness'), 2, 6, 6667),
    one(715, 'Arrojadiza: Veneno x2', splash('poison'), 2, 8, 6667),
    one(716, 'Arrojadiza: Infestación x2', splash('infested'), 2, 12, 6667),
  ]),
  (8, 'Decoración y tintes', 'dark_aqua', [
    (801, 'Pack de 16 tintes (x4 c/u)', [(c + '_dye', 4) for c in
        ('white', 'light_gray', 'gray', 'black', 'brown', 'red', 'orange', 'yellow', 'lime',
         'green', 'cyan', 'light_blue', 'blue', 'purple', 'magenta', 'pink')], 6, 0),
    one(802, 'Lana blanca x64', 'white_wool', 64, 4, 0),
    one(803, 'Hormigón blanco x64', 'white_concrete', 64, 5, 500),
    one(804, 'Terracota blanca x64', 'white_terracotta', 64, 5, 500),
    one(805, 'Vidrio blanco x64', 'white_stained_glass', 64, 5, 500),
    one(806, 'Panel de vidrio blanco x64', 'white_stained_glass_pane', 64, 3, 500),
    one(807, 'Vidrio tintado x32', 'tinted_glass', 32, 8, 2500),
    *[(808 + i, f'Azulejos vidriados {i + 1} (4 colores x4)',
       [(c + '_glazed_terracotta', 4) for c in grp], 6, 1500) for i, grp in enumerate([
        ('white', 'light_gray', 'gray', 'black'), ('brown', 'red', 'orange', 'yellow'),
        ('lime', 'green', 'cyan', 'light_blue'), ('blue', 'purple', 'magenta', 'pink')])],
    (812, 'Faroles x8 (normal y de almas)', [('lantern', 4), ('soul_lantern', 4)], 5, 500),
    one(813, 'Cadena x32', 'iron_chain', 32, 4, 500),
    (814, 'Cuadros y marcos brillantes x16', [('painting', 8), ('glow_item_frame', 8)], 4, 0),
    one(815, 'Maceta decorada x4', 'decorated_pot', 4, 5, 1000),
    one(816, 'Andamio x32', 'scaffolding', 32, 4, 0),
  ]),
  (9, 'Huevos generadores', 'white', [
    one(901, 'Huevo de oveja', 'sheep_spawn_egg', 1, 8, 0),
    one(902, 'Huevo de vaca', 'cow_spawn_egg', 1, 8, 0),
    one(903, 'Huevo de cerdo', 'pig_spawn_egg', 1, 8, 0),
    one(904, 'Huevo de gallina', 'chicken_spawn_egg', 1, 6, 0),
    one(905, 'Huevo de caballo', 'horse_spawn_egg', 1, 14, 1000),
    one(906, 'Huevo de lobo', 'wolf_spawn_egg', 1, 12, 1000),
    one(907, 'Huevo de gato', 'cat_spawn_egg', 1, 10, 1000),
    one(908, 'Huevo de abeja', 'bee_spawn_egg', 1, 12, 1500),
    one(909, 'Huevo de gólem de cobre', 'copper_golem_spawn_egg', 1, 14, 1500),
    one(910, 'Huevo de aldeano', 'villager_spawn_egg', 1, 20, 2500),
    one(911, 'Huevo de gólem de hierro', 'iron_golem_spawn_egg', 1, 20, 3500),
    one(912, 'Huevo de allay', 'allay_spawn_egg', 1, 20, 4000),
    one(913, 'Huevo de Happy Ghast', 'happy_ghast_spawn_egg', 1, 20, 5000),
    one(914, 'Huevo de enderman', 'enderman_spawn_egg', 1, 18, 6667),
    one(915, 'Huevo de blaze', 'blaze_spawn_egg', 1, 18, 6667),
    one(916, 'Huevo de esqueleto wither', 'wither_skeleton_spawn_egg', 1, 20, 7500),
  ]),
  (10, 'Libros encantados', 'light_purple', [
    one(1001, 'Reparación', book(mending=1), 1, 34, 4000),
    one(1002, 'Fortuna III', book(fortune=3), 1, 28, 3500),
    one(1003, 'Toque de seda', book(silk_touch=1), 1, 26, 3500),
    one(1004, 'Eficiencia V', book(efficiency=5), 1, 26, 3500),
    one(1005, 'Irrompibilidad III', book(unbreaking=3), 1, 20, 2000),
    one(1006, 'Filo V', book(sharpness=5), 1, 28, 4000),
    one(1007, 'Protección IV', book(protection=4), 1, 24, 3000),
    one(1008, 'Botín III', book(looting=3), 1, 24, 3500),
    one(1009, 'Caída de pluma IV', book(feather_falling=4), 1, 18, 2500),
    one(1010, 'Poder V', book(power=5), 1, 22, 3500),
    one(1011, 'Infinidad', book(infinity=1), 1, 20, 3000),
  ]),
  (11, 'Llaves y contratos', 'gold', [
    one(1101, 'Llave de prueba', 'trial_key', 1, 14, 5000),
    one(1102, 'Llave ominosa', 'ominous_trial_key', 1, 26, 7000),
    one(1103, 'Botella ominosa', 'ominous_bottle', 1, 18, 6000),
    one(1104, 'Llave del Arquitecto', crate_key('trial_key', 'Llave del Arquitecto', 'aqua', 'Crate del Constructor'), 1, 10, 1500),
    one(1105, 'Llave Silvestre', crate_key('trial_key', 'Llave Silvestre', 'green', 'Crate de la Naturaleza'), 1, 10, 1500),
    one(1106, 'Llave Subterránea', crate_key('trial_key', 'Llave Subterránea', 'gray', 'Crate del Minero'), 1, 12, 2500),
    one(1107, 'Llave de Batalla', crate_key('trial_key', 'Llave de Batalla', 'red', 'Crate de Combate'), 1, 12, 2500),
    one(1108, 'Llave Abisal', crate_key('ominous_trial_key', 'Llave Abisal', 'dark_purple', 'Crate Místico'), 1, 20, 5000),
    one(1109, 'Llave del Vacío', crate_key('ominous_trial_key', 'Llave del Vacío', 'gold', 'Crate Legendario'), 1, 26, 7000),
  ]),
  # Sub-sección: llaves Simply OneBlock. Nombre exacto = custom_name plano compartido con so_crates.
  (13, 'Llaves OneBlock', 'gold', [
    one(1300 + i, n, simply_key(b, n), 1, c, u) for i, (n, b, c, u) in enumerate([
      ('Cemetery Key', 'trial_key', 5, 434), ('Graveyard Key', 'trial_key', 5, 434),
      ('Ossuary Key', 'trial_key', 6, 434), ('Old Tower Key', 'trial_key', 7, 434),
      ('Pyramid Key', 'trial_key', 10, 2500), ('Rusty Mineshaft Key', 'trial_key', 11, 2500),
      ('Treasure Room', 'trial_key', 12, 2500), ('Deep_Key', 'trial_key', 14, 2500),
      ('Elder Guardian Key', 'ominous_trial_key', 22, 7000), ('Warden_Key', 'ominous_trial_key', 26, 7000),
      ('Wither Arena', 'ominous_trial_key', 30, 7000), ('To the End', 'trial_key', 28, 7000)], 1)
  ]),
]
# Ventas: (id, nombre, ítem entregado, cantidad, esmeraldas recibidas)
SELLS = [
  (1201, 'Vender 128 tierra', 'dirt', 128, 8), (1202, 'Vender 128 adoquín', 'cobblestone', 128, 12),
  (1203, 'Vender 128 netherrack', 'netherrack', 128, 10), (1204, 'Vender 64 kelp seco', 'dried_kelp', 64, 8),
  (1205, 'Vender 64 troncos de roble', 'oak_log', 64, 16), (1206, 'Vender 64 arena', 'sand', 64, 10),
  (1207, 'Vender 32 lingotes de hierro', 'iron_ingot', 32, 24), (1208, 'Vender 32 lingotes de oro', 'gold_ingot', 32, 28),
]
STACK1 = ('_pickaxe', '_sword', '_axe', '_shovel', '_hoe', '_chestplate', '_leggings', '_boots',
          '_helmet', 'shears', 'horse_armor', 'harness', 'enchanted_book', 'splash_potion', 'cake',
          '_bed', 'decorated_pot')
STACK16 = ('ender_pearl', 'armor_stand')
PREFIX = {'text': '[SO Shop] ', 'color': 'gold'}


def stack(item):
    base = item.split('[', 1)[0]
    if base.endswith(STACK1):
        return 1
    return 16 if base.endswith(STACK16) else 64


def price(c, t):
    return min(c * t - 1, math.ceil(c * t * MULT[t]))


def w(path, lines):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def dlg(name, obj):
    w(DLG / f'{name}.json', [json.dumps(obj, ensure_ascii=False, indent=2)])


def run(cmd):
    return {'type': 'minecraft:run_command', 'command': cmd}


def show(name):
    return {'type': 'minecraft:show_dialog', 'dialog': f'so_shop:{name}'}


def fmt(n):
    return f'{n:,}'.replace(',', '.')


def lock_guard(unlock, then):
    if not unlock:
        return []
    return [f'execute unless score #bypass so_shop matches 1 unless score #blocks so_shop matches {unlock}.. run return run {then}']


# ---------- Limpieza de la versión anterior (artículos, menús y ventanas se regeneran) ----------
for d in (FN / 'item', FN / 'menu', DLG):
    shutil.rmtree(d, ignore_errors=True)
(FN / 'admin/set_unlock.mcfunction').unlink(missing_ok=True)

ALL = [(sec, it) for sec, _, _, items in SECTIONS for it in items]
dispatch, open_cat = [], []

for sec, (iid, name, gives, cost, unlock) in ALL:
    back = f'cat_{sec}'
    locked_msg = (f'tellraw @s {J([PREFIX, {"text": f"{name}: se desbloquea a los {fmt(unlock)} bloques.", "color": "red"}])}')
    w(FN / f'item/locked_{iid}.mcfunction', [locked_msg,
        'playsound minecraft:block.note_block.bass master @s ~ ~ ~ 0.7 0.6',
        f'dialog show @s so_shop:{back}'])
    for t in (1, *MULT):
        charge = cost if t == 1 else price(cost, t)
        slots = sum(math.ceil(n * t / stack(item)) for item, n in gives)
        total = sum(n * t for _, n in gives)
        w(FN / f'item/{iid}_{t}.mcfunction', [
            f'# {name} x{t}: {total} objetos, {charge} esmeraldas',
            *lock_guard(unlock, f'function so_shop:item/locked_{iid}'),
            f'scoreboard players set #cost so_shop {charge}',
            'execute store result score #have so_shop run clear @s minecraft:emerald 0',
            f'execute if score #have so_shop < #cost so_shop run return run function so_shop:lib/fail_reopen {{d:"buy_{iid}"}}',
            'scoreboard players set #slots so_shop 0',
            *[f'execute unless items entity @s container.{n} * run scoreboard players add #slots so_shop 1' for n in range(36)],
            f'execute unless score #slots so_shop matches {slots}.. run return run function so_shop:lib/no_space',
            f'clear @s minecraft:emerald {charge}',
            *[f'give @s minecraft:{item} {n * t}' for item, n in gives],
            'scoreboard players set @s so_shop_cd 20',
            'scoreboard players add @s so_shop_buys 1',
            f'tellraw @s {J([PREFIX, {"text": "Compraste ", "color": "green"}, {"text": name + (f" (x{t})" if t > 1 else ""), "color": "white"}, {"text": f" por {charge} esmeraldas." + (f" Ahorraste {cost * t - charge}." if t > 1 else ""), "color": "green"}])}',
            'playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1',
            'playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4',
            f'dialog show @s so_shop:buy_{iid}'])
        dispatch.append((iid * 10 + t, f'function so_shop:item/{iid}_{t}'))
    # Ventana de detalle con lotes
    tip = f'{cost} E · ' + ('libre' if not unlock else f'desde {fmt(unlock)} bloques')
    dlg(f'buy_{iid}', {
        'type': 'minecraft:multi_action',
        'title': {'text': name, 'color': 'gold'},
        'body': [
            {'type': 'minecraft:item', 'item': {'id': 'minecraft:' + gives[0][0].split('[', 1)[0], 'count': min(99, gives[0][1])},
             'description': {'contents': {'text': name, 'color': 'white'}}},
            {'type': 'minecraft:plain_message', 'contents': {'text': f'Precio unitario: {cost} esmeraldas. Los lotes tienen descuento.', 'color': 'green'}},
        ],
        'columns': 2, 'can_close_with_escape': True, 'pause': False,
        'actions': [{'label': {'text': f'x1 · {cost} E', 'color': 'white'}, 'width': 150, 'action': run(f'/trigger shop_buy set {iid * 10 + 1}')}] + [
            {'label': {'text': f'x{t} · {price(cost, t)} E', 'color': 'green'},
             'tooltip': {'text': f'Ahorrás {cost * t - price(cost, t)} esmeraldas', 'color': 'green'},
             'width': 150, 'action': run(f'/trigger shop_buy set {iid * 10 + t}')} for t in MULT],
        'exit_action': {'label': {'text': '« Volver'}, 'width': 150, 'action': show(back)},
    })
    open_cat.append((10000 + iid, lock_guard(unlock, f'function so_shop:item/locked_{iid}') + [f'dialog show @s so_shop:buy_{iid}']))

for iid, name, item, n, reward in SELLS:
    w(FN / f'item/{iid}_1.mcfunction', [
        f'# {name} -> {reward} esmeraldas',
        'scoreboard players add @s so_sold 0',
        'execute if score @s so_sold >= #sell_limit so_shop run return run function so_shop:lib/sell_limit',
        f'scoreboard players set #cost so_shop {n}',
        f'execute store result score #have so_shop run clear @s minecraft:{item} 0',
        'execute if score #have so_shop < #cost so_shop run return run function so_shop:lib/fail_reopen {d:"cat_12"}',
        f'clear @s minecraft:{item} {n}', f'give @s minecraft:emerald {reward}',
        'scoreboard players set @s so_shop_cd 20', 'scoreboard players add @s so_sold 1',
        f'tellraw @s {J([PREFIX, {"text": f"Venta realizada: +{reward} esmeraldas.", "color": "green"}])}',
        'playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1',
        'dialog show @s so_shop:cat_12'])
    dispatch.append((iid * 10 + 1, f'function so_shop:item/{iid}_1'))
    dlg(f'buy_{iid}', {
        'type': 'minecraft:confirmation', 'title': {'text': 'Confirmar venta', 'color': 'gold'},
        'body': [{'type': 'minecraft:item', 'item': {'id': f'minecraft:{item}', 'count': min(99, n)},
                  'description': {'contents': {'text': name, 'color': 'white'}}},
                 {'type': 'minecraft:plain_message', 'contents': {'text': f'Recibes: {reward} esmeraldas', 'color': 'green'}}],
        'can_close_with_escape': True, 'pause': False,
        'yes': {'label': {'text': 'Vender', 'color': 'green'}, 'action': run(f'/trigger shop_buy set {iid * 10 + 1}')},
        'no': {'label': {'text': '« Volver'}, 'action': show('cat_12')},
    })

# ---------- Ventanas de sección y principal ----------
for sec, title, color, items in SECTIONS:
    actions = []
    if sec == 11:
        actions.append({'label': {'text': '★ Llaves OneBlock', 'color': 'gold', 'bold': True}, 'width': 150, 'action': show('cat_13')})
    for iid, name, _, cost, unlock in items:
        actions.append({'label': {'text': name},
                        'tooltip': {'text': f'{cost} E · ' + ('disponible siempre' if not unlock else f'se desbloquea a los {fmt(unlock)} bloques'), 'color': 'green'},
                        'width': 150, 'action': run(f'/trigger shop_menu set {10000 + iid}')})
    dlg(f'cat_{sec}', {
        'type': 'minecraft:multi_action', 'title': {'text': title, 'color': color, 'bold': True},
        'body': [{'type': 'minecraft:plain_message', 'contents': {'text': 'Toca un artículo para ver precios y lotes. Si está bloqueado, te digo cuántos bloques faltan.', 'color': 'gray'}}],
        'columns': 2, 'can_close_with_escape': True, 'pause': False, 'actions': actions,
        'exit_action': {'label': {'text': '« Volver'}, 'width': 150, 'action': show('cat_11' if sec == 13 else 'main')},
    })
dlg('cat_12', {
    'type': 'minecraft:multi_action', 'title': {'text': 'Vender excedentes', 'color': 'white', 'bold': True},
    'body': [{'type': 'minecraft:plain_message', 'contents': {'text': 'Cambiá lo que te sobra por esmeraldas. Hay un límite de ventas por día.', 'color': 'gray'}}],
    'columns': 2, 'can_close_with_escape': True, 'pause': False,
    'actions': [{'label': {'text': name}, 'tooltip': {'text': f'+{r} esmeraldas', 'color': 'green'}, 'width': 150, 'action': show(f'buy_{iid}')} for iid, name, _, _, r in SELLS],
    'exit_action': {'label': {'text': '« Volver'}, 'width': 150, 'action': show('main')},
})
MAIN = [(s, t, c) for s, t, c, _ in SECTIONS if s != 13] + [(12, 'Vender excedentes', 'white')]
dlg('main', {
    'type': 'minecraft:multi_action', 'title': {'text': 'Tienda OneBlock', 'color': 'gold', 'bold': True},
    'external_title': {'text': 'Tienda'},
    'body': [{'type': 'minecraft:plain_message', 'contents': {'text': 'Todas las secciones están abiertas; algunos artículos se desbloquean con el progreso del OneBlock.', 'color': 'gray'}}],
    'columns': 2, 'can_close_with_escape': True, 'pause': False,
    'actions': [{'label': {'text': t, 'color': c}, 'width': 150, 'action': show(f'cat_{s}')} for s, t, c in MAIN],
    'exit_action': {'label': {'text': 'Menú en el chat'}, 'width': 150, 'action': run('/trigger shop set 2')},
})

# ---------- Menú de chat (respaldo) ----------
main_lines = ['tellraw @s {"text":""}',
    'tellraw @s [{"text":"════ ","color":"dark_gray"},{"text":"TIENDA ONEBLOCK","color":"gold","bold":true},{"text":" ════","color":"dark_gray"}]',
    'tellraw @s [{"text":"Progreso del mundo: ","color":"gray"},{"score":{"name":"#blocks","objective":"so_shop"},"color":"yellow"},{"text":" bloques","color":"gray"}]']
for s, t, c in MAIN + [(13, 'Llaves OneBlock', 'gold')]:
    main_lines.append('tellraw @s ' + J([{'text': '  ▸ ', 'color': 'dark_gray'}, {'text': t, 'color': c, 'bold': True,
        'click_event': {'action': 'run_command', 'command': f'/trigger shop_menu set {100 + s}'}}]))
main_lines.append('playsound minecraft:item.book.page_turn master @s ~ ~ ~ 0.6 1.2')
w(FN / 'menu/main.mcfunction', main_lines)
for sec, title, color, items in SECTIONS:
    lines = ['tellraw @s {"text":""}', 'tellraw @s ' + J({'text': f'══ {title.upper()} ══', 'color': color, 'bold': True})]
    for iid, name, _, cost, unlock in items:
        ok = J([{'text': '  ▸ ', 'color': 'dark_gray'}, {'text': name, 'color': 'white',
                'click_event': {'action': 'run_command', 'command': f'/trigger shop_buy set {iid * 10 + 1}'}},
                {'text': f'  —  {cost} E', 'color': 'green'}])
        if unlock:
            lines.append(f'execute if score #blocks so_shop matches {unlock}.. run tellraw @s {ok}')
            lines.append(f'execute unless score #blocks so_shop matches {unlock}.. run tellraw @s ' + J({'text': f'  ✖ {name} — {fmt(unlock)} bloques', 'color': 'dark_gray'}))
        else:
            lines.append(f'tellraw @s {ok}')
    lines.append('tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}')
    w(FN / f'menu/cat_{sec}.mcfunction', lines)
w(FN / 'menu/cat_12.mcfunction', ['tellraw @s {"text":""}', 'tellraw @s {"text":"══ VENDER EXCEDENTES ══","color":"white","bold":true}'] + [
    'tellraw @s ' + J([{'text': '  ▸ ', 'color': 'dark_gray'}, {'text': name, 'color': 'white', 'click_event': {'action': 'run_command', 'command': f'/trigger shop_buy set {iid * 10 + 1}'}}, {'text': f'  →  +{r} E', 'color': 'green'}])
    for iid, name, _, _, r in SELLS] + ['tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}'])

# ---------- Despachadores agrupados por sección (menos comprobaciones por clic) ----------
def grouped(entries, score, prefix):
    groups = {}
    for val, cmd in entries:
        key = val // 1000 if score == 'shop_buy' else (val - 10000) // 100
        groups.setdefault(key, []).append((val, cmd))
    top = []
    for key, rows in sorted(groups.items()):
        lo, hi = min(v for v, _ in rows), max(v for v, _ in rows)
        top.append(f'execute if score @s {score} matches {lo}..{hi} run function so_shop:lib/{prefix}_{key}')
        out = []
        for v, cmd in rows:
            if isinstance(cmd, list):
                if len(cmd) == 1:
                    out.append(f'execute if score @s {score} matches {v} run {cmd[0]}')
                else:
                    w(FN / f'lib/{prefix}_item_{v}.mcfunction', cmd)
                    out.append(f'execute if score @s {score} matches {v} run function so_shop:lib/{prefix}_item_{v}')
            else:
                out.append(f'execute if score @s {score} matches {v} run {cmd}')
        w(FN / f'lib/{prefix}_{key}.mcfunction', out)
    return top

for old in FN.glob('lib/d_*.mcfunction'):
    old.unlink()
for old in FN.glob('lib/o_*.mcfunction'):
    old.unlink()
w(FN / 'lib/dispatch.mcfunction', ['# shop_buy = id*10 + lote (1,2,3,4,8). Ventas: id 12xx, lote 1.'] + grouped(dispatch, 'shop_buy', 'd'))
w(FN / 'lib/open_cat.mcfunction', [
    '# 1..13: ventana de sección · 101..113: menú de chat · 10000+id: detalle (verifica desbloqueo)',
    *[f'execute if score @s shop_menu matches {s} run dialog show @s so_shop:cat_{s}' for s in range(1, 14)],
    *[f'execute if score @s shop_menu matches {100 + s} run function so_shop:menu/cat_{s}' for s in range(1, 14)],
    *grouped(open_cat, 'shop_menu', 'o')])
w(FN / 'lib/fail_reopen.mcfunction', ['function so_shop:lib/fail', '$dialog show @s so_shop:$(d)'])
w(FN / 'admin/unlock_all.mcfunction', ['scoreboard players set #bypass so_shop 1',
    'tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Todos los artículos desbloqueados (modo admin). Usa so_shop:admin/relock para volver.","color":"yellow"}]'])
w(FN / 'admin/relock.mcfunction', ['scoreboard players set #bypass so_shop 0',
    'tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Los desbloqueos vuelven a depender del progreso del OneBlock.","color":"yellow"}]'])

n_buy = len(ALL)
print(f'so_shop v0.6: {n_buy} artículos de compra, {len(SELLS)} ventas, {len(dispatch)} acciones')
