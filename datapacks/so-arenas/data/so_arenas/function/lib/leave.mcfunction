tag @s remove so_ar_zone
tag @s remove so_ar_in
tag @s remove so_ar_pad
tag @s remove so_ar_ready
tag @s remove so_ar_win
tag @s remove so_ar_pvpw
tag @s remove so_ar_dgp
clear @s *[minecraft:custom_data~{so_arena_loan:1b}]
clear @s *[minecraft:custom_data~{so_ar_dgkey:1b}]
tag @s remove so_ar_loan
execute if entity @s[tag=so_ar_spec] run effect clear @s minecraft:invisibility
tag @s remove so_ar_spec
execute if entity @s[tag=so_ar_gm,gamemode=adventure] run gamemode survival @s
tag @s remove so_ar_gm
stopsound @s record
scoreboard players reset @s so_ar_air
