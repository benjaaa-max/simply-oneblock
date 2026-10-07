tellraw @s {"text":"=== SO Status ===","color":"gold","bold":true}
tellraw @s [{"text":"Activo: ","color":"yellow"},{"score":{"name":"#enabled","objective":"so_cfg"},"color":"white"},{"text":"  HUD: ","color":"yellow"},{"score":{"name":"#hud_on","objective":"so_cfg"},"color":"white"},{"text":"  Barra: ","color":"yellow"},{"score":{"name":"#bar_on","objective":"so_cfg"},"color":"white"}]
tellraw @s [{"text":"Tu rango: ","color":"yellow"},{"selector":"@s","color":"white"}]
