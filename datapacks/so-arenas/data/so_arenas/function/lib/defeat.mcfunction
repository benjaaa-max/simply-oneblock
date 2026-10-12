function so_arenas:lib/music_stop
execute as @a[tag=so_ar_zone] at @s run playsound minecraft:entity.wither.death master @s ~ ~ ~ 0.4 1.6
title @a[tag=so_ar_in] title {"text": "Derrota", "color": "dark_red", "bold": true}
scoreboard players set @a[tag=so_ar_in] so_ar_streak 0
function so_arenas:lib/end_fight
scoreboard players set #exit so_ar 1
scoreboard players set #ext so_ar 3
