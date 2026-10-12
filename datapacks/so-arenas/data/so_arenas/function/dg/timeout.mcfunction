tellraw @a[tag=so_ar_dgp] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Se acabó el tiempo (20 min). La mazmorra los expulsa.", "color": "red", "bold": false}]
execute as @a[tag=so_ar_dgp] run function so_arenas:dg/exit_one
function so_arenas:dg/end
