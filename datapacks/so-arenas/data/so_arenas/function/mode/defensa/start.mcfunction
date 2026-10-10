setblock -5000 96 -5000 minecraft:crying_obsidian
scoreboard players set #mode so_ar 3
scoreboard players set #hp so_ar 100
scoreboard players set #anticamp so_ar 0
bossbar set so_arenas:fight color purple
bossbar set so_arenas:fight max 100
bossbar set so_arenas:fight value 100
bossbar set so_arenas:fight name {"text": "Núcleo", "color": "dark_purple"}
title @a[tag=so_ar_in] title {"text": "¡Defiendan el Núcleo!", "color": "dark_purple", "bold": true}
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Contrato: protegé el Núcleo (obsidiana llorosa del centro) 2 minutos. Acá la altura está permitida.", "color": "dark_purple", "bold": false}]
function so_arenas:mode/defensa/wave
