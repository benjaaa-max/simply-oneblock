execute if score @s arena_pr matches 20 run return run function so_arenas:npc_menu_pr
execute unless entity @s[tag=so_ar_zone] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Primero entrá al Coliseo con /trigger arena.", "color": "red", "bold": false}]
execute unless score #mode so_ar matches 0 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Ya hay un desafío en curso. Podés unirte con el botón Unirse.", "color": "red", "bold": false}]
function so_arenas:lib/blocks
scoreboard players operation #tier so_ar = @s arena_pr
execute if score #tier so_ar matches 11..14 run scoreboard players remove #tier so_ar 10
scoreboard players set #loan so_ar 1
execute if score @s arena_pr matches 11..14 run scoreboard players set #loan so_ar 0
execute unless score #tier so_ar matches 1..4 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Opción de práctica inválida.", "color": "red", "bold": false}]
execute if score #tier so_ar matches 2 unless score #blk so_ar matches 3334.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "El Tier Veterano se desbloquea a los 3.334 bloques.", "color": "red", "bold": false}]
execute if score #tier so_ar matches 3 unless score #blk so_ar matches 7501.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "El Tier Élite se desbloquea a los 7.501 bloques.", "color": "red", "bold": false}]
execute if score #tier so_ar matches 4 unless score #blk so_ar matches 15000.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "El Tier Maestro se desbloquea a los 15.000 bloques.", "color": "red", "bold": false}]
execute if score #loan so_ar matches 1 run function so_arenas:lib/kit
execute if score #loan so_ar matches 0 run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Entrás con tu propio equipo: si morís, tus cosas quedan en el foso.", "color": "yellow", "bold": false}]
function so_arenas:lib/enter_pit
scoreboard players set #mode so_ar 1
scoreboard players set #wave so_ar 0
scoreboard players set #t so_ar 0
scoreboard players set #anticamp so_ar 1
bossbar set so_arenas:fight name {"text": "Práctica", "color": "yellow"}
bossbar set so_arenas:fight color yellow
bossbar set so_arenas:fight max 2
bossbar set so_arenas:fight value 0
bossbar set so_arenas:fight players @a[tag=so_ar_in]
bossbar set so_arenas:fight visible true
title @s title {"text": "¡Práctica!", "color": "yellow", "bold": true}
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "La práctica comienza: 2 oleadas. ¡Golpeá, esquivá y sobreviví!", "color": "yellow", "bold": false}]
function so_arenas:mode/practice/wave
