fill -5005 60 -5013 -5005 63 -5011 minecraft:air replace minecraft:iron_bars
playsound minecraft:block.piston.extend master @a[tag=so_ar_dgp] -5005 61 -5012 2 0.6
particle minecraft:cloud -5005 61.5 -5012 0.3 1 1 0.02 30 force
scoreboard players set #dgs so_ar 4
setblock -5016 60 -5012 minecraft:chest[facing=west]
execute as @a[tag=so_ar_dgp] run loot insert -5016 60 -5012 loot so_arenas:dg_room_hi
particle minecraft:happy_villager -5016.5 61 -5012.5 0.4 0.4 0.4 0 15 force
tellraw @a[tag=so_ar_dgp] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Apareció un cofre en el centro de la sala anterior.", "color": "yellow", "bold": false}]
tellraw @a[tag=so_ar_dgp] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "¡Sala despejada! La reja se abrió: avanzá.", "color": "green", "bold": false}]
