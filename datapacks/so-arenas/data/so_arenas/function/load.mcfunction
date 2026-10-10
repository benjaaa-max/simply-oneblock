scoreboard objectives add so_ar dummy
scoreboard objectives add arena trigger
scoreboard objectives add volver trigger
scoreboard objectives add arena_pr trigger
scoreboard objectives add arena_con trigger
scoreboard objectives add levelrank trigger
scoreboard objectives add so_ar_air dummy
scoreboard objectives add so_ar_rank dummy
scoreboard objectives add so_ar_x dummy
scoreboard objectives add so_ar_y dummy
scoreboard objectives add so_ar_z dummy
scoreboard objectives add so_ar_saved dummy
execute unless score #enabled so_ar matches 0..1 run scoreboard players set #enabled so_ar 1
execute unless score #mode so_ar matches 0..3 run scoreboard players set #mode so_ar 0
scoreboard players set #beat so_ar 0
scoreboard players set #twentyfive so_ar 25
scoreboard players set #anticamp so_ar 1
bossbar add so_arenas:fight {"text": "Coliseo"}
bossbar set so_arenas:fight max 100
bossbar set so_arenas:fight visible false
tellraw @a[tag=oneblock_admin] [{"text": "[SO Arenas] ", "color": "gold"}, {"text": "v2 cargado. Ayuda: /function so_arenas:admin/help", "color": "gray"}]
