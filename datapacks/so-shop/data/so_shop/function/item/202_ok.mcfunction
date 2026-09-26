clear @s minecraft:emerald 8
give @s minecraft:blue_glazed_terracotta 16
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste ","color":"green"},{"text":"Terracota vidriada surtida x16","color":"white"},{"text":" por 8 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4
