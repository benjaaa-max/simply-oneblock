clear @s minecraft:emerald 83
give @s minecraft:ominous_trial_key[minecraft:custom_name="Wither Arena"] 3
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x3 (3 objetos) por 83 esmeraldas. Ahorraste 7.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
