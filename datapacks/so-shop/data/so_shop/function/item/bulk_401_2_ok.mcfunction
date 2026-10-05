clear @s minecraft:emerald 27
give @s minecraft:iron_pickaxe[minecraft:enchantments={"minecraft:efficiency":3}] 1
give @s minecraft:iron_pickaxe[minecraft:enchantments={"minecraft:efficiency":3}] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x2 (2 objetos) por 27 esmeraldas. Ahorraste 1.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
