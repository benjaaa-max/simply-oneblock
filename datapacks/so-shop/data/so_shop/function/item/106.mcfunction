# Campana
scoreboard players set #cost so_shop 12
execute store result score #have so_shop run clear @s minecraft:emerald 0
execute if score #have so_shop >= #cost so_shop run function so_shop:item/106_ok
execute if score #have so_shop < #cost so_shop run function so_shop:lib/fail
