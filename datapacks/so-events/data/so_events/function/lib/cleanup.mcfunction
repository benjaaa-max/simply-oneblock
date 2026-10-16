# Limpieza total: mobs al vacío (sin drops), barras, marcas y regla de griefing.
tp @e[tag=so_ev_mob] 0 -300 0
kill @e[tag=so_ev_mob]
execute as @e[type=minecraft:marker,tag=so_ev_beacon] at @s run function so_events:event/altar/unbuild
kill @e[tag=so_ev_altar]
stopsound @a record
kill @e[tag=so_ev_mimic]
kill @e[tag=so_ev_llama]
scoreboard players set #alpha so_ev 0
scoreboard players set #mimic so_ev 0
bossbar set so_events:ev visible false
bossbar set so_events:boss visible false
execute if score #mg_saved so_ev matches 1 if score #mg_prev so_ev matches 1 run gamerule mob_griefing true
scoreboard players set #mg_saved so_ev 0
effect clear @a[tag=so_ev_in] minecraft:darkness
tag @a remove so_ev_in
scoreboard players set #active so_ev 0
scoreboard players set #t so_ev 0
scoreboard players set #stage so_ev 0
scoreboard players set #wave so_ev 0
scoreboard players set #hits so_ev 0
scoreboard players set #paid so_ev 0
