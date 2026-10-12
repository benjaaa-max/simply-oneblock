execute as @e[tag=so_ar_dgm] run tp @s -5000 -300 -5000
kill @e[tag=so_ar_dgm]
scoreboard players set #dgs so_ar 9
scoreboard players set #dgx so_ar 90
execute store result score #r so_ar run random value 0..6
execute if score #r so_ar matches 0 run setblock -4970 60 -4984 minecraft:chest[facing=north]
execute if score #r so_ar matches 1 run setblock -4970 60 -4984 minecraft:trapped_chest[facing=north]
execute if score #r so_ar matches 2 run setblock -4970 60 -4984 minecraft:barrel[facing=up]
execute if score #r so_ar matches 3 run setblock -4970 60 -4984 minecraft:copper_chest[facing=north]
execute if score #r so_ar matches 4 run setblock -4970 60 -4984 minecraft:exposed_copper_chest[facing=north]
execute if score #r so_ar matches 5 run setblock -4970 60 -4984 minecraft:weathered_copper_chest[facing=north]
execute if score #r so_ar matches 6 run setblock -4970 60 -4984 minecraft:oxidized_copper_chest[facing=north]
execute as @a[tag=so_ar_dgp] run loot insert -4970 60 -4984 loot so_arenas:dg_boss3
setblock -4962 59 -4984 minecraft:gold_block
setblock -4962 60 -4984 minecraft:light_weighted_pressure_plate
scoreboard players add @a[tag=so_ar_dgp] so_ar_rank 1
summon minecraft:firework_rocket -4975 61 -4989 {LifeTime:15,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1b,explosions:[{shape:"large_ball",colors:[I;16750848,16711680,16776960],has_trail:1b,has_twinkle:1b}]}}}}
summon minecraft:firework_rocket -4965 61 -4979 {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1b,explosions:[{shape:"large_ball",colors:[I;16750848,16711680,16776960],has_trail:1b,has_twinkle:1b}]}}}}
summon minecraft:firework_rocket -4975 61 -4979 {LifeTime:25,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1b,explosions:[{shape:"large_ball",colors:[I;16750848,16711680,16776960],has_trail:1b,has_twinkle:1b}]}}}}
summon minecraft:firework_rocket -4965 61 -4989 {LifeTime:30,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1b,explosions:[{shape:"large_ball",colors:[I;16750848,16711680,16776960],has_trail:1b,has_twinkle:1b}]}}}}
execute as @a[tag=so_ar_dgp] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
title @a[tag=so_ar_dgp] times 5 60 15
title @a[tag=so_ar_dgp] title {"text": "¡Mazmorra completada!", "color": "green", "bold": true}
title @a[tag=so_ar_dgp] subtitle {"text": "Cofre en el centro · salida: placa dorada", "color": "yellow"}
execute unless score #rec3 so_ar matches 1.. run scoreboard players set #rec3 so_ar 999999
execute store success score #nr so_ar if score #dgt so_ar < #rec3 so_ar
execute if score #nr so_ar matches 1 run scoreboard players operation #rec3 so_ar = #dgt so_ar
execute if score #nr so_ar matches 1 run tellraw @a[tag=so_ar_zone] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true},{"selector":"@a[tag=so_ar_dgp]","color":"white"},{"text":" ¡nuevo récord en Templo Sumergido: ","color":"gold","bold":false},{"score":{"name":"#dgt","objective":"so_ar"},"color":"white","bold":true},{"text":" s!","color":"gold","bold":false}]
execute if score #nr so_ar matches 0 run tellraw @a[tag=so_ar_dgp] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true},{"text":"Tiempo: ","color":"gray","bold":false},{"score":{"name":"#dgt","objective":"so_ar"},"color":"white"},{"text":" s · récord: ","color":"gray"},{"score":{"name":"#rec3","objective":"so_ar"},"color":"gold"},{"text":" s","color":"gray"}]
function so_arenas:dg/board
bossbar set so_arenas:dg name {"text": "Salida: placa dorada (o esperá)", "color": "green"}
bossbar set so_arenas:dg color green
bossbar set so_arenas:dg max 90
bossbar set so_arenas:dg value 90
