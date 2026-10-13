execute as @a[scores={evento=1..}] run function so_events:lib/info
execute as @a[scores={evento_diario=1..}] run function so_events:lib/diary
scoreboard players reset @a evento
scoreboard players enable @a evento
scoreboard players reset @a evento_diario
scoreboard players enable @a evento_diario
scoreboard players add #beat so_ev 1
execute if score #beat so_ev matches 20.. run function so_events:lib/second
execute if score #beat so_ev matches 20.. run scoreboard players set #beat so_ev 0
