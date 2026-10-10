# Anti-camping: 3 s por encima del muro del foso y te baja al centro.
execute as @a[tag=so_ar_in] at @s if entity @s[y=101,dy=80] run scoreboard players add @s so_ar_air 1
execute as @a[tag=so_ar_in] at @s unless entity @s[y=101,dy=80] run scoreboard players set @s so_ar_air 0
execute as @a[tag=so_ar_in,scores={so_ar_air=3..}] run title @s actionbar {"text": "¡Nada de campear en las gradas!", "color": "red", "bold": true}
execute as @a[tag=so_ar_in,scores={so_ar_air=3..}] run tp @s -5000 96 -4986
scoreboard players set @a[scores={so_ar_air=3..}] so_ar_air 0
