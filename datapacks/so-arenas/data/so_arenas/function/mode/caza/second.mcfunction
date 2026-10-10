scoreboard players add #t so_ar 1
execute unless entity @e[tag=so_ar_target,limit=3] run function so_arenas:lib/win_contract
execute if score #t so_ar matches 420.. run function so_arenas:lib/fail_contract
title @a[tag=so_ar_in] actionbar [{"text": "Caza en curso: quedan ", "color": "aqua"}, {"score": {"name": "#alive", "objective": "so_ar"}, "color": "white", "bold": true}, {"text": " bajas objetivo", "color": "gray"}]
execute store result score #alive so_ar if entity @e[tag=so_ar_target,limit=4]
execute unless entity @e[tag=so_ar_target,limit=4] run scoreboard players set #alive so_ar 3
execute store result bossbar so_arenas:fight value run scoreboard players get #alive so_ar
scoreboard players operation #m so_ar = #t so_ar
scoreboard players operation #m so_ar %= #twentyfive so_ar
execute if score #m so_ar matches 1 as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"skeleton"}
execute if score #m so_ar matches 1 as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"spider"}
