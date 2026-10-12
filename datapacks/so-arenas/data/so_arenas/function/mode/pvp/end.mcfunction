effect give @a[tag=so_ar_pvp] minecraft:instant_health 1 10 true
effect clear @a[tag=so_ar_pvp] minecraft:resistance
tag @a remove so_ar_pvp
function so_arenas:lib/music_stop
scoreboard players set #mode so_ar 0
scoreboard players set #exit so_ar 1
scoreboard players set #ext so_ar 4
