execute unless score #mode so_ar matches 0 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Ya hay un desafío en curso en el coliseo.", "color": "red", "bold": false}]
function so_arenas:lib/blocks
execute unless score #blk so_ar matches 3334.. if score @s arena_pr matches 2.. if score @s arena_pr matches 12.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Tier Veterano se desbloquea a los 3.334 bloques.", "color": "red", "bold": false}]
execute unless score #blk so_ar matches 7501.. if score @s arena_pr matches 3..13 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Tier Élite se desbloquea a los 7.501 bloques.", "color": "red", "bold": false}]
execute unless score #blk so_ar matches 15000.. if score @s arena_pr matches 4..14 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Tier Maestro se desbloquea en el After Phase (15.000).", "color": "red", "bold": false}]
# Identifica tier (1-4) y si usa kit prestado (1-4) o equipo propio (11-14).
scoreboard players operation #tier so_ar = @s arena_pr
execute if score @s arena_pr matches 11..14 run scoreboard players remove #tier so_ar 10
execute if score @s arena_pr matches 11..14 run scoreboard players set #loan so_ar 0
execute unless score @s arena_pr matches 11..14 run scoreboard players set #loan so_ar 1
scoreboard players reset @s arena_pr
execute if score #loan so_ar matches 1 run function so_arenas:lib/kit
execute positioned -5000 96 -5000 run function so_arenas:lib/enter
scoreboard players set #mode so_ar 1
scoreboard players set #wave so_ar 0
scoreboard players set #t so_ar 0
bossbar set so_arenas:fight name {"text": "Práctica", "color": "yellow"}
bossbar set so_arenas:fight color yellow
bossbar set so_arenas:fight max 2
bossbar set so_arenas:fight value 0
bossbar set so_arenas:fight players @a[tag=so_ar_in]
bossbar set so_arenas:fight visible true
execute as @a[tag=so_ar_in] run title @s title {"text": "¡Práctica!", "color": "yellow", "bold": true}
tellraw @a [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "La práctica comienza: 2 oleadas. ¡Golpe, esquiva y sobreviví!", "color": "yellow", "bold": false}]
function so_arenas:mode/practice/wave
