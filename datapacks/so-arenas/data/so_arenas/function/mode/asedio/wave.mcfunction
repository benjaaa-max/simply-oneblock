scoreboard players add #wave so_ar 1
execute store result bossbar so_arenas:fight value run scoreboard players get #wave so_ar
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"phantom",t:0}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"phantom",t:0}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"vex",t:0}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"phantom",t:0}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"phantom",t:0}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"phantom_big",t:0}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"vex",t:0}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"phantom_big",t:0}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"phantom_big",t:0}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"vex",t:0}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"vex",t:0}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"phantom",t:0}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"phantom_big",t:0}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"phantom_big",t:0}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"vex",t:0}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"vex",t:0}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"breeze",t:0}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"phantom",t:0}
execute if score #wave so_ar matches 2.. if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"phantom",t:0}
execute if score #wave so_ar matches 2.. if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"phantom",t:0}
execute if score #wave so_ar matches 2.. if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"phantom",t:0}
execute if score #wave so_ar matches 2.. if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"phantom",t:0}
execute if score #wave so_ar matches 2.. if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"phantom_big",t:0}
execute if score #wave so_ar matches 2.. if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"phantom_big",t:0}
execute if score #wave so_ar matches 2.. if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"phantom_big",t:0}
execute if score #wave so_ar matches 2.. if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"phantom_big",t:0}
execute if score #wave so_ar matches 3 if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn_boss {b:"espectro_alfa"}
execute if score #wave so_ar matches 3 if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"espectro_alfa"}
execute if score #wave so_ar matches 3 if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn_boss {b:"espectro_alfa"}
execute as @a[tag=so_ar_in] at @s run playsound minecraft:entity.phantom.swoop master @s ~ ~ ~ 1 0.8
