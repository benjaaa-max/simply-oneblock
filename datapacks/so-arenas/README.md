# so_arenas v4 — el Coliseo VorNeX

Zona en **-5000 100 -5000** (Overworld). Enemigos y jefes de `so_events:api/*` (sin duplicar mobs).

## Instalar / actualizar
1. Borrá la carpeta vieja `so-arenas` de `world/datapacks` y poné la nueva. `/reload`.
2. **Reconstruí** (hay terraza, palco, luces y túnel nuevos): `/trigger arena` y `/function so_arenas:admin/build` (14 pasos, ~9 s).
3. Si algún aldeano se pierde: `/function so_arenas:admin/npcs`.

## Flujo de un desafío
1. Elegís práctica o contrato (aldeanos, carteles, placas del piso, diálogo o chat).
2. Vas al **túnel de gladiadores**: elegís el tema (carteles, diálogo, chat o poniendo tu disco en el tocadiscos), activás mutadores y tocás la **campana**, el cartel ¡COMENZAR! o la placa del portón. A los 30 s arranca sola. Sin elección suena un tema épico al azar (Pigstep, Otherside, Creator, Relic, Precipice, Strad, Chirp).
3. Los jueces saludan, se abre la reja y la música suena en todo el estadio.
4. **Victoria**: cohetes, fanfarria, portones abiertos 60 s y un **cofre de recompensa** (cofre, cofre trampa, barril o cofre de cobre al azar) en el pedestal del lobby. Salís a pie por el túnel o pisando la placa dorada. Después el foso se limpia solo.
5. **Derrota / abandono**: sin recompensa, el foso se limpia a los 3 s.

## Limpieza segura
Solo se borran ítems, flechas y orbes del piso del foso, y bloques dentro del óvalo interior (barricadas). Nunca se tocan muros, labio anti-arañas, gradas, túnel, lobby, tocadiscos ni terraza.

## Desafíos
- Práctica Tier I–IV (0 / 3.334 / 7.501 / 15.000 bloques), con kit prestado o equipo propio.
- Contratos: Caza: 15 bajas objetivo (400+), Oleadas dobles (400+), Defensa del Núcleo (2.501+), Rey de la Colina (400+), Asedio Volador (2.501+), Duelo de Campeones (3.334+), Desafío de Jefes (6.667+).
- Mutadores (botín doble): Niebla de Oscuridad, Furia Monstruosa, Vampirismo.
- Racha: ganar sin morir; cofre extra a las 3, 5 y desde 10. Se ve con `/trigger levelrank`.
- Duelo PvP amistoso (`/trigger arena_pvp`): termina a los 3 corazones. Requiere PvP activado en el servidor.

## v4
- Música: 16 temas de batalla (sin 11, 13, 5 ni discos raros). El disco que pongas en el tocadiscos del túnel manda.
- Cestas de apoyo: fuera de combate te devuelven lo que tiraste.
- Rey de la Colina: colina física con anillo dorado; captura 90 s dentro de 120 s.
- Arañas, endermans y wardens siempre te persiguen.
- Defensa: el aldeano "Núcleo Vivo" recibe golpes reales; no le pegues.
- Los cofres de premio pueden traer llaves de so_crates (Simply OneBlock comunes; Arquitecto/Silvestre, Subterránea/Batalla, Elder/To the End raras; Warden/Wither/Abisal/Vacío legendarias) y Fragmentos de Llave.

## Las Catacumbas
Entrada: placa de obsidiana llorosa en la plaza sur (o menú). Cripta de los Caídos (0), Mina Abandonada (3.000), Templo Sumergido (6.000).
3 salas con reja que se cierra hasta vencer a todos, cofre tras la sala 2, Llave de Sala + barril tras la sala 3, jefe con cofre final y récord de tiempo en el cartel de la plaza. Se reinicia sola al ganar, morir o abandonar. Admins entran a todas.

## Estadio
- Lobby con techo de vidrio, arcos hacia una plaza y una terraza que rodea el coliseo: fuentes, pérgolas, cerezos, glorietas con tocadiscos, jardineras y faroles.
- Palco de jueces (norte) con tablero en vivo, público en las gradas, cofres de cobre con cohetes, cestas de apoyo (lo que tirás aparece junto a un luchador), médica de campaña, tacho de descarte.
- `/trigger arena_ver`: subir/bajar de las tribunas como espectador invisible.
