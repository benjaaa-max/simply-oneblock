scoreboard players set #mimic so_ev 1
execute as @e[tag=so_ev_mim_real] at @s run particle minecraft:firework ~ ~1 ~ 0.4 0.4 0.4 0.05 40
execute as @e[tag=so_ev_mim_real] at @s run playsound minecraft:ui.toast.challenge_complete master @a ~ ~ ~ 1 1
execute as @e[tag=so_ev_mim_fake] at @s run particle minecraft:large_smoke ~ ~0.5 ~ 0.3 0.4 0.3 0.02 30
execute as @e[tag=so_ev_mim_fake] at @s run playsound minecraft:entity.illusioner.mirror_move master @a ~ ~ ~ 1 1
execute as @e[tag=so_ev_mim_fake] at @s run setblock ~ ~ ~ minecraft:air
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Elegiste bien! El cofre era un tesoro de verdad y su gemelo se desvaneció en humo.", "color": "gold", "bold": false}]
