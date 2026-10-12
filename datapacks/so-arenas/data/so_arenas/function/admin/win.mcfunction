execute if score #mode so_ar matches 1 run return run function so_arenas:lib/win_practice
execute if score #mode so_ar matches 2..8 run return run function so_arenas:lib/win_contract
tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "No hay desafío en curso (si estás en el túnel, tocá la campana primero).", "color": "gray", "bold": false}]
