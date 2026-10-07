execute if score @s sqs_212 matches 1 run return run dialog show @s so_quests:claim_212
execute if score @s sqs_212 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Pico de diamante: completada y reclamada.", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 2"}}]
execute unless score @s sqs_212 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Pico de diamante: ", "color": "white"}, {"score": {"name": "@s", "objective": "sqp_212"}, "color": "yellow"}, {"text": " / 1", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 2"}}]
playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.5 1
function so_quests:menu/cat_2 with storage so_quests:menu
