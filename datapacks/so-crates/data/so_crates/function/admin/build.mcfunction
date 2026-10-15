# Construye el Templo de las Bóvedas (no hace falta estar cerca: forzamos la carga de chunks).
execute in minecraft:overworld run forceload add 4960 4970 5040 5030
tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Construyendo el templo en 3 pasos (~2 s)...","color":"yellow"}]
schedule function so_crates:build/s1 20t
