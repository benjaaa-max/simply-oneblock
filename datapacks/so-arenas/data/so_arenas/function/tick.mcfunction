scoreboard players add #beat so_ar 1
execute as @a[scores={arena=1..}] run function so_arenas:lib/dispatch
execute if score #beat so_ar matches 20.. run function so_arenas:lib/second
execute if score #beat so_ar matches 20.. run scoreboard players set #beat so_ar 0
