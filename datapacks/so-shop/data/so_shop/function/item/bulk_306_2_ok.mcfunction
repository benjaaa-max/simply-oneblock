clear @s minecraft:emerald 18
give @s minecraft:amethyst_block 32
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x2 (32 objetos) por 18 esmeraldas. Ahorraste 0.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
