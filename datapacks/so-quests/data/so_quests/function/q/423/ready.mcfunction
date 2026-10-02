scoreboard players set @s sqs_423 1
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "¡Misión lista para reclamar! ", "color": "green"}, {"text": "Cazador de monstruos", "color": "white"}, {"text": " [Abrir]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_view set 423"}}]
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.7 1.6
