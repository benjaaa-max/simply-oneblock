execute as @a[tag=so_ev_in] at @s run function so_events:lib/chest {t:"reward_small"}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Sobreviviste a la trampa del espejismo. Algo es algo.", "color": "green", "bold": false}]
function so_events:event/mimic/end
