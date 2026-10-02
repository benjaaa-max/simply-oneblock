execute unless score @s sqs_414 matches 1 run return fail
execute unless function so_quests:lib/space run return run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Inventario lleno: libera un espacio y vuelve a reclamar.", "color": "red"}]
scoreboard players set @s sqs_414 2
give @s minecraft:emerald 16
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Reclamaste ", "color": "green"}, {"text": "Ojo espía", "color": "white"}, {"text": " → 16 emerald", "color": "gray"}]
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.6 1.2
