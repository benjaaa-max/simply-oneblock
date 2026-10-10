tellraw @s {"text": "SO Events — ayuda admin", "color": "gold"}
tellraw @s {"text": "/function so_events:admin/start_<lluvia|suministro|mineria|mercader|invasion|oscuridad>", "color": "gray"}
tellraw @s {"text": "/function so_events:admin/start_invasion_<1..5>  (1 zombis, 2 slimes, 3 acorazados, 4 raid, 5 Nether)", "color": "gray"}
tellraw @s {"text": "/function so_events:admin/stop | status | enable | disable | auto_on | auto_off", "color": "gray"}
tellraw @s {"text": "/scoreboard players set #every so_ev 400   (bloques entre eventos)", "color": "gray"}
tellraw @s {"text": "/scoreboard players set #min so_ev 300     (primer evento posible)", "color": "gray"}
tellraw @s {"text": "/scoreboard players set #mine_goal so_ev 150", "color": "gray"}
tellraw @s {"text": "Jugadores: /trigger evento  (estado del evento actual)", "color": "gray"}
