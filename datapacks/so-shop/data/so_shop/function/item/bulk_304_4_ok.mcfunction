clear @s minecraft:emerald 71
give @s minecraft:echo_shard 8
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x4 (8 objetos) por 71 esmeraldas. Ahorraste 9.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
