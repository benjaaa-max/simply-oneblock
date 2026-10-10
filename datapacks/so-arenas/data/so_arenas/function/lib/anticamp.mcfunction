# Anti-camping por altura: 3 s sobre el foso (6 s en defensa) y el viento te baja.
execute as @a[tag=so_ar_in,scores={so_ar_air=6..}] at @s if score #anticamp so_ar matches 1 run summon minecraft:wind_charge ~ ~2 ~
execute as @a[tag=so_ar_in,scores={so_ar_air=6..}] at @s run title @s actionbar {"text": "¡El viento del coliseo te empuja al piso!", "color": "red", "bold": true}
execute as @a[tag=so_ar_in,scores={so_ar_air=6..}] run scoreboard players set @s so_ar_air 0
execute as @a[tag=so_ar_in] at @s if entity @s[y=104..] run scoreboard players add @s so_ar_air 1
execute as @a[tag=so_ar_in] at @s unless entity @s[y=104..] run scoreboard players set @s so_ar_air 0
