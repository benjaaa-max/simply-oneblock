clear @s minecraft:emerald 85
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:efficiency":4}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:efficiency":4}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:efficiency":4}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:efficiency":4}] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x4 (4 objetos) por 85 esmeraldas. Ahorraste 11.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
