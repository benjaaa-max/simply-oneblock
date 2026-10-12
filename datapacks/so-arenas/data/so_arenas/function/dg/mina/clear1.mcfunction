fill -5027 60 -5013 -5027 63 -5011 minecraft:air replace minecraft:iron_bars
playsound minecraft:block.piston.extend master @a[tag=so_ar_dgp] -5027 61 -5012 2 0.6
particle minecraft:cloud -5027 61.5 -5012 0.3 1 1 0.02 30 force
scoreboard players set #dgs so_ar 2
tellraw @a[tag=so_ar_dgp] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "¡Sala despejada! La reja se abrió: avanzá.", "color": "green", "bold": false}]
