# SO Shop — Tienda por comando para Simply OneBlock

Datapack secundario para **Simply OneBlock 26.2** (Minecraft Java 26.2 / Purpur).
No modifica el datapack principal: solo lee su contador de progreso.

Base original de Lovable AI, revisado, corregido y ampliado por Claude
(ver `docs/CAMBIOS.md`).

## Instalación

1. Copia `so-shop-v0.1.zip` (o esta carpeta) en `world/datapacks/`.
2. En el servidor: `/minecraft:reload` o reinicia.
3. Verás en el chat: `[SO Shop] Tienda cargada.`

Compatible con `so-core`: si está instalado, la tienda usa su contador; si no,
lee `ib_minedcount` de Simply OneBlock directamente. Da igual que el contador
llegue a 9000, 15000 o 20000 — los desbloqueos son valores configurables.

## Uso para jugadores

```
/trigger shop
```

Abre el menú en el chat. Cada categoría y cada artículo es clicable.
Al hacer clic se cobra el pago y se entrega el objeto al instante.
No hace falta ser operador.

Tras cada compra o venta hay un breve cooldown (1 segundo) antes de poder
volver a comprar, para evitar dobles clics accidentales.

### Alias real `/shop` en Purpur/Paper

Edita `commands.yml` en la raíz del servidor:

```yaml
aliases:
  shop:
  - "trigger shop"
```

Reinicia el servidor. A partir de ahí `/shop` funciona para todos.

## Catálogo

| # | Sección | Se abre a (bloques) |
|---|---|---|
| 1 | Bloques decorativos | 0 |
| 2 | Bloques de color | 0 |
| 3 | Materiales raros | 2500 |
| 4 | Herramientas | 550 |
| 5 | Libros encantados | 4000 |
| 6 | Huevos generadores | 7000 |
| 7 | Llaves y contratos | 8250 |
| 8 | Vender excedentes | 0 |

Las secciones bloqueadas se muestran en gris con su requisito.
Moneda: **esmeralda**. La sección de venta convierte excedentes (tierra, piedra,
netherrack, troncos, arena, hierro, oro, kelp) en esmeraldas, con un límite de
**6 ventas por jugador y por día** para no romper la economía. El límite se
reinicia para todos al amanecer del mundo, esté cada jugador conectado o no
en ese momento exacto.

No se venden elytras ni objetos de final de juego: eso queda como recompensa del mundo.

## Comandos de administración (operador)

```
function so_shop:admin/status                              estado, umbrales y desbloqueo de un vistazo
function so_shop:admin/help                                 lista de comandos
function so_shop:admin/enable                                activar la tienda
function so_shop:admin/disable                               desactivarla
function so_shop:admin/unlock_all                            abrir todas las secciones
function so_shop:admin/set_unlock {cat:3,value:2500}        mover el desbloqueo de una sección
function so_shop:admin/set_sell_limit {value:6}              límite diario de ventas
function so_shop:admin/give_emeralds {value:32}              darte esmeraldas para probar
function so_shop:uninstall                                   retirar todo sin rastro
```

Números de sección: 1 decorativos, 2 colores, 3 raros, 4 herramientas,
5 libros, 6 huevos, 7 llaves, 8 venta.

## Editar precios y artículos

Los `.mcfunction` están en `data/so_shop/function/item/` (uno por artículo, con
su `_ok` correspondiente que se ejecuta si el jugador puede pagarlo) y
`data/so_shop/function/menu/` (las 8 categorías). No viene con este ZIP el
script generador original; edita los `.mcfunction` directamente y aplica con
`/minecraft:reload`.

## Rendimiento

- Sin escaneo de bloques ni de entidades.
- No invoca ninguna entidad permanente.
- Cada compra son dos comandos (`clear` + `give`) más el cooldown.
- Seguro para un servidor de 2-3 GB (probado en el contexto de Aternos).

## Desinstalar

`function so_shop:uninstall`, luego quita el zip de `world/datapacks/` y
`/minecraft:reload`. Simply OneBlock queda intacto.
