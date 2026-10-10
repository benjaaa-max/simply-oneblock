scoreboard objectives add so_ar dummy
scoreboard objectives add arena trigger
scoreboard objectives add arena_pr trigger
scoreboard objectives add arena_con trigger
scoreboard objectives add levelrank trigger
scoreboard objectives add so_ar_air dummy
scoreboard objectives add so_ar_rank dummy
execute unless score #enabled so_ar matches 0..1 run scoreboard players set #enabled so_ar 1
execute unless score #mode so_ar matches 0..4 run scoreboard players set #mode so_ar 0
execute unless score #beat so_ar matches 0.. run scoreboard players set #beat so_ar 0
bossbar add so_arenas:fight {"text": "Coliseo"}
bossbar set so_arenas:fight color red
bossbar set so_arenas:fight max 100
bossbar set so_arenas:fight visible false
tellraw @a[tag=oneblock_admin] [{"text": "[SO Arenas] ", "color": "gold"}, {"text": "cargado. Ayuda: /function so_arenas:admin/help", "color": "gray"}]
scoreboard players set #twentyfive so_ar 25
function so_arenas:load2
