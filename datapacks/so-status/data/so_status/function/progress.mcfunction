# Lee progreso global sin escribir el contador de Simply OneBlock.
scoreboard players set #src so_sys 0
execute if score #blocks so_core matches -2147483648.. run scoreboard players set #src so_sys 1
execute if score #src so_sys matches 0 if score fake_player ib_minedcount matches -2147483648.. run scoreboard players set #src so_sys 2
execute if score #src so_sys matches 1 run scoreboard players operation #blk so_sys = #blocks so_core
execute if score #src so_sys matches 2 run scoreboard players operation #blk so_sys = fake_player ib_minedcount
execute if score #src so_sys matches 0 run scoreboard players set #blk so_sys 0
scoreboard players set #phase_idx so_sys 1
scoreboard players set #phase_lo so_sys 0
scoreboard players set #phase_hi so_sys 92
execute if score #blk so_sys matches 0..92 run scoreboard players set #phase_idx so_sys 1
execute if score #blk so_sys matches 0..92 run scoreboard players set #phase_lo so_sys 0
execute if score #blk so_sys matches 0..92 run scoreboard players set #phase_hi so_sys 92
execute if score #blk so_sys matches 93..433 run scoreboard players set #phase_idx so_sys 2
execute if score #blk so_sys matches 93..433 run scoreboard players set #phase_lo so_sys 93
execute if score #blk so_sys matches 93..433 run scoreboard players set #phase_hi so_sys 433
execute if score #blk so_sys matches 434..917 run scoreboard players set #phase_idx so_sys 3
execute if score #blk so_sys matches 434..917 run scoreboard players set #phase_lo so_sys 434
execute if score #blk so_sys matches 434..917 run scoreboard players set #phase_hi so_sys 917
execute if score #blk so_sys matches 918..1667 run scoreboard players set #phase_idx so_sys 4
execute if score #blk so_sys matches 918..1667 run scoreboard players set #phase_lo so_sys 918
execute if score #blk so_sys matches 918..1667 run scoreboard players set #phase_hi so_sys 1667
execute if score #blk so_sys matches 1668..2500 run scoreboard players set #phase_idx so_sys 5
execute if score #blk so_sys matches 1668..2500 run scoreboard players set #phase_lo so_sys 1668
execute if score #blk so_sys matches 1668..2500 run scoreboard players set #phase_hi so_sys 2500
execute if score #blk so_sys matches 2501..3333 run scoreboard players set #phase_idx so_sys 6
execute if score #blk so_sys matches 2501..3333 run scoreboard players set #phase_lo so_sys 2501
execute if score #blk so_sys matches 2501..3333 run scoreboard players set #phase_hi so_sys 3333
execute if score #blk so_sys matches 3334..4167 run scoreboard players set #phase_idx so_sys 7
execute if score #blk so_sys matches 3334..4167 run scoreboard players set #phase_lo so_sys 3334
execute if score #blk so_sys matches 3334..4167 run scoreboard players set #phase_hi so_sys 4167
execute if score #blk so_sys matches 4168..5000 run scoreboard players set #phase_idx so_sys 8
execute if score #blk so_sys matches 4168..5000 run scoreboard players set #phase_lo so_sys 4168
execute if score #blk so_sys matches 4168..5000 run scoreboard players set #phase_hi so_sys 5000
execute if score #blk so_sys matches 5001..5833 run scoreboard players set #phase_idx so_sys 9
execute if score #blk so_sys matches 5001..5833 run scoreboard players set #phase_lo so_sys 5001
execute if score #blk so_sys matches 5001..5833 run scoreboard players set #phase_hi so_sys 5833
execute if score #blk so_sys matches 5834..6667 run scoreboard players set #phase_idx so_sys 10
execute if score #blk so_sys matches 5834..6667 run scoreboard players set #phase_lo so_sys 5834
execute if score #blk so_sys matches 5834..6667 run scoreboard players set #phase_hi so_sys 6667
execute if score #blk so_sys matches 6668..7500 run scoreboard players set #phase_idx so_sys 11
execute if score #blk so_sys matches 6668..7500 run scoreboard players set #phase_lo so_sys 6668
execute if score #blk so_sys matches 6668..7500 run scoreboard players set #phase_hi so_sys 7500
execute if score #blk so_sys matches 7501..8333 run scoreboard players set #phase_idx so_sys 12
execute if score #blk so_sys matches 7501..8333 run scoreboard players set #phase_lo so_sys 7501
execute if score #blk so_sys matches 7501..8333 run scoreboard players set #phase_hi so_sys 8333
execute if score #blk so_sys matches 8334..9167 run scoreboard players set #phase_idx so_sys 13
execute if score #blk so_sys matches 8334..9167 run scoreboard players set #phase_lo so_sys 8334
execute if score #blk so_sys matches 8334..9167 run scoreboard players set #phase_hi so_sys 9167
execute if score #blk so_sys matches 9168..10000 run scoreboard players set #phase_idx so_sys 14
execute if score #blk so_sys matches 9168..10000 run scoreboard players set #phase_lo so_sys 9168
execute if score #blk so_sys matches 9168..10000 run scoreboard players set #phase_hi so_sys 10000
execute if score #blk so_sys matches 10001..10833 run scoreboard players set #phase_idx so_sys 15
execute if score #blk so_sys matches 10001..10833 run scoreboard players set #phase_lo so_sys 10001
execute if score #blk so_sys matches 10001..10833 run scoreboard players set #phase_hi so_sys 10833
execute if score #blk so_sys matches 10834..11667 run scoreboard players set #phase_idx so_sys 16
execute if score #blk so_sys matches 10834..11667 run scoreboard players set #phase_lo so_sys 10834
execute if score #blk so_sys matches 10834..11667 run scoreboard players set #phase_hi so_sys 11667
execute if score #blk so_sys matches 11668..12500 run scoreboard players set #phase_idx so_sys 17
execute if score #blk so_sys matches 11668..12500 run scoreboard players set #phase_lo so_sys 11668
execute if score #blk so_sys matches 11668..12500 run scoreboard players set #phase_hi so_sys 12500
execute if score #blk so_sys matches 12501..13333 run scoreboard players set #phase_idx so_sys 18
execute if score #blk so_sys matches 12501..13333 run scoreboard players set #phase_lo so_sys 12501
execute if score #blk so_sys matches 12501..13333 run scoreboard players set #phase_hi so_sys 13333
execute if score #blk so_sys matches 13334..14167 run scoreboard players set #phase_idx so_sys 19
execute if score #blk so_sys matches 13334..14167 run scoreboard players set #phase_lo so_sys 13334
execute if score #blk so_sys matches 13334..14167 run scoreboard players set #phase_hi so_sys 14167
execute if score #blk so_sys matches 14168..14999 run scoreboard players set #phase_idx so_sys 20
execute if score #blk so_sys matches 14168..14999 run scoreboard players set #phase_lo so_sys 14168
execute if score #blk so_sys matches 14168..14999 run scoreboard players set #phase_hi so_sys 14999
execute if score #blk so_sys matches 15000.. run scoreboard players set #phase_idx so_sys 21
execute if score #blk so_sys matches 15000.. run scoreboard players set #phase_lo so_sys 15000
execute if score #blk so_sys matches 15000.. run scoreboard players set #phase_hi so_sys 15000
