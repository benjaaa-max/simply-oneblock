execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function so_events:lib/spawn {mob:"boss/caudillo_saqueador"}
playsound minecraft:event.raid.horn hostile @a ~ ~ ~ 1 0.8
title @a[tag=so_ev_in] title {"text": "¡El Caudillo Saqueador!", "color": "red", "bold": true}
title @a[tag=so_ev_in] subtitle {"text": "Derrotalo para salvar la caravana", "color": "gray"}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡El Caudillo Saqueador llegó montado en su devastador! Derrotalo para asegurar la caravana.", "color": "red", "bold": false}]
