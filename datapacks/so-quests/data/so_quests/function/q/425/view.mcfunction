execute if score @s sqs_425 matches 1 run return run dialog show @s so_quests:claim_425
execute if score @s sqs_425 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Más allá de la tumba: completada y reclamada.", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 4"}}]
execute unless score @s sqs_425 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Más allá de la tumba: ", "color": "white"}, {"text": "pendiente", "color": "yellow"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 4"}}]
playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.5 1
function so_quests:menu/cat_4 with storage so_quests:menu
