function so_events:lib/begin
scoreboard players set #active so_ev 8
bossbar set so_events:ev name {"text": "Tormenta de maná", "color": "aqua"}
bossbar set so_events:ev max 45
bossbar set so_events:ev color blue
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Tormenta de maná! Corran: los orbes de experiencia caen por 45 segundos.", "color": "aqua", "bold": false}]
