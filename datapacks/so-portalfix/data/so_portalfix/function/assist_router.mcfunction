# v4: choose behaviour by dimension.
execute if dimension minecraft:overworld run function so_portalfix:assist_near
execute if predicate so_portalfix:in_phase run function so_portalfix:return_near
execute if dimension simply_oneblock:phase_20 run function so_portalfix:hub_near
