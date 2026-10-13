function so_events:lib/begin
scoreboard players set #active so_ev 13
function so_events:lib/no_grief
bossbar set so_events:ev name {"text": "Caravana perdida", "color": "gold"}
bossbar set so_events:ev max 120
bossbar set so_events:ev color yellow
scoreboard players set #near so_ev 1
execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function so_events:lib/spawn {mob:"mob/llama_caravan"}
execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function so_events:lib/spawn {mob:"mob/llama_caravan"}
execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function so_events:lib/spawn {mob:"mob/llama_caravan"}
scoreboard players set #near so_ev 0
title @a[tag=so_ev_in] title {"text": "¡Caravana perdida!", "color": "gold", "bold": true}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Una caravana de llamas cargadas llegó a la isla. ¡Saqueadores las persiguen! Defendé al menos una por 3 minutos.", "color": "gold", "bold": false}]
