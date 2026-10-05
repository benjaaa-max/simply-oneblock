clear @s minecraft:emerald 120
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x4 (4 objetos) por 120 esmeraldas. Ahorraste 16.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
