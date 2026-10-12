scoreboard players add #st so_ar 1
execute unless entity @a[tag=so_ar_ready] run return run function so_arenas:lib/stage_cancel
scoreboard players set #left so_ar 30
scoreboard players operation #left so_ar -= #st so_ar
title @a[tag=so_ar_ready] actionbar [{"text": "Tocá la campana · arranca solo en ", "color": "yellow"}, {"score": {"name": "#left", "objective": "so_ar"}, "color": "white", "bold": true}, {"text": " s", "color": "yellow"}]
execute if score #st so_ar matches 30.. run function so_arenas:lib/go_fight
