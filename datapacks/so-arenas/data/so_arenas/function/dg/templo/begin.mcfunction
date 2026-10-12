forceload add -5048 -5054 -4958 -4970
scoreboard players set #dg so_ar 3
scoreboard players set #dgs so_ar 0
scoreboard players set #dgt so_ar 0
scoreboard players set #dgr so_ar 1
tp @s -5044 60 -4984 -90 0
tag @s add so_ar_dgp
effect give @s minecraft:resistance 3 4 true
title @s times 5 50 15
title @s title {"text": "Templo Sumergido", "color": "dark_aqua", "bold": true}
title @s subtitle {"text": "Sala 1/4 · limpiá la sala para abrir la reja", "color": "gray"}
playsound minecraft:block.iron_door.close master @s ~ ~ ~ 1 0.6
bossbar set so_arenas:dg name {"text": "Templo Sumergido · Sala 1/4", "color": "dark_purple"}
bossbar set so_arenas:dg color purple
bossbar set so_arenas:dg max 4
bossbar set so_arenas:dg value 1
bossbar set so_arenas:dg players @a[tag=so_ar_dgp]
bossbar set so_arenas:dg visible true
tellraw @a[tag=so_ar_zone] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true},{"selector":"@s","color":"white"},{"text":" bajó a Templo Sumergido. Sumate con Unirse (menú de Catacumbas).","color":"light_purple","bold":false}]
schedule function so_arenas:dg/templo/go 30t
