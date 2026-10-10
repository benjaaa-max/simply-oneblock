$execute if score #near so_ev matches 1 positioned ~2 ~ ~ run function so_events:$(mob)
$execute unless score #near so_ev matches 1 run function so_events:$(mob)
