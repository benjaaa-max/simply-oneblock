title @a[tag=so_ev_in] title {"text": "¡Altar satisfecho!", "color": "gold", "bold": true}
execute as @a[tag=so_ev_in] at @s run summon minecraft:lightning_bolt ~ ~ ~ {visual_only:1b}
execute as @a[tag=so_ev_in] run effect give @s minecraft:haste 180 1 true
execute as @a[tag=so_ev_in] run effect give @s minecraft:regeneration 180 1 true
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "El altar premió a la isla: Prisa II y Regeneración II por 3 minutos.", "color": "gold", "bold": false}]
function so_events:lib/cleanup
