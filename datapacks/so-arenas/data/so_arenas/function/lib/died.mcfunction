scoreboard players reset @s so_ar_death
execute if score @s so_ar_streak matches 1.. run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Moriste: tu racha de victorias vuelve a 0.", "color": "red", "bold": false}]
scoreboard players set @s so_ar_streak 0
