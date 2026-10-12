execute unless score #mode so_ar matches 9 run return 0
scoreboard players set #mode so_ar 0
# mutadores activos
scoreboard players operation #mutc so_ar = #mut_n so_ar
scoreboard players operation #mutc so_ar += #mut_f so_ar
scoreboard players operation #mutc so_ar += #mut_v so_ar
function so_arenas:lib/music_pick
function so_arenas:lib/gate_pit_open
function so_arenas:lib/judges_salute
title @a[tag=so_ar_zone] times 5 50 15
title @a[tag=so_ar_zone] title {"text": "¡Que empiece la batalla!", "color": "gold", "bold": true}
execute if score #mutc so_ar matches 1.. run title @a[tag=so_ar_zone] subtitle {"text": "Mutadores activos: botín doble", "color": "red"}
execute as @a[tag=so_ar_zone] at @s run playsound minecraft:block.bell.resonate master @s ~ ~ ~ 1 0.8
execute as @a[tag=so_ar_ready] run function so_arenas:lib/enter_pit
tag @a remove so_ar_ready
function so_arenas:lib/refill
execute if score #ptype so_ar matches 1 run function so_arenas:mode/practice/start
execute if score #ptype so_ar matches 2 run function so_arenas:lib/con_begin
function so_arenas:lib/music_play
schedule function so_arenas:lib/gate_pit_close 60t
