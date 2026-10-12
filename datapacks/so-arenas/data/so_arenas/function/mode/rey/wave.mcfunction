scoreboard players add #wave so_ar 1
execute store result score #alive so_ar if entity @e[tag=so_ar_mob]
execute if score #alive so_ar matches 25.. run return 0
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"zombie",t:0}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"husk",t:0}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"skeleton",t:0}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"skeleton",t:0}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"zombie_armor",t:0}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"piglin",t:0}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"bogged",t:0}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"witch",t:0}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"vindicator",t:0}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"pillager",t:0}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"witch",t:0}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"spider_big",t:0}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"zombie_ominous",t:0}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"breeze",t:0}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"bogged",t:0}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"wither_skeleton",t:0}
execute as @a[tag=so_ar_in] at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 1.2
