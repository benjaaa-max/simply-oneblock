scoreboard players add #t so_ev 1
execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in
scoreboard players operation #prog so_ev = #blk so_ev
scoreboard players operation #prog so_ev -= #start so_ev
execute store result bossbar so_events:ev value run scoreboard players get #prog so_ev
bossbar set so_events:ev players @a[tag=so_ev_in]
execute if score #prog so_ev >= #mine_goal so_ev run function so_events:event/mining/win
execute if score #active so_ev matches 3 if score #t so_ev matches 180.. run function so_events:event/mining/fail
