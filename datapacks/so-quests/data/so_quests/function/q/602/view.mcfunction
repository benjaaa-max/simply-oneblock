execute if score @s sqs_602 matches 1 run return run dialog show @s so_quests:claim_602
execute if score @s sqs_602 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Cantera diaria: completada y reclamada.", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 6"}}]
execute unless score @s sqs_602 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Cantera diaria: ", "color": "white"}, {"score": {"name": "@s", "objective": "sqp_602"}, "color": "yellow"}, {"text": " / 128", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 6"}}]
playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.5 1
function so_quests:menu/cat_6 with storage so_quests:menu
