scoreboard players add #bstep so_ar 1
execute if score #bstep so_ar matches 1 run function so_arenas:admin/build_01
execute if score #bstep so_ar matches 2 run function so_arenas:admin/build_02
execute if score #bstep so_ar matches 3 run function so_arenas:admin/build_03
execute if score #bstep so_ar matches 4 run function so_arenas:admin/build_04
execute if score #bstep so_ar matches 5 run function so_arenas:admin/build_05
execute if score #bstep so_ar matches 6 run function so_arenas:admin/build_06
execute if score #bstep so_ar matches 7 run function so_arenas:admin/build_07
execute if score #bstep so_ar matches 8 run function so_arenas:admin/build_08
execute if score #bstep so_ar matches 9 run function so_arenas:admin/build_09
execute if score #bstep so_ar matches 10 run function so_arenas:admin/build_10
execute if score #bstep so_ar matches 11 run function so_arenas:admin/build_11
execute if score #bstep so_ar matches 12 run function so_arenas:admin/build_12
execute if score #bstep so_ar matches 13 run function so_arenas:admin/build_13
execute if score #bstep so_ar matches 14 run function so_arenas:admin/build_14
title @a[tag=so_ar_zone] actionbar [{"text":"Construyendo paso ","color":"yellow"},{"score":{"name":"#bstep","objective":"so_ar"},"color":"white"},{"text":"/14","color":"yellow"}]
execute if score #bstep so_ar matches ..13 run schedule function so_arenas:admin/build_step 10t
execute if score #bstep so_ar matches 14 run function so_arenas:admin/build_finish
