execute as @a[tag=so_ar_dgp] unless entity @s[x=-4980,y=59,z=-5022,dx=20,dy=11,dz=20] run tp @s -4979 60 -5012 -90 0
fill -4984 60 -5013 -4984 63 -5011 minecraft:iron_bars
playsound minecraft:block.iron_door.close master @a[tag=so_ar_dgp] -4984 61 -5012 2 0.6
scoreboard players set #dgs so_ar 8
scoreboard players set #dgr so_ar 4
bossbar set so_arenas:dg value 4
bossbar set so_arenas:dg name {"text": "Mina Abandonada · Sala 4/4", "color": "dark_purple"}
title @a[tag=so_ar_dgp] title {"text": "Rey Araña", "color": "dark_red", "bold": true}
function so_arenas:dg/mina/spawn4
execute as @a[tag=so_ar_dgp] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.6 0.8
