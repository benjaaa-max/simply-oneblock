clear @s minecraft:emerald 94
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:mending":1}] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x3 (3 objetos) por 94 esmeraldas. Ahorraste 8.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
