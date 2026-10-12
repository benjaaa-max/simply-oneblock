clear @a *[minecraft:custom_data~{so_ar_dgkey:1b}]
fill -4984 60 -5041 -4984 63 -5039 minecraft:air replace minecraft:iron_bars
scoreboard players set #dgs so_ar 7
playsound minecraft:block.iron_door.open master @a[tag=so_ar_dgp] -4984 61 -5040 2 0.5
particle minecraft:wax_on -4984 61.5 -5040 0.3 1 1 0 30 force
tellraw @a[tag=so_ar_dgp] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "La llave giró. Más allá espera Caballero No-Muerto...", "color": "red", "bold": false}]
