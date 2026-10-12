# Zona: quien sale (o muere y reaparece afuera) pierde marcas y kit; quien entra volando queda marcado.
execute as @a[tag=so_ar_zone] at @s unless dimension minecraft:overworld run function so_arenas:lib/leave
execute as @a[tag=so_ar_zone] at @s unless entity @s[x=-5056,y=50,z=-5066,dx=112,dy=160,dz=158] run function so_arenas:lib/leave
execute as @a[tag=!so_ar_zone,x=-5056,y=50,z=-5066,dx=112,dy=160,dz=158] at @s if dimension minecraft:overworld run function so_arenas:lib/enter_zone
# Muertes: cortan la racha.
execute as @a[scores={so_ar_death=1..}] run function so_arenas:lib/died
# Participantes: quienes están dentro del foso.
tag @a remove so_ar_in
execute as @a[tag=so_ar_zone,x=-5027,y=90,z=-5032,dx=54,dy=50,dz=64] run tag @s add so_ar_in
# Kits prestados tirados al piso: se borran (no se exportan).
kill @e[type=minecraft:item,x=-5056,y=50,z=-5066,dx=112,dy=160,dz=158,nbt={Item:{components:{"minecraft:custom_data":{so_arena_loan:1b}}}}]
function so_arenas:lib/trash
function so_arenas:lib/donations
execute if score #mode so_ar matches 9 run function so_arenas:lib/stage_second
execute if score #mode so_ar matches 1 run function so_arenas:mode/practice/second
execute if score #mode so_ar matches 2 run function so_arenas:mode/caza/second
execute if score #mode so_ar matches 3 run function so_arenas:mode/defensa/second
execute if score #mode so_ar matches 4 run function so_arenas:mode/caza2/second
execute if score #mode so_ar matches 5 run function so_arenas:mode/rey/second
execute if score #mode so_ar matches 6 run function so_arenas:mode/jefes/second
execute if score #mode so_ar matches 7 run function so_arenas:mode/asedio/second
execute if score #mode so_ar matches 10 run function so_arenas:mode/pvp/second
execute if score #mode so_ar matches 1..8 if score #mut_n so_ar matches 1 run effect give @a[tag=so_ar_in] minecraft:darkness 3 0 true
execute if score #mode so_ar matches 1..8 if score #anticamp so_ar matches 1 run function so_arenas:lib/anticamp
execute if score #mode so_ar matches 10 run function so_arenas:lib/anticamp
execute if score #mode so_ar matches 1..8 unless entity @a[tag=so_ar_in] run function so_arenas:lib/vacio
execute if score #mode so_ar matches 1..8 run function so_arenas:lib/board
execute if score #playing so_ar matches 1 run function so_arenas:lib/music_second
execute if score #exit so_ar matches 1 run function so_arenas:lib/exit_second
# Las Catacumbas
execute if score #dg so_ar matches 1.. run function so_arenas:dg/second
execute if score #dg so_ar matches 0 run tag @a remove so_ar_dgp
# Aggro forzado (arañas, endermans, wardens): golpe invisible a nombre del jugador más cercano, cada 2 s.
scoreboard players add #sec so_ar 1
scoreboard players operation #m2 so_ar = #sec so_ar
scoreboard players operation #m2 so_ar %= #two so_ar
execute if score #m2 so_ar matches 0 as @e[tag=so_ar_aggro,x=-5056,y=50,z=-5066,dx=112,dy=160,dz=158] at @s if entity @p[tag=so_ar_zone,distance=..40] run damage @s 0.01 minecraft:player_attack by @p[tag=so_ar_zone,distance=..40]
execute if score #mode so_ar matches 0 if score #exit so_ar matches 0 as @a[tag=so_ar_zone,tag=!so_ar_in,tag=!so_ar_spec,tag=!so_ar_dgp] run title @s actionbar {"text": "Menú: aldeanos, carteles, placas del piso o /trigger arena", "color": "gray"}
