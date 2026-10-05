clear @s minecraft:emerald 57
give @s minecraft:ominous_trial_key[minecraft:custom_name="Wither Arena"] 2
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x2 (2 objetos) por 57 esmeraldas. Ahorraste 3.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
