scoreboard players set #phase so_ev 1
title @a[tag=so_ev_in] title {"text": "Fase I: Bendición", "color": "gold", "bold": true}
effect give @a[tag=so_ev_in] minecraft:haste 180 1 true
execute as @e[tag=so_ev_altar,limit=1] at @s run particle minecraft:totem_of_undying ~0.5 ~1 ~0.5 1 1 1 0.4 80
execute as @e[tag=so_ev_altar,limit=1] at @s run playsound minecraft:block.respawn_anchor.set_spawn master @a ~ ~ ~ 2 1
playsound minecraft:block.bell.use master @a ~ ~ ~ 1 1.5
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Fase I! Prisa II para la isla. Sigan ofrendando…", "color": "gold", "bold": false}]
