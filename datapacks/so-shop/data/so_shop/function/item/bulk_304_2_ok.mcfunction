clear @s minecraft:emerald 38
give @s minecraft:echo_shard 4
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x2 (4 objetos) por 38 esmeraldas. Ahorraste 2.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
