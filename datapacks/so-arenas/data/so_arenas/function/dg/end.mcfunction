# Reinicio limpio: enemigos, ítems, trampas, llaves, cofres, puertas y bloques de la mazmorra activa.
execute as @e[tag=so_ar_dgm] run tp @s -5000 -300 -5000
kill @e[tag=so_ar_dgm]
kill @e[type=minecraft:item,x=-5048,y=50,z=-5054,dx=90,dy=26,dz=84]
kill @e[type=minecraft:experience_orb,x=-5048,y=50,z=-5054,dx=90,dy=26,dz=84]
kill @e[type=minecraft:arrow,x=-5048,y=50,z=-5054,dx=90,dy=26,dz=84]
kill @e[type=minecraft:spectral_arrow,x=-5048,y=50,z=-5054,dx=90,dy=26,dz=84]
kill @e[type=minecraft:trident,x=-5048,y=50,z=-5054,dx=90,dy=26,dz=84]
kill @e[type=minecraft:falling_block,x=-5048,y=50,z=-5054,dx=90,dy=26,dz=84]
clear @a *[minecraft:custom_data~{so_ar_dgkey:1b}]
bossbar set so_arenas:dg visible false
execute if score #dg so_ar matches 1 run function so_arenas:dg/cripta/reset
execute if score #dg so_ar matches 2 run function so_arenas:dg/mina/reset
execute if score #dg so_ar matches 3 run function so_arenas:dg/templo/reset
scoreboard players set #dg so_ar 0
scoreboard players set #dgs so_ar 0
scoreboard players set #dgr so_ar 0
tag @a remove so_ar_dgp
schedule function so_arenas:dg/unload 40t
