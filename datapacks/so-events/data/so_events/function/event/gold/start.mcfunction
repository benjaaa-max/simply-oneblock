function so_events:lib/begin
scoreboard players set #active so_ev 11
bossbar set so_events:ev name {"text": "Fiebre del oro", "color": "gold"}
bossbar set so_events:ev max 60
bossbar set so_events:ev color yellow
title @a[tag=so_ev_in] title {"text": "¡Fiebre del oro!", "color": "gold", "bold": true}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡El OneBlock brilla! Durante 60 segundos el oro brota de la isla.", "color": "gold", "bold": false}]
