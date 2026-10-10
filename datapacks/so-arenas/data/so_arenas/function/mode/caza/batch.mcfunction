scoreboard players add #spawned so_ar 5
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"zombie",t:1}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"husk",t:1}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"skeleton",t:1}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"spider",t:1}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. run function so_arenas:lib/spawn {m:"zombie",t:1}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"zombie_armor",t:1}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"piglin",t:1}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"bogged",t:1}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"cave_spider",t:1}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. run function so_arenas:lib/spawn {m:"zombie_armor",t:1}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"vindicator",t:1}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"pillager",t:1}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"witch",t:1}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"drowned_trident",t:1}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"vindicator",t:1}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"zombie_ominous",t:1}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"breeze",t:1}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"bogged",t:1}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"enderman",t:1}
execute if score #blk so_ar matches 15000.. run function so_arenas:lib/spawn {m:"zombie_ominous",t:1}
execute as @a[tag=so_ar_in] at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 1.1
