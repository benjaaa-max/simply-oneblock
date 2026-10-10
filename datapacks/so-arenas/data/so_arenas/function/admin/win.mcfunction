execute if score #mode so_ar matches 1 run return run function so_arenas:lib/win_practice
execute unless score #mode so_ar matches 0 run return run function so_arenas:lib/win_contract
tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "No hay desafío en curso.", "color": "gray", "bold": false}]
