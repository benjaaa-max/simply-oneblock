scoreboard players add #wave so_ar 1
execute store result bossbar so_arenas:fight value run scoreboard players get #wave so_ar
execute if score #wave so_ar matches 1 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"zombie_armor"}
execute if score #wave so_ar matches 1 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"zombie_armor"}
execute if score #wave so_ar matches 2 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"zombie_armor"}
execute if score #wave so_ar matches 2 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"zombie_armor"}
execute if score #wave so_ar matches 3 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"zombie_armor"}
execute if score #wave so_ar matches 3 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"zombie_armor"}
execute if score #wave so_ar matches 1 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"skeleton_armor"}
execute if score #wave so_ar matches 1 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"skeleton_armor"}
execute if score #wave so_ar matches 2 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"skeleton_armor"}
execute if score #wave so_ar matches 2 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"skeleton_armor"}
execute if score #wave so_ar matches 3 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"skeleton_armor"}
execute if score #wave so_ar matches 3 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"skeleton_armor"}
execute if score #wave so_ar matches 1 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"pillager"}
execute if score #wave so_ar matches 2 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"pillager"}
execute if score #wave so_ar matches 3 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"pillager"}
execute if score #wave so_ar matches 1 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"vindicator"}
execute if score #wave so_ar matches 2 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"vindicator"}
execute if score #wave so_ar matches 3 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"vindicator"}
execute if score #wave so_ar matches 1 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"witch"}
execute if score #wave so_ar matches 2 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"witch"}
execute if score #wave so_ar matches 3 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"witch"}
execute if score #wave so_ar matches 1 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"spider_big"}
execute if score #wave so_ar matches 2 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"spider_big"}
execute if score #wave so_ar matches 3 as @a[tag=so_ar_in] at @s run function so_arenas:lib/spawn_near {m:"spider_big"}
playsound minecraft:entity.zombie.ambient hostile @a[tag=so_ar_in] ~ ~ ~ 1 0.8
