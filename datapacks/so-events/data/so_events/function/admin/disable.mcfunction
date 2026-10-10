function so_events:lib/cleanup
scoreboard players set #enabled so_ev 0
tellraw @s [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Eventos desactivados.", "color": "red", "bold": false}]
