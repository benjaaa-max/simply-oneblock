# Lee el progreso (ver lib/read_count) y calcula secciones desbloqueadas.
function so_shop:lib/read_count
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
function so_shop:lib/day_timer

# Sincroniza el límite de cada jugador CONECTADO contra el día global (#day_id).
# Cubre al jugador que se conecta después de que new_day ya corrió (reset @a no lo
# alcanzó en ese momento): si su so_sold_day quedó atrás, se le resetea so_sold ahora.
execute as @a unless score @s so_sold_day >= #day_id so_shop run scoreboard players reset @s so_sold
execute as @a unless score @s so_sold_day >= #day_id so_shop run scoreboard players operation @s so_sold_day = #day_id so_shop
