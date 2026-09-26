clear @s minecraft:cobblestone 128
give @s minecraft:emerald 6
scoreboard players set @s so_shop_cd 20
scoreboard players add @s so_sold 1
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Venta realizada: +6 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
