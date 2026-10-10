scoreboard players set #stage so_ev 1
scoreboard players add #wave so_ev 1
scoreboard players set #wt so_ev 0
bossbar set so_events:ev max 3
execute store result bossbar so_events:ev value run scoreboard players get #wave so_ev
execute if score #wave so_ev matches 4.. run function so_events:event/invasion/boss
execute if score #wave so_ev matches 1 if score #type so_ev matches 1 run function so_events:event/invasion/w_1_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 1 run function so_events:event/invasion/w_1_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 1 run function so_events:event/invasion/w_1_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 2 run function so_events:event/invasion/w_2_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 2 run function so_events:event/invasion/w_2_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 2 run function so_events:event/invasion/w_2_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 3 run function so_events:event/invasion/w_3_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 3 run function so_events:event/invasion/w_3_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 3 run function so_events:event/invasion/w_3_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 4 run function so_events:event/invasion/w_4_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 4 run function so_events:event/invasion/w_4_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 4 run function so_events:event/invasion/w_4_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 5 run function so_events:event/invasion/w_5_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 5 run function so_events:event/invasion/w_5_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 5 run function so_events:event/invasion/w_5_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 6 run function so_events:event/invasion/w_6_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 6 run function so_events:event/invasion/w_6_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 6 run function so_events:event/invasion/w_6_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 7 run function so_events:event/invasion/w_7_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 7 run function so_events:event/invasion/w_7_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 7 run function so_events:event/invasion/w_7_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 8 run function so_events:event/invasion/w_8_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 8 run function so_events:event/invasion/w_8_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 8 run function so_events:event/invasion/w_8_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 9 run function so_events:event/invasion/w_9_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 9 run function so_events:event/invasion/w_9_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 9 run function so_events:event/invasion/w_9_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 10 run function so_events:event/invasion/w_10_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 10 run function so_events:event/invasion/w_10_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 10 run function so_events:event/invasion/w_10_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 11 run function so_events:event/invasion/w_11_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 11 run function so_events:event/invasion/w_11_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 11 run function so_events:event/invasion/w_11_3
execute if score #wave so_ev matches 1..3 run title @a[tag=so_ev_in] title [{"text": "Oleada ", "color": "red", "bold": true}, {"score": {"name": "#wave", "objective": "so_ev"}, "color": "white"}]
execute if score #wave so_ev matches 1..3 run playsound minecraft:entity.zombie.ambient hostile @a[tag=so_ev_in] ~ ~ ~ 1 0.7
