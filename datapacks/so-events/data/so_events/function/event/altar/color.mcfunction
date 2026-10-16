scoreboard players operation #m so_ev = #t so_ev
scoreboard players operation #m so_ev %= #six so_ev
execute if score #m so_ev matches 0 run setblock ~ ~2 ~ minecraft:purple_stained_glass
execute if score #m so_ev matches 1 run setblock ~ ~2 ~ minecraft:magenta_stained_glass
execute if score #m so_ev matches 2 run setblock ~ ~2 ~ minecraft:cyan_stained_glass
execute if score #m so_ev matches 3 run setblock ~ ~2 ~ minecraft:light_blue_stained_glass
execute if score #m so_ev matches 4 run setblock ~ ~2 ~ minecraft:yellow_stained_glass
execute if score #m so_ev matches 5 run setblock ~ ~2 ~ minecraft:white_stained_glass
playsound minecraft:block.amethyst_block.chime master @a ~ ~ ~ 1 1.2
