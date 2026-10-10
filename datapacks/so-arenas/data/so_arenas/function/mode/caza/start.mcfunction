scoreboard players set #mode so_ar 2
bossbar set so_arenas:fight name {"text": "Caza: objetivos restantes", "color": "aqua"}
bossbar set so_arenas:fight color blue
bossbar set so_arenas:fight max 15
bossbar set so_arenas:fight value 15
title @a[tag=so_ar_in] title {"text": "¡Caza de monstruos!", "color": "aqua", "bold": true}
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Contrato: 15 bajas objetivo (en tandas de 5). Los de apoyo son extra.", "color": "aqua", "bold": false}]
function so_arenas:mode/caza/batch
