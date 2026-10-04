execute unless entity @s[tag=so_cr_in] run return run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Este comando solo funciona dentro de la zona de Crates.","color":"red"}]
execute store result storage so_crates:tmp x int 1 run scoreboard players get @s so_cr_x
execute store result storage so_crates:tmp y int 1 run scoreboard players get @s so_cr_y
execute store result storage so_crates:tmp z int 1 run scoreboard players get @s so_cr_z
execute if score @s so_cr_saved matches 1 run function so_crates:lib/back_tp with storage so_crates:tmp
execute unless score @s so_cr_saved matches 1 in minecraft:overworld run tp @s 0 65 0
scoreboard players reset @s so_cr_saved
function so_crates:lib/leave
execute at @s run playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1
