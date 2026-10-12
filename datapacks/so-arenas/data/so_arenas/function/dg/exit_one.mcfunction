tag @s remove so_ar_dgp
clear @s *[minecraft:custom_data~{so_ar_dgkey:1b}]
tp @s -5000 96 -4918 180 0
playsound minecraft:block.iron_door.open master @s ~ ~ ~ 1 1
tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "De vuelta en la plaza del Coliseo.", "color": "green", "bold": false}]
