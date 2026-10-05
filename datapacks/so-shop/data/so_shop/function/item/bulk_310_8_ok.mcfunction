clear @s minecraft:emerald 296
give @s minecraft:shulker_shell 16
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x8 (16 objetos) por 296 esmeraldas. Ahorraste 64.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
