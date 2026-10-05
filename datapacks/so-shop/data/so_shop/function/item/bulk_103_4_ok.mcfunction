clear @s minecraft:emerald 18
give @s minecraft:decorated_pot 16
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x4 (16 objetos) por 18 esmeraldas. Ahorraste 2.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
