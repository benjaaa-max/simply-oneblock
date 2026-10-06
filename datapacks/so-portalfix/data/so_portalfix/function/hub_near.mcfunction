# v4: phase 20 hub. Only the home gateway (standing on bedrock) returns via the datapack; other gateways keep v3 assist.
scoreboard players set @s spf_found 0
execute if score @s spf_found matches 0 if block ~1 ~ ~ minecraft:end_gateway if block ~1 ~-1 ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~1 ~ ~ minecraft:end_gateway if block ~1 ~-1 ~ minecraft:end_gateway if block ~1 ~-2 ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~-1 ~ ~ minecraft:end_gateway if block ~-1 ~-1 ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~-1 ~ ~ minecraft:end_gateway if block ~-1 ~-1 ~ minecraft:end_gateway if block ~-1 ~-2 ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~ ~1 minecraft:end_gateway if block ~ ~-1 ~1 minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~ ~1 minecraft:end_gateway if block ~ ~-1 ~1 minecraft:end_gateway if block ~ ~-2 ~1 minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~ ~-1 minecraft:end_gateway if block ~ ~-1 ~-1 minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~ ~-1 minecraft:end_gateway if block ~ ~-1 ~-1 minecraft:end_gateway if block ~ ~-2 ~-1 minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~1 ~1 ~ minecraft:end_gateway if block ~1 ~ ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~1 ~1 ~ minecraft:end_gateway if block ~1 ~ ~ minecraft:end_gateway if block ~1 ~-1 ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~-1 ~1 ~ minecraft:end_gateway if block ~-1 ~ ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~-1 ~1 ~ minecraft:end_gateway if block ~-1 ~ ~ minecraft:end_gateway if block ~-1 ~-1 ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~1 ~1 minecraft:end_gateway if block ~ ~ ~1 minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~1 ~1 minecraft:end_gateway if block ~ ~ ~1 minecraft:end_gateway if block ~ ~-1 ~1 minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~1 ~-1 minecraft:end_gateway if block ~ ~ ~-1 minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~1 ~-1 minecraft:end_gateway if block ~ ~ ~-1 minecraft:end_gateway if block ~ ~-1 ~-1 minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~-1 ~ minecraft:end_gateway if block ~ ~-2 ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~-1 ~ minecraft:end_gateway if block ~ ~-2 ~ minecraft:end_gateway if block ~ ~-3 ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~ ~ minecraft:end_gateway if block ~ ~-1 ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~ ~ minecraft:end_gateway if block ~ ~-1 ~ minecraft:end_gateway if block ~ ~-2 ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~1 ~ minecraft:end_gateway if block ~ ~ ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 if block ~ ~1 ~ minecraft:end_gateway if block ~ ~ ~ minecraft:end_gateway if block ~ ~-1 ~ minecraft:bedrock run function so_portalfix:do_return
execute if score @s spf_found matches 0 run function so_portalfix:assist_near
