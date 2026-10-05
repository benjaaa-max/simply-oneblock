clear @s minecraft:emerald 224
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x8 (8 objetos) por 224 esmeraldas. Ahorraste 48.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
