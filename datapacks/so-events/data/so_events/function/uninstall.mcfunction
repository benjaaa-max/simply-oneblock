function so_events:lib/cleanup
bossbar remove so_events:ev
bossbar remove so_events:boss
scoreboard objectives remove so_ev
scoreboard objectives remove evento
tellraw @s [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "so_events desinstalado. Quitá el datapack y hacé /reload.", "color": "gray", "bold": false}]
