# so_status — Rangos, HUD y barra de progreso para Simply OneBlock V2

Datapack secundario e independiente. Minecraft Java **26.2** / Purpur, sin mods de cliente.

- Namespace propio: `so_status`. Objetivos de scoreboard con prefijo `so_`.
- **Solo lee** `fake_player ib_minedcount` (o `#blocks so_core` si algún día existe `so_core`). Nunca lo escribe.
- No modifica Simply OneBlock, `oneblock_adventure_traders`, `so_shop` ni `so_quests`.
- Los únicos archivos compartidos son `data/minecraft/tags/function/load.json` y `tick.json` (con `"replace": false`, se suman).

## Instalación

1. Copia `so_status.zip` en `world/datapacks/`.
2. `/minecraft:reload`.
3. `/function so_status:admin/status` debe imprimir el estado.

## Qué trae

### 1. Rangos (equipos de Minecraft)

| Rango | Prefijo visible (Tab y sobre la cabeza) |
|---|---|
| `so_admin` → **NeXAdmin** | `[NeXAdmin]` en rojo |
| `so_vorlegend` → **VorLegend** | `[VorLegend]` en dorado |
| `so_nexlord` → **NeXLord** | `[NeXLord]` en morado |
| `so_voruser` → **VorUser** | sin prefijo (rango por defecto) |

Un jugador sin rango asignado pasa a `VorUser` automáticamente. Para asignar un rango (como operador):

```
/team join so_admin <jugador>
/team join so_vorlegend <jugador>
/team join so_nexlord <jugador>
```

**Limitación real, no un olvido:** Minecraft no permite que un datapack cambie lo que aparece en comandos (`/tp`, `/tag`, etc.) a un "alias" distinto del nombre real de la cuenta — el prefijo de equipo se **agrega** delante del nombre real, nunca lo reemplaza. `[NeXAdmin] iTz_xChux_23` es posible; `[NeXAdmin] xChux` (nombre inventado reemplazando el real) no lo es con un datapack.

### 2. Barra de progreso (bossbar)

Igual que la barra de salud del Ender Dragon, pero para el progreso del OneBlock: muestra la fase actual (de las 19 reales de Simply OneBlock V2, con sus nombres y rangos de bloques reales extraídos de `tick.mcfunction`) y cuántos bloques lleva el servidor dentro de esa fase.

Es progreso **del servidor**, no de un jugador: todos ven la misma barra, basada en `fake_player ib_minedcount`.

### 3. HUD (panel lateral)

Tres líneas fijas, visibles siempre para cada jugador:

```
VorNeX - OneBlock
[NeXAdmin] iTz_xChux_23
01h 02m 03s
```

La tercera línea es el tiempo jugado **real** en el servidor (estadística nativa de Minecraft, no un contador propio), con cero a la izquierda cuando corresponde.

## Comandos de administración

```
/function so_status:admin/status     tu rango y el estado del módulo
/function so_status:admin/help
/scoreboard players set #hud_on so_cfg 0|1    activar/desactivar el HUD
/scoreboard players set #bar_on so_cfg 0|1    activar/desactivar la barra
/function so_status:uninstall        retirada limpia
```

## Cambiar el nombre del servidor

El nombre `VorNeX - OneBlock` está fijado en `hud_update.mcfunction` (buscá `VorNeX - OneBlock` y reemplazalo en las 3 líneas que lo usan). Tras editar: `/minecraft:reload`.

## Rendimiento

- El HUD (lo único que corre por jugador) se refresca 1 vez por segundo, no cada tick.
- La barra de progreso se recalcula cada tick (es barata: un puñado de comparaciones de score).
- Sin entidades, sin escaneo de bloques.

## Desinstalar

`/function so_status:uninstall`, luego borra el zip y `/minecraft:reload`. No toca ningún otro datapack.
