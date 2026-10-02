clear @s minecraft:emerald 6
give @s minecraft:cyan_stained_glass 64
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste ","color":"green"},{"text":"Cristal coloreado x64 (cian)","color":"white"},{"text":" por 6 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4
scoreboard players add @s so_shop_buys 1
