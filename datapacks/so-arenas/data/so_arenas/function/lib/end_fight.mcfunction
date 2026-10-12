# Fin de combate: mobs al vacío (sin drops), cebo, núcleo y barra.
tp @e[tag=so_ar_mob] -5000 -300 -5000
kill @e[tag=so_ar_mob]
kill @e[tag=so_ar_bait,x=-5056,y=50,z=-5066,dx=112,dy=160,dz=158]
setblock -5000 96 -5000 minecraft:air
bossbar set so_arenas:fight visible false
scoreboard players set #mode so_ar 0
scoreboard players set #wave so_ar 0
scoreboard players set #t so_ar 0
scoreboard players set #anticamp so_ar 1
scoreboard players reset @a so_ar_air
