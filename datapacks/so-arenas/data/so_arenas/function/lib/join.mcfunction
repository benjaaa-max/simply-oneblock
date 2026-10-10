execute unless entity @s[tag=so_ar_zone] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Primero entrá al Coliseo con /trigger arena.", "color": "red", "bold": false}]
execute if score #mode so_ar matches 0 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "No hay ningún desafío en curso. Elegí una práctica o un contrato.", "color": "gray", "bold": false}]
execute if entity @s[tag=so_ar_in] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Ya estás en el foso.", "color": "gray", "bold": false}]
function so_arenas:lib/enter_pit
bossbar set so_arenas:fight players @a[tag=so_ar_in]
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "¡Un gladiador más se suma al desafío!", "color": "green", "bold": false}]
