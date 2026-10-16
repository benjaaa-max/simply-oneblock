scoreboard players set #phase so_ev 3
title @a[tag=so_ev_in] title {"text": "Fase III: Ascensión", "color": "gold", "bold": true}
effect give @a[tag=so_ev_in] minecraft:absorption 180 2 true
effect give @a[tag=so_ev_in] minecraft:luck 180 0 true
execute as @e[tag=so_ev_altar,limit=1] at @s run particle minecraft:totem_of_undying ~0.5 ~1 ~0.5 1 1 1 0.4 80
execute as @e[tag=so_ev_altar,limit=1] at @s run playsound minecraft:block.respawn_anchor.set_spawn master @a ~ ~ ~ 2 1
playsound minecraft:block.bell.use master @a ~ ~ ~ 1 1.5
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Fase III! Absorción III. El altar está pleno.", "color": "gold", "bold": false}]
