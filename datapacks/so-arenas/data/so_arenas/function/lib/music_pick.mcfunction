# Disco puesto en el tocadiscos del túnel > elección por cartel/menú > azar (solo temas épicos).
scoreboard players set #dsc so_ar 0
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_pigstep"}} store success score #dsc so_ar run scoreboard players set #song so_ar 1
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_otherside"}} store success score #dsc so_ar run scoreboard players set #song so_ar 2
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_creator"}} store success score #dsc so_ar run scoreboard players set #song so_ar 3
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_relic"}} store success score #dsc so_ar run scoreboard players set #song so_ar 4
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_precipice"}} store success score #dsc so_ar run scoreboard players set #song so_ar 5
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_strad"}} store success score #dsc so_ar run scoreboard players set #song so_ar 6
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_chirp"}} store success score #dsc so_ar run scoreboard players set #song so_ar 7
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_blocks"}} store success score #dsc so_ar run scoreboard players set #song so_ar 8
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_cat"}} store success score #dsc so_ar run scoreboard players set #song so_ar 9
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_far"}} store success score #dsc so_ar run scoreboard players set #song so_ar 10
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_mall"}} store success score #dsc so_ar run scoreboard players set #song so_ar 11
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_stal"}} store success score #dsc so_ar run scoreboard players set #song so_ar 12
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_ward"}} store success score #dsc so_ar run scoreboard players set #song so_ar 13
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_wait"}} store success score #dsc so_ar run scoreboard players set #song so_ar 14
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_tears"}} store success score #dsc so_ar run scoreboard players set #song so_ar 15
execute if block -5003 96 -4965 minecraft:jukebox{RecordItem:{id:"minecraft:music_disc_lava_chicken"}} store success score #dsc so_ar run scoreboard players set #song so_ar 16
execute if data block -5003 96 -4965 RecordItem if score #dsc so_ar matches 0 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Ese disco no suena en el Coliseo (solo temas de batalla): va otro tema.", "color": "gray", "bold": false}]
execute if data block -5003 96 -4965 RecordItem run function so_arenas:lib/juke_pop
execute unless score #song so_ar matches 1..16 store result score #song so_ar run random value 1..16
