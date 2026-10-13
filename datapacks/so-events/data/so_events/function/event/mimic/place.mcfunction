execute if score #side so_ev matches 1 positioned ~2 ~ ~2 if block ~ ~ ~ #minecraft:air run setblock ~ ~ ~ minecraft:chest[facing=north]{LootTable:"so_events:mimic_treasure"}
execute if score #side so_ev matches 1 positioned ~-2 ~ ~2 if block ~ ~ ~ #minecraft:air run setblock ~ ~ ~ minecraft:chest[facing=north]{LootTable:"so_events:mimic_junk"}
execute if score #side so_ev matches 2 positioned ~2 ~ ~2 if block ~ ~ ~ #minecraft:air run setblock ~ ~ ~ minecraft:chest[facing=north]{LootTable:"so_events:mimic_junk"}
execute if score #side so_ev matches 2 positioned ~-2 ~ ~2 if block ~ ~ ~ #minecraft:air run setblock ~ ~ ~ minecraft:chest[facing=north]{LootTable:"so_events:mimic_treasure"}
execute positioned ~2 ~ ~2 if block ~ ~ ~ minecraft:chest run summon minecraft:marker ~ ~ ~ {Tags:["so_ev_mimic","so_ev_mim_a"]}
execute positioned ~-2 ~ ~2 if block ~ ~ ~ minecraft:chest run summon minecraft:marker ~ ~ ~ {Tags:["so_ev_mimic","so_ev_mim_b"]}
execute if score #side so_ev matches 1 as @e[tag=so_ev_mim_a] run tag @s add so_ev_mim_real
execute if score #side so_ev matches 2 as @e[tag=so_ev_mim_b] run tag @s add so_ev_mim_real
tag @e[tag=so_ev_mimic,tag=!so_ev_mim_real] add so_ev_mim_fake
execute as @e[tag=so_ev_mimic] at @s run particle minecraft:witch ~ ~0.5 ~ 0.3 0.3 0.3 0.02 20
execute as @e[tag=so_ev_mimic] at @s run playsound minecraft:block.amethyst_block.chime master @a ~ ~ ~ 1 0.6
