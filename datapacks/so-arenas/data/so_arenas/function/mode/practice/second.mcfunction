scoreboard players add #t so_ar 1
execute store result score #alive so_ar if entity @e[tag=so_ar_mob]
title @a[tag=so_ar_in] actionbar [{"text": "Oleada ", "color": "yellow", "bold": true}, {"score": {"name": "#wave", "objective": "so_ar"}, "color": "white"}, {"text": " · enemigos: ", "color": "gray"}, {"score": {"name": "#alive", "objective": "so_ar"}, "color": "white"}]
execute if score #alive so_ar matches 0 if score #wave so_ar matches 1 run function so_arenas:mode/practice/wave
execute if score #alive so_ar matches 0 if score #wave so_ar matches 2.. run function so_arenas:lib/win_practice
execute if score #t so_ar matches 300.. run function so_arenas:lib/fail_practice
