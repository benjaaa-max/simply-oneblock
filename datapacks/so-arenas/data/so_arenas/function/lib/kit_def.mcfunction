# Barricadas de Defensa: se pueden poner sobre cualquier bloque (modo aventura) y se borran al limpiar el foso.
give @s minecraft:oak_planks[minecraft:custom_data={so_arena_loan:1b},minecraft:lore=[{text:"Prestado por el Coliseo",color:"gray",italic:false}],minecraft:can_place_on=[{}]] 48
give @s minecraft:cobblestone_wall[minecraft:custom_data={so_arena_loan:1b},minecraft:lore=[{text:"Prestado por el Coliseo",color:"gray",italic:false}],minecraft:can_place_on=[{}]] 24
tag @s add so_ar_loan
tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Barricadas prestadas: tablas y muros. Armá defensas alrededor del Núcleo.", "color": "dark_purple", "bold": false}]
