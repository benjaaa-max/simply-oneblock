clear @s minecraft:netherrack 128
give @s minecraft:emerald 5
scoreboard players add @s so_sold 1
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Venta realizada: +5 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
