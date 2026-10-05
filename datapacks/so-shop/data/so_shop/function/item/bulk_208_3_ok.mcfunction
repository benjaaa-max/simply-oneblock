clear @s minecraft:emerald 20
give @s minecraft:copper_grate 64
give @s minecraft:copper_grate 32
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x3 (96 objetos) por 20 esmeraldas. Ahorraste 1.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
