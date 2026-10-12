# Médica de campaña: cura, alimenta y quita efectos negativos. Gratis.
execute if score #mode so_ar matches 1..8 if entity @s[tag=so_ar_in] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "No puedo atenderte en pleno combate.", "color": "red", "bold": false}]
effect give @s minecraft:instant_health 1 10 true
effect give @s minecraft:saturation 1 20 true
effect clear @s minecraft:poison
effect clear @s minecraft:wither
effect clear @s minecraft:weakness
effect clear @s minecraft:slowness
effect clear @s minecraft:mining_fatigue
effect clear @s minecraft:nausea
effect clear @s minecraft:blindness
effect clear @s minecraft:hunger
effect clear @s minecraft:darkness
effect clear @s minecraft:levitation
effect clear @s minecraft:unluck
playsound minecraft:block.brewing_stand.brew master @s ~ ~ ~ 1 1.2
particle minecraft:heart ~ ~2 ~ 0.4 0.3 0.4 0 6
tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Médica: vida y comida al máximo, efectos negativos fuera. ¡A la arena!", "color": "light_purple", "bold": false}]
