function so_events:lib/begin
scoreboard players set #active so_ev 4
execute store result score #ttype so_ev run random value 1..4
execute if score #force_trader so_ev matches 1..4 run scoreboard players operation #ttype so_ev = #force_trader so_ev
scoreboard players set #force_trader so_ev 0
bossbar set so_events:ev max 300
bossbar set so_events:ev color blue
execute if score #ttype so_ev matches 1 run bossbar set so_events:ev name {"text": "Mercader Misterioso", "color": "aqua"}
execute if score #ttype so_ev matches 2 run bossbar set so_events:ev name {"text": "Alquimista Errante", "color": "light_purple"}
execute if score #ttype so_ev matches 3 run bossbar set so_events:ev name {"text": "Armero de la Corte", "color": "gold"}
execute if score #ttype so_ev matches 4 run bossbar set so_events:ev name {"text": "Minero Ambulante", "color": "gray"}
scoreboard players set #near so_ev 1
execute if score #ttype so_ev matches 1 in minecraft:overworld positioned 0 65 0 run function so_events:lib/spawn {mob:"npc/trader_1"}
execute if score #ttype so_ev matches 2 in minecraft:overworld positioned 0 65 0 run function so_events:lib/spawn {mob:"npc/trader_2"}
execute if score #ttype so_ev matches 3 in minecraft:overworld positioned 0 65 0 run function so_events:lib/spawn {mob:"npc/trader_3"}
execute if score #ttype so_ev matches 4 in minecraft:overworld positioned 0 65 0 run function so_events:lib/spawn {mob:"npc/trader_4"}
scoreboard players set #near so_ev 0
execute if score #ttype so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Mercader Misterioso", "color": "aqua", "bold": true}, {"text": " llegó junto al OneBlock por 5 minutos.", "color": "aqua", "bold": false}]
execute if score #ttype so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Alquimista Errante", "color": "light_purple", "bold": true}, {"text": " llegó junto al OneBlock por 5 minutos.", "color": "aqua", "bold": false}]
execute if score #ttype so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Armero de la Corte", "color": "gold", "bold": true}, {"text": " llegó junto al OneBlock por 5 minutos.", "color": "aqua", "bold": false}]
execute if score #ttype so_ev matches 4 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Minero Ambulante", "color": "gray", "bold": true}, {"text": " llegó junto al OneBlock por 5 minutos.", "color": "aqua", "bold": false}]
