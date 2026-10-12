scoreboard players set #mode so_ar 7
bossbar set so_arenas:fight name {"text": "Asedio Volador", "color": "aqua"}
bossbar set so_arenas:fight color blue
bossbar set so_arenas:fight max 3
bossbar set so_arenas:fight value 0
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Contrato: el cielo ataca. 3 oleadas de phantoms y vexes. ¡Arco, ballesta y escudo!", "color": "aqua", "bold": false}]
function so_arenas:mode/asedio/wave
