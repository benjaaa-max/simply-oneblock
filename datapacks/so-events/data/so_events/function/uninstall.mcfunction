function so_events:lib/cleanup
bossbar remove so_events:ev
bossbar remove so_events:boss
scoreboard objectives remove so_ev
scoreboard objectives remove evento
scoreboard objectives remove evento_diario
scoreboard objectives remove so_ev_win
scoreboard objectives remove so_ev_inv
scoreboard objectives remove so_ev_pos
data remove storage so_events:offers alq
data remove storage so_events:offers arm
data remove storage so_events:offers min
tellraw @s [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "so_events desinstalado. Quitá el datapack y hacé /reload.", "color": "gray", "bold": false}]
