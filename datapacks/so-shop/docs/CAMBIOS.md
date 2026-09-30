# Cambios respecto a la versión original de Lovable AI

## Corregidos

1. **`pack.mcmeta`**: usaba solo `pack_format` (formato viejo). En Minecraft 26.2
   eso puede hacer que el datapack se rechace entero sin aviso en pantalla.
   Cambiado a `min_format`/`max_format`, igual que Simply OneBlock.

2. **Ítem inexistente**: la "Cadena x32" (artículo 105, categoría Herramientas)
   entregaba `minecraft:chain`, que no existe en el registro de 26.2.
   Corregido a `minecraft:iron_chain`.

3. **Reinicio diario del límite de venta**: el original usaba
   `scoreboard players reset @a so_sold`, que solo alcanza a jugadores
   **conectados en el instante exacto** en que amanece. Un jugador que se
   conectara después de ese momento se quedaba con el contador del día
   anterior, potencialmente bloqueado sin haber vendido nada ese día.
   Se agregó un identificador de día global (`#day_id`) comparado contra
   uno por jugador (`so_sold_day`): cualquier jugador que se conecte, en
   cualquier momento, se sincroniza automáticamente al primer tick.

## Agregado

4. **Cooldown de compra/venta** (1 segundo, objetivo `so_shop_cd`): evita que
   un doble clic accidental compre o venda dos veces. Se tomó la idea de
   `so_extras` (Emergent.sh), pero ahí el cooldown nunca se decrementaba
   (bug: el objetivo se declaraba pero ningún `tick` lo bajaba) — se
   implementó de nuevo con el decremento real en `tick.mcfunction`.

5. **Lore y rareza en los objetos especiales** (Llave de Mazmorra, Contrato
   de Invasión, Boleto de Arena): antes solo tenían nombre; ahora incluyen
   una descripción de qué hacen y su rareza, con el mismo patrón de
   componentes de ítem (`lore`, `enchantment_glint_override`) que ya usaba
   `so_shop` para el nombre.

6. **`admin/status`**: nuevo comando que muestra de un vistazo si la tienda
   está activa, el conteo leído, el umbral y desbloqueo de las 8 secciones,
   el cooldown y las ventas del día de quien lo ejecuta.

7. **`admin/help`**: lista todos los comandos de administración en un solo
   lugar.

8. **`uninstall`**: se agregaron a la lista de limpieza los dos objetivos
   nuevos (`so_sold_day`, `so_shop_cd`) para que la desinstalación siga
   siendo completa.

## Verificación

- 1044 comandos, 0 fallos de sintaxis contra el árbol oficial de comandos de
  Minecraft 26.2.
- 0 ítems o encantamientos inexistentes en el catálogo completo (64 artículos).
- Lógica probada con un simulador dedicado: cooldown bloqueando compras
  repetidas, sincronización del límite diario con un jugador que se conecta
  después del reinicio, y una partida simulada de progreso sin errores.
- No se probó todavía en un servidor real — ver `docs/PRUEBAS.md` para el
  plan de verificación en el juego.

## 1.1 (fix post-entrega: el conteo no se leía)

9. **Bug crítico: la tienda nunca desbloqueaba nada.** La detección de
   `so_core` usaba `execute if/unless score #blocks so_core matches ...`
   sin haber creado antes el objetivo `so_core`. Cuando ese datapack no
   está instalado (caso normal, ya que `so_core` se deja para el final del
   proyecto), Minecraft trata la consulta a un objetivo inexistente como
   "Unknown scoreboard objective" en vez de simplemente evaluar la condición
   como falsa, y ninguna de las dos ramas (leer de `so_core` / leer
   `ib_minedcount`) llegaba a ejecutarse. `#blocks so_shop` se quedaba
   siempre en 0, y por lo tanto `admin/unlock_all` tampoco tenía efecto real:
   movía los umbrales, pero la comparación seguía sin tener un conteo válido
   con qué comparar. Arreglado creando el objetivo `so_core` en el propio
   `init.mcfunction` de so_shop (no pisa nada si el datapack so_core real
   se instala después) para que la consulta sea siempre segura.

10. **Límite diario de venta**: subido de 6 a 20 transacciones por defecto
    (más cómodo para probar); el mensaje en el menú de venta ahora aclara
    que el límite es por transacción, no por cantidad de bloques.

11. **`admin/status`**: ahora muestra explícitamente de dónde viene el
    conteo (`so_core` o `ib_minedcount`) y avisa en rojo si por algún
    motivo no se está leyendo nada, en vez de mostrar un campo vacío sin
    explicación.

## 0.3 (piloto ventanas)
- `/trigger shop` abre una ventana con botones (dialog). `/trigger shop set 2` abre el menú clásico del chat.
- Sección Decorativos en ventana con confirmación e ícono del objeto antes de comprar. El resto de secciones siguen en chat.
- Ventanas en `data/so_shop/dialog/`, generadas con `tools/build_so_shop_dialogs.py`.
