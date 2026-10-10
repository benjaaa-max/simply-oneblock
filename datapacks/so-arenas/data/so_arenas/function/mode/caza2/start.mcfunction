scoreboard players set #mode so_ar 4
bossbar set so_arenas:fight name {"text": "Oleadas dobles", "color": "aqua"}
bossbar set so_arenas:fight color blue
bossbar set so_arenas:fight max 3
bossbar set so_arenas:fight value 0
title @a[tag=so_ar_in] title {"text": "¡Oleadas dobles!", "color": "aqua", "bold": true}
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Contrato: superá 3 oleadas, cada una más dura.", "color": "aqua", "bold": false}]
function so_arenas:mode/caza2/wave
