execute store result score #len so_ev run data get storage so_events:tmp pool
scoreboard players remove #len so_ev 1
execute if score #len so_ev matches 1.. store result storage so_events:tmp max int 1 run scoreboard players get #len so_ev
execute if score #len so_ev matches 1.. run function so_events:lib/offer_take with storage so_events:tmp
