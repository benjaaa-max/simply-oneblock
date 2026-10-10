tag @a remove so_ev_in
execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in
execute as @a[tag=so_ev_in] at @s run loot spawn ~ ~3 ~ loot so_events:supply
execute as @a[tag=so_ev_in] at @s run particle minecraft:firework ~ ~3 ~ 0.4 0.4 0.4 0.05 40
execute as @a[tag=so_ev_in] at @s run playsound minecraft:entity.firework_rocket.blast master @s ~ ~ ~ 1 1
title @a[tag=so_ev_in] title {"text": "¡Suministro!", "color": "gold", "bold": true}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Cayó un suministro sobre la isla. ¡Juntalo antes que caiga al vacío!", "color": "gold", "bold": false}]
tag @a remove so_ev_in
