execute if score #dgs so_ar matches 9 run return run function so_arenas:dg/end
tellraw @a[tag=so_ar_zone] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "La expedición terminó: nadie quedó en las catacumbas.", "color": "gray", "bold": false}]
function so_arenas:dg/end
