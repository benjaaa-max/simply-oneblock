execute unless score #dg so_ar matches 3 run return 0
function so_arenas:dg/templo/spawn1
scoreboard players set #dgs so_ar 1
scoreboard players set #dgt so_ar 0
execute as @a[tag=so_ar_dgp] at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 0.8
