execute unless entity @s[tag=so_ar_zone] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "La música se elige dentro del Coliseo.", "color": "red", "bold": false}]
execute if score @s arena_dj matches 1..16 run scoreboard players operation #song so_ar = @s arena_dj
execute if score @s arena_dj matches 99 run scoreboard players set #song so_ar 0
execute if score @s arena_dj matches 1 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Pigstep", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 2 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Otherside", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 3 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Creator", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 4 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Relic", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 5 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Precipice", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 6 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Strad", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 7 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Chirp", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 8 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Blocks", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 9 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Cat", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 10 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Far", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 11 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Mall", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 12 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Stal", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 13 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Ward", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 14 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Wait", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 15 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Tears", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 16 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema elegido: Lava Chicken", "color": "light_purple", "bold": false}]
execute if score @s arena_dj matches 99 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "♪ Tema al azar: la campana tira los dados.", "color": "light_purple", "bold": false}]
execute at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.5
execute if score #playing so_ar matches 1 if score #song so_ar matches 1.. run function so_arenas:lib/music_play
