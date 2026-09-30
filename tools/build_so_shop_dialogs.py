#!/usr/bin/env python3
"""Genera TODAS las ventanas (dialogs) de so_shop leyendo el catálogo ya generado
(menu/cat_*.mcfunction para nombres/precios, item/*_ok.mcfunction para objetos).
Uso: python3 tools/build_so_shop_dialogs.py
"""
import json, pathlib, re

DP = pathlib.Path(__file__).resolve().parent.parent / "datapacks/so-shop/data/so_shop"
FN, ROOT = DP / "function", DP / "dialog"
ROOT.mkdir(parents=True, exist_ok=True)
for f in ROOT.glob("*.json"):
    f.unlink()

SECTIONS = [  # (id, nombre, color, archivo menu)
    (1, "Bloques decorativos", "green", "cat_deco"), (2, "Bloques de color", "aqua", "cat_color"),
    (3, "Materiales raros", "gold", "cat_raros"), (4, "Herramientas", "yellow", "cat_tools"),
    (5, "Libros encantados", "light_purple", "cat_books"), (6, "Huevos generadores", "red", "cat_eggs"),
    (7, "Llaves y contratos", "dark_aqua", "cat_keys"), (8, "Vender excedentes", "white", "cat_sell"),
]
LINE = re.compile(r'"text":"([^"]+)","color":"white","click_event":\{"action":"run_command","command":"/trigger shop_buy set (\d+)"\}.*?"text":"(\d+) ([^"]+)"')


def cmd(c): return {"type": "minecraft:run_command", "command": c}
def show(d): return {"type": "minecraft:show_dialog", "dialog": d}
def msg(t, c="gray"): return {"type": "minecraft:plain_message", "contents": {"text": t, "color": c}}
def write(n, d): (ROOT / f"{n}.json").write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def stack(line):  # "give @s minecraft:x[...] 3" -> (id, count)
    m = re.match(r'(?:give|clear) @s (minecraft:[a-z0-9_]+)(?:\[.*\])? (\d+)\s*$', line.strip())
    return (m.group(1), int(m.group(2))) if m else None


write("main", {
    "type": "minecraft:multi_action",
    "title": {"text": "Tienda OneBlock", "color": "gold", "bold": True},
    "external_title": {"text": "Tienda"},
    "body": [msg("Elige una sección. Las bloqueadas te dirán cuántos bloques faltan.")],
    "columns": 2, "can_close_with_escape": True, "pause": False,
    "actions": [{"label": {"text": n, "color": c}, "width": 150, "action": cmd(f"/trigger shop_menu set {i}")}
                for i, n, c, _ in SECTIONS],
    "exit_action": {"label": {"text": "Menú en el chat"}, "width": 150, "action": cmd("/trigger shop set 2")},
})

total = 0
for sid, sname, color, mfile in SECTIONS:
    sell = sid == 8
    items = []
    for ln in (FN / "menu" / f"{mfile}.mcfunction").read_text(encoding="utf-8").splitlines():
        m = LINE.search(ln)
        if not m:
            continue
        name, iid, price, cur = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        ok = (FN / "item" / f"{iid}_ok.mcfunction").read_text(encoding="utf-8").splitlines()
        pay = stack(next(l for l in ok if l.startswith("clear")))
        get = stack(next(l for l in ok if l.startswith("give")))
        items.append((iid, name, price, cur, pay, get))
    body = [msg("Toca un artículo para ver el detalle y confirmar.")]
    if sell:
        body = [msg("Toca lo que quieras vender. Hay un límite diario de ventas (se reinicia cada día)."),]
    write(mfile, {
        "type": "minecraft:multi_action",
        "title": {"text": sname, "color": color, "bold": True},
        "body": body, "columns": 2, "can_close_with_escape": True, "pause": False,
        "actions": [{"label": {"text": n}, "tooltip": {"text": f"{p} {c}", "color": "green"},
                     "width": 150, "action": show(f"so_shop:buy_{i}")} for i, n, p, c, _, _ in items],
        "exit_action": {"label": {"text": "« Volver"}, "width": 150, "action": show("so_shop:main")},
    })
    for iid, name, price, cur, pay, get in items:
        shown, give_line = (pay, f"Recibes: {price} {cur}") if sell else (get, f"Precio: {price} {cur}")
        b = []
        if shown:
            b.append({"type": "minecraft:item", "item": {"id": shown[0], "count": min(shown[1], 99)},
                      "description": {"contents": {"text": name, "color": "white"}}})
        else:
            b.append(msg(name, "white"))
        b.append(msg(give_line, "green"))
        write(f"buy_{iid}", {
            "type": "minecraft:confirmation",
            "title": {"text": "Confirmar venta" if sell else "Confirmar compra", "color": "gold"},
            "body": b, "can_close_with_escape": True, "pause": False,
            "yes": {"label": {"text": "Vender" if sell else "Comprar", "color": "green"},
                    "action": cmd(f"/trigger shop_buy set {iid}")},
            "no": {"label": {"text": "« Volver"}, "action": show(f"so_shop:{mfile}")},
        })
        total += 1
    print(sname, len(items))

# open_cat: todas las secciones abren su ventana
oc = []
for sid, _, _, mfile in SECTIONS:
    oc.append(f"execute if score @s shop_menu matches {sid} if score #u{sid} so_shop matches 1 run dialog show @s so_shop:{mfile}")
    oc.append(f"execute if score @s shop_menu matches {sid} if score #u{sid} so_shop matches 0 run function so_shop:lib/locked")
(FN / "lib/open_cat.mcfunction").write_text("\n".join(oc) + "\n", encoding="utf-8")
print("artículos:", total)
