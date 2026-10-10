scoreboard players operation #next so_ev = #blk so_ev
scoreboard players operation #next so_ev += #every so_ev
scoreboard players set #n so_ev 0
execute positioned 0 64 0 store result score #n so_ev if entity @a[distance=..64,gamemode=!spectator]
# Sin nadie en la isla: se pospone un poco.
execute if score #n so_ev matches 0 run scoreboard players operation #next so_ev = #blk so_ev
execute if score #n so_ev matches 0 run scoreboard players add #next so_ev 50
execute if score #n so_ev matches 0 run return 0
execute store result score #r so_ev run random value 1..9
# Noche oscura solo desde la fase 5 (1668 bloques).
execute if score #r so_ev matches 6 if score #blk so_ev matches ..1667 run scoreboard players set #r so_ev 1
execute if score #r so_ev matches 1 run function so_events:event/rain/start
execute if score #r so_ev matches 2 run function so_events:event/supply/start
execute if score #r so_ev matches 3 run function so_events:event/mining/start
execute if score #r so_ev matches 4 run function so_events:event/trader/start
execute if score #r so_ev matches 5 run function so_events:event/invasion/start
execute if score #r so_ev matches 6 run function so_events:event/dark/start
execute if score #r so_ev matches 7 run function so_events:event/runner/start
execute if score #r so_ev matches 8 run function so_events:event/mana/start
execute if score #r so_ev matches 9 run function so_events:event/altar/start
