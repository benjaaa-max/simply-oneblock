clear @s minecraft:emerald 105
give @s minecraft:shears[minecraft:enchantments={"minecraft:silk_touch":1}] 1
give @s minecraft:shears[minecraft:enchantments={"minecraft:silk_touch":1}] 1
give @s minecraft:shears[minecraft:enchantments={"minecraft:silk_touch":1}] 1
give @s minecraft:shears[minecraft:enchantments={"minecraft:silk_touch":1}] 1
give @s minecraft:shears[minecraft:enchantments={"minecraft:silk_touch":1}] 1
give @s minecraft:shears[minecraft:enchantments={"minecraft:silk_touch":1}] 1
give @s minecraft:shears[minecraft:enchantments={"minecraft:silk_touch":1}] 1
give @s minecraft:shears[minecraft:enchantments={"minecraft:silk_touch":1}] 1
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x8 (8 objetos) por 105 esmeraldas. Ahorraste 23.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
