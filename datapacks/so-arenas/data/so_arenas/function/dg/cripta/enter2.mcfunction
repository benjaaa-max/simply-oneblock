execute as @a[tag=so_ar_dgp] unless entity @s[x=-5023,y=59,z=-5047,dx=14,dy=7,dz=14] run tp @s -5022 60 -5040 -90 0
fill -5027 60 -5041 -5027 63 -5039 minecraft:iron_bars
playsound minecraft:block.iron_door.close master @a[tag=so_ar_dgp] -5027 61 -5040 2 0.6
scoreboard players set #dgs so_ar 3
scoreboard players set #dgr so_ar 2
bossbar set so_arenas:dg value 2
bossbar set so_arenas:dg name {"text": "Cripta de los Caídos · Sala 2/4", "color": "dark_purple"}
title @a[tag=so_ar_dgp] title {"text": "Sala 2/4", "color": "gold", "bold": true}
function so_arenas:dg/cripta/spawn2
