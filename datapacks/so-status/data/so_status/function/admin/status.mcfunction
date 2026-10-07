tellraw @s {"text":"=== SO Status ===","color":"gold","bold":true}
tellraw @s [{"text":"Activo: ","color":"yellow"},{"score":{"name":"#enabled","objective":"so_cfg"},"color":"white"},{"text":"  HUD: ","color":"yellow"},{"score":{"name":"#hud_on","objective":"so_cfg"},"color":"white"},{"text":"  Barra: ","color":"yellow"},{"score":{"name":"#bar_on","objective":"so_cfg"},"color":"white"}]
tellraw @s [{"text":"Jugador/rango: ","color":"yellow"},{"selector":"@s","color":"white"}]
tellraw @s [{"text":"Bloques detectados: ","color":"yellow"},{"score":{"name":"#blk","objective":"so_sys"},"color":"white"},{"text":"  Fase: ","color":"yellow"},{"score":{"name":"#phase_idx","objective":"so_sys"},"color":"white"}]
execute if score #src so_sys matches 0 run tellraw @s {"text":"AVISO: no se encontró el contador del OneBlock.","color":"red"}
