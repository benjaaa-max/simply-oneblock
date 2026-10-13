execute if score #mimic so_ev matches 0 as @e[tag=so_ev_mimic] at @s run setblock ~ ~ ~ minecraft:air
execute as @e[tag=so_ev_mimic] at @s run particle minecraft:large_smoke ~ ~0.5 ~ 0.3 0.4 0.3 0.02 20
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "El espejismo se desvaneció.", "color": "gray", "bold": false}]
function so_events:lib/cleanup
