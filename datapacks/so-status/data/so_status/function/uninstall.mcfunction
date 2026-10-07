# Desinstalación limpia. No toca Simply OneBlock ni ningún otro datapack.
scoreboard objectives setdisplay sidebar
scoreboard objectives remove so_sys
scoreboard objectives remove so_cfg
scoreboard objectives remove so_playtime
scoreboard objectives remove so_h
scoreboard objectives remove so_m
scoreboard objectives remove so_s
scoreboard objectives remove so_sidebar
bossbar remove so_status:progress
team remove so_admin
team remove so_vorlegend
team remove so_nexlord
team remove so_voruser
# so_core NO se borra: podría pertenecer al datapack so_core real si está instalado.
tellraw @a {"text":"[SO Status] Retirado. Los demás datapacks no fueron modificados.","color":"red"}
