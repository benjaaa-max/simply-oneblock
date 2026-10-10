execute unless score #mode so_ar matches 0 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Ya hay un desafío en curso en el coliseo.", "color": "red", "bold": false}]
function so_arenas:lib/blocks
execute unless score #blk so_ar matches 400.. run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Los contratos se abren a los 400 bloques: preparate en la isla o entrá a la práctica.", "color": "red", "bold": false}]
execute unless score #blk so_ar matches 2501.. if score @s arena_con matches 3 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "El contrato de defensa se desbloquea a los 2.501 bloques.", "color": "red", "bold": false}]
scoreboard players operation #con so_ar = @s arena_con
scoreboard players reset @s arena_con
execute if score #con so_ar matches 1 run function so_arenas:mode/caza/start
execute if score #con so_ar matches 2 run function so_arenas:mode/caza2/start
execute if score #con so_ar matches 3 run function so_arenas:mode/defensa/start
