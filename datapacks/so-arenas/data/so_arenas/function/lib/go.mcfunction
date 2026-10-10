execute if score #enabled so_ar matches 0 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "La arena está desactivada por un administrador.", "color": "red", "bold": false}]
execute if entity @s[tag=so_ar_in] run return run dialog show @s so_arenas:main
tp @s -5000 98 -4938
effect give @s minecraft:resistance 3 4 true
title @s title {"text": "Coliseo VorNeX", "color": "gold", "bold": true}
subtitle @s subtitle {"text": "Habla con los aldeanos o abre el menú.", "color": "gray"}
playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1
dialog show @s so_arenas:main
