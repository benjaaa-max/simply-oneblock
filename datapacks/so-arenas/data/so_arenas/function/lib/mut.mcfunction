execute unless entity @s[tag=so_ar_zone] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Los mutadores se eligen dentro del Coliseo.", "color": "red", "bold": false}]
execute if score #mode so_ar matches 1..8 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Los mutadores se eligen antes de la campana.", "color": "red", "bold": false}]
execute if score @s arena_mut matches 1 store success score #tmp so_ar if score #mut_n so_ar matches 0
execute if score @s arena_mut matches 1 run scoreboard players operation #mut_n so_ar = #tmp so_ar
execute if score @s arena_mut matches 1 if score #mut_n so_ar matches 1 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Mutador ACTIVADO: Niebla de Oscuridad (botín doble).", "color": "red", "bold": false}]
execute if score @s arena_mut matches 1 if score #mut_n so_ar matches 0 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Mutador desactivado: Niebla de Oscuridad.", "color": "gray", "bold": false}]
execute if score @s arena_mut matches 2 store success score #tmp so_ar if score #mut_f so_ar matches 0
execute if score @s arena_mut matches 2 run scoreboard players operation #mut_f so_ar = #tmp so_ar
execute if score @s arena_mut matches 2 if score #mut_f so_ar matches 1 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Mutador ACTIVADO: Furia Monstruosa (botín doble).", "color": "red", "bold": false}]
execute if score @s arena_mut matches 2 if score #mut_f so_ar matches 0 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Mutador desactivado: Furia Monstruosa.", "color": "gray", "bold": false}]
execute if score @s arena_mut matches 3 store success score #tmp so_ar if score #mut_v so_ar matches 0
execute if score @s arena_mut matches 3 run scoreboard players operation #mut_v so_ar = #tmp so_ar
execute if score @s arena_mut matches 3 if score #mut_v so_ar matches 1 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Mutador ACTIVADO: Vampirismo (botín doble).", "color": "red", "bold": false}]
execute if score @s arena_mut matches 3 if score #mut_v so_ar matches 0 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Mutador desactivado: Vampirismo.", "color": "gray", "bold": false}]
execute if score @s arena_mut matches 4 run scoreboard players set #mut_n so_ar 0
execute if score @s arena_mut matches 4 run scoreboard players set #mut_f so_ar 0
execute if score @s arena_mut matches 4 run scoreboard players set #mut_v so_ar 0
execute if score @s arena_mut matches 4 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Mutadores quitados.", "color": "gray", "bold": false}]
execute at @s run playsound minecraft:block.enchantment_table.use master @s ~ ~ ~ 1 1
