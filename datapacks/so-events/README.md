# so_events v1 — lo que pasa en la isla

Eventos automáticos cada `#every` bloques minados (por defecto 400, el primero desde 300), solo si hay alguien en la isla (64 bloques alrededor de 0 64 0).

| Evento | Duración | Qué pasa |
|---|---|---|
| Lluvia de recursos | 60 s | Caen materiales sobre los jugadores |
| Suministro | instantáneo | Cae un paquete de botín sobre cada jugador |
| Desafío de minería | 3 min | Romper `#mine_goal` bloques entre todos |
| Mercader errante | 5 min | Mercader especial con ofertas raras |
| Invasión | hasta 7 min | Alerta, cuenta atrás, 3 oleadas y jefe invasor |
| Noche oscura | 90 s | Oscuridad + mobs cada 20 s (desde fase 5) |

Invasiones según fase: zombis/slimes al inicio, acorazados y raid desde 2501, Nether desde 6667.
Sin creepers, `mob_griefing` desactivado durante el evento y restaurado al final, mobs que nunca aparecen sobre el vacío, limpieza total al terminar y recompensa para todos los participantes.

Jefes: Rey Zombi, Slime Rey, Comandante Óseo, Capitán Saqueador, Caballero del Nether.

Para `so_arenas`: `function so_events:api/boss {id:"rey_zombi"}`, `api/mob {id:"husk"}`, `api/cleanup`.
Ayuda admin: `/function so_events:admin/help`. Jugadores: `/trigger evento`.
