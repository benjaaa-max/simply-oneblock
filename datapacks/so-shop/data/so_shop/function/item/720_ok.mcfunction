clear @s minecraft:emerald 26
give @s minecraft:ominous_trial_key[minecraft:custom_name="Warden_Key"] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste Warden_Key por 26 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
