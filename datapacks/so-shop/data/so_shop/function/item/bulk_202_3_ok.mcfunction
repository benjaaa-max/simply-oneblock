clear @s minecraft:emerald 23
give @s minecraft:blue_glazed_terracotta 48
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x3 (48 objetos) por 23 esmeraldas. Ahorraste 1.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
