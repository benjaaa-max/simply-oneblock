execute if score @s sqs_206 matches 1 run return run dialog show @s so_quests:claim_206
execute if score @s sqs_206 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Brillo azul: completada y reclamada.", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 2"}}]
execute unless score @s sqs_206 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Brillo azul: ", "color": "white"}, {"score": {"name": "@s", "objective": "sqp_206"}, "color": "yellow"}, {"text": " / 16", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 2"}}]
playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.5 1
function so_quests:menu/cat_2 with storage so_quests:menu
