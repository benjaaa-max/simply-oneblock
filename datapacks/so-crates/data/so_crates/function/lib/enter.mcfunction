tag @s add so_cr_in
execute unless entity @s[tag=oneblock_admin] if entity @s[gamemode=survival] run tag @s add so_cr_gm
execute unless entity @s[tag=oneblock_admin] run gamemode adventure @s
title @s actionbar {"text":"✦ Zona de Crates ✦","color":"gold"}
execute if entity @s[tag=oneblock_admin,gamemode=!adventure] run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"⚠ Estás en la zona de Crates. ","color":"yellow"},{"text":"[Pasar a Aventura]","color":"green","underlined":true,"click_event":{"action":"run_command","command":"/gamemode adventure"},"hover_event":{"action":"show_text","value":"Clic para cambiar a modo aventura"}}]
execute if entity @s[tag=oneblock_admin,gamemode=!adventure] at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 0.6 1.2
