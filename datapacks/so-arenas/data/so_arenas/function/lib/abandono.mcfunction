# El jugador huyó en pleno desafío.
function so_arenas:lib/end
title @s title [{"text": "¡ABANDONASTE,", "color": "red", "bold": true}, {"text": " CAGÓN!", "color": "dark_red", "bold": true}]
title @s times 0 60 20
playsound minecraft:entity.villager.no hostile @s ~ ~ ~ 1 0.7
playsound minecraft:ui.toast.challenge_failed master @s ~ ~ ~ 1 0.9
execute positioned -5000 96 -5000 run summon minecraft:wind_charge ~ ~2 ~
execute positioned -5000 96 -5000 as @s run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Ya podés volver a la isla con ", "color": "gray", "bold": false}, {"text": "/trigger volver", "color": "yellow", "bold": true}]
