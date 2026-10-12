execute unless score #mode so_ar matches 10 run return 0
tag @s remove so_ar_pvp
effect give @s minecraft:instant_health 1 10 true
effect clear @s minecraft:resistance
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true},{"selector":"@a[tag=so_ar_pvp]","color":"gold","bold":true},{"text":" gana el duelo contra ","color":"yellow","bold":false},{"selector":"@s","color":"white"}]
title @a[tag=so_ar_pvp] title {"text": "¡Ganaste el duelo!", "color": "gold", "bold": true}
function so_arenas:lib/celebrar
function so_arenas:mode/pvp/end
