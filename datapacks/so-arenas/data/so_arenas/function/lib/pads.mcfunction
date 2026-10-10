execute as @a[tag=so_ar_pad] at @s unless block ~ ~ ~ minecraft:light_weighted_pressure_plate run tag @s remove so_ar_pad
execute as @a[tag=so_ar_zone,tag=!so_ar_pad,x=-5003,y=96,z=-4931,dx=0,dy=0,dz=0] run function so_arenas:lib/pad_pr
execute as @a[tag=so_ar_zone,tag=!so_ar_pad,x=-5001,y=96,z=-4931,dx=0,dy=0,dz=0] run function so_arenas:lib/pad_con
execute as @a[tag=so_ar_zone,tag=!so_ar_pad,x=-4999,y=96,z=-4931,dx=0,dy=0,dz=0] run function so_arenas:lib/pad_join
execute as @a[tag=so_ar_zone,tag=!so_ar_pad,x=-4997,y=96,z=-4931,dx=0,dy=0,dz=0] run function so_arenas:lib/pad_back
