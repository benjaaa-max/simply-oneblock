execute if score @s arena_con matches 20 run return run function so_arenas:npc_menu_con
execute if score @s arena_con matches 9 run return run function so_arenas:lib/join
execute if score @s arena_con matches 30 run return run function so_arenas:lib/bell
execute unless entity @s[tag=so_ar_zone] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Primero entrá al Coliseo con /trigger arena.", "color": "red", "bold": false}]
execute if score #exit so_ar matches 1 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "El foso se está despejando. Esperá unos segundos (o salí por el portón).", "color": "red", "bold": false}]
execute unless score #mode so_ar matches 0 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Ya hay un desafío en curso. Podés unirte con el botón Unirse.", "color": "red", "bold": false}]
function so_arenas:lib/blocks
execute unless score @s arena_con matches 1..7 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Contrato inválido.", "color": "red", "bold": false}]
execute if score @s arena_con matches 1 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 400.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Caza: 15 bajas objetivo se desbloquea a los 400 bloques. Mientras, probá la práctica.", "color": "red", "bold": false}]
execute if score @s arena_con matches 2 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 400.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Oleadas dobles se desbloquea a los 400 bloques. Mientras, probá la práctica.", "color": "red", "bold": false}]
execute if score @s arena_con matches 3 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 2501.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Defensa del Núcleo se desbloquea a los 2.501 bloques. Mientras, probá la práctica.", "color": "red", "bold": false}]
execute if score @s arena_con matches 4 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 400.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Rey de la Colina se desbloquea a los 400 bloques. Mientras, probá la práctica.", "color": "red", "bold": false}]
execute if score @s arena_con matches 5 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 2501.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Asedio Volador se desbloquea a los 2.501 bloques. Mientras, probá la práctica.", "color": "red", "bold": false}]
execute if score @s arena_con matches 6 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 3334.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Duelo de Campeones se desbloquea a los 3.334 bloques. Mientras, probá la práctica.", "color": "red", "bold": false}]
execute if score @s arena_con matches 7 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 6667.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Desafío de Jefes se desbloquea a los 6.667 bloques. Mientras, probá la práctica.", "color": "red", "bold": false}]
scoreboard players operation #con so_ar = @s arena_con
scoreboard players set #ptype so_ar 2
execute if score #con so_ar matches 1 run data modify storage so_arenas:b n set value "Caza: 15 bajas objetivo"
execute if score #con so_ar matches 2 run data modify storage so_arenas:b n set value "Oleadas dobles"
execute if score #con so_ar matches 3 run data modify storage so_arenas:b n set value "Defensa del Núcleo"
execute if score #con so_ar matches 4 run data modify storage so_arenas:b n set value "Rey de la Colina"
execute if score #con so_ar matches 5 run data modify storage so_arenas:b n set value "Asedio Volador"
execute if score #con so_ar matches 6 run data modify storage so_arenas:b n set value "Duelo de Campeones"
execute if score #con so_ar matches 7 run data modify storage so_arenas:b n set value "Desafío de Jefes"
function so_arenas:lib/prepare
