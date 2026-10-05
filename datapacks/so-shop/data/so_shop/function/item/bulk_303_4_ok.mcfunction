clear @s minecraft:emerald 50
give @s minecraft:sculk 64
give @s minecraft:sculk 64
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x4 (128 objetos) por 50 esmeraldas. Ahorraste 6.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
