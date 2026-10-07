# so_quests v3

Misiones para Simply OneBlock. Abrir: `/trigger quests` (alias `/shop`-style: en Purpur `quests: trigger quests` en commands.yml).

- 50 individuales (Fases y progreso, Recoleccion y fabricacion, Combate y exploracion)
- 28 logros de Minecraft con recompensa extra
- 36 Metas de la Isla (grupales): suman lo que hace todo el servidor; cada jugador reclama su parte una vez
- 3 diarias (se reinician cada dia de Minecraft)
- Colores por estado en el menu: gris (sin empezar), rojo/amarillo (en progreso),
  verde [!] en negrita (lista para reclamar), tachado (ya reclamada). Las misiones
  de un solo objetivo nunca usan rojo/amarillo.
- El menu se reabre solo: al ver una mision incompleta o al reclamar, la ventana
  vuelve sola para seguir jugando con el menu abierto.
- Aviso unico al completar una mision: actionbar + sonido (sin spam).

Reclamo manual con ventana de confirmacion y chequeo de inventario lleno.
Cuenta de bloques: so_core primero, si no existe lee `fake_player ib_minedcount`.
Puente con so_shop v0.4: `so_shop_seen` (abrio la tienda) y `so_shop_buys` (compras).
Mercaderes: advancements `so_quests:trade/*` con los tags `oba_trader` / `oba_t_<id>`.

Editar numeros/premios: `tools/build_so_quests.py` y regenerar.
Admin: `/function so_quests:admin/help`. Desinstalar: `/function so_quests:uninstall`.
Importante: reemplaza a so_quests v1 (mismo nombre interno). Quita la v1 antes de instalar.

La lista de objetivos que la ventana no explica esta en `README-OBJETIVOS.md`.
