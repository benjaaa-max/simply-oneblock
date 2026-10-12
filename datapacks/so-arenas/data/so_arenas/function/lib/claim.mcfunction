tag @s add so_ar_mob
tag @s remove so_ev_mob
execute if score #tg so_ar matches 1 run tag @s add so_ar_target
execute if entity @s[type=#so_arenas:aggro] run tag @s add so_ar_aggro
execute if entity @s[tag=so_ev_boss] run function so_arenas:lib/claim_boss
execute if score #mut_f so_ar matches 1 run effect give @s minecraft:speed infinite 1 true
execute if score #mut_v so_ar matches 1 run effect give @s minecraft:regeneration infinite 1 true
