# Plan de pruebas de so_status

## A. Prueba de humo

1. `/function so_status:admin/status` -> debe decir tu rango (VorUser por defecto).
2. Mirá el panel lateral derecho: debe mostrar las 3 líneas (servidor, nombre+rango, tiempo).
3. Esperá un minuto y confirmá que el tiempo avanza y nunca muestra un solo dígito (siempre "0X").
4. `/team join so_admin <tu nombre>`: el prefijo `[NeXAdmin]` debe aparecer en el panel, sobre tu cabeza, y en el Tab (tecla Tab).
5. Mirá la barra de progreso arriba de la pantalla: debe decir la fase actual y los bloques dentro de ella.
6. Mina un bloque del OneBlock y confirmá que la barra se mueve.

## B. Rangos

Probá los 4 rangos (`so_admin`, `so_vorlegend`, `so_nexlord`, `so_voruser`) y confirmá que el prefijo del Tab coincide con la tabla del README. Un jugador recién conectado sin rango debe quedar en VorUser automáticamente.

## C. Fases reales

Comprobá con `/scoreboard players get fake_player ib_minedcount` que el número coincide con lo que muestra la barra, y que el nombre de fase coincide con el bioma real donde estás parado en el mundo.

## D. Desinstalación

`/function so_status:uninstall`, luego `/scoreboard objectives list`: no debe quedar ningún `so_*` salvo `so_core` (es a propósito, ver README).

## Qué se verificó ya, sin el juego

- Sintaxis de 197 comandos contra el árbol oficial de comandos de 26.2.
- Cálculo de tiempo jugado: 7 casos (incluidos 0 segundos, justo 1 hora, 23:59:59) todos exactos.
- Cálculo de porcentaje de la barra: inicio exacto de fase (0%), medio (13% en un caso real), final exacto (100%).
- Rango persiste tras reasignación y tras el tick de asignación por defecto (no pisa un rango ya puesto).
- 100 iteraciones de progreso con 3 jugadores conectados, sin errores.
- Desinstalación limpia.

**Lo que ninguna simulación cubre:** cómo se ve el prefijo de equipo en el Tab y sobre la cabeza del jugador en el cliente real, y si el panel lateral se superpone bien con otros elementos de la UI (inventario, chat).
