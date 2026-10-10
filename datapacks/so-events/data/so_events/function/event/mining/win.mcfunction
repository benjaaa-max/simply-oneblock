execute as @a[tag=so_ev_in] run loot give @s loot so_events:reward_small
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Desafío superado! Recompensa entregada a los participantes.", "color": "green", "bold": false}]
execute as @a[tag=so_ev_in] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
function so_events:lib/cleanup
