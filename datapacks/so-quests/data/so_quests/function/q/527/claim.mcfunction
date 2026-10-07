execute unless score #done_527 sq_group matches 1 run return fail
execute if score @s sqs_527 matches 2 run return fail
execute unless function so_quests:lib/space run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Inventario lleno: libera un espacio y vuelve a reclamar.", "color": "red"}]
execute unless function so_quests:lib/space run dialog show @s so_quests:claim_527
execute unless function so_quests:lib/space run return fail
scoreboard players set @s sqs_527 2
give @s minecraft:emerald 10
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Reclamaste ", "color": "green"}, {"text": "Hornear 500 panes", "color": "white"}, {"text": " → 10 esmeraldas", "color": "gray"}]
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.6 1.2
function so_quests:menu/cat_5 with storage so_quests:menu
