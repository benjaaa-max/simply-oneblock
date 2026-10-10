function so_arenas:lib/end
scoreboard players set #enabled so_ar 0
tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Arena desactivada.", "color": "red", "bold": false}]
