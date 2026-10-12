execute unless entity @s[tag=so_ar_dgp] run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "No estás en ninguna mazmorra.", "color": "gray", "bold": false}]
clear @s *[minecraft:custom_data~{so_ar_dgkey:1b}]
tag @s remove so_ar_dgp
tp @s -5000 96 -4918 180 0
tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Saliste de Las Catacumbas.", "color": "gray", "bold": false}]
