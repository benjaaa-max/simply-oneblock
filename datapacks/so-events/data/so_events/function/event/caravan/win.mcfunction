execute as @a[tag=so_ev_in] run loot give @s loot so_events:caravan
# Por cada llama viva, un rollo extra de cargamento para la isla.
execute as @e[tag=so_ev_llama] at @s run loot spawn ~ ~1 ~ loot so_events:caravan
scoreboard players add @a[tag=so_ev_in] so_ev_win 1
scoreboard players add @a[tag=so_ev_in] so_ev_pos 1
function so_events:lib/streak_up
title @a[tag=so_ev_in] title {"text": "¡Caravana a salvo!", "color": "green", "bold": true}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "La caravana sobrevivió y les deja su cargamento. Las llamas se quedan en la isla como mascotas.", "color": "green", "bold": false}]
# Las llamas dejan de ser del evento: el limpiador ya no las toca.
execute as @e[tag=so_ev_llama] at @s run particle minecraft:heart ~ ~1.8 ~ 0.4 0.3 0.4 0 6
execute as @e[tag=so_ev_llama] run data merge entity @s {PersistenceRequired:1b,Tame:1b,CustomName:{text:"Llama de la Isla",color:"gold"}}
tag @e[tag=so_ev_llama] add so_ev_saved
tag @e[tag=so_ev_llama] remove so_ev_mob
tag @e[tag=so_ev_llama] remove so_ev_llama
function so_events:lib/cleanup
