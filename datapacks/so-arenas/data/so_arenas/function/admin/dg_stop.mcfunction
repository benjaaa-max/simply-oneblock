execute as @a[tag=so_ar_dgp] run function so_arenas:dg/exit_one
execute if score #dg so_ar matches 1.. run function so_arenas:dg/end
tellraw @s [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Mazmorra cerrada y reiniciada.", "color": "gray", "bold": false}]
