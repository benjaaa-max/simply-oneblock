scoreboard objectives add so_shop dummy
scoreboard objectives add so_sold dummy
scoreboard objectives add shop trigger
scoreboard objectives add shop_menu trigger
scoreboard objectives add shop_buy trigger

execute unless score #enabled so_shop matches -2147483648.. run scoreboard players set #enabled so_shop 1
execute unless score #day so_shop matches -2147483648.. run scoreboard players set #day so_shop 0
execute unless score #sell_limit so_shop matches -2147483648.. run scoreboard players set #sell_limit so_shop 6
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
