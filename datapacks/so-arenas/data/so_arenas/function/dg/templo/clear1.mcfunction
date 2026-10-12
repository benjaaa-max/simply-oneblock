fill -5027 60 -4985 -5027 63 -4983 minecraft:air replace minecraft:iron_bars
playsound minecraft:block.piston.extend master @a[tag=so_ar_dgp] -5027 61 -4984 2 0.6
particle minecraft:cloud -5027 61.5 -4984 0.3 1 1 0.02 30 force
scoreboard players set #dgs so_ar 2
tellraw @a[tag=so_ar_dgp] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "¡Sala despejada! La reja se abrió: avanzá.", "color": "green", "bold": false}]
