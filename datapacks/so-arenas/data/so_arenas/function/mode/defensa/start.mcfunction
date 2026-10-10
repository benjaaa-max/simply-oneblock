function so_arenas:lib/enter_con
setblock -5000 96 -5000 minecraft:crying_obsidian
scoreboard players set #mode so_ar 3
scoreboard players set #t so_ar 0
scoreboard players set #wave so_ar 0
scoreboard players set #hp so_ar 100
scoreboard players set #anticamp so_ar 0
bossbar set so_arenas:fight color purple
bossbar set so_arenas:fight max 100
bossbar set so_arenas:fight value 100
bossbar set so_arenas:fight players @a[tag=so_ar_in]
bossbar set so_arenas:fight visible true
execute as @a[tag=so_ar_in] run title @s title {"text": "¡Defendan el Núcleo!", "color": "dark_purple", "bold": true}
tellraw @a [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Contrato: protegí el Núcleo 2 minutos. Aquí sí se puede usar la altura.", "color": "dark_purple", "bold": false}]
function so_arenas:mode/defensa/wave
