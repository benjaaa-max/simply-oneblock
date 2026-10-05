#!/usr/bin/env python3
"""Extiende el pack YA corregido de so-shop: llaves OneBlock y lotes.
Uso: python3 tools/extend_so_shop.py (después del generador original, si se regenera).
Es idempotente: no duplica artículos ni menús al repetirlo.
"""
from pathlib import Path
import json
import math
import re
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent / 'datapacks/so-shop'
FN = ROOT / 'data/so_shop/function'
# (ID, nombre exacto, ítem, coste, fase mínima de compra)
# Estas llaves son exactamente las de so_crates:give/*: el nombre plano es el componente custom_name.
KEYS = [
    (711, 'Cemetery Key', 'trial_key', 5, 434),
    (712, 'Graveyard Key', 'trial_key', 5, 434),
    (713, 'Ossuary Key', 'trial_key', 6, 434),
    (714, 'Old Tower Key', 'trial_key', 7, 434),
    (715, 'Pyramid Key', 'trial_key', 10, 2500),
    (716, 'Rusty Mineshaft Key', 'trial_key', 11, 2500),
    (717, 'Treasure Room', 'trial_key', 12, 2500),
    (718, 'Deep_Key', 'trial_key', 14, 2500),
    (719, 'Elder Guardian Key', 'ominous_trial_key', 22, 7000),
    (720, 'Warden_Key', 'ominous_trial_key', 26, 7000),
    (721, 'Wither Arena', 'ominous_trial_key', 30, 7000),
    (722, 'To the End', 'trial_key', 28, 7000),
]
# Coste final = techo(cost_unitario * cantidad * factor). Nunca supera el precio normal.
MULTIPLIERS = {2: .95, 3: .92, 4: .88, 8: .82}
UNSTACKABLE = {'water_bucket', 'lava_bucket', 'iron_pickaxe', 'diamond_pickaxe',
               'diamond_axe', 'diamond_hoe', 'shears', 'enchanted_book',
               'recovery_compass'}


def write(path, lines):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def price(base, times):
    return min(base * times - 1, math.ceil(base * times * MULTIPLIERS[times]))


def dialog(name, obj):
    path = ROOT / f'data/so_shop/dialog/{name}.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def show(name):
    return {'type': 'minecraft:show_dialog', 'dialog': f'so_shop:{name}'}


def command(text):
    return {'type': 'minecraft:run_command', 'command': text}


# Existing article data comes from the actual corrected pack, not the old baseline generator.
existing = []
names = {}
for path in sorted((FN / 'item').glob('*_ok.mcfunction')):
    if not path.stem[:-3].isdigit():
        continue
    iid = int(path.stem[:-3])
    if iid >= 800 or 711 <= iid <= 722:
        continue
    text = path.read_text(encoding='utf-8')
    clear = re.search(r'^clear @s minecraft:emerald (\d+)$', text, re.M)
    give = re.search(r'^give @s (.+) (\d+)$', text, re.M)
    if not clear or not give:
        raise ValueError(f'No puedo reconocer precio/entrega: {path}')
    existing.append((iid, iid // 100, int(clear[1]), give[1], int(give[2])))
    detail = ROOT / f'data/so_shop/dialog/buy_{iid}.json'
    names[iid] = json.loads(detail.read_text(encoding='utf-8'))['body'][0].get('description', {}).get('contents', {}).get('text', f'Artículo {iid}')
assert len(existing) >= 56, f'Faltan artículos en la tienda: {len(existing)}'

for iid, name, item, cost, unlock in KEYS:
    p = FN / f'item/{iid}.mcfunction'
    okay = FN / f'item/{iid}_ok.mcfunction'
    cmd_item = f'minecraft:{item}[minecraft:custom_name={json.dumps(name, ensure_ascii=False)}]'
    write(p, [f'# {name} · llave Simply OneBlock',
              f'execute unless score #blocks so_shop matches {unlock}.. run return run tellraw @s '
              + json.dumps([{'text':'[SO Shop] ','color':'gold'}, {'text':f'Esta llave se desbloquea a los {unlock} bloques.','color':'red'}], ensure_ascii=False, separators=(',', ':')),
              f'scoreboard players set #cost so_shop {cost}',
              'execute store result score #have so_shop run clear @s minecraft:emerald 0',
              'execute if score #have so_shop >= #cost so_shop run function so_shop:item/%s_ok' % iid,
              'execute if score #have so_shop < #cost so_shop run function so_shop:lib/fail'])
    write(okay, [f'clear @s minecraft:emerald {cost}', f'give @s {cmd_item} 1',
                 'scoreboard players set @s so_shop_cd 20',
                 'tellraw @s ' + json.dumps([{'text':'[SO Shop] ','color':'gold'}, {'text':f'Compraste {name} por {cost} esmeraldas.','color':'green'}], ensure_ascii=False, separators=(',', ':')),
                 'playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1',
                 'scoreboard players add @s so_shop_buys 1'])
    existing.append((iid, 9, cost, cmd_item, 1))
    names[iid] = name

# Subsección de llaves dentro de la categoría original; no se cambia el umbral de las demás.
menu = FN / 'menu/cat_oneblock.mcfunction'
lines = ['tellraw @s {"text":""}', 'tellraw @s {"text":"══ LLAVES ONEBLOCK ══","color":"gold","bold":true}']
for iid, name, _, cost, unlock in KEYS:
    display = json.dumps([{'text':'  ▸ ','color':'dark_gray'},
        {'text':name,'color':'white','click_event':{'action':'run_command','command':f'/trigger shop_buy set {iid}'}},
        {'text':'  —  ','color':'dark_gray'}, {'text':f'{cost} esmeraldas · {unlock} bloques','color':'green'}], ensure_ascii=False, separators=(',', ':'))
    lines.append(f'execute if score #blocks so_shop matches {unlock}.. run tellraw @s {display}')
    lines.append(f'execute unless score #blocks so_shop matches {unlock}.. run tellraw @s '
                 + json.dumps({'text':f'  ✖ {name} — {unlock} bloques','color':'dark_gray'}, ensure_ascii=False, separators=(',', ':')))
lines += ['tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop_menu set 7"}}',
          'playsound minecraft:item.book.page_turn master @s ~ ~ ~ 0.6 1.2']
write(menu, lines)
cat = FN / 'menu/cat_keys.mcfunction'
text = cat.read_text(encoding='utf-8')
link = 'tellraw @s [{"text":"  ▸ Llaves OneBlock","color":"gold","bold":true,"click_event":{"action":"run_command","command":"/trigger shop_menu set 9"}}]'
if link not in text:
    cat.write_text(text.replace('tellraw @s {"text":""}\n', 'tellraw @s {"text":""}\n' + link + '\n', 1), encoding='utf-8')

oc = FN / 'lib/open_cat.mcfunction'
text = oc.read_text(encoding='utf-8')
addition = 'execute if score @s shop_menu matches 9 run dialog show @s so_shop:cat_oneblock\n'
if addition not in text:
    oc.write_text(text + addition, encoding='utf-8')

dispatch = FN / 'lib/dispatch.mcfunction'
text = dispatch.read_text(encoding='utf-8')
for iid, *_ in KEYS:
    line = f'execute if score @s shop_buy matches {iid} run function so_shop:item/{iid}\n'
    if line not in text:
        text += line
# Lotes codificados como id*10 + multiplicador; siempre verifican el desbloqueo original.
for iid, catid, cost, item, count in existing:
    for times in MULTIPLIERS:
        bid = iid * 10 + times
        prefix = f'execute if score @s shop_buy matches {bid}'
        line = prefix + (f' if score #u{catid} so_shop matches 1' if catid != 9 else '') + f' run function so_shop:item/bulk_{iid}_{times}\n'
        if line not in text:
            text += line
            if catid != 9:
                text += prefix + f' if score #u{catid} so_shop matches 0 run function so_shop:lib/locked\n'
        total = count * times
        charge = price(cost, times)
        stack_limit = 1 if item.split('[', 1)[0].split(':')[-1] in UNSTACKABLE else 64
        slots = math.ceil(total / stack_limit)
        guard = [f'# {iid} x{times}: {total} objetos, {charge} esmeraldas ({cost * times - charge} de ahorro)',
                 f'execute unless score #blocks so_shop matches {next((u for k, _, _, _, u in KEYS if k == iid), 0)}.. run return run function so_shop:lib/locked' if iid >= 711 else '# Desbloqueo de categoría comprobado en lib/dispatch',
                 f'scoreboard players set #cost so_shop {charge}',
                 'execute store result score #have so_shop run clear @s minecraft:emerald 0',
                 'execute if score #have so_shop < #cost so_shop run return run function so_shop:lib/fail',
                 # Chequeo conservador: requiere huecos aunque el pago pudiera liberar espacio.
                 'scoreboard players set #slots so_shop 0']
        guard += [f'execute unless items entity @s container.{n} * run scoreboard players add #slots so_shop 1' for n in range(36)]
        guard += [f'execute unless score #slots so_shop matches {slots}.. run return run function so_shop:lib/no_space',
                  f'function so_shop:item/bulk_{iid}_{times}_ok']
        write(FN / f'item/bulk_{iid}_{times}.mcfunction', guard)
        # /give may create multiple stacks; ensure an individual give never exceeds normal inventory size.
        gives = []
        remaining = total
        while remaining:
            part = min(remaining, stack_limit)
            gives.append(f'give @s {item} {part}')
            remaining -= part
        write(FN / f'item/bulk_{iid}_{times}_ok.mcfunction',
              [f'clear @s minecraft:emerald {charge}', *gives,
               'scoreboard players set @s so_shop_cd 20',
               'tellraw @s ' + json.dumps([{'text':'[SO Shop] ','color':'gold'}, {'text':f'Compraste x{times} ({total} objetos) por {charge} esmeraldas. Ahorraste {cost * times - charge}.','color':'green'}], ensure_ascii=False, separators=(',', ':')),
               'playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1',
               'scoreboard players add @s so_shop_buys 1'])
dispatch.write_text(text, encoding='utf-8')
write(FN / 'lib/no_space.mcfunction', [
    'tellraw @s {"text":"[SO Shop] No hay espacio suficiente en tu inventario para ese lote. Libera algunos espacios y vuelve a intentarlo.","color":"red"}',
    'playsound minecraft:entity.villager.no master @s ~ ~ ~ 1 1'])

# Botón directo: la sección 7 mantiene su umbral; llaves OneBlock muestran bloqueos individuales.
main_menu = FN / 'menu/main.mcfunction'
text = main_menu.read_text(encoding='utf-8')
entry = 'tellraw @s [{"text":"  ▸ Llaves OneBlock","color":"gold","bold":true,"click_event":{"action":"run_command","command":"/trigger shop_menu set 9"}}]\n'
if entry not in text:
    text = text.replace('tellraw @s [{"text":"Pago en esmeraldas.', entry + 'tellraw @s [{"text":"Pago en esmeraldas.')
    main_menu.write_text(text, encoding='utf-8')

# Ventanas nativas: cantidades visibles en el mismo detalle. Las ventas mantienen su confirmación.
groups = defaultdict(list)
for iid, catid, cost, item, count in existing:
    groups[catid].append((iid, cost))
    path = ROOT / f'data/so_shop/dialog/buy_{iid}.json'
    back = 'cat_oneblock' if catid == 9 else ['','cat_deco','cat_color','cat_raros','cat_tools','cat_books','cat_eggs','cat_keys'][catid]
    if catid == 9:
        data = {
            'type': 'minecraft:multi_action',
            'title': {'text':'Comprar llave OneBlock','color':'gold'},
            'body': [
                {'type':'minecraft:item','item':{'id': item.split('[', 1)[0], 'count':1},
                 'description':{'contents':{'text':names[iid], 'color':'white'}}},
                {'type':'minecraft:plain_message','contents':{'text':f'Precio: {cost} esmeraldas','color':'green'}},
            ],
        }
    else:
        data = json.loads(path.read_text(encoding='utf-8'))
        data['type'] = 'minecraft:multi_action'
        data.pop('yes', None)
        data.pop('no', None)
        data.pop('exit_action', None)
    data['columns'] = 2
    data['can_close_with_escape'] = True
    data['pause'] = False
    data['actions'] = [
        {'label':{'text':f'x1 · {cost} E'}, 'width':150, 'action':command(f'/trigger shop_buy set {iid}')},
        *[{'label':{'text':f'x{times} · {price(cost,times)} E'},
           'tooltip':{'text':f'Ahorrás {cost * times - price(cost,times)} esmeraldas','color':'green'},
           'width':150,'action':command(f'/trigger shop_buy set {iid * 10 + times}')}
          for times in MULTIPLIERS],
    ]
    data['exit_action'] = {'label':{'text':'« Volver'}, 'width':150, 'action':show(back)}
    dialog(f'buy_{iid}', data)

dialog('cat_oneblock', {
    'type':'minecraft:multi_action',
    'title':{'text':'Llaves OneBlock','color':'gold','bold':True},
    'body':[{'type':'minecraft:plain_message','contents':{'text':'Las llaves se desbloquean según el progreso del OneBlock. También abren sus puertas originales.','color':'gray'}}],
    'columns':2,'can_close_with_escape':True,'pause':False,
    'actions':[
        {'label':{'text':name},'tooltip':{'text':f'{cost} esmeraldas · {unlock} bloques','color':'green'},
         'width':150,'action':command(f'/trigger shop_menu set {900 + iid - 711}')}
        for iid, name, _, cost, unlock in KEYS
    ],
    'exit_action':{'label':{'text':'« Volver'},'width':150,'action':show('main')},
})

# Pasar por trigger impide saltarse un desbloqueo desde la ventana.
extra_menu = FN / 'lib/open_cat.mcfunction'
content = extra_menu.read_text(encoding='utf-8')
for iid, name, _, _, unlock in KEYS:
    menu_id = 900 + iid - 711
    line = f'execute if score @s shop_menu matches {menu_id} if score #blocks so_shop matches {unlock}.. run dialog show @s so_shop:buy_{iid}\n'
    if line not in content:
        content += line
        content += f'execute if score @s shop_menu matches {menu_id} unless score #blocks so_shop matches {unlock}.. run function so_shop:lib/locked\n'
extra_menu.write_text(content, encoding='utf-8')

cat_dialog = ROOT / 'data/so_shop/dialog/cat_keys.json'
data = json.loads(cat_dialog.read_text(encoding='utf-8'))
link_action = {'label':{'text':'Llaves OneBlock','color':'gold'}, 'width':150, 'action':show('cat_oneblock')}
data['actions'] = [a for a in data['actions'] if a.get('label',{}).get('text') != 'Llaves OneBlock'] + [link_action]
dialog('cat_keys', data)

main_dialog = ROOT / 'data/so_shop/dialog/main.json'
data = json.loads(main_dialog.read_text(encoding='utf-8'))
link_action = {'label':{'text':'Llaves OneBlock','color':'gold'}, 'width':150, 'action':show('cat_oneblock')}
data['actions'] = [a for a in data['actions'] if a.get('label',{}).get('text') != 'Llaves OneBlock'] + [link_action]
dialog('main', data)
print(f'Extensión lista: {len(KEYS)} llaves, {len(existing) * len(MULTIPLIERS)} lotes')
