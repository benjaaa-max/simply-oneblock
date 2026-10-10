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
execute if score #wave so_ev matches 1 if score #type so_ev matches 12 run function so_events:event/invasion/w_12_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 12 run function so_events:event/invasion/w_12_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 12 run function so_events:event/invasion/w_12_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 13 run function so_events:event/invasion/w_13_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 13 run function so_events:event/invasion/w_13_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 13 run function so_events:event/invasion/w_13_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 14 run function so_events:event/invasion/w_14_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 14 run function so_events:event/invasion/w_14_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 14 run function so_events:event/invasion/w_14_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 15 run function so_events:event/invasion/w_15_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 15 run function so_events:event/invasion/w_15_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 15 run function so_events:event/invasion/w_15_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 16 run function so_events:event/invasion/w_16_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 16 run function so_events:event/invasion/w_16_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 16 run function so_events:event/invasion/w_16_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 17 run function so_events:event/invasion/w_17_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 17 run function so_events:event/invasion/w_17_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 17 run function so_events:event/invasion/w_17_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 18 run function so_events:event/invasion/w_18_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 18 run function so_events:event/invasion/w_18_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 18 run function so_events:event/invasion/w_18_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 19 run function so_events:event/invasion/w_19_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 19 run function so_events:event/invasion/w_19_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 19 run function so_events:event/invasion/w_19_3
execute if score #wave so_ev matches 1 if score #type so_ev matches 20 run function so_events:event/invasion/w_20_1
execute if score #wave so_ev matches 2 if score #type so_ev matches 20 run function so_events:event/invasion/w_20_2
execute if score #wave so_ev matches 3 if score #type so_ev matches 20 run function so_events:event/invasion/w_20_3
# Nivel III: la oleada final suma la primera como refuerzo.
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 1 run function so_events:event/invasion/w_1_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 2 run function so_events:event/invasion/w_2_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 3 run function so_events:event/invasion/w_3_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 4 run function so_events:event/invasion/w_4_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 5 run function so_events:event/invasion/w_5_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 6 run function so_events:event/invasion/w_6_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 7 run function so_events:event/invasion/w_7_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 8 run function so_events:event/invasion/w_8_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 9 run function so_events:event/invasion/w_9_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 10 run function so_events:event/invasion/w_10_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 11 run function so_events:event/invasion/w_11_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 12 run function so_events:event/invasion/w_12_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 13 run function so_events:event/invasion/w_13_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 14 run function so_events:event/invasion/w_14_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 15 run function so_events:event/invasion/w_15_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 16 run function so_events:event/invasion/w_16_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 17 run function so_events:event/invasion/w_17_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 18 run function so_events:event/invasion/w_18_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 19 run function so_events:event/invasion/w_19_1
execute if score #tier so_ev matches 3.. if score #wave so_ev matches 3 if score #type so_ev matches 20 run function so_events:event/invasion/w_20_1
function so_events:lib/tier_up
execute if score #wave so_ev matches 1..3 run title @a[tag=so_ev_in] title [{"text": "Oleada ", "color": "red", "bold": true}, {"score": {"name": "#wave", "objective": "so_ev"}, "color": "white"}]
execute if score #wave so_ev matches 1..3 run playsound minecraft:entity.zombie.ambient hostile @a[tag=so_ev_in] ~ ~ ~ 1 0.7
