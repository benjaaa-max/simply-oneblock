execute store result score #cnt so_ev run data get entity @s Item.count 1
scoreboard players operation #paid so_ev += #cnt so_ev
particle minecraft:soul_fire_flame ~ ~0.3 ~ 0.2 0.2 0.2 0.05 12
playsound minecraft:block.respawn_anchor.charge master @a ~ ~ ~ 0.8 1.4
kill @s
title @a[tag=so_ev_in] actionbar [{"text": "Tributo: ", "color": "gold"}, {"score": {"name": "#paid", "objective": "so_ev"}, "color": "white", "bold": true}, {"text": " / 32", "color": "gold"}]
