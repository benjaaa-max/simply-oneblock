tag @a remove so_ar_win
tag @a[tag=so_ar_in] add so_ar_win
function so_arenas:lib/music_stop
function so_arenas:lib/celebrar
function so_arenas:lib/judges_salute
function so_arenas:lib/end_fight
scoreboard players add @a[tag=so_ar_win] so_ar_streak 1
function so_arenas:lib/reward_chest
function so_arenas:lib/gates_open
scoreboard players set #exit so_ar 1
scoreboard players set #ext so_ar 60
bossbar set so_arenas:fight name {"text": "Portón abierto · el foso se limpia en", "color": "green"}
bossbar set so_arenas:fight color green
bossbar set so_arenas:fight max 60
bossbar set so_arenas:fight value 60
bossbar set so_arenas:fight players @a[tag=so_ar_zone]
bossbar set so_arenas:fight visible true
title @a[tag=so_ar_win] subtitle {"text": "Salí por el portón: tu cofre te espera en el lobby", "color": "yellow"}
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Los portones están abiertos 60 s. Festejen, junten lo que quieran y salgan por el túnel (o pisen la placa dorada).", "color": "green", "bold": false}]
