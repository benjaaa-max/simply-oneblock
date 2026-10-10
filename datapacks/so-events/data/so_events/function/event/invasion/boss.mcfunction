scoreboard players set #stage so_ev 2
execute if score #type so_ev matches 1 as @a[tag=so_ev_in,limit=1,sort=random] at @s run function so_events:lib/spawn {mob:"boss/rey_zombi"}
execute if score #type so_ev matches 2 as @a[tag=so_ev_in,limit=1,sort=random] at @s run function so_events:lib/spawn {mob:"boss/slime_rey"}
execute if score #type so_ev matches 3 as @a[tag=so_ev_in,limit=1,sort=random] at @s run function so_events:lib/spawn {mob:"boss/comandante"}
execute if score #type so_ev matches 4 as @a[tag=so_ev_in,limit=1,sort=random] at @s run function so_events:lib/spawn {mob:"boss/capitan"}
execute if score #type so_ev matches 5 as @a[tag=so_ev_in,limit=1,sort=random] at @s run function so_events:lib/spawn {mob:"boss/caballero"}
title @a[tag=so_ev_in] title {"text": "¡JEFE INVASOR!", "color": "dark_red", "bold": true}
