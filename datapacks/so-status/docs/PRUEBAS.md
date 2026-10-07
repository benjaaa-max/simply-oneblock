# Pruebas rápidas
1. `/minecraft:reload`: el log no debe mostrar errores de `so_status`.
2. El panel lateral debe mostrar `VorNeX • Tiempo (min)` y una fila por jugador conectado.
3. `/scoreboard players set #hud_on so_cfg 0` debe ocultarlo; valor `1` debe restaurarlo en hasta un segundo.
4. La barra debe mostrar fase y bloques; `#bar_on so_cfg 0|1` debe ocultarla/restaurarla.
5. Probá cada rango y sus triggers según README; un rango incorrecto debe recibir rechazo.
6. `heal`/`feed`: el segundo uso debe mostrar enfriamiento.
7. `craft`/`enderchest`: apuntá a aire; el bloque debe desaparecer a los 15 segundos sin borrar bloques reemplazados por otra cosa.
8. Con `so_crates` activo, `/trigger crates` y `/trigger isla` deben conservar su comportamiento original.
9. `/function so_status:uninstall` debe retirar HUD, barra, equipos, bloques temporales y objetivos propios.
