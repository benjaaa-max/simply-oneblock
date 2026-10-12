scoreboard players add #t so_ar 1
particle minecraft:end_rod -4996.90 99.2 -4999.50 0 0.3 0 0.01 2 force
particle minecraft:end_rod -4997.10 99.2 -4998.51 0 0.3 0 0.01 2 force
particle minecraft:end_rod -4997.66 99.2 -4997.66 0 0.3 0 0.01 2 force
particle minecraft:end_rod -4998.51 99.2 -4997.10 0 0.3 0 0.01 2 force
particle minecraft:end_rod -4999.50 99.2 -4996.90 0 0.3 0 0.01 2 force
particle minecraft:end_rod -5000.49 99.2 -4997.10 0 0.3 0 0.01 2 force
particle minecraft:end_rod -5001.34 99.2 -4997.66 0 0.3 0 0.01 2 force
particle minecraft:end_rod -5001.90 99.2 -4998.51 0 0.3 0 0.01 2 force
particle minecraft:end_rod -5002.10 99.2 -4999.50 0 0.3 0 0.01 2 force
particle minecraft:end_rod -5001.90 99.2 -5000.49 0 0.3 0 0.01 2 force
particle minecraft:end_rod -5001.34 99.2 -5001.34 0 0.3 0 0.01 2 force
particle minecraft:end_rod -5000.49 99.2 -5001.90 0 0.3 0 0.01 2 force
particle minecraft:end_rod -4999.50 99.2 -5002.10 0 0.3 0 0.01 2 force
particle minecraft:end_rod -4998.51 99.2 -5001.90 0 0.3 0 0.01 2 force
particle minecraft:end_rod -4997.66 99.2 -5001.34 0 0.3 0 0.01 2 force
particle minecraft:end_rod -4997.10 99.2 -5000.49 0 0.3 0 0.01 2 force
particle minecraft:glow -5000.5 100 -5000.5 0.3 1.5 0.3 0 10 force
execute positioned -4999.5 99 -4999.5 if entity @a[tag=so_ar_in,distance=..2.8] run scoreboard players add #hold so_ar 1
execute store result bossbar so_arenas:fight value run scoreboard players get #hold so_ar
bossbar set so_arenas:fight name [{"text": "Captura ", "color": "gold", "bold": true}, {"score": {"name": "#hold", "objective": "so_ar"}, "color": "white"}, {"text": "/90", "color": "gold"}]
scoreboard players operation #wave so_ar = #hold so_ar
title @a[tag=so_ar_in] actionbar [{"text": "Captura: ", "color": "gold"}, {"score": {"name": "#hold", "objective": "so_ar"}, "color": "white", "bold": true}, {"text": "/90 · tiempo ", "color": "gray"}, {"score": {"name": "#t", "objective": "so_ar"}, "color": "white"}, {"text": "/120 s", "color": "gray"}]
execute if score #hold so_ar matches 90.. run return run function so_arenas:lib/win_contract
execute if score #t so_ar matches 120.. run return run function so_arenas:lib/fail
scoreboard players operation #m so_ar = #t so_ar
scoreboard players operation #m so_ar %= #ten so_ar
execute if score #m so_ar matches 0 run function so_arenas:mode/rey/wave
