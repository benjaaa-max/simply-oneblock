scoreboard objectives setdisplay sidebar
bossbar remove so_status:progress
execute as @e[type=minecraft:marker,tag=so_status_craft] at @s if block ~ ~ ~ minecraft:crafting_table run setblock ~ ~ ~ minecraft:air
execute as @e[type=minecraft:marker,tag=so_status_ender] at @s if block ~ ~ ~ minecraft:ender_chest run setblock ~ ~ ~ minecraft:air
kill @e[type=minecraft:marker,tag=so_status_temp]
tag @a remove so_afk
team remove so_admin
team remove so_vorlegend
team remove so_nexlord
team remove so_voruser
scoreboard objectives remove heal
scoreboard objectives remove feed
scoreboard objectives remove craft
scoreboard objectives remove enderchest
scoreboard objectives remove hat
scoreboard objectives remove afk
scoreboard objectives remove so_cd_heal
scoreboard objectives remove so_cd_feed
scoreboard objectives remove so_temp_age
scoreboard objectives remove so_playtime
scoreboard objectives remove so_sidebar
scoreboard objectives remove so_sys
scoreboard objectives remove so_cfg
tellraw @a {"text":"[SO Status] Retirado. Los demás datapacks no fueron modificados.","color":"red"}
