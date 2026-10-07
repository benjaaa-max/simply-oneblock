execute unless score #done_510 sq_group matches 1 run return fail
execute if score @s sqs_510 matches 2 run return fail
execute unless function so_quests:lib/space run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Inventario lleno: libera un espacio y vuelve a reclamar.", "color": "red"}]
execute unless function so_quests:lib/space run dialog show @s so_quests:claim_510
execute unless function so_quests:lib/space run return fail
scoreboard players set @s sqs_510 2
give @s minecraft:emerald 10
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Reclamaste ", "color": "green"}, {"text": "Minar 300 menas de lapislázuli", "color": "white"}, {"text": " → 10 esmeraldas", "color": "gray"}]
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.6 1.2
function so_quests:menu/cat_5 with storage so_quests:menu
