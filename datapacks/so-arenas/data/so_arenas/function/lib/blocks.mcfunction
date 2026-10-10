scoreboard players set #blk so_ar 0
execute if score fake_player ib_minedcount matches -2147483648.. run scoreboard players operation #blk so_ar = fake_player ib_minedcount
execute if score #blocks so_core matches -2147483648.. run scoreboard players operation #blk so_ar = #blocks so_core
# modo prueba admin: bloques simulados
execute if score #fake so_ar matches 0.. run scoreboard players operation #blk so_ar = #fake so_ar
