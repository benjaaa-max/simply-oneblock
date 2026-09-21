# Vender 128 piedra
scoreboard players add @s so_sold 0
scoreboard players set #cost so_shop 128
execute store result score #have so_shop run clear @s minecraft:cobblestone 0
execute if score @s so_sold >= #sell_limit so_shop run function so_shop:lib/sell_limit
execute if score @s so_sold < #sell_limit so_shop if score #have so_shop >= #cost so_shop run function so_shop:item/802_ok
execute if score @s so_sold < #sell_limit so_shop if score #have so_shop < #cost so_shop run function so_shop:lib/fail
