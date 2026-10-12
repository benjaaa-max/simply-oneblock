scoreboard players add #t so_ar 1
# Daño real que recibió el aldeano cebo (cada 2 de vida = 1% de núcleo); después se cura al máximo.
scoreboard players set #bh so_ar 1024
execute as @e[tag=so_ar_bait,limit=1] store result score #bh so_ar run data get entity @s Health
scoreboard players set #dmg so_ar 1025
scoreboard players operation #dmg so_ar -= #bh so_ar
scoreboard players operation #dmg so_ar /= #two so_ar
scoreboard players operation #hp so_ar -= #dmg so_ar
execute as @e[tag=so_ar_bait] run data modify entity @s Health set value 1024f
execute if score #dmg so_ar matches 1.. run particle minecraft:damage_indicator -5000.5 98 -5000.5 0.4 0.6 0.4 0.1 8 force
execute if score #dmg so_ar matches 1.. run playsound minecraft:block.anvil.land master @a[tag=so_ar_in] -5000 97 -5000 0.4 1.6
execute store result bossbar so_arenas:fight value run scoreboard players get #hp so_ar
title @a[tag=so_ar_in] actionbar [{"text": "Núcleo: ", "color": "dark_purple"}, {"score": {"name": "#hp", "objective": "so_ar"}, "color": "white", "bold": true}, {"text": "% · tiempo: ", "color": "gray"}, {"score": {"name": "#t", "objective": "so_ar"}, "color": "white"}, {"text": "/120 s", "color": "gray"}]
execute if score #hp so_ar matches ..0 run return run function so_arenas:lib/fail
execute if score #t so_ar matches 120.. run return run function so_arenas:lib/win_contract
scoreboard players operation #m so_ar = #t so_ar
scoreboard players operation #m so_ar %= #fifteen so_ar
execute if score #m so_ar matches 0 run function so_arenas:mode/defensa/wave
