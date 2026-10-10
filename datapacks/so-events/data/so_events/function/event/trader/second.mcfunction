scoreboard players add #t so_ev 1
execute store result bossbar so_events:ev value run scoreboard players get #t so_ev
execute if score #t so_ev matches 300.. run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "El mercader se fue.", "color": "gray", "bold": false}]
execute if score #t so_ev matches 300.. run function so_events:lib/cleanup
