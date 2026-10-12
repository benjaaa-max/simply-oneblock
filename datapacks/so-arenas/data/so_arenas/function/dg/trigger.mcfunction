execute if score @s arena_dg matches 20 run return run function so_arenas:dg/menu
execute if score @s arena_dg matches 9 run return run function so_arenas:dg/join
execute if score @s arena_dg matches 8 run return run function so_arenas:dg/abandon
execute unless entity @s[tag=so_ar_zone] run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Primero entrá al Coliseo con /trigger arena.", "color": "red", "bold": false}]
execute if score #enabled so_ar matches 0 run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "La arena está desactivada por un administrador.", "color": "red", "bold": false}]
execute unless score @s arena_dg matches 1..3 run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Opción inválida.", "color": "red", "bold": false}]
execute if score #dg so_ar matches 1.. run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Ya hay una expedición en curso. Podés sumarte con Unirse.", "color": "red", "bold": false}]
execute if entity @s[tag=so_ar_in] run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Estás en un desafío del Coliseo.", "color": "red", "bold": false}]
execute if entity @s[tag=so_ar_ready] run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Estás en el túnel de preparación del Coliseo.", "color": "red", "bold": false}]
function so_arenas:lib/blocks
execute if score @s arena_dg matches 2 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 3000.. run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Mina Abandonada se desbloquea a los 3.000 bloques.", "color": "red", "bold": false}]
execute if score @s arena_dg matches 3 unless entity @s[tag=oneblock_admin] unless score #blk so_ar matches 6000.. run return run tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Templo Sumergido se desbloquea a los 6.000 bloques.", "color": "red", "bold": false}]
execute if score @s arena_dg matches 1 run function so_arenas:dg/cripta/begin
execute if score @s arena_dg matches 2 run function so_arenas:dg/mina/begin
execute if score @s arena_dg matches 3 run function so_arenas:dg/templo/begin
