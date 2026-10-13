execute as @a[tag=so_ev_in] run loot give @s loot so_events:reward_small
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Sobreviviste a la trampa del espejismo. Algo es algo.", "color": "green", "bold": false}]
function so_events:event/mimic/end
