# Fin de desafío: limpia mobs, núcleo, barra y kits; a los 3 s devuelve el foso al lobby.
tp @e[tag=so_ar_mob] -5000 -300 -5000
kill @e[tag=so_ar_mob]
setblock -5000 96 -5000 minecraft:air
bossbar set so_arenas:fight visible false
scoreboard players set #mode so_ar 0
scoreboard players set #wave so_ar 0
scoreboard players set #t so_ar 0
scoreboard players set #anticamp so_ar 1
scoreboard players reset @a so_ar_air
schedule function so_arenas:lib/to_lobby 60t
