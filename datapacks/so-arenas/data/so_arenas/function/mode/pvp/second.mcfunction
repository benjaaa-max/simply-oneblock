scoreboard players add #t so_ar 1
execute as @a[tag=so_ar_pvp] unless entity @s[x=-5027,y=90,z=-5032,dx=54,dy=50,dz=64] run function so_arenas:mode/pvp/lose
execute if score #mode so_ar matches 10 unless entity @a[tag=so_ar_pvp] run function so_arenas:mode/pvp/end
execute if score #t so_ar matches 300.. run function so_arenas:mode/pvp/draw
