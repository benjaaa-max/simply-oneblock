function so_events:lib/begin
scoreboard players set #active so_ev 3
scoreboard players operation #start so_ev = #blk so_ev
scoreboard players set #prog so_ev 0
bossbar set so_events:ev name {"text": "Desafío de minería", "color": "green"}
bossbar set so_events:ev color green
execute store result bossbar so_events:ev max run scoreboard players get #mine_goal so_ev
bossbar set so_events:ev value 0
title @a[tag=so_ev_in] title {"text": "¡Desafío de minería!", "color": "green", "bold": true}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Rompan ", "color": "green", "bold": false}, {"score": {"name": "#mine_goal", "objective": "so_ev"}, "color": "white"}, {"text": " bloques del OneBlock entre todos en 3 minutos.", "color": "green"}]
