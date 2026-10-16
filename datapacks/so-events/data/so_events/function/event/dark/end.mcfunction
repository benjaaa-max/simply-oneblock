execute as @a[tag=so_ev_in] at @s run function so_events:lib/chest {t:"reward_small"}
scoreboard players add @a[tag=so_ev_in] so_ev_win 1
scoreboard players add @a[tag=so_ev_in] so_ev_inv 1
function so_events:lib/streak_up
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Amaneció. Los sobrevivientes recibieron una recompensa.", "color": "green", "bold": false}]
function so_events:lib/cleanup
