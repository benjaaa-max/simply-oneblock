forceload add -5060 -5070 -4940 -4906
scoreboard players set #bstep so_ar 0
tellraw @a [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Construyendo el Coliseo en 14 pasos (~9 s). Cargando chunks...", "color": "yellow", "bold": false}]
schedule function so_arenas:admin/build_step 40t
