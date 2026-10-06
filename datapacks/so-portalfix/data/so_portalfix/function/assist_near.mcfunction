# Auto-assist: if a gateway touches the player, pull them into its centre so Simply OneBlock detects it.
scoreboard players set @s spf_found 0
execute if score @s spf_found matches 0 if block ~1 ~0 ~0 minecraft:end_gateway positioned ~1 ~0 ~0 align xyz run function so_portalfix:assist_tp
execute if score @s spf_found matches 0 if block ~-1 ~0 ~0 minecraft:end_gateway positioned ~-1 ~0 ~0 align xyz run function so_portalfix:assist_tp
execute if score @s spf_found matches 0 if block ~0 ~0 ~1 minecraft:end_gateway positioned ~0 ~0 ~1 align xyz run function so_portalfix:assist_tp
execute if score @s spf_found matches 0 if block ~0 ~0 ~-1 minecraft:end_gateway positioned ~0 ~0 ~-1 align xyz run function so_portalfix:assist_tp
execute if score @s spf_found matches 0 if block ~1 ~1 ~0 minecraft:end_gateway positioned ~1 ~1 ~0 align xyz run function so_portalfix:assist_tp
execute if score @s spf_found matches 0 if block ~-1 ~1 ~0 minecraft:end_gateway positioned ~-1 ~1 ~0 align xyz run function so_portalfix:assist_tp
execute if score @s spf_found matches 0 if block ~0 ~1 ~1 minecraft:end_gateway positioned ~0 ~1 ~1 align xyz run function so_portalfix:assist_tp
execute if score @s spf_found matches 0 if block ~0 ~1 ~-1 minecraft:end_gateway positioned ~0 ~1 ~-1 align xyz run function so_portalfix:assist_tp
execute if score @s spf_found matches 0 if block ~0 ~-1 ~0 minecraft:end_gateway positioned ~0 ~-1 ~0 align xyz run function so_portalfix:assist_tp
execute if score @s spf_found matches 0 if block ~0 ~0 ~0 minecraft:end_gateway positioned ~0 ~0 ~0 align xyz run function so_portalfix:assist_tp
execute if score @s spf_found matches 0 if block ~0 ~1 ~0 minecraft:end_gateway positioned ~0 ~1 ~0 align xyz run function so_portalfix:assist_tp
