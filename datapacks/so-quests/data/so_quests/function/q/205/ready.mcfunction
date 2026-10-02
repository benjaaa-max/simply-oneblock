scoreboard players set @s sqs_205 1
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "¡Misión lista para reclamar! ", "color": "green"}, {"text": "Fiebre del oro", "color": "white"}, {"text": " [Abrir]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_view set 205"}}]
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.7 1.6
