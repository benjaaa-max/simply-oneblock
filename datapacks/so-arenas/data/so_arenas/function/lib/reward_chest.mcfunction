# Contenedor estético al azar en el pedestal del lobby (el anterior se reemplaza).
execute store result score #r so_ar run random value 0..6
setblock -4997 96 -4938 minecraft:air
execute if score #r so_ar matches 0 run setblock -4997 96 -4938 minecraft:chest[facing=west]
execute if score #r so_ar matches 1 run setblock -4997 96 -4938 minecraft:trapped_chest[facing=west]
execute if score #r so_ar matches 2 run setblock -4997 96 -4938 minecraft:barrel[facing=up]
execute if score #r so_ar matches 3 run setblock -4997 96 -4938 minecraft:copper_chest[facing=west]
execute if score #r so_ar matches 4 run setblock -4997 96 -4938 minecraft:exposed_copper_chest[facing=west]
execute if score #r so_ar matches 5 run setblock -4997 96 -4938 minecraft:weathered_copper_chest[facing=west]
execute if score #r so_ar matches 6 run setblock -4997 96 -4938 minecraft:oxidized_copper_chest[facing=west]
execute as @a[tag=so_ar_win] run function so_arenas:lib/reward_one
particle minecraft:happy_villager -4997.5 97 -4938.5 0.4 0.4 0.4 0 20 force
