execute if score @s sqs_107 matches 1 run return run dialog show @s so_quests:claim_107
execute if score @s sqs_107 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Diez mil: completada y reclamada.", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 1"}}]
execute unless score @s sqs_107 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Diez mil: ", "color": "white"}, {"score": {"name": "#blocks", "objective": "sq"}, "color": "yellow"}, {"text": " / 10000 bloques", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 1"}}]
playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.5 1
function so_quests:menu/cat_1 with storage so_quests:menu
