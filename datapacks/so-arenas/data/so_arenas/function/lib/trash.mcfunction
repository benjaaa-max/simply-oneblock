execute positioned -5003 96 -4938 if entity @e[type=minecraft:item,dx=0,dy=1,dz=0] run particle minecraft:large_smoke -5003.5 97 -4938.5 0.2 0.2 0.2 0.01 10
execute positioned -5003 96 -4938 if entity @e[type=minecraft:item,dx=0,dy=1,dz=0] run playsound minecraft:block.lava.extinguish master @a[distance=..12] ~ ~ ~ 0.6 1
execute positioned -5003 96 -4938 run kill @e[type=minecraft:item,dx=0,dy=1,dz=0]
execute if score #playing so_ar matches 1 run particle minecraft:note -4996.5 110.2 -5047.5 0.3 0.2 0.3 1 2
execute if score #playing so_ar matches 1 run particle minecraft:note -4972.5 102.2 -5000.5 0.3 0.2 0.3 1 2
execute if score #playing so_ar matches 1 run particle minecraft:note -5028.5 102.2 -5000.5 0.3 0.2 0.3 1 2
execute if score #playing so_ar matches 1 run particle minecraft:note -5043.5 97.2 -4979.5 0.3 0.2 0.3 1 2
execute if score #playing so_ar matches 1 run particle minecraft:note -4957.5 97.2 -5021.5 0.3 0.2 0.3 1 2
