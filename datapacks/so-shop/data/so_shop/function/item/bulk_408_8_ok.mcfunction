clear @s minecraft:emerald 197
give @s minecraft:recovery_compass 1
give @s minecraft:recovery_compass 1
give @s minecraft:recovery_compass 1
give @s minecraft:recovery_compass 1
give @s minecraft:recovery_compass 1
give @s minecraft:recovery_compass 1
give @s minecraft:recovery_compass 1
give @s minecraft:recovery_compass 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x8 (8 objetos) por 197 esmeraldas. Ahorraste 43.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
