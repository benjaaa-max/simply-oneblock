tag @s remove so_ev_mob
tag @s add so_ar_dgm
execute if entity @s[type=#so_arenas:aggro] run tag @s add so_ar_aggro
execute if entity @s[tag=so_ev_boss] run function so_arenas:dg/claim_boss
