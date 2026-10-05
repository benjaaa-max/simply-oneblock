clear @s minecraft:emerald 17
give @s minecraft:lantern 24
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x3 (24 objetos) por 17 esmeraldas. Ahorraste 1.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
