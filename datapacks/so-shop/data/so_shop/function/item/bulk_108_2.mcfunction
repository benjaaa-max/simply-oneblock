# 108 x2: 16 objetos, 10 esmeraldas (0 de ahorro)
# Desbloqueo de categoría comprobado en lib/dispatch
scoreboard players set #cost so_shop 10
execute store result score #have so_shop run clear @s minecraft:emerald 0
execute if score #have so_shop < #cost so_shop run return run function so_shop:lib/fail
scoreboard players set #slots so_shop 0
execute unless items entity @s container.0 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.1 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.2 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.3 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.4 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.5 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.6 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.7 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.8 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.9 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.10 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.11 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.12 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.13 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.14 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.15 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.16 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.17 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.18 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.19 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.20 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.21 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.22 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.23 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.24 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.25 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.26 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.27 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.28 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.29 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.30 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.31 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.32 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.33 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.34 * run scoreboard players add #slots so_shop 1
execute unless items entity @s container.35 * run scoreboard players add #slots so_shop 1
execute unless score #slots so_shop matches 1.. run return run function so_shop:lib/no_space
function so_shop:item/bulk_108_2_ok
