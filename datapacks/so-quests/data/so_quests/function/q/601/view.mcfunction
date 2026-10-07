execute if score @s sqs_601 matches 1 run return run dialog show @s so_quests:claim_601
execute if score @s sqs_601 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Patrulla diaria: completada y reclamada.", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 6"}}]
execute unless score @s sqs_601 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Patrulla diaria: ", "color": "white"}, {"score": {"name": "@s", "objective": "sqp_601"}, "color": "yellow"}, {"text": " / 20", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 6"}}]
playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.5 1
function so_quests:menu/cat_6 with storage so_quests:menu
