function so_arenas:lib/enter_con
scoreboard players set #mode so_ar 2
scoreboard players set #t so_ar 0
bossbar set so_arenas:fight name {"text": "Caza: 15 bajas", "color": "aqua"}
bossbar set so_arenas:fight color aqua
bossbar set so_arenas:fight max 15
bossbar set so_arenas:fight value 0
bossbar set so_arenas:fight players @a[tag=so_ar_in]
bossbar set so_arenas:fight visible true
execute as @a[tag=so_ar_in] run title @s title {"text": "¡Caza de monstruos!", "color": "aqua", "bold": true}
tellraw @a [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Contrato: 15 bajas objetivo. Los molestos de apoyo son extra.", "color": "aqua", "bold": false}]
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"husk"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"skeleton"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"spider"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"husk"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"skeleton"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"spider"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"husk"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"skeleton"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"spider"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"husk"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"skeleton"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"spider"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"husk"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"skeleton"}
execute if score #blk so_ar matches 0.. unless score #blk so_ar matches 3334.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"spider"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie_armor"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"piglin"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"bogged"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"cave_spider"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie_armor"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"piglin"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"bogged"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"cave_spider"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie_armor"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"piglin"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"bogged"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"cave_spider"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie_armor"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"piglin"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"bogged"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"cave_spider"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie_armor"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"piglin"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"bogged"}
execute if score #blk so_ar matches 3334.. unless score #blk so_ar matches 7501.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"cave_spider"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"vindicator"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"pillager"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"witch"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"drowned_trident"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"vindicator"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"pillager"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"witch"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"drowned_trident"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"vindicator"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"pillager"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"witch"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"drowned_trident"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"vindicator"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"pillager"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"witch"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"drowned_trident"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"vindicator"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"pillager"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"witch"}
execute if score #blk so_ar matches 7501.. unless score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"drowned_trident"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie_ominous"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"breeze"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"bogged"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"enderman"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie_ominous"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"breeze"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"bogged"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"enderman"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie_ominous"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"breeze"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"bogged"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"enderman"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie_ominous"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"breeze"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"bogged"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"enderman"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"zombie_ominous"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"breeze"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"bogged"}
execute if score #blk so_ar matches 15000.. as @a[tag=so_ar_in,limit=1,sort=random] at @s run function so_arenas:lib/spawn_near {m:"enderman"}
