function so_events:lib/begin
scoreboard players set #active so_ev 14
function so_events:lib/no_grief
bossbar set so_events:ev name {"text": "Eclipse", "color": "dark_purple", "bold": true}
bossbar set so_events:ev max 90
bossbar set so_events:ev color purple
title @a[tag=so_ev_in] title {"text": "¡ECLIPSE!", "color": "dark_purple", "bold": true}
title @a[tag=so_ev_in] subtitle {"text": "Sobreviví 90 segundos a la élite", "color": "light_purple"}
execute as @a[tag=so_ev_in] at @s run playsound minecraft:entity.wither.spawn hostile @s ~ ~ ~ 0.8 0.6
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Un eclipse cubre la isla. Jinetes y enemigos de élite cada 15 s: sobrevivan 90 segundos por un botín legendario.", "color": "dark_purple", "bold": false}]
