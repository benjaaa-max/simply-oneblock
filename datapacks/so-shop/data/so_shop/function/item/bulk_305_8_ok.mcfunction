clear @s minecraft:emerald 184
give @s minecraft:heart_of_the_sea 8
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x8 (8 objetos) por 184 esmeraldas. Ahorraste 40.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
