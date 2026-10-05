clear @s minecraft:emerald 50
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:protection":4}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:protection":4}] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x2 (2 objetos) por 50 esmeraldas. Ahorraste 2.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
