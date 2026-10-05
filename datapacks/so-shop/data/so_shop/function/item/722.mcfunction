# To the End · llave Simply OneBlock
execute unless score #blocks so_shop matches 7000.. run return run tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Esta llave se desbloquea a los 7000 bloques.","color":"red"}]
scoreboard players set #cost so_shop 28
execute store result score #have so_shop run clear @s minecraft:emerald 0
execute if score #have so_shop >= #cost so_shop run function so_shop:item/722_ok
execute if score #have so_shop < #cost so_shop run function so_shop:lib/fail
