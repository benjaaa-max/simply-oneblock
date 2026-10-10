execute as @a[tag=so_ar_zone] run clear @s *[minecraft:custom_data~{so_arena_loan:1b}]
tag @a remove so_ar_loan
execute as @a[tag=so_ar_zone,x=-5027,y=90,z=-5032,dx=54,dy=50,dz=64] run tp @s -5000 96 -4926 180 0
tag @a remove so_ar_in
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "De vuelta en el lobby. Otro desafío, o /trigger volver para ir a la isla.", "color": "gray", "bold": false}]
