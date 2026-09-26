# Lectura del contador de bloques minados de Simply OneBlock.
# 1) so_core (si existe y tiene valor)  2) lectura autonoma de fake_player ib_minedcount
# Los objetivos se crean en init para que ninguna consulta falle.
scoreboard players set #src so_shop 0
execute if score #blocks so_core matches -2147483648.. run scoreboard players set #src so_shop 1
execute if score #src so_shop matches 1 run scoreboard players operation #blocks so_shop = #blocks so_core
execute if score #src so_shop matches 0 if score fake_player ib_minedcount matches -2147483648.. run scoreboard players set #src so_shop 2
execute if score #src so_shop matches 2 run scoreboard players operation #blocks so_shop = fake_player ib_minedcount
execute if score #src so_shop matches 0 run scoreboard players set #blocks so_shop 0
