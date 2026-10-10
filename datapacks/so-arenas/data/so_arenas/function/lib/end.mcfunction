# Fin de desafio: limpia mobs del coliseo, núcleo, barras y kits prestados.
tp @e[tag=so_ar_mob] -5000 -300 -5000
kill @e[tag=so_ar_mob]
setblock -5000 96 -5000 minecraft:air
bossbar set so_arenas:fight visible false
tag @a[tag=so_ar_loan] remove so_ar_loan
execute as @a[tag=so_ar_loan] run clear @s stone_sword[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s leather_helmet[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s leather_chestplate[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s leather_leggings[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s leather_boots[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s iron_chestplate[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s bow[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s arrow[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s bread[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s crossbow[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s iron_sword[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s diamond_sword[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s golden_apple[minecraft:custom_data={so_arena_loan:1b}]
execute as @a[tag=so_ar_loan] run clear @s splash_potion[minecraft:custom_data={so_arena_loan:1b}]
tag @a[tag=so_ar_loan] remove so_ar_loan
scoreboard players set #mode so_ar 0
scoreboard players set #wave so_ar 0
scoreboard players set #t so_ar 0
scoreboard players set #anticamp so_ar 1
scoreboard players reset @a so_ar_air
