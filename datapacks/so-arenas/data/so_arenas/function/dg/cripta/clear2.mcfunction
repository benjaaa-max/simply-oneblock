fill -5005 60 -5041 -5005 63 -5039 minecraft:air replace minecraft:iron_bars
playsound minecraft:block.piston.extend master @a[tag=so_ar_dgp] -5005 61 -5040 2 0.6
particle minecraft:cloud -5005 61.5 -5040 0.3 1 1 0.02 30 force
scoreboard players set #dgs so_ar 4
setblock -5016 60 -5040 minecraft:chest[facing=west]
execute as @a[tag=so_ar_dgp] run loot insert -5016 60 -5040 loot so_arenas:dg_room
particle minecraft:happy_villager -5016.5 61 -5040.5 0.4 0.4 0.4 0 15 force
tellraw @a[tag=so_ar_dgp] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Apareció un cofre en el centro de la sala anterior.", "color": "yellow", "bold": false}]
tellraw @a[tag=so_ar_dgp] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "¡Sala despejada! La reja se abrió: avanzá.", "color": "green", "bold": false}]
