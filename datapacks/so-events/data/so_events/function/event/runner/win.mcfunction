execute as @a[tag=so_ev_in] at @s run function so_events:lib/chest {t:"runner"}
execute as @e[tag=so_ev_runner,limit=1] at @s run particle minecraft:firework ~ ~0.5 ~ 0.3 0.3 0.3 0.1 60
title @a[tag=so_ev_in] title {"text": "¡Atraparon al fugitivo!", "color": "gold", "bold": true}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡El fugitivo cayó! Esmeraldas, botellas de XP y oro en el piso.", "color": "gold", "bold": false}]
kill @e[tag=so_ev_runner]
scoreboard players add @a[tag=so_ev_in] so_ev_win 1
scoreboard players add @a[tag=so_ev_in] so_ev_pos 1
function so_events:lib/streak_up
function so_events:lib/cleanup
