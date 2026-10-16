scoreboard players add #t so_ev 1
scoreboard players set #six so_ev 6
scoreboard players set #ten so_ev 10
execute store result bossbar so_events:ev value run scoreboard players get #t so_ev
execute as @e[type=minecraft:marker,tag=so_ev_beacon] at @s run function so_events:event/altar/color
execute as @e[tag=so_ev_altar,limit=1] at @s run particle minecraft:end_rod ~0.5 ~1 ~0.5 0.3 0.6 0.3 0.02 10
execute as @e[tag=so_ev_altar,limit=1] at @s positioned ~0.5 ~ ~0.5 run function so_events:event/altar/take
scoreboard players operation #m so_ev = #t so_ev
scoreboard players operation #m so_ev %= #ten so_ev
execute if score #m so_ev matches 0 as @e[tag=so_ev_altar,limit=1] at @s run playsound minecraft:block.bell.resonate master @a ~ ~ ~ 1.5 0.8
title @a[tag=so_ev_in] actionbar [{"text": "Ofrendas: ", "color": "gold"}, {"score": {"name": "#paid", "objective": "so_ev"}, "color": "white", "bold": true}, {"text": "  (fases: 64 / 192 / 400)", "color": "gray"}]
execute if score #phase so_ev matches 0 if score #paid so_ev matches 64.. run function so_events:event/altar/phase1
execute if score #phase so_ev matches 1 if score #paid so_ev matches 192.. run function so_events:event/altar/phase2
execute if score #phase so_ev matches 2 if score #paid so_ev matches 400.. run function so_events:event/altar/phase3
execute if score #t so_ev matches 120.. if score #phase so_ev matches 1.. run function so_events:event/altar/win
execute if score #t so_ev matches 120.. if score #phase so_ev matches 0 run function so_events:event/altar/fail
