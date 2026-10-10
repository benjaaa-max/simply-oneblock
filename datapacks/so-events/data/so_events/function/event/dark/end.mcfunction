execute as @a[tag=so_ev_in] run loot give @s loot so_events:reward_small
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Amaneció. Los sobrevivientes recibieron una recompensa.", "color": "green", "bold": false}]
function so_events:lib/cleanup
