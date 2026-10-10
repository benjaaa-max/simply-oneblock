# Zona: quien sale (o muere y reaparece afuera) pierde marcas y kit; quien entra volando queda marcado.
execute as @a[tag=so_ar_zone] at @s unless dimension minecraft:overworld run function so_arenas:lib/leave
execute as @a[tag=so_ar_zone] at @s unless entity @s[x=-5050,y=80,z=-5058,dx=100,dy=130,dz=142] run function so_arenas:lib/leave
execute as @a[tag=!so_ar_zone,x=-5050,y=80,z=-5058,dx=100,dy=130,dz=142] at @s if dimension minecraft:overworld run function so_arenas:lib/enter_zone
# Participantes: quienes están dentro del foso.
tag @a remove so_ar_in
execute as @a[tag=so_ar_zone,x=-5027,y=90,z=-5032,dx=54,dy=50,dz=64] run tag @s add so_ar_in
# Kits prestados tirados al piso: se borran (no se exportan).
kill @e[type=minecraft:item,x=-5050,y=80,z=-5058,dx=100,dy=130,dz=142,nbt={Item:{components:{"minecraft:custom_data":{so_arena_loan:1b}}}}]
execute if score #mode so_ar matches 1 run function so_arenas:mode/practice/second
execute if score #mode so_ar matches 2 run function so_arenas:mode/caza/second
execute if score #mode so_ar matches 4 run function so_arenas:mode/caza2/second
execute if score #mode so_ar matches 3 run function so_arenas:mode/defensa/second
execute if score #mode so_ar matches 1.. if score #anticamp so_ar matches 1 run function so_arenas:lib/anticamp
execute if score #mode so_ar matches 1.. unless entity @a[tag=so_ar_in] run function so_arenas:lib/vacio
execute if score #mode so_ar matches 0 as @a[tag=so_ar_zone,tag=!so_ar_in] run title @s actionbar {"text": "Menú: aldeanos, carteles, placas del piso o /trigger arena", "color": "gray"}
