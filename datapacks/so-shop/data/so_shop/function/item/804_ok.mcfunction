clear @s minecraft:dried_kelp 64
give @s minecraft:emerald 4
scoreboard players add @s so_sold 1
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Venta realizada: +4 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
