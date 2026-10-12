# Cierre: todos al lobby, kits fuera, foso limpio, portones cerrados.
execute as @a[tag=so_ar_zone,x=-5027,y=90,z=-5032,dx=54,dy=50,dz=64] run tp @s -5000 96 -4926 180 0
execute as @a[tag=so_ar_zone,x=-5003,y=95,z=-4968,dx=6,dy=6,dz=28] run tp @s -5000 96 -4926 180 0
execute as @a[tag=so_ar_zone] run clear @s *[minecraft:custom_data~{so_arena_loan:1b}]
tag @a remove so_ar_loan
tag @a remove so_ar_in
tag @a remove so_ar_win
tag @a remove so_ar_ready
function so_arenas:lib/reset_pit
function so_arenas:lib/gates_close
function so_arenas:lib/board_idle
bossbar set so_arenas:fight visible false
scoreboard players set #exit so_ar 0
scoreboard players set #mut_n so_ar 0
scoreboard players set #mut_f so_ar 0
scoreboard players set #mut_v so_ar 0
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Foso limpio y portones cerrados. Otro desafío, o /trigger volver para ir a la isla.", "color": "gray", "bold": false}]
