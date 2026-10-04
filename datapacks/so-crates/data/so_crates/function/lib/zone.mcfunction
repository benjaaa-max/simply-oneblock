scoreboard players set #t so_crates 0
execute in minecraft:overworld run tag @a[x=4984,y=194,z=4984,dx=32,dy=20,dz=32] add so_cr_now
execute as @a[tag=so_cr_now,tag=!so_cr_in] run function so_crates:lib/enter
execute as @a[tag=so_cr_in,tag=!so_cr_now] run function so_crates:lib/leave
scoreboard players add #r so_crates 1
execute if score #r so_crates matches 2.. if entity @a[tag=so_cr_now] in minecraft:overworld run function so_crates:lib/reset_vaults
execute if score #r so_crates matches 2.. run scoreboard players set #r so_crates 0
tag @a remove so_cr_now
