clear @s minecraft:emerald 27
give @s minecraft:white_wool 64
give @s minecraft:white_wool 64
give @s minecraft:white_wool 64
give @s minecraft:white_wool 64
give @s minecraft:white_wool 64
give @s minecraft:white_wool 64
give @s minecraft:white_wool 64
give @s minecraft:white_wool 64
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x8 (512 objetos) por 27 esmeraldas. Ahorraste 5.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
