scoreboard players set #mode so_ar 0
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Preparación cancelada: nadie quedó en el túnel.", "color": "gray", "bold": false}]
execute as @a[tag=so_ar_zone] run clear @s *[minecraft:custom_data~{so_arena_loan:1b}]
