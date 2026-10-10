# Huyó en pleno desafío: pierde recompensa y kit. El resto sigue peleando.
title @s title [{"text": "¡ABANDONASTE,", "color": "red", "bold": true}, {"text": " CAGÓN!", "color": "dark_red", "bold": true}]
title @s times 0 60 20
playsound minecraft:entity.villager.no master @s ~ ~ ~ 1 0.7
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Un gladiador abandonó el desafío.", "color": "red", "bold": false}]
