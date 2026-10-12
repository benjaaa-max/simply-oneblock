scoreboard players set #mode so_ar 9
scoreboard players set #st so_ar 0
function so_arenas:lib/stage_in
dialog show @s so_arenas:dj
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Un gladiador se prepara en el túnel. ¡Pueden unirse antes de la campana!", "color": "gold", "bold": false}]
