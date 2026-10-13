title @a[tag=so_ev_in] title {"text": "¡Altar satisfecho!", "color": "gold", "bold": true}
execute as @a[tag=so_ev_in] at @s run summon minecraft:lightning_bolt ~ ~ ~ {visual_only:1b}
execute as @a[tag=so_ev_in] run effect give @s minecraft:haste 180 1 true
execute as @a[tag=so_ev_in] run effect give @s minecraft:regeneration 180 1 true
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "El altar premió a la isla: Prisa II y Regeneración II por 3 minutos.", "color": "gold", "bold": false}]
scoreboard players add @a[tag=so_ev_in] so_ev_win 1
scoreboard players add @a[tag=so_ev_in] so_ev_pos 1
function so_events:lib/streak_up
function so_events:lib/cleanup
