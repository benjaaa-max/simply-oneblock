# Refuerza a los mobs nuevos del evento segun #tier (vida, daño, armadura, velocidad).
tag @e[tag=so_ev_mob,tag=!so_ev_t] add so_ev_tn
execute if score #tier so_ev matches 2 as @e[tag=so_ev_tn] run function so_events:lib/tier_2
execute if score #tier so_ev matches 3.. as @e[tag=so_ev_tn] run function so_events:lib/tier_3
execute if score #tier so_ev matches 2.. as @e[tag=so_ev_tn,tag=so_ev_boss,limit=1] store result bossbar so_events:boss max run attribute @s minecraft:max_health get
tag @e[tag=so_ev_tn] add so_ev_t
tag @e[tag=so_ev_tn] remove so_ev_tn
