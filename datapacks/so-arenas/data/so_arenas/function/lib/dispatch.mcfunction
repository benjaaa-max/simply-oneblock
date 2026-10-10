execute if score @s arena matches 1 run function so_arenas:lib/go
execute if score @s arena matches 2 run function so_arenas:lib/volver
execute if score @s arena_pr matches 1..14 run function so_arenas:lib/start_pr
execute if score @s arena_con matches 1..3 run function so_arenas:lib/start_con
scoreboard players reset @a arena
scoreboard players reset @a arena_pr
scoreboard players reset @a arena_con
scoreboard players enable @a arena
scoreboard players enable @a arena_pr
scoreboard players enable @a arena_con
scoreboard players enable @a levelrank
