scoreboard players set #t so_crates 0
execute in minecraft:overworld run tag @a[x=4969,y=95,z=4979,dx=62,dy=30,dz=42] add so_cr_now
execute as @a[tag=so_cr_now,tag=!so_cr_in] run function so_crates:lib/enter
execute as @a[tag=so_cr_in,tag=!so_cr_now] run function so_crates:lib/leave
execute in minecraft:overworld as @a[tag=so_cr_in,x=4999,y=101,z=5018,dx=2,dy=1,dz=0] at @s run function so_crates:lib/back
scoreboard players add #r so_crates 1
execute if score #r so_crates matches 2.. if entity @a[tag=so_cr_now] in minecraft:overworld run function so_crates:lib/reset_vaults
execute if score #r so_crates matches 2.. run scoreboard players set #r so_crates 0
tag @a remove so_cr_now
