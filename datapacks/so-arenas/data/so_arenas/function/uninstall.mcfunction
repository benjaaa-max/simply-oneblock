function so_arenas:lib/end
bossbar remove so_arenas:fight
scoreboard objectives remove so_ar
scoreboard objectives remove arena
scoreboard objectives remove arena_pr
scoreboard objectives remove arena_con
scoreboard objectives remove levelrank
scoreboard objectives remove so_ar_air
scoreboard objectives remove so_ar_rank
tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "so_arenas desinstalado (el coliseo construido queda en el mundo). Quitá el datapack y hacé /reload.", "color": "gray", "bold": false}]
