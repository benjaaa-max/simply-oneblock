execute unless entity @s[tag=so_ar_zone] run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Primero entrá al Coliseo con /trigger arena.", "color": "red", "bold": false}]
execute if score #dg so_ar matches 0 run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "No hay ninguna expedición en curso. Elegí una mazmorra.", "color": "gray", "bold": false}]
execute if score #dgs so_ar matches 9 run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "La expedición ya terminó.", "color": "gray", "bold": false}]
execute if entity @s[tag=so_ar_dgp] run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Ya estás en la mazmorra.", "color": "gray", "bold": false}]
execute if entity @s[tag=so_ar_in] run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Estás en un desafío del Coliseo.", "color": "red", "bold": false}]
execute if score #dg so_ar matches 1 if score #dgr so_ar matches 1 run tp @s -5044 60 -5040 -90 0
execute if score #dg so_ar matches 1 if score #dgr so_ar matches 2 run tp @s -5022 60 -5040 -90 0
execute if score #dg so_ar matches 1 if score #dgr so_ar matches 3 run tp @s -5000 60 -5040 -90 0
execute if score #dg so_ar matches 1 if score #dgr so_ar matches 4 run tp @s -4979 60 -5040 -90 0
execute if score #dg so_ar matches 2 if score #dgr so_ar matches 1 run tp @s -5044 60 -5012 -90 0
execute if score #dg so_ar matches 2 if score #dgr so_ar matches 2 run tp @s -5022 60 -5012 -90 0
execute if score #dg so_ar matches 2 if score #dgr so_ar matches 3 run tp @s -5000 60 -5012 -90 0
execute if score #dg so_ar matches 2 if score #dgr so_ar matches 4 run tp @s -4979 60 -5012 -90 0
execute if score #dg so_ar matches 3 if score #dgr so_ar matches 1 run tp @s -5044 60 -4984 -90 0
execute if score #dg so_ar matches 3 if score #dgr so_ar matches 2 run tp @s -5022 60 -4984 -90 0
execute if score #dg so_ar matches 3 if score #dgr so_ar matches 3 run tp @s -5000 60 -4984 -90 0
execute if score #dg so_ar matches 3 if score #dgr so_ar matches 4 run tp @s -4979 60 -4984 -90 0
tag @s add so_ar_dgp
effect give @s minecraft:resistance 3 4 true
tellraw @a[tag=so_ar_dgp] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true},{"selector":"@s","color":"white"},{"text":" se sumó a la expedición.","color":"green","bold":false}]
