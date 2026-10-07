execute unless score @s sqs_105 matches 1 run return fail
execute unless function so_quests:lib/space run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Inventario lleno: libera un espacio y vuelve a reclamar.", "color": "red"}]
execute unless function so_quests:lib/space run dialog show @s so_quests:claim_105
execute unless function so_quests:lib/space run return fail
scoreboard players set @s sqs_105 2
give @s minecraft:emerald 24
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Reclamaste ", "color": "green"}, {"text": "Cinco mil", "color": "white"}, {"text": " → 24 esmeraldas", "color": "gray"}]
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.6 1.2
function so_quests:menu/cat_1 with storage so_quests:menu
