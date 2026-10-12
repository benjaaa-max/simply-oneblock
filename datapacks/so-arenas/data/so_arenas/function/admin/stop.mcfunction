function so_arenas:lib/music_stop
tag @a remove so_ar_pvp
function so_arenas:lib/end_fight
function so_arenas:lib/close_pit
tellraw @a [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Desafío del coliseo detenido por un administrador.", "color": "gray", "bold": false}]
