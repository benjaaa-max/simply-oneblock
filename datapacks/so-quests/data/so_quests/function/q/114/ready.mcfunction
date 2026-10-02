scoreboard players set @s sqs_114 1
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "¡Misión lista para reclamar! ", "color": "green"}, {"text": "El buzo del abismo", "color": "white"}, {"text": " [Abrir]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_view set 114"}}]
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.7 1.6
