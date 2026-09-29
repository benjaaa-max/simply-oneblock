#!/usr/bin/env python3
"""Genera las ventanas (dialogs) de so_shop. Prueba piloto: menú principal + sección Decorativos.
Uso: python3 tools/build_so_shop_dialogs.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "datapacks/so-shop/data/so_shop/dialog"
ROOT.mkdir(parents=True, exist_ok=True)

SECTIONS = [
    (1, "Bloques decorativos", "green"), (2, "Bloques de color", "aqua"),
    (3, "Materiales raros", "gold"), (4, "Herramientas", "yellow"),
    (5, "Libros encantados", "light_purple"), (6, "Huevos generadores", "red"),
    (7, "Llaves y contratos", "dark_aqua"), (8, "Vender excedentes", "white"),
]

DECO = [
    (101, "Farol", "minecraft:lantern", 8, 6),
    (102, "Andamio", "minecraft:scaffolding", 32, 4),
    (103, "Maceta decorada", "minecraft:decorated_pot", 4, 5),
    (104, "Bloque de panal", "minecraft:honeycomb_block", 8, 6),
    (105, "Cadena", "minecraft:iron_chain", 32, 5),
    (106, "Campana", "minecraft:bell", 1, 12),
    (107, "Cuadro", "minecraft:painting", 8, 4),
    (108, "Marco brillante", "minecraft:glow_item_frame", 8, 5),
]


def cmd(c):
    return {"type": "minecraft:run_command", "command": c}


def show(d):
    return {"type": "minecraft:show_dialog", "dialog": d}


def msg(text, color="gray"):
    return {"type": "minecraft:plain_message", "contents": {"text": text, "color": color}}


def write(name, data):
    (ROOT / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


main = {
    "type": "minecraft:multi_action",
    "title": {"text": "Tienda OneBlock", "color": "gold", "bold": True},
    "external_title": {"text": "Tienda"},
    "body": [msg("Elige una sección. Las bloqueadas te dirán cuántos bloques faltan.")],
    "columns": 2,
    "can_close_with_escape": True,
    "pause": False,
    "actions": [
        {"label": {"text": n, "color": c}, "width": 150, "action": cmd(f"/trigger shop_menu set {i}")}
        for i, n, c in SECTIONS
    ],
    "exit_action": {"label": {"text": "Menú en el chat"}, "width": 150, "action": cmd("/trigger shop set 2")},
}
write("main", main)

deco = {
    "type": "minecraft:multi_action",
    "title": {"text": "Bloques decorativos", "color": "green", "bold": True},
    "body": [msg("Toca un artículo para ver el precio y confirmar la compra.")],
    "columns": 2,
    "can_close_with_escape": True,
    "pause": False,
    "actions": [
        {"label": {"text": f"{n} x{q}" if q > 1 else n},
         "tooltip": {"text": f"{p} esmeraldas", "color": "green"},
         "width": 150, "action": show(f"so_shop:buy_{i}")}
        for i, n, _, q, p in DECO
    ],
    "exit_action": {"label": {"text": "« Volver"}, "width": 150, "action": show("so_shop:main")},
}
write("cat_deco", deco)

for i, n, item, q, p in DECO:
    write(f"buy_{i}", {
        "type": "minecraft:confirmation",
        "title": {"text": "Confirmar compra", "color": "gold"},
        "body": [
            {"type": "minecraft:item", "item": {"id": item, "count": q},
             "description": {"contents": {"text": f"{n} x{q}", "color": "white"}}},
            msg(f"Precio: {p} esmeraldas", "green"),
        ],
        "can_close_with_escape": True,
        "pause": False,
        "yes": {"label": {"text": "Comprar", "color": "green"}, "action": cmd(f"/trigger shop_buy set {i}")},
        "no": {"label": {"text": "« Volver"}, "action": show("so_shop:cat_deco")},
    })

print("dialogs:", sorted(p.name for p in ROOT.iterdir()))
