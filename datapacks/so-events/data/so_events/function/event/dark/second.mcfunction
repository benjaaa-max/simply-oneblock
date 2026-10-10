scoreboard players add #t so_ev 1
execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in
execute store result bossbar so_events:ev value run scoreboard players get #t so_ev
effect give @a[tag=so_ev_in] minecraft:darkness 3 0 true
scoreboard players operation #m so_ev = #t so_ev
scoreboard players operation #m so_ev %= #twenty so_ev
execute if score #m so_ev matches 1 if score #t so_ev matches ..80 run function so_events:event/dark/spawn
execute if score #t so_ev matches 81 run function so_events:event/dark/final
execute if score #t so_ev matches 90.. run function so_events:event/dark/end
