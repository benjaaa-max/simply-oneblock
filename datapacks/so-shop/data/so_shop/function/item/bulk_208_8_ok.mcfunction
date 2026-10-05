clear @s minecraft:emerald 46
give @s minecraft:copper_grate 64
give @s minecraft:copper_grate 64
give @s minecraft:copper_grate 64
give @s minecraft:copper_grate 64
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x8 (256 objetos) por 46 esmeraldas. Ahorraste 10.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
