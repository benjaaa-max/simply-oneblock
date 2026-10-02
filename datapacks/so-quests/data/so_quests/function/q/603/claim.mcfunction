execute if score @s sqs_603 matches 2 run return fail
execute store result score @s sq_tmp run clear @s minecraft:cobblestone 0
execute unless score @s sq_tmp matches 32.. run return run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Te faltan objetos para entregar.", "color": "red"}]
execute unless function so_quests:lib/space run return run tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Inventario lleno: libera un espacio y vuelve a reclamar.", "color": "red"}]
clear @s minecraft:cobblestone 32
scoreboard players set @s sqs_603 2
give @s minecraft:emerald 5
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Reclamaste ", "color": "green"}, {"text": "Entrega: 32 adoquines", "color": "white"}, {"text": " → 5 esmeraldas", "color": "gray"}]
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.6 1.2
