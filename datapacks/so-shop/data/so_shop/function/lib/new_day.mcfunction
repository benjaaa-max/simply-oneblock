scoreboard players set #day so_shop 1
# Se incrementa un id de día global en vez de resetear @a (que solo alcanza a jugadores
# conectados en este instante). so_sold se compara contra so_sold_day por jugador en
# lib/sell_limit: si no coinciden, el límite de ese jugador se considera vencido, esté
# o no conectado ahora mismo.
scoreboard players add #day_id so_shop 1
scoreboard players reset @a so_sold
execute as @a run scoreboard players operation @s so_sold_day = #day_id so_shop
tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Nuevo día: el límite de ventas se ha reiniciado.","color":"gray"}]
