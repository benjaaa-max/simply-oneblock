execute if score #enabled so_cfg matches 1 run function so_status:assign_default_rank
execute if score #enabled so_cfg matches 1 run function so_status:commands
execute if score #enabled so_cfg matches 1 run function so_status:temp/tick
execute if score #enabled so_cfg matches 1 if score #bar_on so_cfg matches 1 run function so_status:progress
execute if score #enabled so_cfg matches 1 if score #bar_on so_cfg matches 1 run function so_status:bossbar_update
execute unless score #enabled so_cfg matches 1 run bossbar set so_status:progress visible false
execute if score #enabled so_cfg matches 1 unless score #bar_on so_cfg matches 1 run bossbar set so_status:progress visible false
scoreboard players add #beat so_sys 1
execute if score #enabled so_cfg matches 1 if score #hud_on so_cfg matches 1 if score #beat so_sys matches 20.. run function so_status:hud_update
execute unless score #enabled so_cfg matches 1 run scoreboard objectives setdisplay sidebar
execute if score #enabled so_cfg matches 1 unless score #hud_on so_cfg matches 1 run scoreboard objectives setdisplay sidebar
execute if score #beat so_sys matches 20.. run scoreboard players set #beat so_sys 0
