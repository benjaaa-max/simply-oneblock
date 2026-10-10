execute if score #r so_ev matches 1 run effect give @s minecraft:minecraft:haste 300 9 true
execute if score #r so_ev matches 2 run effect give @s minecraft:minecraft:regeneration 60 2 true
execute if score #r so_ev matches 3 run effect give @s minecraft:minecraft:strength 60 4 true
execute if score #r so_ev matches 4 run effect give @s minecraft:minecraft:speed 120 1 true
execute if score #r so_ev matches 5 run effect give @s minecraft:minecraft:absorption 180 8 true
execute if score #r so_ev matches ..0 run effect give @s minecraft:haste 300 9 true
execute if score #r so_ev matches 1 run title @s actionbar [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Bendición: Prisa Minera X", "color": "gold", "bold": true}, {"text": " (5 minutos)", "color": "gray"}]
execute if score #r so_ev matches 2 run title @s actionbar [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Bendición: Regeneración III", "color": "light_purple", "bold": true}, {"text": " (60 segundos)", "color": "gray"}]
execute if score #r so_ev matches 3 run title @s actionbar [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Bendición: Fuerza V", "color": "red", "bold": true}, {"text": " (60 segundos)", "color": "gray"}]
execute if score #r so_ev matches 4 run title @s actionbar [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Bendición: Velocidad II", "color": "aqua", "bold": true}, {"text": " (2 minutos)", "color": "gray"}]
execute if score #r so_ev matches 5 run title @s actionbar [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Bendición: Absorción IX", "color": "yellow", "bold": true}, {"text": " (3 minutos)", "color": "gray"}]
execute if score #r so_ev matches ..0 run title @s actionbar [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Bendición: Prisa Minera X", "color": "gold", "bold": true}, {"text": " (5 minutos)", "color": "gray"}]
playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.6
particle minecraft:end_rod ~ ~1 ~ 0.4 0.6 0.4 0.03 20
