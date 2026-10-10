# Limpieza total: mobs al vacío (sin drops), barras, marcas y regla de griefing.
tp @e[tag=so_ev_mob] 0 -300 0
kill @e[tag=so_ev_mob]
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
