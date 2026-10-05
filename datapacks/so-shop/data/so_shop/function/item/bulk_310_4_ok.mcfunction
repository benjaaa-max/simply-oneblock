clear @s minecraft:emerald 159
give @s minecraft:shulker_shell 8
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x4 (8 objetos) por 159 esmeraldas. Ahorraste 21.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
