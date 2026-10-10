scoreboard players add #t so_ev 1
execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in
bossbar set so_events:ev players @a[tag=so_ev_in]
execute if score #stage so_ev matches 0 run function so_events:event/invasion/countdown
execute if score #stage so_ev matches 1 run function so_events:event/invasion/waves
execute if score #stage so_ev matches 2 unless entity @e[tag=so_ev_boss] run function so_events:event/invasion/win
execute if score #active so_ev matches 5 if score #t so_ev matches 420.. run function so_events:event/invasion/fail
execute if score #active so_ev matches 5 unless entity @a[tag=so_ev_in] run function so_events:event/invasion/fail
