scoreboard objectives add so_crates dummy
scoreboard objectives add crates trigger
scoreboard objectives add isla trigger
scoreboard objectives add so_cr_x dummy
scoreboard objectives add so_cr_y dummy
scoreboard objectives add so_cr_z dummy
scoreboard objectives add so_cr_saved dummy
execute unless score #enabled so_crates matches 0..1 run scoreboard players set #enabled so_crates 1
tellraw @a[tag=oneblock_admin] [{"text":"[SO Crates v2.0] ","color":"gold"},{"text":"cargado. Ayuda: /function so_crates:admin/help","color":"gray"}]
