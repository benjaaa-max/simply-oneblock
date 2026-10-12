execute as @a[tag=so_ar_pvp] store result score @s so_ar_hp run data get entity @s Health
execute as @a[tag=so_ar_pvp,scores={so_ar_hp=..6},limit=1] run function so_arenas:mode/pvp/lose
