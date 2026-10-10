execute if score @s arena_con matches 20 run return run function so_arenas:npc_menu_con
execute if score @s arena_con matches 9 run return run function so_arenas:lib/join
execute unless entity @s[tag=so_ar_zone] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Primero entrá al Coliseo con /trigger arena.", "color": "red", "bold": false}]
execute unless score #mode so_ar matches 0 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Ya hay un desafío en curso. Podés unirte con el botón Unirse.", "color": "red", "bold": false}]
function so_arenas:lib/blocks
execute unless score #blk so_ar matches 400.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Los contratos se abren a los 400 bloques. Mientras, probá la práctica.", "color": "red", "bold": false}]
execute if score @s arena_con matches 3 unless score #blk so_ar matches 2501.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "La Defensa del Núcleo se desbloquea a los 2.501 bloques.", "color": "red", "bold": false}]
scoreboard players operation #con so_ar = @s arena_con
execute unless score #con so_ar matches 1..3 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Contrato inválido.", "color": "red", "bold": false}]
function so_arenas:lib/enter_pit
scoreboard players set #t so_ar 0
scoreboard players set #wave so_ar 0
scoreboard players set #spawned so_ar 0
scoreboard players set #anticamp so_ar 1
bossbar set so_arenas:fight players @a[tag=so_ar_in]
bossbar set so_arenas:fight visible true
execute if score #con so_ar matches 1 run function so_arenas:mode/caza/start
execute if score #con so_ar matches 2 run function so_arenas:mode/caza2/start
execute if score #con so_ar matches 3 run function so_arenas:mode/defensa/start
