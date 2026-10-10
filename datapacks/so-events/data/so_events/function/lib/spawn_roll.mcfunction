execute store result storage so_events:tmp a int 1 run random value 0..359
execute if score #near so_ev matches 1 store result storage so_events:tmp d int 1 run random value 3..7
execute unless score #near so_ev matches 1 store result storage so_events:tmp d int 1 run random value 6..14
