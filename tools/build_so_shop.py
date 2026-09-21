#!/usr/bin/env python3
"""Genera el datapack so-shop (tienda por comando para Simply OneBlock).

Ejecutar:  python3 tools/build_so_shop.py
Salida:    datapacks/so-shop/  (archivos del datapack)
"""
import json, os, shutil

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "datapacks", "so-shop")
NS = os.path.join(ROOT, "data", "so_shop")
FN = os.path.join(NS, "function")

# ---------------------------------------------------------------- categorias
# (id, clave, titulo, color, umbral por defecto de ib_minedcount)
CATS = [
    (1, "deco",   "Bloques decorativos", "green",        0),
    (2, "color",  "Bloques de color",    "aqua",         0),
    (3, "raros",  "Materiales raros",    "gold",      2500),
    (4, "tools",  "Herramientas",        "yellow",     550),
    (5, "books",  "Libros encantados",   "light_purple", 4000),
    (6, "eggs",   "Huevos generadores",  "red",       7000),
    (7, "keys",   "Llaves y contratos",  "dark_purple", 8250),
    (8, "sell",   "Vender excedentes",   "white",        0),
]

E = "minecraft:emerald"

# (id, cat, nombre visible, item que se entrega, cantidad, item de pago, coste)
ITEMS = [
    # --- 1 decorativos -----------------------------------------------------
    (101, 1, "Farol x8",            "minecraft:lantern", 8,            E, 6),
    (102, 1, "Andamio x32",         "minecraft:scaffolding", 32,       E, 4),
    (103, 1, "Maceta decorada x4",  "minecraft:decorated_pot", 4,      E, 5),
    (104, 1, "Bloque de ámbar x8",  "minecraft:honeycomb_block", 8,    E, 6),
    (105, 1, "Cadena x32",          "minecraft:chain", 32,             E, 5),
    (106, 1, "Campana",             "minecraft:bell", 1,               E, 12),
    (107, 1, "Cuadro x8",           "minecraft:painting", 8,           E, 4),
    (108, 1, "Marco de ítem brillante x8", "minecraft:glow_item_frame", 8, E, 5),
    # --- 2 colores ---------------------------------------------------------
    (201, 2, "Lana de colores x64 (blanca)", "minecraft:white_wool", 64, E, 4),
    (202, 2, "Terracota vidriada surtida x16", "minecraft:blue_glazed_terracotta", 16, E, 8),
    (203, 2, "Cristal tintado x32", "minecraft:tinted_glass", 32,      E, 10),
    (204, 2, "Concreto x64 (rojo)",  "minecraft:red_concrete", 64,     E, 6),
    (205, 2, "Concreto x64 (azul)",  "minecraft:blue_concrete", 64,    E, 6),
    (206, 2, "Tintes surtidos x16",  "minecraft:lapis_lazuli", 16,     E, 3),
    (207, 2, "Cristal coloreado x64 (cian)", "minecraft:cyan_stained_glass", 64, E, 6),
    (208, 2, "Copper grate x32",     "minecraft:copper_grate", 32,     E, 7),
    # --- 3 materiales raros ------------------------------------------------
    (301, 3, "Bloque de cuarzo x32", "minecraft:quartz_block", 32,     E, 12),
    (302, 3, "Fragmento de prismarina x32", "minecraft:prismarine_shard", 32, E, 10),
    (303, 3, "Sculk x32",            "minecraft:sculk", 32,            E, 14),
    (304, 3, "Fragmento de eco x2",  "minecraft:echo_shard", 2,        E, 20),
    (305, 3, "Corazón del mar",      "minecraft:heart_of_the_sea", 1,  E, 28),
    (306, 3, "Bloque de amatista x16", "minecraft:amethyst_block", 16, E, 9),
    (307, 3, "Netherite scrap x2",   "minecraft:netherite_scrap", 2,   E, 40),
    (308, 3, "Lodestone",            "minecraft:lodestone", 1,         E, 24),
    (309, 3, "Fruta chorus x32",     "minecraft:chorus_fruit", 32,     E, 10),
    (310, 3, "Caparazón de shulker x2", "minecraft:shulker_shell", 2,  E, 45),
    # --- 4 herramientas ----------------------------------------------------
    (401, 4, "Pico de hierro (Eficiencia III)", "minecraft:iron_pickaxe[minecraft:enchantments={\"minecraft:efficiency\":3}]", 1, E, 14),
    (402, 4, "Pico de diamante",     "minecraft:diamond_pickaxe", 1,   E, 26),
    (403, 4, "Hacha de diamante",    "minecraft:diamond_axe", 1,       E, 24),
    (404, 4, "Azada de diamante (Fortuna II)", "minecraft:diamond_hoe[minecraft:enchantments={\"minecraft:fortune\":2}]", 1, E, 22),
    (405, 4, "Tijeras (Toque de seda)", "minecraft:shears[minecraft:enchantments={\"minecraft:silk_touch\":1}]", 1, E, 16),
    (406, 4, "Cubo de agua x2",      "minecraft:water_bucket", 2,      E, 8),
    (407, 4, "Yunque",               "minecraft:anvil", 1,             E, 18),
    (408, 4, "Brújula de recuperación", "minecraft:recovery_compass", 1, E, 30),
    # --- 5 libros encantados ----------------------------------------------
    (501, 5, "Libro: Reparación",    "minecraft:enchanted_book[minecraft:stored_enchantments={\"minecraft:mending\":1}]", 1, E, 34),
    (502, 5, "Libro: Fortuna III",   "minecraft:enchanted_book[minecraft:stored_enchantments={\"minecraft:fortune\":3}]", 1, E, 30),
    (503, 5, "Libro: Toque de seda", "minecraft:enchanted_book[minecraft:stored_enchantments={\"minecraft:silk_touch\":1}]", 1, E, 28),
    (504, 5, "Libro: Eficiencia IV", "minecraft:enchanted_book[minecraft:stored_enchantments={\"minecraft:efficiency\":4}]", 1, E, 24),
    (505, 5, "Libro: Irrompibilidad III", "minecraft:enchanted_book[minecraft:stored_enchantments={\"minecraft:unbreaking\":3}]", 1, E, 22),
    (506, 5, "Libro: Protección IV", "minecraft:enchanted_book[minecraft:stored_enchantments={\"minecraft:protection\":4}]", 1, E, 26),
    (507, 5, "Libro: Botín III",     "minecraft:enchanted_book[minecraft:stored_enchantments={\"minecraft:looting\":3}]", 1, E, 26),
    (508, 5, "Libro: Caída de pluma IV", "minecraft:enchanted_book[minecraft:stored_enchantments={\"minecraft:feather_falling\":4}]", 1, E, 18),
    # --- 6 huevos generadores ---------------------------------------------
    (601, 6, "Huevo: Oveja",         "minecraft:sheep_spawn_egg", 1,   E, 12),
    (602, 6, "Huevo: Vaca",          "minecraft:cow_spawn_egg", 1,     E, 12),
    (603, 6, "Huevo: Gallina",       "minecraft:chicken_spawn_egg", 1, E, 10),
    (604, 6, "Huevo: Cerdo",         "minecraft:pig_spawn_egg", 1,     E, 12),
    (605, 6, "Huevo: Abeja",         "minecraft:bee_spawn_egg", 1,     E, 18),
    (606, 6, "Huevo: Allay",         "minecraft:allay_spawn_egg", 1,   E, 40),
    (607, 6, "Huevo: Axolote",       "minecraft:axolotl_spawn_egg", 1, E, 22),
    (608, 6, "Huevo: Sniffer",       "minecraft:sniffer_spawn_egg", 1, E, 45),
    # --- 7 llaves y contratos ---------------------------------------------
    (701, 7, "Llave de prueba",      "minecraft:trial_key", 1,         E, 16),
    (702, 7, "Llave ominosa",        "minecraft:ominous_trial_key", 1, E, 32),
    (703, 7, "Botella ominosa",      "minecraft:ominous_bottle", 1,    E, 20),
    (704, 7, "Llave de Mazmorra",    "minecraft:tripwire_hook[minecraft:item_name='{\"text\":\"Llave de Mazmorra\",\"color\":\"gold\",\"italic\":false}',minecraft:custom_data={so_key:\"dungeon\"},minecraft:enchantment_glint_override=true]", 1, E, 24),
    (705, 7, "Contrato de Invasión", "minecraft:paper[minecraft:item_name='{\"text\":\"Contrato de Invasión\",\"color\":\"red\",\"italic\":false}',minecraft:custom_data={so_contract:\"invasion\"},minecraft:enchantment_glint_override=true]", 1, E, 28),
    (706, 7, "Boleto de Arena",      "minecraft:paper[minecraft:item_name='{\"text\":\"Boleto de Arena\",\"color\":\"aqua\",\"italic\":false}',minecraft:custom_data={so_ticket:\"arena\"},minecraft:enchantment_glint_override=true]", 1, E, 18),
]

# venta de excedentes: (id, nombre, item entregado, cant pago, item de pago, coste)
SELL = [
    (801, "Vender 128 tierra",      4,  "minecraft:dirt", 128),
    (802, "Vender 128 piedra",      6,  "minecraft:cobblestone", 128),
    (803, "Vender 128 netherrack",  5,  "minecraft:netherrack", 128),
    (804, "Vender 64 kelp seco",    4,  "minecraft:dried_kelp", 64),
    (805, "Vender 64 troncos",      8,  "minecraft:oak_log", 64),
    (806, "Vender 64 arena",        5,  "minecraft:sand", 64),
    (807, "Vender 32 hierro",      12,  "minecraft:iron_ingot", 32),
    (808, "Vender 32 oro",         14,  "minecraft:gold_ingot", 32),
]

SELL_DAILY_LIMIT = 6  # ventas por jugador y por día


def w(path, text):
    full = os.path.join(FN, path + ".mcfunction")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")


def jw(path, obj):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def build():
    if os.path.isdir(ROOT):
        shutil.rmtree(ROOT)
    os.makedirs(ROOT, exist_ok=True)

    jw("pack.mcmeta", {"pack": {"pack_format": 107,
                               "description": "Simply OneBlock Expansion - Shop (/trigger shop)"}})
    jw("data/minecraft/tags/function/load.json", {"replace": False, "values": ["so_shop:init"]})
    jw("data/minecraft/tags/function/tick.json", {"replace": False, "values": ["so_shop:tick"]})

    # ------------------------------------------------------------------ init
    init = [
        "scoreboard objectives add so_shop dummy",
        "scoreboard objectives add so_sold dummy",
        'scoreboard objectives add shop trigger',
        'scoreboard objectives add shop_menu trigger',
        'scoreboard objectives add shop_buy trigger',
        "",
        "execute unless score #enabled so_shop matches -2147483648.. run scoreboard players set #enabled so_shop 1",
        "execute unless score #day so_shop matches -2147483648.. run scoreboard players set #day so_shop 0",
        f"execute unless score #sell_limit so_shop matches -2147483648.. run scoreboard players set #sell_limit so_shop {SELL_DAILY_LIMIT}",
    ]
    for cid, key, title, color, thr in CATS:
        init.append(f"execute unless score #t{cid} so_shop matches -2147483648.. run scoreboard players set #t{cid} so_shop {thr}")
        init.append(f"scoreboard players set #u{cid} so_shop 0")
    init += [
        "",
        'tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Tienda cargada. Usa ","color":"green"},{"text":"/trigger shop","color":"yellow"},{"text":" para abrirla.","color":"green"}]',
    ]
    w("init", "\n".join(init))

    # ------------------------------------------------------------------ tick
    w("tick", "\n".join([
        "execute if score #enabled so_shop matches 1 run function so_shop:lib/progress",
        "execute if score #enabled so_shop matches 1 as @a[scores={shop=1..}] at @s run function so_shop:menu/main",
        "scoreboard players reset @a shop",
        "scoreboard players enable @a shop",
        "execute if score #enabled so_shop matches 1 as @a[scores={shop_menu=1..}] at @s run function so_shop:lib/open_cat",
        "scoreboard players reset @a shop_menu",
        "scoreboard players enable @a shop_menu",
        "execute if score #enabled so_shop matches 1 as @a[scores={shop_buy=1..}] at @s run function so_shop:lib/dispatch",
        "scoreboard players reset @a shop_buy",
        "scoreboard players enable @a shop_buy",
    ]))

    # -------------------------------------------------------------- progreso
    prog = [
        "# Lee el progreso del mundo. Usa so_core si esta presente; si no, lee ib_minedcount.",
        "execute if score #blocks so_core matches -2147483648.. run scoreboard players operation #blocks so_shop = #blocks so_core",
        "execute unless score #blocks so_core matches -2147483648.. if score fake_player ib_minedcount matches -2147483648.. run scoreboard players operation #blocks so_shop = fake_player ib_minedcount",
        "execute unless score #blocks so_shop matches -2147483648.. run scoreboard players set #blocks so_shop 0",
    ]
    for cid, key, title, color, thr in CATS:
        prog.append(f"scoreboard players set #u{cid} so_shop 0")
        prog.append(f"execute if score #blocks so_shop >= #t{cid} so_shop run scoreboard players set #u{cid} so_shop 1")
    prog += [
        "# Reinicio diario del limite de venta",
        "execute store result score #tod so_shop run time query daytime",
        "execute if score #tod so_shop matches 0..40 if score #day so_shop matches 0 run function so_shop:lib/new_day",
        "execute if score #tod so_shop matches 41.. run scoreboard players set #day so_shop 0",
    ]
    w("lib/progress", "\n".join(prog))

    w("lib/new_day", "\n".join([
        "scoreboard players set #day so_shop 1",
        "scoreboard players reset @a so_sold",
        'tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Nuevo día: el límite de ventas se ha reiniciado.","color":"gray"}]',
    ]))

    # ------------------------------------------------------------ menu main
    main = ['tellraw @s {"text":""}',
            'tellraw @s [{"text":"════ ","color":"dark_gray"},{"text":"TIENDA ONEBLOCK","color":"gold","bold":true},{"text":" ════","color":"dark_gray"}]',
            'tellraw @s [{"text":"Progreso del mundo: ","color":"gray"},{"score":{"name":"#blocks","objective":"so_shop"},"color":"yellow"},{"text":" bloques","color":"gray"}]',
            'tellraw @s {"text":""}']
    for cid, key, title, color, thr in CATS:
        main.append(
            f'execute if score #u{cid} so_shop matches 1 run tellraw @s [{{"text":"  ▸ ","color":"dark_gray"}},'
            f'{{"text":"{title}","color":"{color}","bold":true,'
            f'"click_event":{{"action":"run_command","command":"/trigger shop_menu set {cid}"}},'
            f'"hover_event":{{"action":"show_text","value":{{"text":"Abrir {title}","color":"{color}"}}}}}}]'
        )
        main.append(
            f'execute if score #u{cid} so_shop matches 0 run tellraw @s [{{"text":"  ✖ ","color":"dark_gray"}},'
            f'{{"text":"{title}","color":"dark_gray","strikethrough":true}},'
            f'{{"text":"  (se abre a ","color":"dark_gray"}},'
            f'{{"score":{{"name":"#t{cid}","objective":"so_shop"}},"color":"dark_gray"}},'
            f'{{"text":" bloques)","color":"dark_gray"}}]'
        )
    main += ['tellraw @s {"text":""}',
             'tellraw @s [{"text":"Pago en esmeraldas. Haz clic en un artículo para comprarlo.","color":"dark_gray","italic":true}]',
             "playsound minecraft:item.book.page_turn master @s ~ ~ ~ 0.6 1.4"]
    w("menu/main", "\n".join(main))

    # dispatcher de categorias
    oc = []
    for cid, key, title, color, thr in CATS:
        oc.append(f"execute if score @s shop_menu matches {cid} if score #u{cid} so_shop matches 1 run function so_shop:menu/cat_{key}")
        oc.append(f"execute if score @s shop_menu matches {cid} if score #u{cid} so_shop matches 0 run function so_shop:lib/locked")
    w("lib/open_cat", "\n".join(oc))

    w("lib/locked", "\n".join([
        'tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Esa sección todavía no está disponible. Sigue minando el OneBlock.","color":"red"}]',
        "playsound minecraft:block.note_block.bass master @s ~ ~ ~ 0.7 0.6",
    ]))

    # ---------------------------------------------------------- paginas cat
    for cid, key, title, color, thr in CATS:
        lines = ['tellraw @s {"text":""}',
                 f'tellraw @s [{{"text":"════ ","color":"dark_gray"}},{{"text":"{title.upper()}","color":"{color}","bold":true}},{{"text":" ════","color":"dark_gray"}}]']
        if cid == 8:
            lines.append('tellraw @s [{"text":"Ventas restantes hoy: ","color":"gray"},{"score":{"name":"@s","objective":"so_sold"},"color":"yellow"},{"text":" / ","color":"gray"},{"score":{"name":"#sell_limit","objective":"so_shop"},"color":"yellow"},{"text":" usadas","color":"gray"}]')
            for iid, name, pay, item, cnt in SELL:
                lines.append(
                    f'tellraw @s [{{"text":"  ▸ ","color":"dark_gray"}},'
                    f'{{"text":"{name}","color":"white",'
                    f'"click_event":{{"action":"run_command","command":"/trigger shop_buy set {iid}"}},'
                    f'"hover_event":{{"action":"show_text","value":{{"text":"Clic para vender","color":"green"}}}}}},'
                    f'{{"text":"  →  ","color":"dark_gray"}},'
                    f'{{"text":"{pay} esmeraldas","color":"green"}}]'
                )
        else:
            for iid, icat, name, give, gcnt, pitem, pcnt in ITEMS:
                if icat != cid:
                    continue
                lines.append(
                    f'tellraw @s [{{"text":"  ▸ ","color":"dark_gray"}},'
                    f'{{"text":"{name}","color":"white",'
                    f'"click_event":{{"action":"run_command","command":"/trigger shop_buy set {iid}"}},'
                    f'"hover_event":{{"action":"show_text","value":{{"text":"Clic para comprar","color":"green"}}}}}},'
                    f'{{"text":"  —  ","color":"dark_gray"}},'
                    f'{{"text":"{pcnt} esmeraldas","color":"green"}}]'
                )
        lines += ['tellraw @s {"text":""}',
                  'tellraw @s [{"text":"  « Volver al menú","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop"}}]',
                  "playsound minecraft:item.book.page_turn master @s ~ ~ ~ 0.6 1.2"]
        w(f"menu/cat_{key}", "\n".join(lines))

    # ------------------------------------------------------------- dispatch
    dis = []
    for iid, icat, name, give, gcnt, pitem, pcnt in ITEMS:
        dis.append(f"execute if score @s shop_buy matches {iid} if score #u{icat} so_shop matches 1 run function so_shop:item/{iid}")
        dis.append(f"execute if score @s shop_buy matches {iid} if score #u{icat} so_shop matches 0 run function so_shop:lib/locked")
    for iid, name, pay, item, cnt in SELL:
        dis.append(f"execute if score @s shop_buy matches {iid} run function so_shop:item/{iid}")
    w("lib/dispatch", "\n".join(dis))

    # --------------------------------------------------------------- items
    for iid, icat, name, give, gcnt, pitem, pcnt in ITEMS:
        w(f"item/{iid}", "\n".join([
            f"# {name}",
            f"scoreboard players set #cost so_shop {pcnt}",
            f"execute store result score #have so_shop run clear @s {pitem} 0",
            f"execute if score #have so_shop >= #cost so_shop run function so_shop:item/{iid}_ok",
            "execute if score #have so_shop < #cost so_shop run function so_shop:lib/fail",
        ]))
        w(f"item/{iid}_ok", "\n".join([
            f"clear @s {pitem} {pcnt}",
            f"give @s {give} {gcnt}",
            f'tellraw @s [{{"text":"[SO Shop] ","color":"gold"}},{{"text":"Compraste ","color":"green"}},{{"text":"{name}","color":"white"}},{{"text":" por {pcnt} esmeraldas.","color":"green"}}]',
            "playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1",
            "playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4",
        ]))

    for iid, name, pay, item, cnt in SELL:
        w(f"item/{iid}", "\n".join([
            f"# {name}",
            "scoreboard players add @s so_sold 0",
            f"scoreboard players set #cost so_shop {cnt}",
            f"execute store result score #have so_shop run clear @s {item} 0",
            f"execute if score @s so_sold >= #sell_limit so_shop run function so_shop:lib/sell_limit",
            f"execute if score @s so_sold < #sell_limit so_shop if score #have so_shop >= #cost so_shop run function so_shop:item/{iid}_ok",
            f"execute if score @s so_sold < #sell_limit so_shop if score #have so_shop < #cost so_shop run function so_shop:lib/fail",
        ]))
        w(f"item/{iid}_ok", "\n".join([
            f"clear @s {item} {cnt}",
            f"give @s minecraft:emerald {pay}",
            "scoreboard players add @s so_sold 1",
            f'tellraw @s [{{"text":"[SO Shop] ","color":"gold"}},{{"text":"Venta realizada: +{pay} esmeraldas.","color":"green"}}]',
            "playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1",
        ]))

    w("lib/fail", "\n".join([
        "scoreboard players operation #falta so_shop = #cost so_shop",
        "scoreboard players operation #falta so_shop -= #have so_shop",
        'tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"No te alcanza. Te faltan ","color":"red"},{"score":{"name":"#falta","objective":"so_shop"},"color":"yellow"},{"text":" unidades del pago.","color":"red"}]',
        "playsound minecraft:entity.villager.no master @s ~ ~ ~ 1 1",
    ]))

    w("lib/sell_limit", "\n".join([
        'tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Llegaste al límite de ventas de hoy. Vuelve mañana.","color":"red"}]',
        "playsound minecraft:entity.villager.no master @s ~ ~ ~ 1 1",
    ]))

    # ---------------------------------------------------------------- admin
    w("admin/enable", '\n'.join([
        "scoreboard players set #enabled so_shop 1",
        'tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Tienda activada.","color":"green"}]',
    ]))
    w("admin/disable", '\n'.join([
        "scoreboard players set #enabled so_shop 0",
        'tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Tienda desactivada.","color":"yellow"}]',
    ]))
    w("admin/unlock_all", "\n".join(
        [f"scoreboard players set #t{cid} so_shop 0" for cid, *_ in CATS] +
        ['tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Todas las secciones desbloqueadas.","color":"yellow"}]']
    ))
    w("admin/set_unlock", "\n".join([
        "# Uso: function so_shop:admin/set_unlock {cat:3,value:2500}",
        "$scoreboard players set #t$(cat) so_shop $(value)",
        '$tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Sección $(cat) se abre a $(value) bloques.","color":"yellow"}]',
    ]))
    w("admin/set_sell_limit", "\n".join([
        "# Uso: function so_shop:admin/set_sell_limit {value:6}",
        "$scoreboard players set #sell_limit so_shop $(value)",
        '$tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Límite diario de ventas: $(value).","color":"yellow"}]',
    ]))
    w("admin/give_emeralds", "\n".join([
        "# Uso: function so_shop:admin/give_emeralds {value:32}",
        "$give @s minecraft:emerald $(value)",
    ]))
    w("uninstall", "\n".join([
        "scoreboard objectives remove so_shop",
        "scoreboard objectives remove so_sold",
        "scoreboard objectives remove shop",
        "scoreboard objectives remove shop_menu",
        "scoreboard objectives remove shop_buy",
        'tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Tienda retirada. Simply OneBlock no fue modificado.","color":"red"}]',
    ]))

    n = sum(len(files) for _, _, files in os.walk(ROOT))
    print(f"so-shop generado en {ROOT} ({n} archivos)")
    print(f"Artículos: {len(ITEMS)} compras + {len(SELL)} ventas")


if __name__ == "__main__":
    build()
