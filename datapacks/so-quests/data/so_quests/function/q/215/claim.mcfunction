execute unless score @s sqs_215 matches 1 run return fail
execute unless function so_quests:lib/space run return run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Inventario lleno: libera un espacio y vuelve a reclamar.", "color": "red"}]
scoreboard players set @s sqs_215 2
give @s minecraft:emerald 8
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Reclamaste ", "color": "green"}, {"text": "Yunque propio", "color": "white"}, {"text": " → 8 emerald", "color": "gray"}]
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.6 1.2
