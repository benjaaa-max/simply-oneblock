clear @s minecraft:emerald 10
give @s minecraft:trial_key[minecraft:custom_name="Pyramid Key"] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste Pyramid Key por 10 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
