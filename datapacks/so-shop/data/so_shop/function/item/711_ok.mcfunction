clear @s minecraft:emerald 5
give @s minecraft:trial_key[minecraft:custom_name="Cemetery Key"] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste Cemetery Key por 5 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
