clear @s minecraft:emerald 78
give @s minecraft:ominous_trial_key[minecraft:custom_name="Elder Guardian Key"] 4
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x4 (4 objetos) por 78 esmeraldas. Ahorraste 10.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
