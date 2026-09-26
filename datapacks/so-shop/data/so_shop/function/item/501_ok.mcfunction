clear @s minecraft:emerald 34
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste ","color":"green"},{"text":"Libro: Reparación","color":"white"},{"text":" por 34 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4
