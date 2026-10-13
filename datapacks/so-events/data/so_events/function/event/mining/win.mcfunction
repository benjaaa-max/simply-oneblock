execute as @a[tag=so_ev_in] run loot give @s loot so_events:reward_small
scoreboard players add @a[tag=so_ev_in] so_ev_win 1
scoreboard players add @a[tag=so_ev_in] so_ev_pos 1
function so_events:lib/streak_up
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Desafío superado! Recompensa entregada a los participantes.", "color": "green", "bold": false}]
execute as @a[tag=so_ev_in] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
function so_events:lib/cleanup
