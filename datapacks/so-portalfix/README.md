# so_portalfix

Parche de salida y recuperación para Simply OneBlock, pensado para el fallo observado en Aternos.

## Causa observada en los archivos

Simply OneBlock usa un `end_gateway` en `0 65 0` como portal de entrada. Varios retornos —incluido el portal de vuelta de la dimensión `phase_20`— envían al jugador a esas mismas coordenadas del Overworld. Si el jugador reaparece allí o usa un teletransporte cuyo destino es ese bloque, el gateway puede activarse otra vez y devolverlo a una dimensión de Simply OneBlock.

El OneBlock del Overworld funciona como fue diseñado; el problema aquí es llegar sobre el gateway activo. Este parche no cambia las dimensiones ni la progresión de las fases.

## Qué hace

- Al cambiar de dimensión hacia `minecraft:overworld`, comprueba si el jugador llegó sobre el gateway de Simply OneBlock y lo aparta inmediatamente.
- Después de una muerte, intenta llevar al jugador al Overworld si reapareció en otra dimensión; si reaparece sobre el gateway, lo aparta.
- Permite pedir una salida manual desde cualquier dimensión: `/trigger spf_escape set 1`.
- Reintenta un regreso solicitado durante 40 ticks. Si el servidor no acepta el cambio de dimensión, avisa al jugador y detiene los intentos.
- Incluye un chequeo por tick como respaldo para jugadores que queden sobre el gateway en el Overworld.

La salida segura configurada es `-2.5 65 0.5`, junto al punto OneBlock y fuera del gateway. El parche requiere que Simply OneBlock esté activo y exponga el predicado `simply_oneblock:portal`.

## Instalación

1. Conserva una copia de seguridad del mundo.
2. Sube `so_portalfix_aternos_v2.zip` a la carpeta `datapacks` del mundo, junto a Simply OneBlock.
3. Ejecuta `/minecraft:reload` o reinicia el servidor.
4. Si quedas atrapado, escribe `/trigger spf_escape set 1` en el chat.

## Desinstalación

Ejecuta `/function so_portalfix:uninstall`, desactiva el datapack y elimina el ZIP. La función elimina los objetivos de scoreboard que crea este parche.

## Límite de la corrección

El datapack puede rescatar al jugador cuando el servidor permite ejecutar un cambio de dimensión, y puede apartarlo del gateway de llegada. No puede corregir una falla interna del software del servidor que rechace o revierta todos los cambios de dimensión. La versión adjunta no se pudo probar dentro de un servidor Aternos; si el `/trigger` informa que no pudo confirmar el regreso, hace falta revisar el software y la versión exactos del servidor.

## v3 — Entrada a portales desde Bedrock (celular / Geyser)

Los jugadores de Bedrock ven el `end_gateway` como un bloque sólido y no pueden entrar. Ahora:

- **Automático:** si un jugador toca un portal (lo choca de frente, desde cualquier lado), el servidor lo coloca dentro del portal y Simply OneBlock hace el viaje normal. Funciona en el Overworld y en las dimensiones de fase.
- **Respaldo:** `/trigger spf_enter` busca un portal a menos de 3 bloques y te mete en él.
- Hay 3 segundos de espera tras cada viaje para no rebotar entre dimensiones.
- Admins: `/function so_portalfix:admin/assist_off` (o `assist_on`) desactiva la entrada automática solo para quien lo ejecuta.

Pendiente para v4: el retorno donde hoy solo funciona el comando.
