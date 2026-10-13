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
execute if score #type so_ev matches 12 run function so_events:event/invasion/boss_12
execute if score #type so_ev matches 13 run function so_events:event/invasion/boss_13
execute if score #type so_ev matches 14 run function so_events:event/invasion/boss_14
execute if score #type so_ev matches 15 run function so_events:event/invasion/boss_15
execute if score #type so_ev matches 16 run function so_events:event/invasion/boss_16
execute if score #type so_ev matches 17 run function so_events:event/invasion/boss_17
execute if score #type so_ev matches 18 run function so_events:event/invasion/boss_18
execute if score #type so_ev matches 19 run function so_events:event/invasion/boss_19
execute if score #type so_ev matches 20 run function so_events:event/invasion/boss_20
function so_events:lib/tier_up
# Versión alfa: jefe con aura, refuerzos de la primera oleada y anuncio especial.
execute if score #alpha so_ev matches 1 if score #type so_ev matches 1 run function so_events:event/invasion/w_1_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 2 run function so_events:event/invasion/w_2_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 3 run function so_events:event/invasion/w_3_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 4 run function so_events:event/invasion/w_4_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 5 run function so_events:event/invasion/w_5_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 6 run function so_events:event/invasion/w_6_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 7 run function so_events:event/invasion/w_7_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 8 run function so_events:event/invasion/w_8_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 9 run function so_events:event/invasion/w_9_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 10 run function so_events:event/invasion/w_10_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 11 run function so_events:event/invasion/w_11_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 12 run function so_events:event/invasion/w_12_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 13 run function so_events:event/invasion/w_13_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 14 run function so_events:event/invasion/w_14_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 15 run function so_events:event/invasion/w_15_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 16 run function so_events:event/invasion/w_16_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 17 run function so_events:event/invasion/w_17_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 18 run function so_events:event/invasion/w_18_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 19 run function so_events:event/invasion/w_19_1
execute if score #alpha so_ev matches 1 if score #type so_ev matches 20 run function so_events:event/invasion/w_20_1
execute if score #alpha so_ev matches 1 run function so_events:lib/tier_up
execute if score #alpha so_ev matches 1 as @e[tag=so_ev_boss] run effect give @s minecraft:resistance infinite 1 true
execute if score #alpha so_ev matches 1 as @e[tag=so_ev_boss] run effect give @s minecraft:strength infinite 0 true
execute if score #alpha so_ev matches 1 run title @a[tag=so_ev_in] title {"text": "¡JEFE ALFA!", "color": "dark_purple", "bold": true}
execute if score #alpha so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Es una invasión ALFA! El jefe viene con aura y refuerzos; la recompensa es mucho mayor.", "color": "dark_purple", "bold": true}]
execute unless score #alpha so_ev matches 1 run title @a[tag=so_ev_in] title {"text": "¡JEFE INVASOR!", "color": "dark_red", "bold": true}
