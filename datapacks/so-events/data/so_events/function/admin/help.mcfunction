tellraw @s {"text": "SO Events v2 — ayuda admin", "color": "gold"}
tellraw @s {"text": "/function so_events:admin/start_<lluvia|suministro|mineria|mercader|invasion|oscuridad>", "color": "gray"}
tellraw @s {"text": "/function so_events:admin/start_invasion_<1..11>", "color": "gray"}
tellraw @s {"text": "  1 horda de zombis, 2 ataque de slimes, 3 oleada acorazada, 4 raid de saqueadores, 5 invasión del nether, 6 invasión del end, 7 plaga de artrópodos, 8 asedio marino, 9 prueba ominosa, 10 tormenta de huesos, 11 rebelión de gólems", "color": "gray"}
tellraw @s {"text": "/function so_events:admin/start_mercader_<1..4>  (1 misterioso, 2 alquimista, 3 armero, 4 minero)", "color": "gray"}
tellraw @s {"text": "/function so_events:admin/stop | status | enable | disable | auto_on | auto_off", "color": "gray"}
tellraw @s {"text": "/scoreboard players set #every so_ev 400   (bloques entre eventos)", "color": "gray"}
tellraw @s {"text": "/scoreboard players set #min so_ev 300     (primer evento posible)", "color": "gray"}
tellraw @s {"text": "/scoreboard players set #mine_goal so_ev 150", "color": "gray"}
tellraw @s {"text": "Jugadores: /trigger evento  (estado del evento actual)", "color": "gray"}
