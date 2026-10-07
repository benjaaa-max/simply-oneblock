# Vender 128 netherrack -> 10 esmeraldas
scoreboard players add @s so_sold 0
execute if score @s so_sold >= #sell_limit so_shop run return run function so_shop:lib/sell_limit
scoreboard players set #cost so_shop 128
execute store result score #have so_shop run clear @s minecraft:netherrack 0
execute if score #have so_shop < #cost so_shop run return run function so_shop:lib/fail_reopen {d:"cat_12"}
clear @s minecraft:netherrack 128
give @s minecraft:emerald 10
scoreboard players set @s so_shop_cd 20
scoreboard players add @s so_sold 1
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Venta realizada: +10 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
dialog show @s so_shop:cat_12
