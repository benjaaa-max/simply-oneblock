execute if score #mode so_ar matches 1..3 if entity @s[tag=so_ar_in] run return run function so_arenas:lib/abandono
tp @s 0 70 2
effect give @s minecraft:slow_falling 5 0 true
effect give @s minecraft:resistance 3 4 true
title @s actionbar {"text": "De vuelta a la isla.", "color": "green"}
