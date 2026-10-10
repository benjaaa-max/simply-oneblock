scoreboard players add #t so_ar 1
execute positioned -5000 96 -5000 store result score #near so_ar if entity @e[tag=so_ar_mob,distance=..6]
execute if score #hp so_ar matches 1.. run scoreboard players operation #hp so_ar -= #near so_ar
execute if score #hp so_ar matches ..0 run function so_arenas:lib/fail_contract
execute if score #hp so_ar matches 1.. run bossbar set so_arenas:fight name [{"text": "Núcleo: ", "color": "dark_purple"}, {"score": {"name": "#hp", "objective": "so_ar"}, "color": "white", "bold": true}, {"text": "%", "color": "gray"}]
execute if score #hp so_ar matches 1.. store result bossbar so_arenas:fight value run scoreboard players get #hp so_ar
scoreboard players operation #m so_ar = #t so_ar
scoreboard players operation #m so_ar %= #twentyfive so_ar
execute if score #m so_ar matches 1 if score #wave so_ar matches ..5 run function so_arenas:mode/defensa/wave
execute if score #t so_ar matches 120.. run function so_arenas:lib/win_contract
