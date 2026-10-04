# SO Crates (so_crates) v0.1

Zona de Crates con bóvedas de Minecraft (vaults). Abrís con llave, la bóveda gira unos segundos y te tira el premio.
Canje ilimitado: mientras tengas llaves, podés abrir la misma bóveda las veces que quieras.

## Instalación (admin)
1. Copiá la carpeta `so-crates` a `world/datapacks/` y `/reload`.
2. `/function so_crates:admin/goto` (te lleva a 5000 200 5000 del mundo normal).
3. `/function so_crates:admin/build` (construye la plataforma con barreras y las 18 bóvedas).

## Jugadores
- `/trigger crates` → viaja a la zona (solo desde el mundo normal). Guarda dónde estabas.
- `/trigger isla` o tocar el cartel "Volver a la isla" → regresa al lugar de donde viniste.
- Dentro de la zona se pasa a modo aventura (no se puede romper ni construir). Al salir vuelve a supervivencia.
- Admins (tag `oneblock_admin`): no se les cambia el modo; reciben un aviso con clic para pasar a aventura.

## OneBlock Crate (12 bóvedas, fila norte)
Una bóveda por cada llave de Simply OneBlock. Mayor nivel = más premios y mejores chances (y chance de Llave del Vacío en nivel 3).
- Cemetery Key — nivel 1
- Graveyard Key — nivel 1
- Ossuary Key — nivel 1
- Old Tower Key — nivel 1
- Pyramid Key — nivel 2
- Rusty Mineshaft Key — nivel 2
- Treasure Room — nivel 2
- Deep_Key — nivel 2
- Elder Guardian Key — nivel 3
- Warden_Key — nivel 3
- Wither Arena — nivel 3
- To the End — nivel 3

## Crates temáticos (fila sur)
- Llave del Arquitecto → Crate del Constructor
- Llave Subterránea → Crate del Minero
- Llave Silvestre → Crate de la Naturaleza
- Llave de Batalla → Crate de Combate
- Llave Abisal → Crate Místico
- Llave del Vacío → Crate Legendario

## Llaves para probar
`/function so_crates:admin/give_all_keys` o `/function so_crates:give/<id>` (cemetery, warden, builder, legend, ...).
La venta en la tienda se agrega en so_shop (próximo paso).

## Ajustes
Todo se edita en `tools/build_so_crates.py` (centro, botín, llaves) y se regenera.
