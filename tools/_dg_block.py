# ---------------------------------------------------------------- Las Catacumbas (v4)
PFXD = {"text": "[Catacumbas] ", "color": "dark_purple", "bold": True}


def sayd(sel, text, color="light_purple"):
    return f"tellraw {sel} {T(PFXD, {'text': text, 'color': color, 'bold': False})}"


DGP = "@a[tag=so_ar_dgp]"
DX0 = CX - 38
ROOM_X = [DX0, DX0 + 22, DX0 + 44, DX0 + 68]
ROOM_H = [7, 7, 7, 10]
ROOM_TOP = [66, 66, 66, 70]              # último bloque de aire (piso en y=59, se camina en 60)
CORR = [(ROOM_X[k] + ROOM_H[k] + 1, ROOM_X[k + 1] - ROOM_H[k + 1] - 1) for k in range(3)]
GATE_X = [(a + b) // 2 for a, b in CORR]
DG_FL = f"{DX0 - 10} {CZ - 54} {DX0 + 80} {CZ + 30}"
DG_ALL_BOX = f"x={DX0 - 10},y=50,z={CZ - 54},dx=90,dy=26,dz=84"
DGS = [
    dict(n=1, id="cripta", name="Cripta de los Caídos", color="gray", blk=0, zc=CZ - 40,
         wall="minecraft:deepslate_tiles", wall2="minecraft:mossy_stone_bricks", lamp="minecraft:soul_lantern[hanging=true]",
         floor=["minecraft:cracked_stone_bricks", "minecraft:stone_bricks", "minecraft:mossy_stone_bricks"],
         mobs=[["zombie", "zombie", "skeleton", "husk"], ["zombie_armor", "skeleton", "skeleton", "baby_zombie", "zombie"],
               ["skeleton_armor", "zombie_armor", "stray", "zombie_villager", "skeleton"]],
         boss="caballero", bname="Caballero No-Muerto", esc=["skeleton", "skeleton_armor"], loot="dg_room", trap="flechas"),
    dict(n=2, id="mina", name="Mina Abandonada", color="gold", blk=3000, zc=CZ - 12,
         wall="minecraft:tuff", wall2="minecraft:andesite", lamp="minecraft:lantern[hanging=true]",
         floor=["minecraft:coarse_dirt", "minecraft:cobblestone", "minecraft:stone"],
         mobs=[["cave_spider", "cave_spider", "spider", "zombie"], ["spider", "skeleton", "cave_spider", "spider_jockey", "zombie_armor"],
               ["spider_big", "cave_spider", "cave_spider", "skeleton_armor", "spider"]],
         boss="arana_colosal", bname="Rey Araña", esc=["cave_spider", "cave_spider", "cave_spider"], loot="dg_room_hi", trap="derrumbes"),
    dict(n=3, id="templo", name="Templo Sumergido", color="dark_aqua", blk=6000, zc=CZ + 16,
         wall="minecraft:prismarine_bricks", wall2="minecraft:dark_prismarine", lamp="minecraft:sea_lantern",
         floor=["minecraft:prismarine", "minecraft:dark_prismarine", "minecraft:prismarine_bricks"],
         mobs=[["drowned", "drowned", "drowned_trident"], ["drowned_trident", "drowned", "drowned_trident", "drowned"],
               ["drowned_trident", "drowned_trident", "drowned"]],
         boss="guardian_oscuro", bname="Guardián de la Oscuridad", esc=["drowned_trident", "drowned_trident"], loot="dg_room_hi", trap="tridentes"),
]


def room_box(dg, k):
    rx, h, zc = ROOM_X[k], ROOM_H[k], dg["zc"]
    return f"x={rx - h},y=59,z={zc - h},dx={2 * h},dy={ROOM_TOP[k] - 59},dz={2 * h}"


def row_box(dg):
    return f"x={DX0 - 9},y=50,z={dg['zc'] - 12},dx=89,dy=26,dz=24"


def entry(dg, k):
    return f"{ROOM_X[k] - ROOM_H[k] + 1} 60 {dg['zc']}"


def pts(dg, k):
    rx, h, zc = ROOM_X[k], ROOM_H[k], dg["zc"]
    return [(rx + h - 3, zc - 3), (rx + h - 3, zc + 3), (rx + 2, zc - 3), (rx + 2, zc + 3), (rx + h - 2, zc),
            (rx - 1, zc - h + 2), (rx - 1, zc + h - 2), (rx + 4, zc)]


def gate(dg, k, blk):
    zc = dg["zc"]
    return f"fill {GATE_X[k]} 60 {zc - 1} {GATE_X[k]} 63 {zc + 1} {blk}"


def interior(dg):
    zc, out = dg["zc"], []
    for k in range(4):
        rx, h, top = ROOM_X[k], ROOM_H[k], ROOM_TOP[k]
        out.append(f"fill {rx - h} 60 {zc - h} {rx + h} {top} {zc + h} minecraft:air")
        out += [f"fill {rx + dx} 59 {zc - h} {rx + dx} 59 {zc + h} {dg['floor'][(dx // 2) % 3]}" for dx in range(-h, h + 1)]
        out += [f"setblock {rx + a} {top} {zc + b} minecraft:light[level=15]" for a in range(-h + 2, h - 1, 4) for b in range(-h + 2, h - 1, 4)]
        pil = [(rx + sa * (h - 2), zc + sb * (h - 2)) for sa in (-1, 1) for sb in (-1, 1)]
        if dg["id"] == "cripta":
            for x, z in pil:
                out += [f"fill {x} 60 {z} {x} {top} {z} minecraft:polished_deepslate", f"setblock {x} 60 {z} minecraft:chiseled_deepslate"]
            out += [f"setblock {rx + a} {top} {zc} {dg['lamp']}" for a in (-3, 3)]
            out += [f"setblock {rx + a * h} {top} {zc + b * h} minecraft:cobweb" for a in (-1, 1) for b in (-1, 1)]
            if k < 3:
                for x0 in (rx - 4, rx + 3):
                    for sz in (-5, 5):
                        out += [f"fill {x0} 60 {zc + sz} {x0 + 1} 60 {zc + sz} minecraft:polished_deepslate",
                                f"setblock {x0} 61 {zc + sz} minecraft:candle[candles=3,lit=true]"]
                out += [f"setblock {rx - h + 1} 60 {zc + b * (h - 1)} minecraft:skeleton_skull[rotation=4]" for b in (-1, 1)]
        elif dg["id"] == "mina":
            for x, z in pil:
                out.append(f"fill {x} 60 {z} {x} {top} {z} minecraft:spruce_log")
            for sa in (-1, 1):
                x = rx + sa * (h - 2)
                out += [f"fill {x} {top} {zc - h} {x} {top} {zc + h} minecraft:spruce_planks",
                        f"setblock {x} {top - 1} {zc} {dg['lamp']}"]
            out += [f"fill {rx - h + 1} 59 {zc + b * h} {rx + h - 1} 59 {zc + b * h} minecraft:lava" for b in (-1, 1)]
            out += [f"setblock {rx + a * h} {top} {zc + b * h} minecraft:cobweb" for a in (-1, 1) for b in (-1, 1)]
            if k < 3:
                out.append(f"fill {rx - h} 60 {zc} {rx + h} 60 {zc} minecraft:rail[shape=east_west]")
                out += [f"setblock {rx - h + 1} 60 {zc + b * (h - 1)} minecraft:{o}" for b, o in ((-1, "coal_ore"), (1, "iron_ore"))]
        else:
            for x, z in pil:
                out += [f"fill {x} 60 {z} {x} {top} {z} minecraft:prismarine_bricks", f"setblock {x} 63 {z} minecraft:sea_lantern"]
            out += [f"setblock {rx + a} {top} {zc + b} minecraft:sea_lantern" for a in (-3, 3) for b in (-3, 3)]
            out += [f"fill {rx - h + 1} 59 {zc + b * h} {rx + h - 1} 59 {zc + b * h} minecraft:water" for b in (-1, 1)]
            if k == 2:
                out.append(f"fill {rx - 2} 56 {zc - 2} {rx + 2} 59 {zc + 2} minecraft:water")
        if k == 3:  # trono del jefe (pared este)
            out += [f"fill {rx + h - 1} 60 {zc - 1} {rx + h - 1} 62 {zc + 1} {dg['wall2']}",
                    f"fill {rx - h} 60 {zc} {rx + h - 3} 60 {zc} minecraft:red_carpet"]
        if k == 0:
            out.append(f"setblock {rx - h} 61 {zc + 2} minecraft:oak_wall_sign[facing=east]"
                       f"{sign_snbt(['Salida', ('Abandonar', 'dark_red'), 'volver al', 'Coliseo'], '/trigger arena_dg set 8')}")
    for k, (a, b) in enumerate(CORR):
        out += [f"fill {a} 60 {zc - 1} {b} 63 {zc + 1} minecraft:air", f"fill {a} 59 {zc - 1} {b} 59 {zc + 1} {dg['floor'][0]}",
                f"setblock {GATE_X[k] - 2} 63 {zc} minecraft:light[level=15]", f"setblock {GATE_X[k] + 2} 63 {zc} minecraft:light[level=15]"]
    return out


def shell(dg):
    zc, out = dg["zc"], []
    for k in range(4):
        rx, h, top = ROOM_X[k], ROOM_H[k], ROOM_TOP[k]
        out += [f"fill {rx - h - 1} 58 {zc - h - 1} {rx + h + 1} {top + 1} {zc + h + 1} {dg['wall']} hollow",
                f"fill {rx - h - 1} 62 {zc - h - 1} {rx + h + 1} 62 {zc + h + 1} {dg['wall2']} replace {dg['wall']}"]
    for a, b in CORR:
        out.append(f"fill {a} 58 {zc - 2} {b} 64 {zc + 2} {dg['wall']} hollow")
    if dg["id"] == "templo":
        rx = ROOM_X[2]
        out.append(f"fill {rx - 3} 54 {zc - 3} {rx + 3} 58 {zc + 3} minecraft:dark_prismarine")
    return out


REWARD_DG = [b.replace("[facing=west]", "[facing=north]") for b in REWARD_BLOCKS]
for dg in DGS:
    base, zc, n = f"dg/{dg['id']}", dg["zc"], dg["n"]
    F(f"{base}/interior", interior(dg))
    F(f"{base}/gates_close", [gate(dg, k, "minecraft:iron_bars") for k in range(3)])
    F(f"{base}/reset", [f"function {NS}:{base}/interior", f"function {NS}:{base}/gates_close"])
    for k in range(3):
        P_ = pts(dg, k)
        lines = [f'execute positioned {x + 0.5} 60 {z + 0.5} run function so_events:api/mob {{id:"{m}"}}' for m, (x, z) in zip(dg["mobs"][k], P_)]
        if dg["id"] == "templo" and k == 2:
            lines += [f'summon minecraft:guardian {ROOM_X[2] + a + 0.5} 57 {zc + b + 0.5} {{Tags:["so_ar_dgm"],PersistenceRequired:1b}}' for a, b in ((0, 0), (1, -1))]
        lines.append(f"execute as @e[tag=so_ev_mob,{room_box(dg, k)}] run function {NS}:dg/claim")
        F(f"{base}/spawn{k + 1}", lines)
    bx = ROOM_X[3] + 4
    F(f"{base}/spawn4", [
        f'execute positioned {bx + 0.5} 60 {zc + 0.5} run function so_events:api/boss {{id:"{dg["boss"]}"}}',
        *[f'execute positioned {x + 0.5} 60 {z + 0.5} run function so_events:api/mob {{id:"{m}"}}' for m, (x, z) in zip(dg["esc"], pts(dg, 3)[2:])],
        f"execute as @e[tag=so_ev_mob,{room_box(dg, 3)}] run function {NS}:dg/claim",
        f'data modify entity @e[tag=so_ar_dgboss,limit=1] CustomName set value {{text:"{dg["bname"]}",color:"dark_red",bold:true}}',
        "execute unless entity @e[tag=so_ev_boss] run bossbar set so_events:boss visible false",
        f'bossbar set {NS}:dg name {T({"text": dg["bname"], "color": "dark_red", "bold": True})}',
    ])
    F(f"{base}/begin", [
        f"forceload add {DG_FL}",
        f"scoreboard players set #dg so_ar {n}", "scoreboard players set #dgs so_ar 0",
        "scoreboard players set #dgt so_ar 0", "scoreboard players set #dgr so_ar 1",
        f"tp @s {entry(dg, 0)} -90 0", "tag @s add so_ar_dgp",
        "effect give @s minecraft:resistance 3 4 true",
        "title @s times 5 50 15",
        f'title @s title {T({"text": dg["name"], "color": dg["color"], "bold": True})}',
        f'title @s subtitle {T({"text": "Sala 1/4 · limpiá la sala para abrir la reja", "color": "gray"})}',
        "playsound minecraft:block.iron_door.close master @s ~ ~ ~ 1 0.6",
        f'bossbar set {NS}:dg name {T({"text": dg["name"] + " · Sala 1/4", "color": "dark_purple"})}',
        f"bossbar set {NS}:dg color purple", f"bossbar set {NS}:dg max 4", f"bossbar set {NS}:dg value 1",
        f"bossbar set {NS}:dg players {DGP}", f"bossbar set {NS}:dg visible true",
        f'tellraw {ZONE} [{json.dumps(PFXD)},{{"selector":"@s","color":"white"}},{{"text":" bajó a {dg["name"]}. Sumate con Unirse (menú de Catacumbas).","color":"light_purple","bold":false}}]',
        f"schedule function {NS}:{base}/go 30t",
    ])
    F(f"{base}/go", [f"execute unless score #dg so_ar matches {n} run return 0", f"function {NS}:{base}/spawn1",
                     "scoreboard players set #dgs so_ar 1", "scoreboard players set #dgt so_ar 0",
                     f"execute as {DGP} at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 0.8"])

    def clear(k, nxt, extra):
        return [gate(dg, k, "minecraft:air replace minecraft:iron_bars"),
                f"playsound minecraft:block.piston.extend master {DGP} {GATE_X[k]} 61 {zc} 2 0.6",
                f"particle minecraft:cloud {GATE_X[k]} 61.5 {zc} 0.3 1 1 0.02 30 force",
                f"scoreboard players set #dgs so_ar {nxt}", *extra,
                sayd(DGP, "¡Sala despejada! La reja se abrió: avanzá.", "green")]

    def enter(k, nxt):
        return [f"execute as {DGP} unless entity @s[{room_box(dg, k)}] run tp @s {entry(dg, k)} -90 0",
                gate(dg, k - 1, "minecraft:iron_bars"),
                f"playsound minecraft:block.iron_door.close master {DGP} {GATE_X[k - 1]} 61 {zc} 2 0.6",
                f"scoreboard players set #dgs so_ar {nxt}", f"scoreboard players set #dgr so_ar {k + 1}",
                f"bossbar set {NS}:dg value {k + 1}",
                f'bossbar set {NS}:dg name {T({"text": dg["name"] + f" · Sala {k + 1}/4", "color": "dark_purple"})}',
                f"title {DGP} title {T({'text': f'Sala {k + 1}/4' if k < 3 else dg['bname'], 'color': 'dark_red' if k == 3 else 'gold', 'bold': True})}",
                f"function {NS}:{base}/spawn{k + 1}"]

    r1x, r2x = ROOM_X[1], ROOM_X[2]
    F(f"{base}/clear1", clear(0, 2, []))
    F(f"{base}/enter2", enter(1, 3))
    F(f"{base}/clear2", clear(1, 4, [f"setblock {r1x} 60 {zc} minecraft:chest[facing=west]",
                                      f"execute as {DGP} run loot insert {r1x} 60 {zc} loot {NS}:{dg['loot']}",
                                      f"particle minecraft:happy_villager {r1x}.5 61 {zc}.5 0.4 0.4 0.4 0 15 force",
                                      sayd(DGP, "Apareció un cofre en el centro de la sala anterior.", "yellow")]))
    F(f"{base}/enter3", enter(2, 5))
    F(f"{base}/clear3", [
        "scoreboard players set #dgs so_ar 6",
        f'give {DGP} minecraft:tripwire_hook[custom_name={{text:"Llave de Sala",color:"gold",italic:false}},custom_data={{so_ar_dgkey:1b}},lore=[{{text:"Abre la reja del jefe",color:"gray",italic:false}}]] 1',
        "execute store result score #r so_ar run random value 1..10",
        f"setblock {r2x} 60 {zc - 4} minecraft:barrel[facing=up]",
        f"execute if score #r so_ar matches ..4 run loot insert {r2x} 60 {zc - 4} loot {NS}:dg_secret",
        f"execute if score #r so_ar matches 5.. run loot insert {r2x} 60 {zc - 4} loot {NS}:{dg['loot']}",
        f"execute if score #r so_ar matches ..4 run {sayd(DGP, '¡Barril secreto! Algo brilla adentro.', 'gold')}",
        f"execute as {DGP} at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.2",
        f"title {DGP} title {T({'text': '¡Llave de Sala!', 'color': 'gold', 'bold': True})}",
        sayd(DGP, "Sala despejada: recibieron la Llave de Sala. Acercate con ella a la reja del jefe (al este).", "gold"),
    ])
    F(f"{base}/unlock", [
        f"clear @a {DGKEY}",
        gate(dg, 2, "minecraft:air replace minecraft:iron_bars"),
        "scoreboard players set #dgs so_ar 7",
        f"playsound minecraft:block.iron_door.open master {DGP} {GATE_X[2]} 61 {zc} 2 0.5",
        f"particle minecraft:wax_on {GATE_X[2]} 61.5 {zc} 0.3 1 1 0 30 force",
        sayd(DGP, f"La llave giró. Más allá espera {dg['bname']}...", "red"),
    ])
    F(f"{base}/enter4", enter(3, 8) + [f"execute as {DGP} at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.6 0.8"])
    r4, h4 = ROOM_X[3], ROOM_H[3]
    F(f"{base}/win", [
        f"execute as @e[tag=so_ar_dgm] run tp @s {CX} -300 {CZ}", "kill @e[tag=so_ar_dgm]",
        "scoreboard players set #dgs so_ar 9", "scoreboard players set #dgx so_ar 90",
        f"execute store result score #r so_ar run random value 0..{len(REWARD_DG) - 1}",
        *[f"execute if score #r so_ar matches {i} run setblock {r4} 60 {zc} {b}" for i, b in enumerate(REWARD_DG)],
        f"execute as {DGP} run loot insert {r4} 60 {zc} loot {NS}:dg_boss{n}",
        f"setblock {r4 + h4 - 2} 59 {zc} minecraft:gold_block",
        f"setblock {r4 + h4 - 2} 60 {zc} minecraft:light_weighted_pressure_plate",
        f"scoreboard players add {DGP} so_ar_rank 1",
        *[f"summon minecraft:firework_rocket {r4 + a} 61 {zc + b} {FW.format(lt=15 + 5 * i)}" for i, (a, b) in enumerate(((-5, -5), (5, 5), (-5, 5), (5, -5)))],
        f"execute as {DGP} at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1",
        "title @a[tag=so_ar_dgp] times 5 60 15",
        f"title {DGP} title {T({'text': '¡Mazmorra completada!', 'color': 'green', 'bold': True})}",
        f"title {DGP} subtitle {T({'text': 'Cofre en el centro · salida: placa dorada', 'color': 'yellow'})}",
        f"execute unless score #rec{n} so_ar matches 1.. run scoreboard players set #rec{n} so_ar 999999",
        f"execute store success score #nr so_ar if score #dgt so_ar < #rec{n} so_ar",
        f"execute if score #nr so_ar matches 1 run scoreboard players operation #rec{n} so_ar = #dgt so_ar",
        f'execute if score #nr so_ar matches 1 run tellraw @a[tag=so_ar_zone] [{json.dumps(PFXD)},{{"selector":"{DGP}","color":"white"}},{{"text":" ¡nuevo récord en {dg["name"]}: ","color":"gold","bold":false}},{{"score":{{"name":"#dgt","objective":"so_ar"}},"color":"white","bold":true}},{{"text":" s!","color":"gold","bold":false}}]',
        f'execute if score #nr so_ar matches 0 run tellraw {DGP} [{json.dumps(PFXD)},{{"text":"Tiempo: ","color":"gray","bold":false}},{{"score":{{"name":"#dgt","objective":"so_ar"}},"color":"white"}},{{"text":" s · récord: ","color":"gray"}},{{"score":{{"name":"#rec{n}","objective":"so_ar"}},"color":"gold"}},{{"text":" s","color":"gray"}}]',
        f"function {NS}:dg/board",
        f'bossbar set {NS}:dg name {T({"text": "Salida: placa dorada (o esperá)", "color": "green"})}',
        f"bossbar set {NS}:dg color green", f"bossbar set {NS}:dg max 90", f"bossbar set {NS}:dg value 90",
    ])
    traps = []
    for k, st in ((1, 3), (2, 5)):
        rb, top, h = room_box(dg, k), ROOM_TOP[k], ROOM_H[k]
        pre = f"execute if score #dgs so_ar matches {st}"
        if dg["trap"] == "flechas":
            traps += [f"{pre} if score #m3 so_ar matches 0 as @a[tag=so_ar_dgp,{rb}] at @s run summon minecraft:arrow ~ 61.6 {zc - h + 0.7} {{Motion:[0.0d,0.05d,1.4d],pickup:0b,Tags:[\"so_ar_trap\"]}}",
                      f"{pre} if score #m3 so_ar matches 0 as @a[tag=so_ar_dgp,{rb}] at @s run summon minecraft:arrow ~ 61.6 {zc + h + 0.3} {{Motion:[0.0d,0.05d,-1.4d],pickup:0b,Tags:[\"so_ar_trap\"]}}",
                      f"{pre} if score #m3 so_ar matches 0 as @a[tag=so_ar_dgp,{rb}] at @s run playsound minecraft:block.dispenser.launch master @s ~ ~ ~ 1 1"]
        elif dg["trap"] == "derrumbes":
            traps += [f"{pre} if score #m7 so_ar matches 0 as @a[tag=so_ar_dgp,{rb}] at @s run summon minecraft:falling_block ~ {top - 0.2} ~ {{BlockState:{{Name:\"minecraft:gravel\"}},Time:1,DropItem:0b,HurtEntities:1b,FallHurtAmount:1.0f,FallHurtMax:4}}",
                      f"{pre} if score #m7 so_ar matches 0 as @a[tag=so_ar_dgp,{rb}] at @s run particle minecraft:large_smoke ~ {top - 0.5} ~ 0.6 0.1 0.6 0.01 15",
                      f"{pre} if score #m7 so_ar matches 0 as @a[tag=so_ar_dgp,{rb}] at @s run playsound minecraft:block.gravel.break master @s ~ ~ ~ 1 0.6",
                      f"{pre} if score #m7 so_ar matches 0 run title @a[tag=so_ar_dgp,{rb}] actionbar {T({'text': '¡Derrumbe!', 'color': 'red', 'bold': True})}"]
        else:
            traps += [f"{pre} if score #m6 so_ar matches 0 as @a[tag=so_ar_dgp,{rb}] at @s run summon minecraft:trident ~ {top - 0.5} ~ {{Motion:[0.0d,-1.0d,0.0d],pickup:0b,Tags:[\"so_ar_trap\"]}}",
                      f"{pre} if score #m6 so_ar matches 0 as @a[tag=so_ar_dgp,{rb}] at @s run particle minecraft:bubble_pop ~ {top - 0.5} ~ 0.4 0.1 0.4 0.01 20",
                      f"{pre} if score #m6 so_ar matches 0 as @a[tag=so_ar_dgp,{rb}] at @s run playsound minecraft:item.trident.throw master @s ~ ~ ~ 1 0.7"]
    kx0 = ROOM_X[2] + ROOM_H[2] - 2
    keybox = f"x={kx0},y=60,z={zc - 2},dx={GATE_X[2] - 1 - kx0},dy=3,dz=4"
    plate = f"x={r4 + h4 - 2},y=60,z={zc},dx=0,dy=0,dz=0"
    F(f"{base}/second", [
        "scoreboard players add #dgt so_ar 1",
        "tag @a remove so_ar_dgp",
        f"execute as @a[tag=so_ar_zone,{row_box(dg)}] run tag @s add so_ar_dgp",
        f"execute unless entity {DGP} run return run function {NS}:dg/empty",
        f"bossbar set {NS}:dg players {DGP}",
        "# victoria: salida por la placa dorada o a los 90 s",
        "execute if score #dgs so_ar matches 9 run scoreboard players remove #dgx so_ar 1",
        f"execute if score #dgs so_ar matches 9 store result bossbar {NS}:dg value run scoreboard players get #dgx so_ar",
        f"execute if score #dgs so_ar matches 9 as @a[tag=so_ar_dgp,{plate}] run function {NS}:dg/exit_one",
        f"execute if score #dgs so_ar matches 9 if score #dgx so_ar matches ..0 run return run function {NS}:dg/exit_all",
        "execute if score #dgs so_ar matches 9 run return 0",
        f"execute if score #dgt so_ar matches 1200.. run return run function {NS}:dg/timeout",
        "execute store result score #alive so_ar if entity @e[tag=so_ar_dgm]",
        "scoreboard players operation #m3 so_ar = #dgt so_ar", "scoreboard players operation #m3 so_ar %= #three so_ar",
        "scoreboard players operation #m6 so_ar = #dgt so_ar", "scoreboard players operation #m6 so_ar %= #six so_ar",
        "scoreboard players operation #m7 so_ar = #dgt so_ar", "scoreboard players operation #m7 so_ar %= #seven so_ar",
        "execute as @e[tag=so_ar_dgboss,type=minecraft:warden] run data modify entity @s Brain.memories.\"minecraft:dig_cooldown\" set value {value:{},ttl:1200000L}",
        f"execute if score #dgs so_ar matches 8 as @e[tag=so_ar_dgboss,limit=1] store result bossbar {NS}:dg value run data get entity @s Health",
        f"title {DGP} actionbar {T({'text': dg['name'] + ' · sala ', 'color': 'dark_purple'}, {'score': {'name': '#dgr', 'objective': 'so_ar'}, 'color': 'white'}, {'text': '/4 · enemigos ', 'color': 'gray'}, {'score': {'name': '#alive', 'objective': 'so_ar'}, 'color': 'white'}, {'text': ' · ', 'color': 'gray'}, {'score': {'name': '#dgt', 'objective': 'so_ar'}, 'color': 'white'}, {'text': ' s', 'color': 'gray'})}",
        *traps,
        f"execute if score #dgs so_ar matches 1 if score #dgt so_ar matches 3.. if score #alive so_ar matches 0 run return run function {NS}:{base}/clear1",
        f"execute if score #dgs so_ar matches 2 if entity @a[tag=so_ar_dgp,{room_box(dg, 1)}] run return run function {NS}:{base}/enter2",
        f"execute if score #dgs so_ar matches 3 if score #alive so_ar matches 0 run return run function {NS}:{base}/clear2",
        f"execute if score #dgs so_ar matches 4 if entity @a[tag=so_ar_dgp,{room_box(dg, 2)}] run return run function {NS}:{base}/enter3",
        f"execute if score #dgs so_ar matches 5 if score #alive so_ar matches 0 run return run function {NS}:{base}/clear3",
        f"execute if score #dgs so_ar matches 6 as @a[tag=so_ar_dgp,{keybox}] if items entity @s container.* {DGKEY} run return run function {NS}:{base}/unlock",
        f"execute if score #dgs so_ar matches 6 as @a[tag=so_ar_dgp,{keybox}] unless items entity @s container.* {DGKEY} run title @s actionbar {T({'text': 'Esta reja necesita la Llave de Sala.', 'color': 'gold'})}",
        f"execute if score #dgs so_ar matches 7 if entity @a[tag=so_ar_dgp,{room_box(dg, 3)}] run return run function {NS}:{base}/enter4",
        f"execute if score #dgs so_ar matches 8 unless entity @e[tag=so_ar_dgboss] run return run function {NS}:{base}/win",
    ])

# genéricos
F("dg/claim", [
    "tag @s remove so_ev_mob", "tag @s add so_ar_dgm",
    f"execute if entity @s[type=#{NS}:aggro] run tag @s add so_ar_aggro",
    f"execute if entity @s[tag=so_ev_boss] run function {NS}:dg/claim_boss",
])
F("dg/claim_boss", [
    "tag @s remove so_ev_boss", "tag @s add so_ar_dgboss",
    f"execute store result bossbar {NS}:dg max run data get entity @s Health",
    f"execute store result bossbar {NS}:dg value run data get entity @s Health",
    f"bossbar set {NS}:dg color red",
])
F("dg/trigger", [
    f"execute if score @s arena_dg matches 20 run return run function {NS}:dg/menu",
    f"execute if score @s arena_dg matches 9 run return run function {NS}:dg/join",
    f"execute if score @s arena_dg matches 8 run return run function {NS}:dg/abandon",
    f'execute unless entity @s[tag=so_ar_zone] run return run {sayd("@s", "Primero entrá al Coliseo con /trigger arena.", "red")}',
    f'execute if score #enabled so_ar matches 0 run return run {sayd("@s", "La arena está desactivada por un administrador.", "red")}',
    f'execute unless score @s arena_dg matches 1..3 run return run {sayd("@s", "Opción inválida.", "red")}',
    f'execute if score #dg so_ar matches 1.. run return run {sayd("@s", "Ya hay una expedición en curso. Podés sumarte con Unirse.", "red")}',
    f'execute if entity @s[tag=so_ar_in] run return run {sayd("@s", "Estás en un desafío del Coliseo.", "red")}',
    f'execute if entity @s[tag=so_ar_ready] run return run {sayd("@s", "Estás en el túnel de preparación del Coliseo.", "red")}',
    f"function {NS}:lib/blocks",
    *[f'execute if score @s arena_dg matches {dg["n"]} unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches {dg["blk"]}.. run return run {sayd("@s", dg["name"] + " se desbloquea a los " + fmt(dg["blk"]) + " bloques.", "red")}'
      for dg in DGS if dg["blk"] > 0],
    *[f"execute if score @s arena_dg matches {dg['n']} run function {NS}:dg/{dg['id']}/begin" for dg in DGS],
])
F("dg/menu", [f"dialog show @s {NS}:catacumbas", f"function {NS}:dg/chat"])
F("dg/chat", [
    f"tellraw @s {T({'text': '━━━ Las Catacumbas ━━━', 'color': 'dark_purple', 'bold': True})}",
    f"tellraw @s {T({'text': ' ', 'color': 'gray'}, *[link('[' + dg['name'] + '] ', '/trigger arena_dg set ' + str(dg['n']), dg['color'], 'Desde ' + fmt(dg['blk']) + ' bloques. Jefe: ' + dg['bname']) for dg in DGS])}",
    f"tellraw @s {T(link('[Unirse] ', '/trigger arena_dg set 9', 'green', 'Sumarte a la expedición en curso'), link('[Abandonar]', '/trigger arena_dg set 8', 'red', 'Salir de la mazmorra'))}",
])
F("dg/join", [
    f'execute unless entity @s[tag=so_ar_zone] run return run {sayd("@s", "Primero entrá al Coliseo con /trigger arena.", "red")}',
    f'execute if score #dg so_ar matches 0 run return run {sayd("@s", "No hay ninguna expedición en curso. Elegí una mazmorra.", "gray")}',
    f'execute if score #dgs so_ar matches 9 run return run {sayd("@s", "La expedición ya terminó.", "gray")}',
    f'execute if entity @s[tag=so_ar_dgp] run return run {sayd("@s", "Ya estás en la mazmorra.", "gray")}',
    f'execute if entity @s[tag=so_ar_in] run return run {sayd("@s", "Estás en un desafío del Coliseo.", "red")}',
    *[f"execute if score #dg so_ar matches {dg['n']} if score #dgr so_ar matches {k + 1} run tp @s {entry(dg, k)} -90 0" for dg in DGS for k in range(4)],
    "tag @s add so_ar_dgp", "effect give @s minecraft:resistance 3 4 true",
    f'tellraw {DGP} [{json.dumps(PFXD)},{{"selector":"@s","color":"white"}},{{"text":" se sumó a la expedición.","color":"green","bold":false}}]',
])
F("dg/abandon", [
    f'execute unless entity @s[tag=so_ar_dgp] run return run {sayd("@s", "No estás en ninguna mazmorra.", "gray")}',
    f"clear @s {DGKEY}", "tag @s remove so_ar_dgp",
    f"tp @s {P(DG_OUT)} 180 0",
    sayd("@s", "Saliste de Las Catacumbas.", "gray"),
])
F("dg/exit_one", ["tag @s remove so_ar_dgp", f"clear @s {DGKEY}", f"tp @s {P(DG_OUT)} 180 0",
                  "playsound minecraft:block.iron_door.open master @s ~ ~ ~ 1 1",
                  sayd("@s", "De vuelta en la plaza del Coliseo.", "green")])
F("dg/exit_all", [f"execute as {DGP} run function {NS}:dg/exit_one", f"function {NS}:dg/end"])
F("dg/empty", [f"execute if score #dgs so_ar matches 9 run return run function {NS}:dg/end",
               sayd(ZONE, "La expedición terminó: nadie quedó en las catacumbas.", "gray"), f"function {NS}:dg/end"])
F("dg/timeout", [sayd(DGP, "Se acabó el tiempo (20 min). La mazmorra los expulsa.", "red"),
                 f"execute as {DGP} run function {NS}:dg/exit_one", f"function {NS}:dg/end"])
F("dg/end", [
    "# Reinicio limpio: enemigos, ítems, trampas, llaves, cofres, puertas y bloques de la mazmorra activa.",
    f"execute as @e[tag=so_ar_dgm] run tp @s {CX} -300 {CZ}", "kill @e[tag=so_ar_dgm]",
    *[f"kill @e[type=minecraft:{t},{DG_ALL_BOX}]" for t in ("item", "experience_orb", "arrow", "spectral_arrow", "trident", "falling_block")],
    f"clear @a {DGKEY}",
    f"bossbar set {NS}:dg visible false",
    *[f"execute if score #dg so_ar matches {dg['n']} run function {NS}:dg/{dg['id']}/reset" for dg in DGS],
    "scoreboard players set #dg so_ar 0", "scoreboard players set #dgs so_ar 0", "scoreboard players set #dgr so_ar 0",
    "tag @a remove so_ar_dgp",
    f"schedule function {NS}:dg/unload 40t",
])
F("dg/unload", [f"execute if score #dg so_ar matches 0 run forceload remove {DG_FL}"])
F("dg/second", [f"execute if score #dg so_ar matches {dg['n']} run function {NS}:dg/{dg['id']}/second" for dg in DGS])
F("dg/board", [
    *[f"execute if score #rec{dg['n']} so_ar matches 1..999998 store result storage so_arenas:dg r{dg['n']} int 1 run scoreboard players get #rec{dg['n']} so_ar" for dg in DGS],
    *[f'execute unless score #rec{dg["n"]} so_ar matches 1..999998 run data modify storage so_arenas:dg r{dg["n"]} set value "—"' for dg in DGS],
    f"function {NS}:dg/board_set with storage so_arenas:dg",
])
F("dg/board_set", [f'$data modify entity @e[tag=so_ar_dgboard,limit=1,{ZONE_BOX}] text set value {{text:"",extra:[{{text:"⚰ Las Catacumbas\\n",color:"dark_purple",bold:true}},{{text:"Récords (segundos)\\n",color:"gray"}},{{text:"Cripta $(r1) · Mina $(r2) · Templo $(r3)",color:"white"}}]}}'])

dialog("catacumbas", "Las Catacumbas", "dark_purple",
       "Tres mazmorras bajo el coliseo. Cada una: 3 salas que cierran la reja hasta vencer a todos, llave de sala, cofres y un jefe con cofre final. Se reinician solas.",
       [act(f"/trigger arena_dg set {dg['n']}", dg["name"], f"Desde {fmt(dg['blk'])} bloques. Trampas: {dg['trap']}. Jefe: {dg['bname']}.", dg["color"], 250) for dg in DGS] +
       [act("/trigger arena_dg set 9", "Unirse a la expedición", "Entrar a la mazmorra en curso.", "green", 250),
        act("/trigger arena_dg set 8", "Abandonar / salir", "Volvés a la plaza del Coliseo.", "red", 250), BACK | {"width": 250}],
       cols=1, w=250)

# construcción: mausoleo de entrada + una mazmorra por paso
_z6, _z7 = LZ1 + 6, LZ1 + 7
cur = [f"fill {CX - 2} 96 {_z6} {CX - 2} 99 {_z6} minecraft:deepslate_tiles", f"fill {CX + 2} 96 {_z6} {CX + 2} 99 {_z6} minecraft:deepslate_tiles",
       f"fill {CX - 2} 100 {_z6} {CX + 2} 100 {_z6} minecraft:polished_deepslate",
       f"fill {CX - 1} 96 {_z7} {CX + 1} 99 {_z7} minecraft:polished_blackstone_bricks",
       f"setblock {CX} 96 {_z7} minecraft:dark_oak_door[half=lower,facing=north]",
       f"setblock {CX} 97 {_z7} minecraft:dark_oak_door[half=upper,facing=north]",
       f"setblock {CX - 2} 101 {_z6} minecraft:soul_lantern", f"setblock {CX + 2} 101 {_z6} minecraft:soul_lantern",
       f"setblock {DG_PLATE[0]} {G} {DG_PLATE[2]} minecraft:crying_obsidian",
       f"setblock {P(DG_PLATE)} minecraft:polished_blackstone_pressure_plate",
       f"setblock {CX - 1} 96 {DG_PLATE[2]} minecraft:oak_sign[rotation=8]{sign_snbt(['Entrada a', ('Catacumbas', 'dark_purple'), 'pisá la placa', 'o tocá acá'], '/trigger arena_dg set 20')}"]
for dg in DGS:
    steps.append((cur if dg["n"] == 1 else []) + shell(dg) + [f"function {NS}:dg/{dg['id']}/reset"])


def dg_labels():
    out = [label(CX, 101.3, _z6, "Las Catacumbas", "dark_purple", '"so_ar_npc","so_ar_dgboard"', 0.9)]
    for dg in DGS:
        out += [label(GATE_X[2], 62.2, dg["zc"], "Reja del jefe · Llave de Sala", "gold", scale=0.5),
                label(ROOM_X[0] - 5, 63, dg["zc"], dg["name"], dg["color"], scale=0.8)]
    return out + [f"function {NS}:dg/board"]


