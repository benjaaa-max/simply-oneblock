clear @s minecraft:emerald 40
give @s minecraft:netherite_scrap 2
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste ","color":"green"},{"text":"Netherite scrap x2","color":"white"},{"text":" por 40 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4
scoreboard players add @s so_shop_buys 1
