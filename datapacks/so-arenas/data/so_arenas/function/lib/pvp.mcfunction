execute unless entity @s[tag=so_ar_zone] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Los duelos se hacen dentro del Coliseo.", "color": "red", "bold": false}]
execute if score @s arena_pvp matches 2 run return run function so_arenas:mode/pvp/cancel
execute if score #exit so_ar matches 1 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "El foso se está despejando. Esperá unos segundos (o salí por el portón).", "color": "red", "bold": false}]
execute unless score #mode so_ar matches 0 run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Ya hay un desafío en curso. Podés unirte con el botón Unirse.", "color": "red", "bold": false}]
execute if entity @a[tag=so_ar_pvpw,tag=!so_ar_me] unless entity @s[tag=so_ar_pvpw] run return run function so_arenas:mode/pvp/start
execute if entity @s[tag=so_ar_pvpw] run return run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Ya estás esperando rival. Cancelar: /trigger arena_pvp set 2", "color": "gray", "bold": false}]
tag @s add so_ar_pvpw
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true},{"selector":"@s","color":"red"},{"text":" busca un duelo amistoso. ","color":"yellow","bold":false},{"text": "[ACEPTAR]", "color": "green", "click_event": {"action": "run_command", "command": "/trigger arena_pvp set 1"}, "hover_event": {"action": "show_text", "value": "Batirse a duelo (sin perder cosas: termina a los 3 corazones)"}}]
