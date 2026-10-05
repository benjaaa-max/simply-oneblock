clear @s minecraft:emerald 29
give @s minecraft:blue_glazed_terracotta 64
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x4 (64 objetos) por 29 esmeraldas. Ahorraste 3.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
