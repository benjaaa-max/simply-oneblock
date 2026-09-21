# Lee el progreso del mundo. Usa so_core si esta presente; si no, lee ib_minedcount.
execute if score #blocks so_core matches -2147483648.. run scoreboard players operation #blocks so_shop = #blocks so_core
execute unless score #blocks so_core matches -2147483648.. if score fake_player ib_minedcount matches -2147483648.. run scoreboard players operation #blocks so_shop = fake_player ib_minedcount
execute unless score #blocks so_shop matches -2147483648.. run scoreboard players set #blocks so_shop 0
scoreboard players set #u1 so_shop 0
execute if score #blocks so_shop >= #t1 so_shop run scoreboard players set #u1 so_shop 1
scoreboard players set #u2 so_shop 0
execute if score #blocks so_shop >= #t2 so_shop run scoreboard players set #u2 so_shop 1
scoreboard players set #u3 so_shop 0
execute if score #blocks so_shop >= #t3 so_shop run scoreboard players set #u3 so_shop 1
scoreboard players set #u4 so_shop 0
execute if score #blocks so_shop >= #t4 so_shop run scoreboard players set #u4 so_shop 1
scoreboard players set #u5 so_shop 0
execute if score #blocks so_shop >= #t5 so_shop run scoreboard players set #u5 so_shop 1
scoreboard players set #u6 so_shop 0
execute if score #blocks so_shop >= #t6 so_shop run scoreboard players set #u6 so_shop 1
scoreboard players set #u7 so_shop 0
execute if score #blocks so_shop >= #t7 so_shop run scoreboard players set #u7 so_shop 1
scoreboard players set #u8 so_shop 0
execute if score #blocks so_shop >= #t8 so_shop run scoreboard players set #u8 so_shop 1
# Reinicio diario del limite de venta
execute store result score #tod so_shop run time query daytime
execute if score #tod so_shop matches 0..40 if score #day so_shop matches 0 run function so_shop:lib/new_day
execute if score #tod so_shop matches 41.. run scoreboard players set #day so_shop 0
