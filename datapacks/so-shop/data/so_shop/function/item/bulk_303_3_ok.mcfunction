clear @s minecraft:emerald 39
give @s minecraft:sculk 64
give @s minecraft:sculk 32
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x3 (96 objetos) por 39 esmeraldas. Ahorraste 3.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
