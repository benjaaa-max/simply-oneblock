execute if score #enabled so_cfg matches 1 run function so_status:assign_default_rank
execute if score #enabled so_cfg matches 1 if score #bar_on so_cfg matches 1 run function so_status:progress
execute if score #enabled so_cfg matches 1 if score #bar_on so_cfg matches 1 run function so_status:bossbar_update

# El HUD (sidebar, por jugador) se refresca 1 vez por segundo: no necesita tick exacto.
scoreboard players add #beat so_sys 1
execute if score #enabled so_cfg matches 1 if score #hud_on so_cfg matches 1 if score #beat so_sys matches 20.. as @a run function so_status:hud_update
execute if score #beat so_sys matches 20.. run scoreboard players set #beat so_sys 0
