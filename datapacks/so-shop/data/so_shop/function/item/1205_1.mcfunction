# Vender 64 troncos de roble -> 16 esmeraldas
scoreboard players add @s so_sold 0
execute if score @s so_sold >= #sell_limit so_shop run return run function so_shop:lib/sell_limit
scoreboard players set #cost so_shop 64
execute store result score #have so_shop run clear @s minecraft:oak_log 0
execute if score #have so_shop < #cost so_shop run return run function so_shop:lib/fail_reopen {d:"cat_12"}
clear @s minecraft:oak_log 64
give @s minecraft:emerald 16
scoreboard players set @s so_shop_cd 20
scoreboard players add @s so_sold 1
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Venta realizada: +16 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
dialog show @s so_shop:cat_12
