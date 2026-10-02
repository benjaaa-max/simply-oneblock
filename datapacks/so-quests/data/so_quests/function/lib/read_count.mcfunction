# so_core primero; si no existe, lectura autonoma de Simply OneBlock
scoreboard players set #src sq 0
execute if score #blocks so_core matches -2147483648.. run scoreboard players set #src sq 1
execute if score #src sq matches 1 run scoreboard players operation #blocks sq = #blocks so_core
execute if score #src sq matches 0 if score fake_player ib_minedcount matches -2147483648.. run scoreboard players set #src sq 2
execute if score #src sq matches 2 run scoreboard players operation #blocks sq = fake_player ib_minedcount
execute if score #src sq matches 0 run scoreboard players set #blocks sq 0
