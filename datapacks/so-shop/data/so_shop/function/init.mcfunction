scoreboard objectives add so_shop dummy
scoreboard objectives add so_sold dummy
scoreboard objectives add so_sold_day dummy
scoreboard objectives add so_shop_cd dummy
scoreboard objectives add shop trigger
scoreboard objectives add shop_menu trigger
scoreboard objectives add shop_buy trigger
# Se crea (o se reutiliza si ya existe) el objetivo so_core para poder consultarlo
# sin riesgo de "Unknown scoreboard objective": si so_core no está instalado,
# #blocks so_core simplemente nunca tendrá un score, y lib/progress cae al
# fallback de leer fake_player ib_minedcount directamente.
scoreboard objectives add so_core dummy
scoreboard objectives add ib_minedcount dummy
execute unless score #daytick so_shop matches -2147483648.. run scoreboard players set #daytick so_shop 0

execute unless score #enabled so_shop matches -2147483648.. run scoreboard players set #enabled so_shop 1
execute unless score #day so_shop matches -2147483648.. run scoreboard players set #day so_shop 0
execute unless score #day_id so_shop matches -2147483648.. run scoreboard players set #day_id so_shop 0
execute unless score #sell_limit so_shop matches -2147483648.. run scoreboard players set #sell_limit so_shop 20
execute unless score #t1 so_shop matches -2147483648.. run scoreboard players set #t1 so_shop 0
scoreboard players set #u1 so_shop 0
execute unless score #t2 so_shop matches -2147483648.. run scoreboard players set #t2 so_shop 0
scoreboard players set #u2 so_shop 0
execute unless score #t3 so_shop matches -2147483648.. run scoreboard players set #t3 so_shop 2500
scoreboard players set #u3 so_shop 0
execute unless score #t4 so_shop matches -2147483648.. run scoreboard players set #t4 so_shop 550
scoreboard players set #u4 so_shop 0
execute unless score #t5 so_shop matches -2147483648.. run scoreboard players set #t5 so_shop 4000
scoreboard players set #u5 so_shop 0
execute unless score #t6 so_shop matches -2147483648.. run scoreboard players set #t6 so_shop 7000
scoreboard players set #u6 so_shop 0
execute unless score #t7 so_shop matches -2147483648.. run scoreboard players set #t7 so_shop 8250
scoreboard players set #u7 so_shop 0
execute unless score #t8 so_shop matches -2147483648.. run scoreboard players set #t8 so_shop 0
scoreboard players set #u8 so_shop 0

tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Tienda cargada. Usa ","color":"green"},{"text":"/trigger shop","color":"yellow"},{"text":" para abrirla.","color":"green"}]
scoreboard objectives add so_shop_seen dummy
scoreboard objectives add so_shop_buys dummy
