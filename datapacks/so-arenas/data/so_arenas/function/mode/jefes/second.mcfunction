scoreboard players add #t so_ar 1
execute as @e[tag=so_ar_boss,limit=1] store result bossbar so_arenas:fight value run data get entity @s Health
execute if entity @e[tag=so_ar_boss] run title @a[tag=so_ar_in] actionbar [{"text": "Campeón ", "color": "red"}, {"score": {"name": "#champ", "objective": "so_ar"}, "color": "white", "bold": true}, {"text": "/", "color": "gray"}, {"score": {"name": "#cmax", "objective": "so_ar"}, "color": "white"}]
execute if entity @e[tag=so_ar_boss] run return run execute if score #t so_ar matches 600.. run function so_arenas:lib/fail
execute if score #champ so_ar >= #cmax so_ar run kill @e[tag=so_ar_mob]
execute if score #champ so_ar >= #cmax so_ar run return run function so_arenas:lib/win_contract
scoreboard players add #rest so_ar 1
bossbar set so_arenas:fight value 0
title @a[tag=so_ar_in] actionbar [{"text": "¡Campeón caído! Respiro: ", "color": "green"}, {"score": {"name": "#rest", "objective": "so_ar"}, "color": "white", "bold": true}, {"text": " s", "color": "green"}]
execute if score #rest so_ar matches 1 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "¡Campeón derrotado! Respirá: viene el siguiente.", "color": "green", "bold": false}]
execute if score #jt so_ar matches 1 if score #rest so_ar matches 10.. run function so_arenas:mode/jefes/rest_done
execute if score #jt so_ar matches 2 if score #rest so_ar matches 5.. run function so_arenas:mode/jefes/rest_done
execute if score #t so_ar matches 600.. run function so_arenas:lib/fail
