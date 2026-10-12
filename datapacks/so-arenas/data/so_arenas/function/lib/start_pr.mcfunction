execute if score @s arena_pr matches 20 run return run function so_arenas:npc_menu_pr
execute unless entity @s[tag=so_ar_zone] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Primero entrá al Coliseo con /trigger arena.", "color": "red", "bold": false}]
execute if score #exit so_ar matches 1 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "El foso se está despejando. Esperá unos segundos (o salí por el portón).", "color": "red", "bold": false}]
execute unless score #mode so_ar matches 0 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Ya hay un desafío en curso. Podés unirte con el botón Unirse.", "color": "red", "bold": false}]
function so_arenas:lib/blocks
scoreboard players operation #tier so_ar = @s arena_pr
execute if score #tier so_ar matches 11..14 run scoreboard players remove #tier so_ar 10
scoreboard players set #loan so_ar 1
execute if score @s arena_pr matches 11..14 run scoreboard players set #loan so_ar 0
execute unless score #tier so_ar matches 1..4 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Opción de práctica inválida.", "color": "red", "bold": false}]
execute if score #tier so_ar matches 2 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 3334.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "El Tier Veterano se desbloquea a los 3.334 bloques.", "color": "red", "bold": false}]
execute if score #tier so_ar matches 3 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 7501.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "El Tier Élite se desbloquea a los 7.501 bloques.", "color": "red", "bold": false}]
execute if score #tier so_ar matches 4 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 15000.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "El Tier Maestro se desbloquea a los 15.000 bloques.", "color": "red", "bold": false}]
execute if score #loan so_ar matches 1 run function so_arenas:lib/kit
execute if score #loan so_ar matches 0 run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Entrás con tu propio equipo: si morís, tus cosas quedan en el foso.", "color": "yellow", "bold": false}]
scoreboard players set #ptype so_ar 1
execute if score #tier so_ar matches 1 run data modify storage so_arenas:b n set value "Práctica · Tier 1 Novato"
execute if score #tier so_ar matches 2 run data modify storage so_arenas:b n set value "Práctica · Tier 2 Veterano"
execute if score #tier so_ar matches 3 run data modify storage so_arenas:b n set value "Práctica · Tier 3 Élite"
execute if score #tier so_ar matches 4 run data modify storage so_arenas:b n set value "Práctica · Tier 4 Maestro"
function so_arenas:lib/prepare
