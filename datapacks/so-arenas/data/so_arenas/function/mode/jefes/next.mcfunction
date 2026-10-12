scoreboard players add #champ so_ar 1
scoreboard players operation #wave so_ar = #champ so_ar
execute if score #jt so_ar matches 1 if score #champ so_ar matches 1 if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn_boss {b:"rey_zombi"}
execute if score #jt so_ar matches 1 if score #champ so_ar matches 1 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn_boss {b:"capitan"}
execute if score #jt so_ar matches 1 if score #champ so_ar matches 1 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"caballero"}
execute if score #jt so_ar matches 1 if score #champ so_ar matches 1 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"devastador"}
execute if score #jt so_ar matches 1 if score #champ so_ar matches 2 if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn_boss {b:"slime_rey"}
execute if score #jt so_ar matches 1 if score #champ so_ar matches 2 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn_boss {b:"piglin_bruto"}
execute if score #jt so_ar matches 1 if score #champ so_ar matches 2 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"caudillo_bruto"}
execute if score #jt so_ar matches 1 if score #champ so_ar matches 2 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"senor_end"}
execute if score #jt so_ar matches 1 if score #champ so_ar matches 3 if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn_boss {b:"comandante"}
execute if score #jt so_ar matches 1 if score #champ so_ar matches 3 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn_boss {b:"bruja_madre"}
execute if score #jt so_ar matches 1 if score #champ so_ar matches 3 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"archimago"}
execute if score #jt so_ar matches 1 if score #champ so_ar matches 3 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"heraldo_ominoso"}
execute if score #jt so_ar matches 1 if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"skeleton",t:0}
execute if score #jt so_ar matches 1 if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"spider",t:0}
execute if score #jt so_ar matches 1 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"witch",t:0}
execute if score #jt so_ar matches 1 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"skeleton_armor",t:0}
execute if score #jt so_ar matches 1 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"spider_big",t:0}
execute if score #jt so_ar matches 1 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"skeleton_ominous",t:0}
execute if score #jt so_ar matches 1 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"wither_skeleton",t:0}
execute if score #jt so_ar matches 1 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"skeleton_ominous",t:0}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 1 if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn_boss {b:"rey_zombi"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 1 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn_boss {b:"capitan"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 1 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"caballero"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 1 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"senor_llamas"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 2 if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn_boss {b:"comandante"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 2 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn_boss {b:"piglin_bruto"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 2 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"archimago"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 2 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"senor_end"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 3 if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn_boss {b:"slime_rey"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 3 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn_boss {b:"jinete_oseo"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 3 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"caudillo_bruto"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 3 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"heraldo_ominoso"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 4 if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn_boss {b:"arana_colosal"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 4 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn_boss {b:"bruja_madre"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 4 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"bestia_nether"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 4 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"devastador"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 5 if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn_boss {b:"zombi_gigante"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 5 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn_boss {b:"golem_furioso"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 5 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"invocador"}
execute if score #jt so_ar matches 2 if score #champ so_ar matches 5 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"zombi_gigante"}
title @a[tag=so_ar_in] title [{"text": "Campeón ", "color": "red", "bold": true}, {"score": {"name": "#champ", "objective": "so_ar"}, "color": "white"}, {"text": "/", "color": "gray"}, {"score": {"name": "#cmax", "objective": "so_ar"}, "color": "white"}]
execute as @a[tag=so_ar_in] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.5 1.4
