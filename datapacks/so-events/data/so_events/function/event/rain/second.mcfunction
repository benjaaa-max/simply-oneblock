scoreboard players add #t so_ev 1
execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in
execute store result bossbar so_events:ev value run scoreboard players get #t so_ev
execute store result score #r so_ev run random value 1..3
execute if score #r so_ev matches 1 as @a[tag=so_ev_in] at @s run loot spawn ~ ~4 ~ loot so_events:rain
execute as @a[tag=so_ev_in] at @s run particle minecraft:happy_villager ~ ~3 ~ 2 1 2 0 10
execute if score #t so_ev matches 60.. run function so_events:lib/cleanup
