scoreboard players add #t so_ar 1
execute store result score #alive so_ar if entity @e[tag=so_ar_target]
scoreboard players set #left so_ar 15
scoreboard players operation #left so_ar -= #spawned so_ar
scoreboard players operation #left so_ar += #alive so_ar
execute store result bossbar so_arenas:fight value run scoreboard players get #left so_ar
title @a[tag=so_ar_in] actionbar [{"text": "Caza · quedan ", "color": "aqua"}, {"score": {"name": "#left", "objective": "so_ar"}, "color": "white", "bold": true}, {"text": " objetivos", "color": "gray"}]
execute if score #t so_ar matches 3.. if score #left so_ar matches ..0 run return run function so_arenas:lib/win_contract
execute if score #alive so_ar matches ..1 if score #spawned so_ar matches ..10 run function so_arenas:mode/caza/batch
scoreboard players operation #m so_ar = #t so_ar
scoreboard players operation #m so_ar %= #twentyfive so_ar
execute if score #m so_ar matches 0 run function so_arenas:lib/blocks
execute if score #m so_ar matches 0 if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"skeleton",t:0}
execute if score #m so_ar matches 0 if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"spider",t:0}
execute if score #m so_ar matches 0 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"witch",t:0}
execute if score #m so_ar matches 0 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"skeleton_armor",t:0}
execute if score #m so_ar matches 0 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"spider_big",t:0}
execute if score #m so_ar matches 0 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"skeleton_ominous",t:0}
execute if score #m so_ar matches 0 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"wither_skeleton",t:0}
execute if score #m so_ar matches 0 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"skeleton_ominous",t:0}
execute if score #t so_ar matches 420.. run function so_arenas:lib/fail
