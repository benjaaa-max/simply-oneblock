# Marca de presencia dentro del coliseo (por segundo).
tag @a[tag=so_ar_in] remove so_ar_in
execute as @a[x=-5046,y=94,z=-5054,dx=92,dy=74,dz=108] run tag @s add so_ar_in
# Retagea los mobs de so_events que quedaron dentro del coliseo para no pisar eventos de la isla.
execute as @e[tag=so_ev_mob,tag=!so_ar_mob,x=-5042,y=95,z=-5050,dx=84,dy=74,dz=100] run tag @s add so_ar_mob
execute as @a[scores={levelrank=1..}] run function so_arenas:lib/rank
scoreboard players reset @a levelrank
scoreboard players enable @a levelrank
execute if score #mode so_ar matches 1 run function so_arenas:mode/practice/second
execute if score #mode so_ar matches 2 run function so_arenas:mode/caza/second
execute if score #mode so_ar matches 3 run function so_arenas:mode/defensa/second
execute if score #mode so_ar matches 1..3 run function so_arenas:lib/watch
execute unless score #mode so_ar matches 1..3 run function so_arenas:lib/idle
