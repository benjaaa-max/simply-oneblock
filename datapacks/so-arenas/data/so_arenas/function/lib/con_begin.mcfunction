function so_arenas:lib/blocks
scoreboard players set #t so_ar 0
scoreboard players set #wave so_ar 0
scoreboard players set #spawned so_ar 0
scoreboard players set #anticamp so_ar 1
scoreboard players set #rew so_ar 10
bossbar set so_arenas:fight players @a[tag=so_ar_in]
bossbar set so_arenas:fight visible true
execute if score #con so_ar matches 1 run function so_arenas:mode/caza/start
execute if score #con so_ar matches 2 run function so_arenas:mode/caza2/start
execute if score #con so_ar matches 3 run function so_arenas:mode/defensa/start
execute if score #con so_ar matches 4 run function so_arenas:mode/rey/start
execute if score #con so_ar matches 5 run function so_arenas:mode/asedio/start
execute if score #con so_ar matches 6 run scoreboard players set #jt so_ar 1
execute if score #con so_ar matches 7 run scoreboard players set #jt so_ar 2
execute if score #con so_ar matches 6..7 run function so_arenas:mode/jefes/start
