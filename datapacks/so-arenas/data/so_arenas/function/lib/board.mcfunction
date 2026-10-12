execute store result storage so_arenas:b w int 1 run scoreboard players get #wave so_ar
execute store result storage so_arenas:b a int 1 if entity @e[tag=so_ar_mob]
execute store result storage so_arenas:b t int 1 run scoreboard players get #t so_ar
function so_arenas:lib/board_set with storage so_arenas:b
