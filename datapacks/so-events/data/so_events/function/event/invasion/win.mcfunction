execute as @a[tag=so_ev_in] run loot give @s loot so_events:reward_big
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Invasión derrotada! Cada defensor recibió su recompensa.", "color": "green", "bold": false}]
title @a[tag=so_ev_in] title {"text": "¡Victoria!", "color": "green", "bold": true}
execute as @a[tag=so_ev_in] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
function so_events:lib/cleanup
