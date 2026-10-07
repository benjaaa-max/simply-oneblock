execute if score @s sqs_302 matches 1 run return run dialog show @s so_quests:claim_302
execute if score @s sqs_302 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Rompehuesos: completada y reclamada.", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 3"}}]
execute unless score @s sqs_302 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Rompehuesos: ", "color": "white"}, {"score": {"name": "@s", "objective": "sqp_302"}, "color": "yellow"}, {"text": " / 50", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 3"}}]
playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.5 1
function so_quests:menu/cat_3 with storage so_quests:menu
