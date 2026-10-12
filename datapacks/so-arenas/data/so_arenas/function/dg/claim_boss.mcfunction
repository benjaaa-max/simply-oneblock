tag @s remove so_ev_boss
tag @s add so_ar_dgboss
execute store result bossbar so_arenas:dg max run data get entity @s Health
execute store result bossbar so_arenas:dg value run data get entity @s Health
bossbar set so_arenas:dg color red
