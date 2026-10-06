# v4: touching a return gateway inside a phase dimension sends the player home (done by this datapack).
scoreboard players set @s spf_found 0
execute if score @s spf_found matches 0 if block ~1 ~ ~ minecraft:end_gateway run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~-1 ~ ~ minecraft:end_gateway run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~ ~1 minecraft:end_gateway run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~ ~-1 minecraft:end_gateway run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~1 ~1 ~ minecraft:end_gateway run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~-1 ~1 ~ minecraft:end_gateway run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~1 ~1 minecraft:end_gateway run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~1 ~-1 minecraft:end_gateway run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~-1 ~ minecraft:end_gateway run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~ ~ minecraft:end_gateway run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~1 ~ minecraft:end_gateway run function so_portalfix:do_return
