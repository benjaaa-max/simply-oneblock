stopsound @a[tag=so_ar_zone] record
scoreboard players set #mt so_ar 0
scoreboard players set #playing so_ar 1
execute as @a[tag=so_ar_zone,tag=!so_ar_dgp] run function so_arenas:lib/music_one
execute if score #song so_ar matches 1 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Pigstep", "color": "light_purple"}
execute if score #song so_ar matches 2 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Otherside", "color": "light_purple"}
execute if score #song so_ar matches 3 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Creator", "color": "light_purple"}
execute if score #song so_ar matches 4 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Relic", "color": "light_purple"}
execute if score #song so_ar matches 5 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Precipice", "color": "light_purple"}
execute if score #song so_ar matches 6 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Strad", "color": "light_purple"}
execute if score #song so_ar matches 7 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Chirp", "color": "light_purple"}
execute if score #song so_ar matches 8 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Blocks", "color": "light_purple"}
execute if score #song so_ar matches 9 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Cat", "color": "light_purple"}
execute if score #song so_ar matches 10 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Far", "color": "light_purple"}
execute if score #song so_ar matches 11 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Mall", "color": "light_purple"}
execute if score #song so_ar matches 12 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Stal", "color": "light_purple"}
execute if score #song so_ar matches 13 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Ward", "color": "light_purple"}
execute if score #song so_ar matches 14 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Wait", "color": "light_purple"}
execute if score #song so_ar matches 15 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Tears", "color": "light_purple"}
execute if score #song so_ar matches 16 run title @a[tag=so_ar_zone] actionbar {"text": "♪ Suena: Lava Chicken", "color": "light_purple"}
