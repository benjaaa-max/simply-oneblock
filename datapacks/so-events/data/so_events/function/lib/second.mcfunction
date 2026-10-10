function so_events:lib/blocks
execute unless score #next so_ev matches 1.. run scoreboard players operation #next so_ev = #blk so_ev
execute unless score #next so_ev matches 1.. run scoreboard players operation #next so_ev += #every so_ev
execute if score #next so_ev < #min so_ev run scoreboard players operation #next so_ev = #min so_ev
execute if score #enabled so_ev matches 1 if score #auto so_ev matches 1 if score #active so_ev matches 0 if score #blk so_ev >= #next so_ev run function so_events:lib/auto
execute if score #active so_ev matches 1 run function so_events:event/rain/second
execute if score #active so_ev matches 3 run function so_events:event/mining/second
execute if score #active so_ev matches 4 run function so_events:event/trader/second
execute if score #active so_ev matches 5 run function so_events:event/invasion/second
execute if score #active so_ev matches 6 run function so_events:event/dark/second
execute if entity @e[tag=so_ev_boss,limit=1] store result bossbar so_events:boss value run data get entity @e[tag=so_ev_boss,limit=1] Health
execute unless entity @e[tag=so_ev_boss,limit=1] run bossbar set so_events:boss visible false
