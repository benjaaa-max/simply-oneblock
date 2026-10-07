execute unless score @s sqs_414 matches 1 run return fail
execute unless function so_quests:lib/space run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Inventario lleno: libera un espacio y vuelve a reclamar.", "color": "red"}]
execute unless function so_quests:lib/space run dialog show @s so_quests:claim_414
execute unless function so_quests:lib/space run return fail
scoreboard players set @s sqs_414 2
give @s minecraft:emerald 16
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Reclamaste ", "color": "green"}, {"text": "Ojo espía", "color": "white"}, {"text": " → 16 esmeraldas", "color": "gray"}]
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.6 1.2
function so_quests:menu/cat_4 with storage so_quests:menu
