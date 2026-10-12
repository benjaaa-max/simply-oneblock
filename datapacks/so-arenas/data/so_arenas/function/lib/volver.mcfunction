execute unless entity @s[tag=so_ar_zone] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Este comando solo funciona dentro del Coliseo. Para ir: /trigger arena", "color": "red", "bold": false}]
execute if score #mode so_ar matches 1..8 if entity @s[tag=so_ar_in] run function so_arenas:lib/abandono
execute if score #mode so_ar matches 10 if entity @s[tag=so_ar_pvp] run function so_arenas:mode/pvp/lose
function so_arenas:lib/leave
execute store result storage so_arenas:tmp x int 1 run scoreboard players get @s so_ar_x
execute store result storage so_arenas:tmp y int 1 run scoreboard players get @s so_ar_y
execute store result storage so_arenas:tmp z int 1 run scoreboard players get @s so_ar_z
execute if score @s so_ar_saved matches 1 run function so_arenas:lib/back_tp with storage so_arenas:tmp
execute unless score @s so_ar_saved matches 1 in minecraft:overworld run tp @s 0 65 0
scoreboard players reset @s so_ar_saved
effect give @s minecraft:slow_falling 5 0 true
execute at @s run playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1
title @s actionbar {"text": "De vuelta a la isla.", "color": "green"}
