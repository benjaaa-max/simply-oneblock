# Tipo segun fase: slimes/zombis al inicio, acorazados y raid luego, Nether desde 6667.
execute store result score #type so_ev run random value 1..2
execute if score #blk so_ev matches 2501.. store result score #type so_ev run random value 1..4
execute if score #blk so_ev matches 6667.. store result score #type so_ev run random value 1..5
