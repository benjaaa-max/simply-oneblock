execute unless entity @s[tag=so_ar_zone] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Primero entrá al Coliseo con /trigger arena.", "color": "red", "bold": false}]
execute if entity @s[tag=so_ar_spec] run return run function so_arenas:lib/ver_off
execute if entity @s[tag=so_ar_in] if score #mode so_ar matches 1.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Estás peleando: no podés subir a las tribunas.", "color": "red", "bold": false}]
execute if entity @s[tag=so_ar_ready] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Estás en el túnel de preparación.", "color": "red", "bold": false}]
tag @s add so_ar_spec
tp @s -4962 108 -5000 90 15
effect give @s minecraft:invisibility infinite 0 true
effect give @s minecraft:resistance 30 4 true
tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Estás en las tribunas (invisible). Usá las cestas de apoyo para enviar ítems y los cofres de cobre para tirar cohetes. /trigger arena_ver para bajar.", "color": "aqua", "bold": false}]
