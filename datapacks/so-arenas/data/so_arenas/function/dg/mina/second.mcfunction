scoreboard players add #dgt so_ar 1
tag @a remove so_ar_dgp
execute as @a[tag=so_ar_zone,x=-5047,y=50,z=-5024,dx=89,dy=26,dz=24] run tag @s add so_ar_dgp
execute unless entity @a[tag=so_ar_dgp] run return run function so_arenas:dg/empty
bossbar set so_arenas:dg players @a[tag=so_ar_dgp]
# victoria: salida por la placa dorada o a los 90 s
execute if score #dgs so_ar matches 9 run scoreboard players remove #dgx so_ar 1
execute if score #dgs so_ar matches 9 store result bossbar so_arenas:dg value run scoreboard players get #dgx so_ar
execute if score #dgs so_ar matches 9 as @a[tag=so_ar_dgp,x=-4962,y=60,z=-5012,dx=0,dy=0,dz=0] run function so_arenas:dg/exit_one
execute if score #dgs so_ar matches 9 if score #dgx so_ar matches ..0 run return run function so_arenas:dg/exit_all
execute if score #dgs so_ar matches 9 run return 0
execute if score #dgt so_ar matches 1200.. run return run function so_arenas:dg/timeout
execute store result score #alive so_ar if entity @e[tag=so_ar_dgm]
scoreboard players operation #m3 so_ar = #dgt so_ar
scoreboard players operation #m3 so_ar %= #three so_ar
scoreboard players operation #m6 so_ar = #dgt so_ar
scoreboard players operation #m6 so_ar %= #six so_ar
scoreboard players operation #m7 so_ar = #dgt so_ar
scoreboard players operation #m7 so_ar %= #seven so_ar
execute as @e[tag=so_ar_dgboss,type=minecraft:warden] run data modify entity @s Brain.memories."minecraft:dig_cooldown" set value {value:{},ttl:1200000L}
execute if score #dgs so_ar matches 8 as @e[tag=so_ar_dgboss,limit=1] store result bossbar so_arenas:dg value run data get entity @s Health
title @a[tag=so_ar_dgp] actionbar [{"text": "Mina Abandonada · sala ", "color": "dark_purple"}, {"score": {"name": "#dgr", "objective": "so_ar"}, "color": "white"}, {"text": "/4 · enemigos ", "color": "gray"}, {"score": {"name": "#alive", "objective": "so_ar"}, "color": "white"}, {"text": " · ", "color": "gray"}, {"score": {"name": "#dgt", "objective": "so_ar"}, "color": "white"}, {"text": " s", "color": "gray"}]
execute if score #dgs so_ar matches 3 if score #m7 so_ar matches 0 as @a[tag=so_ar_dgp,x=-5023,y=59,z=-5019,dx=14,dy=7,dz=14] at @s run summon minecraft:falling_block ~ 65.8 ~ {BlockState:{Name:"minecraft:gravel"},Time:1,DropItem:0b,HurtEntities:1b,FallHurtAmount:1.0f,FallHurtMax:4}
execute if score #dgs so_ar matches 3 if score #m7 so_ar matches 0 as @a[tag=so_ar_dgp,x=-5023,y=59,z=-5019,dx=14,dy=7,dz=14] at @s run particle minecraft:large_smoke ~ 65.5 ~ 0.6 0.1 0.6 0.01 15
execute if score #dgs so_ar matches 3 if score #m7 so_ar matches 0 as @a[tag=so_ar_dgp,x=-5023,y=59,z=-5019,dx=14,dy=7,dz=14] at @s run playsound minecraft:block.gravel.break master @s ~ ~ ~ 1 0.6
execute if score #dgs so_ar matches 3 if score #m7 so_ar matches 0 run title @a[tag=so_ar_dgp,x=-5023,y=59,z=-5019,dx=14,dy=7,dz=14] actionbar {"text": "¡Derrumbe!", "color": "red", "bold": true}
execute if score #dgs so_ar matches 5 if score #m7 so_ar matches 0 as @a[tag=so_ar_dgp,x=-5001,y=59,z=-5019,dx=14,dy=7,dz=14] at @s run summon minecraft:falling_block ~ 65.8 ~ {BlockState:{Name:"minecraft:gravel"},Time:1,DropItem:0b,HurtEntities:1b,FallHurtAmount:1.0f,FallHurtMax:4}
execute if score #dgs so_ar matches 5 if score #m7 so_ar matches 0 as @a[tag=so_ar_dgp,x=-5001,y=59,z=-5019,dx=14,dy=7,dz=14] at @s run particle minecraft:large_smoke ~ 65.5 ~ 0.6 0.1 0.6 0.01 15
execute if score #dgs so_ar matches 5 if score #m7 so_ar matches 0 as @a[tag=so_ar_dgp,x=-5001,y=59,z=-5019,dx=14,dy=7,dz=14] at @s run playsound minecraft:block.gravel.break master @s ~ ~ ~ 1 0.6
execute if score #dgs so_ar matches 5 if score #m7 so_ar matches 0 run title @a[tag=so_ar_dgp,x=-5001,y=59,z=-5019,dx=14,dy=7,dz=14] actionbar {"text": "¡Derrumbe!", "color": "red", "bold": true}
execute if score #dgs so_ar matches 1 if score #dgt so_ar matches 3.. if score #alive so_ar matches 0 run return run function so_arenas:dg/mina/clear1
execute if score #dgs so_ar matches 2 if entity @a[tag=so_ar_dgp,x=-5023,y=59,z=-5019,dx=14,dy=7,dz=14] run return run function so_arenas:dg/mina/enter2
execute if score #dgs so_ar matches 3 if score #alive so_ar matches 0 run return run function so_arenas:dg/mina/clear2
execute if score #dgs so_ar matches 4 if entity @a[tag=so_ar_dgp,x=-5001,y=59,z=-5019,dx=14,dy=7,dz=14] run return run function so_arenas:dg/mina/enter3
execute if score #dgs so_ar matches 5 if score #alive so_ar matches 0 run return run function so_arenas:dg/mina/clear3
execute if score #dgs so_ar matches 6 as @a[tag=so_ar_dgp,x=-4989,y=60,z=-5014,dx=4,dy=3,dz=4] if items entity @s container.* *[minecraft:custom_data~{so_ar_dgkey:1b}] run return run function so_arenas:dg/mina/unlock
execute if score #dgs so_ar matches 6 as @a[tag=so_ar_dgp,x=-4989,y=60,z=-5014,dx=4,dy=3,dz=4] unless items entity @s container.* *[minecraft:custom_data~{so_ar_dgkey:1b}] run title @s actionbar {"text": "Esta reja necesita la Llave de Sala.", "color": "gold"}
execute if score #dgs so_ar matches 7 if entity @a[tag=so_ar_dgp,x=-4980,y=59,z=-5022,dx=20,dy=11,dz=20] run return run function so_arenas:dg/mina/enter4
execute if score #dgs so_ar matches 8 unless entity @e[tag=so_ar_dgboss] run return run function so_arenas:dg/mina/win
