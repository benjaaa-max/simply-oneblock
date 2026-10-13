scoreboard players set #mimic so_ev 2
execute as @e[tag=so_ev_mim_real] at @s run particle minecraft:large_smoke ~ ~0.5 ~ 0.3 0.4 0.3 0.02 30
execute as @e[tag=so_ev_mim_real] at @s run setblock ~ ~ ~ minecraft:air
execute as @e[tag=so_ev_mim_fake] at @s run playsound minecraft:event.raid.horn hostile @a ~ ~ ~ 1 1.4
execute as @e[tag=so_ev_mim_fake] at @s run playsound minecraft:entity.vex.charge hostile @a ~ ~ ~ 1 0.8
execute as @e[tag=so_ev_mim_fake] at @s run particle minecraft:soul ~ ~1 ~ 0.4 0.4 0.4 0.05 30
execute as @e[tag=so_ev_mim_fake,limit=1] at @s positioned ~ ~1 ~ run function so_events:mob/elite_vex
execute as @e[tag=so_ev_mim_fake,limit=1] at @s positioned ~ ~1 ~ run function so_events:mob/elite_vex
execute as @e[tag=so_ev_mim_fake,limit=1] at @s positioned ~ ~1 ~ run function so_events:mob/elite_vex
execute as @e[tag=so_ev_mim_fake,limit=1] at @s positioned ~ ~6 ~ run function so_events:mob/phantom
execute as @e[tag=so_ev_mim_fake,limit=1] at @s positioned ~ ~6 ~ run function so_events:mob/phantom
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Era una trampa! El cofre solo tenía chatarra y salen vexes espectrales con phantoms. ¡Derrotalos!", "color": "red", "bold": false}]
