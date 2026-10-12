tag @s add so_ar_zone
execute unless entity @s[tag=oneblock_admin] if entity @s[gamemode=survival] run tag @s add so_ar_gm
execute if entity @s[tag=so_ar_gm] run gamemode adventure @s
execute if score #playing so_ar matches 1 run function so_arenas:lib/music_one
