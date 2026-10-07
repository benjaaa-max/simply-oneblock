execute if score @s sqs_603 matches 2 run return fail
execute store result score @s sq_tmp run clear @s minecraft:cobblestone 0
execute unless score @s sq_tmp matches 32.. run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Te faltan objetos para entregar.", "color": "red"}]
execute unless score @s sq_tmp matches 32.. run dialog show @s so_quests:claim_603
execute unless score @s sq_tmp matches 32.. run return fail
execute unless function so_quests:lib/space run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Inventario lleno: libera un espacio y vuelve a reclamar.", "color": "red"}]
execute unless function so_quests:lib/space run dialog show @s so_quests:claim_603
execute unless function so_quests:lib/space run return fail
clear @s minecraft:cobblestone 32
scoreboard players set @s sqs_603 2
give @s minecraft:emerald 5
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Reclamaste ", "color": "green"}, {"text": "Entrega: 32 adoquines", "color": "white"}, {"text": " → 5 esmeraldas", "color": "gray"}]
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.6 1.2
function so_quests:menu/cat_6 with storage so_quests:menu
