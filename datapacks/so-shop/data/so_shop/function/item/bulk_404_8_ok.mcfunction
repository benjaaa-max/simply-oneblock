clear @s minecraft:emerald 145
give @s minecraft:diamond_hoe[minecraft:enchantments={"minecraft:fortune":2}] 1
give @s minecraft:diamond_hoe[minecraft:enchantments={"minecraft:fortune":2}] 1
give @s minecraft:diamond_hoe[minecraft:enchantments={"minecraft:fortune":2}] 1
give @s minecraft:diamond_hoe[minecraft:enchantments={"minecraft:fortune":2}] 1
give @s minecraft:diamond_hoe[minecraft:enchantments={"minecraft:fortune":2}] 1
give @s minecraft:diamond_hoe[minecraft:enchantments={"minecraft:fortune":2}] 1
give @s minecraft:diamond_hoe[minecraft:enchantments={"minecraft:fortune":2}] 1
give @s minecraft:diamond_hoe[minecraft:enchantments={"minecraft:fortune":2}] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x8 (8 objetos) por 145 esmeraldas. Ahorraste 31.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
