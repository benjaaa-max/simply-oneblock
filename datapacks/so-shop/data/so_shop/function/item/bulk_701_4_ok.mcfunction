clear @s minecraft:emerald 57
give @s minecraft:trial_key 4
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x4 (4 objetos) por 57 esmeraldas. Ahorraste 7.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
