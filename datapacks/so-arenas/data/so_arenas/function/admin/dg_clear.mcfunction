execute as @e[tag=so_ar_dgm] run tp @s -5000 -300 -5000
kill @e[tag=so_ar_dgm]
tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Enemigos de la mazmorra eliminados.", "color": "green", "bold": false}]
