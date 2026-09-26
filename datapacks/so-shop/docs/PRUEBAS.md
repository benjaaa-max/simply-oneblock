# Plan de pruebas

## A. Prueba de humo (obligatoria)

1. `/function so_shop:admin/status` -> debe listar las 8 secciones.
2. `/function so_shop:admin/give_emeralds {value:32}`
3. `/trigger shop` -> abre el menú; clic en "Bloques decorativos".
4. Compra el primer artículo -> debe descontar esmeraldas, darte el ítem,
   sonar y mostrar el mensaje de compra.
5. Intenta comprar de nuevo inmediatamente -> debe salir "Espera un momento
   antes de comprar de nuevo" y NO descontar ni entregar nada.
6. Espera 1 segundo, compra de nuevo -> debe funcionar normal.
7. Entra a "Vender excedentes", vende algo -> revisa que `so_sold` suba
   (`/function so_shop:admin/status`).

## B. Reinicio diario del límite de venta

1. Vende hasta llegar al límite (por defecto 6).
2. Confirma que la tienda te niega vender más ese día.
3. Avanza el tiempo del mundo hasta el amanecer (`/time set day` o esperar).
4. Confirma que puedes volver a vender.
5. Para probar el caso "jugador desconectado al amanecer": con otro jugador
   (o el mismo, saliendo y entrando), desconéctate antes del amanecer y
   reconéctate después — el límite debe estar reiniciado igual.

## C. Ítem corregido

`/function so_shop:admin/unlock_all`, abre "Herramientas" y compra "Cadena
x32" — debe darte cadenas de hierro reales, no fallar ni dar un ítem vacío.

## D. Desinstalación

`/function so_shop:uninstall`, revisa que no queden objetivos `so_shop*` ni
`so_sold*` (`/scoreboard objectives list`), y que Simply OneBlock siga
funcionando normal.

## Qué se verificó ya, sin el juego

Sintaxis de 1044 comandos contra el árbol oficial de 26.2, catálogo completo
de 64 ítems contra el registro de 26.2, y la lógica del cooldown y del
reinicio diario con un simulador dedicado. Falta la prueba en el servidor
real — es lo único que este plan cubre.
