# Vender 64 kelp seco
scoreboard players add @s so_sold 0
scoreboard players set #cost so_shop 64
execute store result score #have so_shop run clear @s minecraft:dried_kelp 0
execute if score @s so_sold >= #sell_limit so_shop run function so_shop:lib/sell_limit
execute if score @s so_sold < #sell_limit so_shop if score #have so_shop >= #cost so_shop run function so_shop:item/804_ok
execute if score @s so_sold < #sell_limit so_shop if score #have so_shop < #cost so_shop run function so_shop:lib/fail
