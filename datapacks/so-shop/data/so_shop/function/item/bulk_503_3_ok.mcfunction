clear @s minecraft:emerald 78
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:silk_touch":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:silk_touch":1}] 1
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:silk_touch":1}] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x3 (3 objetos) por 78 esmeraldas. Ahorraste 6.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
