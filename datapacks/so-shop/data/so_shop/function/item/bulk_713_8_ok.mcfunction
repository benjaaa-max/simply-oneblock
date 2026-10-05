clear @s minecraft:emerald 40
give @s minecraft:trial_key[minecraft:custom_name="Ossuary Key"] 8
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x8 (8 objetos) por 40 esmeraldas. Ahorraste 8.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
