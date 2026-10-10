# so_arenas v1 — el Coliseo VorNeX (dónde pasa)

Zona aislada en **-5000 100 -5000** (Overworld). Enemigos del motor `so_events:api` (sin duplicar mobs ni bosses).

## Viaje
- Entrada: `/trigger arena` (teletransporta al lobby y abre el menú).
- Salida: `/trigger volver` (si hay desafío activo cuenta como **abandono**: pierde recompensa, kits y suena el cartel de derrota).
- Rango de cazador: `/trigger levelrank` (oculto por diseño).

## Construcción
1. `/trigger arena` para viajar (carga los chunks).
2. Parate en el lobby y corré `/function so_arenas:admin/build_dispatch`.
3. El coliseo oval (84x100 exterior, gradas de 8 niveles, muralla con arcos, 8 torres de 80 de alto, tunel y lobby con NPC) se levanta por partes (~7 funciones).

## Sistemas
- **Práctica por tiers** (menú táctil del lobby): Tier I (0), II (3.334), III (7.501), IV (15.000). Kit prestado marcado `so_arena_loan` (se retira al terminar) o tu propio equipo.
- **Contratos**: Caza 15 bajas (400+), Oleadas dobles (400+), Defensa del Núcleo (2.501+, altura permitida, anti-camping desactivado).
- **Anti-camping por altura**: 3 s por encima del foso y un wind charge te baja. En defensa está desactivado.
- **Victoria**: fuegos artificiales desde las 8 torres, fanfarria y recompensa (botellas de XP, esmeraldas y Fragmento de Victoria = echo shard renombrada).
- **Abandono/muerte**: limpieza total, sin recompensa, título `¡ABANDONASTE, CAGÓN!` y luego el aviso de `/trigger volver`.

Ayuda admin: `/function so_arenas:admin/help`. Los NPC del lobby dan pistas; el menú táctil es la forma de entrar a retos (compatible Bedrock).
