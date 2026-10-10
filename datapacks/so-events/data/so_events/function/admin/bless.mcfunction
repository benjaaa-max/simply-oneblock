execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run function so_events:bless/give
tellraw @s [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Bendición entregada a la isla.", "color": "green", "bold": false}]
