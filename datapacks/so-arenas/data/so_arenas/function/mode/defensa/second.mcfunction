scoreboard players add #t so_ar 1
execute positioned -5000 96 -5000 store result score #near so_ar if entity @e[tag=so_ar_mob,distance=..5]
scoreboard players operation #hp so_ar -= #near so_ar
execute store result bossbar so_arenas:fight value run scoreboard players get #hp so_ar
title @a[tag=so_ar_in] actionbar [{"text": "Núcleo: ", "color": "dark_purple"}, {"score": {"name": "#hp", "objective": "so_ar"}, "color": "white", "bold": true}, {"text": "% · tiempo: ", "color": "gray"}, {"score": {"name": "#t", "objective": "so_ar"}, "color": "white"}, {"text": "/120 s", "color": "gray"}]
execute if score #hp so_ar matches ..0 run return run function so_arenas:lib/fail
execute if score #t so_ar matches 120.. run return run function so_arenas:lib/win_contract
scoreboard players operation #m so_ar = #t so_ar
scoreboard players operation #m so_ar %= #twentyfive so_ar
execute if score #m so_ar matches 0 run function so_arenas:mode/defensa/wave
