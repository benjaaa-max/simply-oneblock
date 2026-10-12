# Huyó en pleno desafío: pierde recompensa, kit y racha. El resto sigue peleando.
title @s times 0 60 20
title @s title [{"text": "¡ABANDONASTE,", "color": "red", "bold": true}, {"text": " CAGÓN!", "color": "dark_red", "bold": true}]
playsound minecraft:entity.villager.no master @s ~ ~ ~ 1 0.7
scoreboard players set @s so_ar_streak 0
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Un gladiador abandonó el desafío.", "color": "red", "bold": false}]
