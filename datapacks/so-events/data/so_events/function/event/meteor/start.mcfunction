function so_events:lib/begin
scoreboard players set #active so_ev 10
function so_events:lib/no_grief
bossbar set so_events:ev name {"text": "Lluvia de meteoritos", "color": "red"}
bossbar set so_events:ev max 60
bossbar set so_events:ev color red
title @a[tag=so_ev_in] title {"text": "¡Lluvia de meteoritos!", "color": "red", "bold": true}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Meteoritos caen sobre la isla durante 60 segundos! Cada cráter deja botín... si te animás a acercarte.", "color": "red", "bold": false}]
