clear @s minecraft:emerald 29
give @s minecraft:water_bucket 1
give @s minecraft:water_bucket 1
give @s minecraft:water_bucket 1
give @s minecraft:water_bucket 1
give @s minecraft:water_bucket 1
give @s minecraft:water_bucket 1
give @s minecraft:water_bucket 1
give @s minecraft:water_bucket 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x4 (8 objetos) por 29 esmeraldas. Ahorraste 3.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
