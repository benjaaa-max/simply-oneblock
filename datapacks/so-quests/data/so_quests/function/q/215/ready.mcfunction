scoreboard players set @s sqs_215 1
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "¡Misión lista para reclamar! ", "color": "green"}, {"text": "Yunque propio", "color": "white"}, {"text": " [Abrir]", "color": "aqua", "click_event": {"action": "run_command", "command": "/trigger quest_view set 215"}}]
title @s actionbar {text:"¡Misión lista para reclamar!",color:"green"}
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.7 1.6
