clear @s minecraft:emerald 10
give @s minecraft:decorated_pot 8
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x2 (8 objetos) por 10 esmeraldas. Ahorraste 0.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
