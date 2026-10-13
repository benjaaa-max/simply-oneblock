scoreboard players add #t so_ev 1
execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in
execute store result bossbar so_events:ev value run scoreboard players get #t so_ev
scoreboard players operation #m so_ev = #t so_ev
scoreboard players operation #m so_ev %= #two so_ev
execute if score #m so_ev matches 0 as @a[tag=so_ev_in] at @s run loot spawn ~ ~1 ~ loot so_events:gold_fever
execute if score #m so_ev matches 0 as @a[tag=so_ev_in] at @s run particle minecraft:happy_villager ~ ~2 ~ 1 0.5 1 0 8
execute as @a[tag=so_ev_in] at @s run particle minecraft:end_rod ~ ~1.5 ~ 0.6 0.4 0.6 0.01 3
execute if score #t so_ev matches 60.. run function so_events:event/gold/end
