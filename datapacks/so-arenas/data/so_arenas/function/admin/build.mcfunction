forceload add -5048 -5056 -4952 -4916
scoreboard players set #bstep so_ar 0
tellraw @a [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Construyendo el Coliseo en 8 pasos (~6 s). Cargando chunks...", "color": "yellow", "bold": false}]
schedule function so_arenas:admin/build_step 40t
