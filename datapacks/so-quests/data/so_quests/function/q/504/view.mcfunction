execute if score #done_504 sq_group matches 1 unless score @s sqs_504 matches 2 run return run dialog show @s so_quests:claim_504
execute if score @s sqs_504 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Minar 5000 de piedra: ya reclamaste tu parte.", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 5"}}]
execute unless score @s sqs_504 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Minar 5000 de piedra: ", "color": "white"}, {"score": {"name": "#g_504", "objective": "sq_group"}, "color": "yellow"}, {"text": " / 5000", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 5"}}]
playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.5 1
function so_quests:menu/cat_5 with storage so_quests:menu
