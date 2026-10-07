execute if score @s sqs_603 matches 2 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Entrega: 32 adoquines: ya entregada hoy.", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 6"}}]
execute unless score @s sqs_603 matches 2 run execute store result score @s sq_tmp run clear @s minecraft:cobblestone 0
execute unless score @s sqs_603 matches 2 run execute if score @s sq_tmp matches 32.. run return run dialog show @s so_quests:claim_603
execute if score @s sqs_603 matches 0 run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Entrega: 32 adoquines: tienes ", "color": "white"}, {"score": {"name": "@s", "objective": "sq_tmp"}, "color": "yellow"}, {"text": " / 32", "color": "gray"}, {"text": " [Volver]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_menu set 6"}}]
playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.5 1
function so_quests:menu/cat_6 with storage so_quests:menu
