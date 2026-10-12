tag @s remove so_ev_boss
tag @s add so_ar_boss
execute store result bossbar so_arenas:fight max run data get entity @s Health
execute store result bossbar so_arenas:fight value run data get entity @s Health
bossbar set so_arenas:fight name [{"text":"Campeón: ","color":"red","bold":true},{"selector":"@e[tag=so_ar_boss,limit=1]"}]
