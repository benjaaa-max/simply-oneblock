scoreboard players add #tries so_ev 1
execute store result score #type so_ev run random value 1..11
scoreboard players set #ok so_ev 1
execute if score #type so_ev matches 3 unless score #blk so_ev matches 2501.. run scoreboard players set #ok so_ev 0
execute if score #type so_ev matches 4 unless score #blk so_ev matches 2501.. run scoreboard players set #ok so_ev 0
execute if score #type so_ev matches 5 unless score #blk so_ev matches 6667.. run scoreboard players set #ok so_ev 0
execute if score #type so_ev matches 6 unless score #blk so_ev matches 10000.. run scoreboard players set #ok so_ev 0
execute if score #type so_ev matches 7 unless score #blk so_ev matches 1500.. run scoreboard players set #ok so_ev 0
execute if score #type so_ev matches 8 unless score #blk so_ev matches 4000.. run scoreboard players set #ok so_ev 0
execute if score #type so_ev matches 9 unless score #blk so_ev matches 5000.. run scoreboard players set #ok so_ev 0
execute if score #type so_ev matches 10 unless score #blk so_ev matches 2501.. run scoreboard players set #ok so_ev 0
execute if score #type so_ev matches 11 unless score #blk so_ev matches 5000.. run scoreboard players set #ok so_ev 0
execute if score #ok so_ev matches 0 if score #tries so_ev matches ..40 run function so_events:event/invasion/pick_try
execute if score #ok so_ev matches 0 run scoreboard players set #type so_ev 1
