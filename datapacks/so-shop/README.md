# SO Shop — Tienda por comando para Simply OneBlock

Datapack secundario para **Simply OneBlock 26.2** (Minecraft Java 26.2 / Purpur).
No modifica el datapack principal: solo lee su contador de progreso.

## Instalación

1. Copia `so-shop-v0.1.zip` (o esta carpeta) en `world/datapacks/`.
2. En el servidor: `/reload` o reinicia.
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

### Alias real `/shop` en Purpur/Paper

Edita `commands.yml` en la raíz del servidor:

```yaml
aliases:
  shop:
  - "trigger shop"
```

Reinicia el servidor. A partir de ahí `/shop` funciona para todos.

## Catálogo

| Sección | Se abre a (bloques) |
|---|---|
| Bloques decorativos | 0 |
| Bloques de color | 0 |
| Herramientas | 550 |
| Materiales raros | 2500 |
| Libros encantados | 4000 |
| Huevos generadores | 7000 |
| Llaves y contratos | 8250 |
| Vender excedentes | 0 |

Las secciones bloqueadas se muestran en gris con su requisito.
Moneda: **esmeralda**. La sección de venta convierte excedentes (tierra, piedra,
netherrack, troncos, arena, hierro, oro, kelp) en esmeraldas, con un límite de
**6 ventas por jugador y por día** para no romper la economía.

No se venden elytras ni objetos de final de juego: eso queda como recompensa del mundo.

## Comandos de administración (operador)

```
function so_shop:admin/enable                              activar la tienda
function so_shop:admin/disable                             desactivarla
function so_shop:admin/unlock_all                          abrir todas las secciones
function so_shop:admin/set_unlock {cat:3,value:2500}       mover el desbloqueo de una sección
function so_shop:admin/set_sell_limit {value:6}            límite diario de ventas
function so_shop:admin/give_emeralds {value:32}            darte esmeraldas para probar
function so_shop:uninstall                                 retirar todo sin rastro
```

Números de sección: 1 decorativos, 2 colores, 3 raros, 4 herramientas,
5 libros, 6 huevos, 7 llaves, 8 venta.

## Editar precios y artículos

Todo el catálogo está en `tools/build_so_shop.py` (listas `ITEMS` y `SELL`).
Cambia lo que quieras y vuelve a ejecutar:

```
python3 tools/build_so_shop.py
```

También puedes editar a mano los `.mcfunction` dentro de
`data/so_shop/function/item/` y `menu/`.

## Rendimiento

- Sin escaneo de bloques ni de entidades.
- No invoca ninguna entidad permanente.
- Cada compra son dos comandos (`clear` + `give`).
- Seguro para un servidor de 2 GB.

## Desinstalar

`function so_shop:uninstall`, luego quita el zip de `world/datapacks/` y `/reload`.
Simply OneBlock queda intacto.
