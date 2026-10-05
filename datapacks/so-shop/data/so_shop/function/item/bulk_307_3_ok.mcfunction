clear @s minecraft:emerald 111
give @s minecraft:netherite_scrap 6
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x3 (6 objetos) por 111 esmeraldas. Ahorraste 9.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
