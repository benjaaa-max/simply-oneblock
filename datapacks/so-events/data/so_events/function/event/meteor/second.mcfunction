scoreboard players add #t so_ev 1
execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in
execute store result bossbar so_events:ev value run scoreboard players get #t so_ev
scoreboard players operation #m so_ev = #t so_ev
scoreboard players operation #m so_ev %= #three so_ev
execute if score #m so_ev matches 0 as @a[tag=so_ev_in,limit=3] at @s run function so_events:event/meteor/burst
execute if score #t so_ev matches 60.. run function so_events:event/meteor/end
