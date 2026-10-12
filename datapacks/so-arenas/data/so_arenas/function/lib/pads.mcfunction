execute as @a[tag=so_ar_pad] at @s unless block ~ ~ ~ #minecraft:pressure_plates run tag @s remove so_ar_pad
execute as @a[tag=so_ar_zone,tag=!so_ar_pad,x=-5003,y=96,z=-4931,dx=0,dy=0,dz=0] run function so_arenas:lib/pad_pr
execute as @a[tag=so_ar_zone,tag=!so_ar_pad,x=-5001,y=96,z=-4931,dx=0,dy=0,dz=0] run function so_arenas:lib/pad_con
execute as @a[tag=so_ar_zone,tag=!so_ar_pad,x=-4999,y=96,z=-4931,dx=0,dy=0,dz=0] run function so_arenas:lib/pad_join
execute as @a[tag=so_ar_zone,tag=!so_ar_pad,x=-4997,y=96,z=-4931,dx=0,dy=0,dz=0] run function so_arenas:lib/pad_back
execute if score #mode so_ar matches 9 as @a[tag=so_ar_ready,tag=!so_ar_pad,x=-5000,y=96,z=-4967,dx=0,dy=0,dz=0] run function so_arenas:lib/pad_start
execute if score #mode so_ar matches 0 as @a[tag=so_ar_zone,tag=!so_ar_pad,x=-5000,y=96,z=-4941,dx=0,dy=0,dz=0] run function so_arenas:lib/pad_exit
execute as @a[tag=so_ar_zone,tag=!so_ar_pad,x=-5000,y=96,z=-4915,dx=0,dy=0,dz=0] run function so_arenas:lib/pad_dg
