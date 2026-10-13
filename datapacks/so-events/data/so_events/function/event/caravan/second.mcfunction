scoreboard players add #t so_ev 1
execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in
execute store result bossbar so_events:ev value run scoreboard players get #t so_ev
execute store result score #llamas so_ev if entity @e[tag=so_ev_llama]
execute if score #t so_ev matches 15 run function so_events:event/caravan/wave
execute if score #t so_ev matches 45 run function so_events:event/caravan/wave
execute if score #t so_ev matches 75 run function so_events:event/caravan/wave
execute if score #t so_ev matches 90 run function so_events:event/caravan/boss
# Los saqueadores lastiman a la llama más cercana cada 5 s.
scoreboard players operation #m so_ev = #t so_ev
scoreboard players operation #m so_ev %= #five so_ev
execute if score #m so_ev matches 0 as @e[tag=so_ev_mob,tag=!so_ev_llama] at @s if entity @e[tag=so_ev_llama,distance=..16] run damage @e[tag=so_ev_llama,limit=1,sort=nearest] 2 minecraft:mob_attack by @s
execute if score #llamas so_ev matches 0 run function so_events:event/caravan/fail
# Victoria a los 120 s, pero solo si el caudillo ya cayó.
execute if score #t so_ev matches 120.. unless entity @e[tag=so_ev_boss] run function so_events:event/caravan/win
# Si el caudillo se resiste demasiado, la caravana se rinde a los 240 s.
execute if score #t so_ev matches 240.. run function so_events:event/caravan/fail
