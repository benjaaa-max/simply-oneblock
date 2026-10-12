tag @a[tag=so_ar_pvpw,limit=1] add so_ar_pvp
tag @s add so_ar_pvp
tag @a remove so_ar_pvpw
scoreboard players set #mode so_ar 10
scoreboard players set #t so_ar 0
scoreboard players set #anticamp so_ar 1
tp @a[tag=so_ar_pvp,tag=!so_ar_me,limit=1] -5000 96 -5014 0 0
execute as @a[tag=so_ar_pvp] unless entity @s[x=-5027,y=90,z=-5032,dx=54,dy=50,dz=64] run tp @s -5000 96 -4986 180 0
tag @a[tag=so_ar_pvp] add so_ar_in
effect give @a[tag=so_ar_pvp] minecraft:instant_health 1 5 true
effect give @a[tag=so_ar_pvp] minecraft:resistance infinite 0 true
title @a[tag=so_ar_zone] times 5 40 10
title @a[tag=so_ar_zone] title {"text": "¡Duelo!", "color": "red", "bold": true}
title @a[tag=so_ar_zone] subtitle {"text": "Pierde quien baje a 3 corazones", "color": "gray"}
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true},{"text":"Duelo amistoso: ","color":"red","bold":false},{"selector":"@a[tag=so_ar_pvp]","color":"white"}]
execute store result score #song so_ar run random value 1..16
function so_arenas:lib/music_play
function so_arenas:lib/judges_salute
