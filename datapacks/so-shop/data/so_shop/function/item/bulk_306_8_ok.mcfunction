clear @s minecraft:emerald 60
give @s minecraft:amethyst_block 64
give @s minecraft:amethyst_block 64
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x8 (128 objetos) por 60 esmeraldas. Ahorraste 12.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
