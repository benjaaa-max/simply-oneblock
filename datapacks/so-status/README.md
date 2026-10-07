# SO Status — rangos, HUD, progreso y beneficios

Datapack para Minecraft Java **26.2** / Purpur + Geyser. Solo lee el contador global de Simply OneBlock; no modifica su progreso.

## Instalación
1. Reemplazá la versión anterior por este ZIP en `world/datapacks/`.
2. Ejecutá `/minecraft:reload`.
3. Revisá `/function so_status:admin/status`.

Los rangos y enfriamientos existentes se conservan al actualizar. Los jugadores sin equipo reciben `VorUser`.

## HUD corregido
- **Panel lateral:** título `VorNeX • Tiempo (min)`; cada fila muestra prefijo de rango + usuario y sus minutos jugados.
- **Barra superior:** fase y bloques globales de Simply OneBlock.
- Apagar: `/scoreboard players set #hud_on so_cfg 0` o `/scoreboard players set #bar_on so_cfg 0`.
- Encender: usar valor `1`.

## Rangos y comandos
| Rango | Beneficios |
|---|---|
| NeXAdmin | Operador; no necesita beneficios custom. |
| VorLegend | `/trigger heal`, `/trigger craft`, `/trigger enderchest`, `/trigger hat`, `/trigger afk` |
| NeXLord | `/trigger feed`, `/trigger enderchest`, `/trigger hat`, `/trigger afk` |
| VorUser | `/trigger hat`, `/trigger afk` |

`heal` y `feed` tienen 5 minutos de enfriamiento. `craft` y `enderchest` crean un bloque temporal por 15 segundos únicamente si hay aire en el lugar apuntado. `afk` es un aviso visual; no evita cierres o expulsiones de Aternos.

## Viajes
No existe `trigger warp`. **SO Crates ya administra directamente**:
- `/trigger crates` — viajar a Crates y guardar el punto de regreso.
- `/trigger isla` — volver al punto guardado.

Los próximos destinos tendrán su trigger propio cuando sean agregados.

## Asignar rangos
```
/team join so_admin <jugador>
/team join so_vorlegend <jugador>
/team join so_nexlord <jugador>
/team join so_voruser <jugador>
```

## Nota vanilla
Un datapack no puede abrir a distancia las ventanas de Ender Chest o crafteo; por eso se crea un bloque temporal real. `/msg` y `/tell` ya son comandos nativos. `/reply` no puede implementarse con un datapack puro.
