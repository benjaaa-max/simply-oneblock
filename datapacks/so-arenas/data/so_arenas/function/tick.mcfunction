scoreboard players add #beat so_ar 1
execute as @a[scores={arena=1..}] at @s run function so_arenas:lib/go
execute as @a[scores={volver=1..}] at @s run function so_arenas:lib/volver
execute as @a[scores={arena_pr=1..}] at @s run function so_arenas:lib/start_pr
execute as @a[scores={arena_con=1..}] at @s run function so_arenas:lib/start_con
execute as @a[scores={levelrank=1..}] run function so_arenas:lib/rank
execute as @a[scores={arena_dj=1..}] run function so_arenas:lib/dj
execute as @a[scores={arena_mut=1..}] run function so_arenas:lib/mut
execute as @a[scores={arena_ver=1..}] at @s run function so_arenas:lib/ver
execute as @a[scores={arena_pvp=1..}] at @s run function so_arenas:lib/pvp
execute as @a[scores={arena_dg=1..}] at @s run function so_arenas:dg/trigger
scoreboard players reset @a arena
scoreboard players reset @a volver
scoreboard players reset @a arena_pr
scoreboard players reset @a arena_con
scoreboard players reset @a levelrank
scoreboard players reset @a arena_dj
scoreboard players reset @a arena_mut
scoreboard players reset @a arena_ver
scoreboard players reset @a arena_pvp
scoreboard players reset @a arena_dg
scoreboard players enable @a arena
scoreboard players enable @a volver
scoreboard players enable @a arena_pr
scoreboard players enable @a arena_con
scoreboard players enable @a levelrank
scoreboard players enable @a arena_dj
scoreboard players enable @a arena_mut
scoreboard players enable @a arena_ver
scoreboard players enable @a arena_pvp
scoreboard players enable @a arena_dg
# duelo: vida chequeada cada tick (se corta antes de morir)
execute if score #mode so_ar matches 10 run function so_arenas:mode/pvp/tick
execute if score #beat so_ar matches 10 run function so_arenas:lib/pads
execute if score #beat so_ar matches 20.. run function so_arenas:lib/pads
execute if score #beat so_ar matches 20.. run function so_arenas:lib/second
execute if score #beat so_ar matches 20.. run scoreboard players set #beat so_ar 0
