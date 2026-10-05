clear @s minecraft:emerald 263
give @s minecraft:netherite_scrap 16
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x8 (16 objetos) por 263 esmeraldas. Ahorraste 57.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
