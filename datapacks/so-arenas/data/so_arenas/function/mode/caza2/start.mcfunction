function so_arenas:lib/enter_con
scoreboard players set #mode so_ar 2
scoreboard players set #t so_ar 0
scoreboard players set #wave so_ar 0
bossbar set so_arenas:fight name {"text": "Oleadas dobles", "color": "aqua"}
bossbar set so_arenas:fight color aqua
bossbar set so_arenas:fight max 3
bossbar set so_arenas:fight value 0
bossbar set so_arenas:fight players @a[tag=so_ar_in]
bossbar set so_arenas:fight visible true
execute as @a[tag=so_ar_in] run title @s title {"text": "¡Oleadas dobles!", "color": "aqua", "bold": true}
tellraw @a [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Contrato: superá 3 oleadas mixtas.", "color": "aqua", "bold": false}]
function so_arenas:mode/caza2/wave
