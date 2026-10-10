scoreboard players set #stage so_ev 2
execute if score #type so_ev matches 1 run function so_events:event/invasion/boss_1
execute if score #type so_ev matches 2 run function so_events:event/invasion/boss_2
execute if score #type so_ev matches 3 run function so_events:event/invasion/boss_3
execute if score #type so_ev matches 4 run function so_events:event/invasion/boss_4
execute if score #type so_ev matches 5 run function so_events:event/invasion/boss_5
execute if score #type so_ev matches 6 run function so_events:event/invasion/boss_6
execute if score #type so_ev matches 7 run function so_events:event/invasion/boss_7
execute if score #type so_ev matches 8 run function so_events:event/invasion/boss_8
execute if score #type so_ev matches 9 run function so_events:event/invasion/boss_9
execute if score #type so_ev matches 10 run function so_events:event/invasion/boss_10
execute if score #type so_ev matches 11 run function so_events:event/invasion/boss_11
title @a[tag=so_ev_in] title {"text": "¡JEFE INVASOR!", "color": "dark_red", "bold": true}
