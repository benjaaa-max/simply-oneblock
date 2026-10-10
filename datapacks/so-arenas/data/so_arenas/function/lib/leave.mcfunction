tag @s remove so_ar_zone
tag @s remove so_ar_in
tag @s remove so_ar_pad
clear @s *[minecraft:custom_data~{so_arena_loan:1b}]
tag @s remove so_ar_loan
execute if entity @s[tag=so_ar_gm,gamemode=adventure] run gamemode survival @s
tag @s remove so_ar_gm
scoreboard players reset @s so_ar_air
