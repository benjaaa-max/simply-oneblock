# Huevo: Allay
scoreboard players set #cost so_shop 40
execute store result score #have so_shop run clear @s minecraft:emerald 0
execute if score #have so_shop >= #cost so_shop run function so_shop:item/606_ok
execute if score #have so_shop < #cost so_shop run function so_shop:lib/fail
