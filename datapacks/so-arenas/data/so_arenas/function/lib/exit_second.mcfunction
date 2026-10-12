scoreboard players remove #ext so_ar 1
execute if score #ext so_ar matches 4.. store result bossbar so_arenas:fight value run scoreboard players get #ext so_ar
execute if score #ext so_ar matches ..0 run function so_arenas:lib/close_pit
