scoreboard objectives remove so_shop
scoreboard objectives remove so_sold
scoreboard objectives remove so_sold_day
scoreboard objectives remove so_shop_cd
scoreboard objectives remove shop
scoreboard objectives remove shop_menu
scoreboard objectives remove shop_buy
# so_core NO se borra aquí a propósito: si el jugador tiene el datapack so_core.zip
# real instalado, ese objetivo le pertenece a él, no a so_shop (que solo lo crea
# como salvaguarda de lectura, ver init.mcfunction).
tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Tienda retirada. Simply OneBlock no fue modificado.","color":"red"}]
