scoreboard players add @e[type=minecraft:marker,tag=so_status_temp] so_temp_age 1
execute as @e[type=minecraft:marker,tag=so_status_craft,scores={so_temp_age=300..}] at @s if block ~ ~ ~ minecraft:crafting_table run setblock ~ ~ ~ minecraft:air
execute as @e[type=minecraft:marker,tag=so_status_ender,scores={so_temp_age=300..}] at @s if block ~ ~ ~ minecraft:ender_chest run setblock ~ ~ ~ minecraft:air
kill @e[type=minecraft:marker,tag=so_status_temp,scores={so_temp_age=300..}]
