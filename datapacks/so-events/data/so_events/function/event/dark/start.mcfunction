function so_events:lib/begin
scoreboard players set #active so_ev 6
function so_events:lib/no_grief
bossbar set so_events:ev name {"text": "Noche oscura", "color": "dark_purple"}
bossbar set so_events:ev max 90
bossbar set so_events:ev color purple
title @a[tag=so_ev_in] title {"text": "Noche oscura", "color": "dark_purple", "bold": true}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "La oscuridad cubre la plataforma. Sobrevivan 90 segundos.", "color": "dark_purple", "bold": false}]
