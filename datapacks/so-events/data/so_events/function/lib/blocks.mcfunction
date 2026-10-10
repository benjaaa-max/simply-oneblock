# Lee el progreso sin escribir el contador de Simply OneBlock.
scoreboard players set #blk so_ev 0
execute if score fake_player ib_minedcount matches -2147483648.. run scoreboard players operation #blk so_ev = fake_player ib_minedcount
execute if score #blocks so_core matches -2147483648.. run scoreboard players operation #blk so_ev = #blocks so_core
