clear @s minecraft:emerald 15
give @s minecraft:water_bucket 1
give @s minecraft:water_bucket 1
give @s minecraft:water_bucket 1
give @s minecraft:water_bucket 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x2 (4 objetos) por 15 esmeraldas. Ahorraste 1.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
