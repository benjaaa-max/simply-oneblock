scoreboard players add @a[tag=so_ev_in] so_ev_win 1
scoreboard players add @a[tag=so_ev_in] so_ev_pos 1
function so_events:lib/streak_up
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "La fiebre del oro se calmó.", "color": "gold", "bold": false}]
function so_events:lib/cleanup
