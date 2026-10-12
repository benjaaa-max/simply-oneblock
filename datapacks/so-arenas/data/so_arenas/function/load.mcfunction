scoreboard objectives add so_ar dummy
scoreboard objectives add arena trigger
scoreboard objectives add volver trigger
scoreboard objectives add arena_pr trigger
scoreboard objectives add arena_con trigger
scoreboard objectives add levelrank trigger
scoreboard objectives add arena_dj trigger
scoreboard objectives add arena_mut trigger
scoreboard objectives add arena_ver trigger
scoreboard objectives add arena_pvp trigger
scoreboard objectives add arena_dg trigger
scoreboard objectives add so_ar_air dummy
scoreboard objectives add so_ar_rank dummy
scoreboard objectives add so_ar_x dummy
scoreboard objectives add so_ar_y dummy
scoreboard objectives add so_ar_z dummy
scoreboard objectives add so_ar_saved dummy
scoreboard objectives add so_ar_streak dummy
scoreboard objectives add so_ar_hp dummy
scoreboard objectives add so_ar_death deathCount
execute unless score #enabled so_ar matches 0..1 run scoreboard players set #enabled so_ar 1
execute unless score #mode so_ar matches 0..10 run scoreboard players set #mode so_ar 0
execute unless score #exit so_ar matches 0..1 run scoreboard players set #exit so_ar 0
execute unless score #mut_n so_ar matches 0..1 run scoreboard players set #mut_n so_ar 0
execute unless score #mut_f so_ar matches 0..1 run scoreboard players set #mut_f so_ar 0
execute unless score #mut_v so_ar matches 0..1 run scoreboard players set #mut_v so_ar 0
execute unless score #playing so_ar matches 0..1 run scoreboard players set #playing so_ar 0
execute unless score #song so_ar matches 0..16 run scoreboard players set #song so_ar 0
execute unless score #dg so_ar matches 0..3 run scoreboard players set #dg so_ar 0
scoreboard players set #beat so_ar 0
scoreboard players set #two so_ar 2
scoreboard players set #three so_ar 3
scoreboard players set #six so_ar 6
scoreboard players set #seven so_ar 7
scoreboard players set #ten so_ar 10
scoreboard players set #fifteen so_ar 15
scoreboard players set #twentyfive so_ar 25
scoreboard players set #anticamp so_ar 1
bossbar add so_arenas:fight {"text": "Coliseo"}
bossbar set so_arenas:fight max 100
bossbar set so_arenas:fight visible false
bossbar add so_arenas:dg {"text": "Catacumbas"}
bossbar set so_arenas:dg color purple
bossbar set so_arenas:dg visible false
tellraw @a[tag=oneblock_admin] [{"text": "[SO Arenas] ", "color": "gold"}, {"text": "v4 cargado. Ayuda: /function so_arenas:admin/help", "color": "gray"}]
