# so-shop: tienda por comando para Simply OneBlock

Datapack secundario modular que **no modifica** Simply OneBlock. Reemplaza a los aldeanos comerciantes por una tienda abierta con un comando, con catálogo que se desbloquea según el avance real del mundo.

## Lo que ya verifiqué en tus archivos

- Simply OneBlock lleva el progreso en el marcador `ib_minedcount` (jugador falso `fake_player`) y cierra cada fase en: 55, 260, 550, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000 y 9001 en adelante (After Phase). Corrijo que otra IA ([replit.com](http://replit.com)) editará una copia de simply_oneblock para extender los bloques a 15000 antes de llegar a After Phase. Entonces. las creaciones estaran independientes al contador pero debes saber que el contador se modificará a 15000 pero puede modificarse hasta a 20000
- `so-core` ya lee ese contador y calcula si estás en After Phase. Lo reutilizo como base.
- `so-traders` / `oneblock_traders` invocan aldeanos con ofertas fijas por hito, el usado ahora mismo es oneblock_adventure_traders de Claude, oneblock_traders (mi version) es solo una reserva vieja. Esa lógica de precios y catálogos se recicla, pero sin aldeanos.
- `ob_system` es solo referencia; no copio nada de él, solo sirve para ver sintaxis y sistemas que usa por si tenemos errores. 

## Cómo se abrirá la tienda

Un datapack no puede crear un comando propio llamado `/shop`. La forma estándar y que funciona para jugadores sin permisos de operador es:

- `**/trigger shop**` — abre el menú. Funciona igual para todos, sin ser operador.
- En tu servidor Purpur puedes además crear un alias real `/shop` en `commands.yml` que ejecute `trigger shop`, así los jugadores escriben literalmente `/shop`. Te dejo la línea exacta lista para pegar.

El menú aparece en el chat: categorías clicables, y dentro de cada categoría los artículos con precio. Al hacer clic se compra directamente; el pack comprueba que tengas el material, lo cobra y entrega el objeto. Si te falta algo, avisa cuánto falta.

## Estructura del catálogo

En la tienda solo se venderá: bloques decorativos, bloques de colores, bloques dificiles de conseguir, herramientas caras o de material, libros encantados, huevos/generadores de mobs, llaves o "contratos" de invasiones, eventos, etc

## Economía

- Moneda principal: **esmeralda**, más trueques directos con materiales que el OneBlock produce en cantidad (64–256 bloques comunes, 16–64 materiales intermedios).
- Hay también compra inversa: vendes excedentes (tierra, piedra, netherrack, kelp) por esmeraldas, con límite diario para que no se rompa la economía.
- Nada de Elytra ni objetos de final de juego en la tienda; esos quedan como recompensa del mundo.

## Módulos del datapack

```text
so-shop/
  pack.mcmeta
  data/minecraft/tags/function/{load,tick}.json
  data/so_shop/function/
    init            arranque, marcadores, triggers
    tick            lee el progreso y habilita triggers
    menu/           menú principal y páginas por categoría
    buy/            una función por artículo (cobro + entrega)
    lib/            cobro genérico, mensajes, sonidos
    admin/          activar, desactivar, dar esmeraldas, desinstalar
  data/so_shop/loot_table/   objetos especiales (llaves, contratos)
```

Todo cuelga de `so_core` para leer el progreso; si `so-core` no está, el pack lee `ib_minedcount` directamente igual.

## Rendimiento (para tus 2 GB)

- Sin escaneos de bloques ni de entidades por tick; solo una lectura de marcador cada 20 ticks.
- Sin entidades permanentes: la tienda no invoca nada, solo huevos/generadores o contratos.
- Compras resueltas con `clear` + `give`, coste fijo.

## Entrega

- Los archivos quedan en el proyecto, en `datapacks/so-shop/`, para que los puedas editar.
- Genero el `so-shop-v0.1.zip` listo para soltar en `world/datapacks/`.
- Incluyo un `README.md` con instalación, alias `/shop` para Purpur, comandos de administración y cómo desinstalar sin dejar rastro.

## Fuera de alcance por ahora

Jefes, oleadas, arenas, PvP, reputación y contratos quedan para módulos siguientes (`so-bosses`, `so-events`…). Primero dejamos la tienda funcionando y probada. El libro de bienvenida lo añadimos al final, como dijiste.