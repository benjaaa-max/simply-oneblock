execute as @a[tag=so_ar_in] run loot give @s loot so_arenas:practice
title @a[tag=so_ar_in] title {"text": "¡Victoria!", "color": "green", "bold": true}
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Práctica superada. La recompensa ya es de ustedes.", "color": "green", "bold": false}]
function so_arenas:lib/celebrar
function so_arenas:lib/end
