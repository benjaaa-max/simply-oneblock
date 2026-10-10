# so_events v2 — lo que pasa en la isla

Eventos automáticos cada `#every` bloques minados (por defecto 400, el primero desde 300), solo si hay alguien en la isla (64 bloques alrededor de 0 64 0).

| Evento | Duración | Qué pasa |
|---|---|---|
| Lluvia de recursos | 60 s | Caen materiales sobre los jugadores |
| Suministro | instantáneo | Cae un paquete de botín sobre cada jugador |
| Desafío de minería | 3 min | Romper `#mine_goal` bloques entre todos |
| Mercader especial | 5 min | Aparece a 3-7 bloques del OneBlock (uno de 4 mercaderes) |
| Invasión | hasta 7 min | Alerta, cuenta atrás, 3 oleadas y jefe(s) con escoltas |
| Noche oscura | 90 s | Oscuridad + oleadas de 5 mobs cada 20 s y final de 10 |

## Mercaderes
1. Misterioso: siempre las mismas 8 ofertas.
2. Alquimista: 8 pociones arrojadizas al azar (positivas y negativas).
3. Armero de la Corte: 8 al azar entre plantilla de netherita y ornamentos.
4. Minero: 8 minerales al azar, ~1.2x más caro.

## Invasiones (tipo | nombre | desde bloques | final)
| # | Invasión | Desde | Jefes / escoltas |
|---|---|---|---|
| 1 | Horda de zombis | 0 | rey_zombi, zombi_gigante, chicken_jockey, chicken_jockey |
| 2 | Ataque de slimes | 0 | slime_rey |
| 3 | Oleada acorazada | 2501 | comandante, zombie_escort, zombie_escort |
| 4 | Raid de saqueadores | 2501 | capitan, devastador, witch |
| 5 | Invasión del Nether | 6667 | caballero, piglin_bruto |
| 6 | Invasión del End | 10000 | senor_end |
| 7 | Plaga de artrópodos | 1500 | arana_colosal |
| 8 | Asedio marino | 4000 | guardian_abismo, guardian_abismo, guardian_abismo |
| 9 | Prueba ominosa | 5000 | heraldo_ominoso, breeze |
| 10 | Tormenta de huesos | 2501 | jinete_oseo |
| 11 | Rebelión de gólems | 5000 | golem_furioso, golem_furioso, golem_furioso |

Los mobs aparecen a 6-14 bloques del jugador sobre suelo firme (6 intentos; si no hay suelo, junto al jugador).
`mob_griefing` se desactiva durante el evento y se restaura al final; limpieza total al terminar.

Para `so_arenas`: `function so_events:api/boss {id:"zombi_gigante"}`, `api/mob {id:"husk"}`, `api/cleanup`.
Ayuda admin: `/function so_events:admin/help`. Jugadores: `/trigger evento`.
