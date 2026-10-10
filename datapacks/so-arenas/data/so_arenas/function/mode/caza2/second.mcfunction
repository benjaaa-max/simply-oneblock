scoreboard players add #t so_ar 1
execute store result score #alive so_ar if entity @e[tag=so_ar_mob]
title @a[tag=so_ar_in] actionbar [{"text": "Oleada ", "color": "aqua", "bold": true}, {"score": {"name": "#wave", "objective": "so_ar"}, "color": "white"}, {"text": " · enemigos: ", "color": "gray"}, {"score": {"name": "#alive", "objective": "so_ar"}, "color": "white"}]
execute if score #alive so_ar matches 0 if score #wave so_ar matches 1..2 run function so_arenas:mode/caza2/wave
execute if score #alive so_ar matches 0 if score #wave so_ar matches 3.. run function so_arenas:lib/win_contract
execute if score #t so_ar matches 480.. run function so_arenas:lib/fail_contract
