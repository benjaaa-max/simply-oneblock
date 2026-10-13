tellraw @s {"text": "SO Events v4 — ayuda admin", "color": "gold"}
tellraw @s {"text": "/function so_events:admin/start_<lluvia|suministro|mineria|mercader|invasion|oscuridad|duende|mana|altar>", "color": "gray"}
tellraw @s {"text": "/function so_events:admin/start_invasion_<1..20>", "color": "gray"}
tellraw @s {"text": "/function so_events:admin/start_invasion_nivel_<1|2|3>  (invasión al azar con nivel forzado)", "color": "gray"}
tellraw @s {"text": "/function so_events:admin/start_<meteoritos|oro|espejismo|caravana|eclipse>  (eventos v4)", "color": "gray"}
tellraw @s {"text": "/function so_events:admin/alpha_on | alpha_off  (forzar invasiones alfa)", "color": "gray"}
tellraw @s {"text": "/function so_events:admin/bless | bless_<1..5> | bless_on | bless_off", "color": "gray"}
tellraw @s {"text": "  1 prisa X 5 min, 2 regeneración III 60 s, 3 fuerza V 60 s, 4 velocidad II 2 min, 5 absorción IX 3 min", "color": "gray"}
tellraw @s {"text": "  1 horda de zombis, 2 ataque de slimes, 3 oleada acorazada, 4 raid de saqueadores, 5 invasión del nether, 6 invasión del end, 7 plaga de artrópodos, 8 asedio marino, 9 prueba ominosa, 10 tormenta de huesos, 11 rebelión de gólems, 12 ilusionismo oscuro, 13 asalto del bastión, 14 caza del warden, 15 enjambre del cielo, 16 marea anciana, 17 aquelarre de brujas, 18 furia de llamas, 19 horda zombificada, 20 vanguardia del mal", "color": "gray"}
tellraw @s {"text": "/function so_events:admin/start_mercader_<1..4>  (1 misterioso, 2 alquimista, 3 armero, 4 minero)", "color": "gray"}
tellraw @s {"text": "/function so_events:admin/stop | status | enable | disable | auto_on | auto_off", "color": "gray"}
tellraw @s {"text": "/scoreboard players set #every so_ev 400   (bloques entre eventos)", "color": "gray"}
tellraw @s {"text": "/scoreboard players set #min so_ev 300     (primer evento posible)", "color": "gray"}
tellraw @s {"text": "/scoreboard players set #mine_goal so_ev 150", "color": "gray"}
tellraw @s {"text": "/scoreboard players set #bless_every so_ev 200   (bloques entre bendiciones)", "color": "gray"}
tellraw @s {"text": "Jugadores: /trigger evento  (estado del evento actual)  ·  /trigger evento_diario  (estadísticas)", "color": "gray"}
