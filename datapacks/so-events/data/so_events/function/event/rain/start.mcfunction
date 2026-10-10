function so_events:lib/begin
scoreboard players set #active so_ev 1
bossbar set so_events:ev name {"text": "Lluvia de recursos", "color": "aqua"}
bossbar set so_events:ev max 60
bossbar set so_events:ev color blue
title @a[tag=so_ev_in] title {"text": "¡Lluvia de recursos!", "color": "aqua", "bold": true}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Cae una lluvia de recursos sobre la isla durante 60 segundos.", "color": "aqua", "bold": false}]
