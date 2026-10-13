tellraw @s {"text": "—— Diario de eventos ——", "color": "gold", "bold": true}
tellraw @s [{"text": "Eventos ganados: ", "color": "gray"}, {"score": {"name": "@s", "objective": "so_ev_win"}, "color": "white", "bold": true}]
tellraw @s [{"text": "Invasiones derrotadas: ", "color": "gray"}, {"score": {"name": "@s", "objective": "so_ev_inv"}, "color": "red"}]
tellraw @s [{"text": "Eventos positivos completados: ", "color": "gray"}, {"score": {"name": "@s", "objective": "so_ev_pos"}, "color": "green"}]
tellraw @s [{"text": "Racha actual de la isla: x", "color": "gray"}, {"score": {"name": "#streak", "objective": "so_ev"}, "color": "gold"}]
