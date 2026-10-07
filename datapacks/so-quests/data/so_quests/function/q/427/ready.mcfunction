scoreboard players set @s sqs_427 1
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "¡Misión lista para reclamar! ", "color": "green"}, {"text": "Los pájaros y las abejas", "color": "white"}, {"text": " [Abrir]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_view set 427"}}]
title @s actionbar {text:"¡Misión lista para reclamar!",color:"green"}
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.7 1.6
