clear @s minecraft:emerald 125
give @s minecraft:sniffer_spawn_egg 3
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x3 (3 objetos) por 125 esmeraldas. Ahorraste 10.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
