# Panel compartido: título del servidor; una fila por jugador conectado.
# El prefijo del equipo muestra el rango y el número muestra minutos jugados.
scoreboard players reset * so_sidebar
execute as @a run scoreboard players operation @s so_sidebar = @s so_playtime
scoreboard players operation @a so_sidebar /= #1200 so_sys
scoreboard objectives setdisplay sidebar so_sidebar
