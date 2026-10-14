tag @s add so_cr_in
execute unless entity @s[tag=oneblock_admin] if entity @s[gamemode=survival] run tag @s add so_cr_gm
execute unless entity @s[tag=oneblock_admin] run gamemode adventure @s
title @s actionbar {"text":"✦ Templo de las Bóvedas ✦","color":"light_purple"}
execute if entity @s[tag=oneblock_admin,gamemode=!adventure] run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"⚠ Estás en el templo. ","color":"yellow"},{"text":"[Pasar a Aventura]","color":"green","underlined":true,"click_event":{"action":"run_command","command":"/gamemode adventure"},"hover_event":{"action":"show_text","value":"Clic para cambiar a modo aventura"}}]
