function so_arenas:admin/stop
function so_arenas:admin/dg_stop
bossbar remove so_arenas:fight
bossbar remove so_arenas:dg
forceload remove -5048 -5054 -4958 -4970
scoreboard objectives remove so_ar
scoreboard objectives remove arena
scoreboard objectives remove volver
scoreboard objectives remove arena_pr
scoreboard objectives remove arena_con
scoreboard objectives remove levelrank
scoreboard objectives remove arena_dj
scoreboard objectives remove arena_mut
scoreboard objectives remove arena_ver
scoreboard objectives remove arena_pvp
scoreboard objectives remove arena_dg
scoreboard objectives remove so_ar_air
scoreboard objectives remove so_ar_rank
scoreboard objectives remove so_ar_x
scoreboard objectives remove so_ar_y
scoreboard objectives remove so_ar_z
scoreboard objectives remove so_ar_saved
scoreboard objectives remove so_ar_streak
scoreboard objectives remove so_ar_hp
scoreboard objectives remove so_ar_death
tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "so_arenas desinstalado (el coliseo queda en el mundo). Quitá el datapack y hacé /reload.", "color": "gray", "bold": false}]
