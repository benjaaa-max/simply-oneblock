clear @s minecraft:emerald 76
give @s minecraft:allay_spawn_egg 2
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x2 (2 objetos) por 76 esmeraldas. Ahorraste 4.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
