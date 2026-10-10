execute as @a[tag=so_ar_in] run loot give @s loot so_arenas:contract
scoreboard players add @a[tag=so_ar_in] so_ar_rank 1
title @a[tag=so_ar_in] title {"text": "¡Contrato cumplido!", "color": "green", "bold": true}
tellraw @a [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "¡Contrato cumplido! Esmeraldas, botellas de XP y un Fragmento de Victoria.", "color": "green", "bold": false}]
function so_arenas:lib/celebrar
function so_arenas:lib/end
tellraw @a [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Ya podés volver a la isla con /trigger volver.", "color": "gray", "bold": false}]
