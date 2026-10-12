tag @s add so_ar_pad
clear @s *[minecraft:custom_data~{so_arena_loan:1b}]
tag @s remove so_ar_loan
tp @s -4998 96 -4936 0 0
playsound minecraft:block.iron_door.open master @s ~ ~ ~ 1 1
tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Saliste por el portón. Tu cofre de recompensa está en el pedestal (podés dejar ahí lo que no quieras).", "color": "green", "bold": false}]
