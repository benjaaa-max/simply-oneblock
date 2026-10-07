execute if score @s sqs_306 matches 1 run return run dialog show @s so_quests:claim_306
execute if score @s sqs_306 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Bomberos: completada y reclamada.", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 3"}}]
execute unless score @s sqs_306 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Bomberos: ", "color": "white"}, {"score": {"name": "@s", "objective": "sqp_306"}, "color": "yellow"}, {"text": " / 10", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 3"}}]
playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.5 1
function so_quests:menu/cat_3 with storage so_quests:menu
