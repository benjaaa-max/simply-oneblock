clear @s minecraft:emerald 61
give @s minecraft:diamond_hoe[minecraft:enchantments={"minecraft:fortune":2}] 1
give @s minecraft:diamond_hoe[minecraft:enchantments={"minecraft:fortune":2}] 1
give @s minecraft:diamond_hoe[minecraft:enchantments={"minecraft:fortune":2}] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x3 (3 objetos) por 61 esmeraldas. Ahorraste 5.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
