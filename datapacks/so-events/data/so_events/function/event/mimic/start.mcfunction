function so_events:lib/begin
scoreboard players set #active so_ev 12
scoreboard players set #mimic so_ev 0
bossbar set so_events:ev name {"text": "Espejismo: elegí un cofre", "color": "light_purple"}
bossbar set so_events:ev max 120
bossbar set so_events:ev color purple
execute store result score #side so_ev run random value 1..2
execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function so_events:event/mimic/place
title @a[tag=so_ev_in] title {"text": "Espejismo", "color": "light_purple", "bold": true}
title @a[tag=so_ev_in] subtitle {"text": "Dos cofres gemelos... solo uno es real", "color": "gray"}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Dos cofres gemelos aparecieron junto a vos. Uno guarda un tesoro, el otro es una trampa. Abrí solo uno: tenés 2 minutos.", "color": "light_purple", "bold": false}]
