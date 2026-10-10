execute if score @s arena matches 2 run return run function so_arenas:lib/volver
execute if score #enabled so_ar matches 0 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "La arena está desactivada por un administrador.", "color": "red", "bold": false}]
execute if entity @s[tag=so_ar_zone] run return run function so_arenas:lib/menu
execute unless dimension minecraft:overworld run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Solo podés viajar desde el mundo normal (no desde el Nether, el End ni las fases).", "color": "red", "bold": false}]
execute store result score @s so_ar_x run data get entity @s Pos[0]
execute store result score @s so_ar_y run data get entity @s Pos[1]
execute store result score @s so_ar_z run data get entity @s Pos[2]
scoreboard players set @s so_ar_saved 1
tp @s -5000 96 -4926 180 0
function so_arenas:lib/enter_zone
effect give @s minecraft:resistance 3 4 true
title @s title {"text": "Coliseo VorNeX", "color": "gold", "bold": true}
title @s subtitle {"text": "Aldeanos, carteles o placas del piso", "color": "gray"}
playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1
function so_arenas:lib/menu
