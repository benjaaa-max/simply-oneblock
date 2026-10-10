# Kit prestado según tier. Todos los ítems llevan marca so_arena_loan (no salen del coliseo).
execute if score #tier so_ar matches 1 run give @s stone_sword[minecraft:custom_data={so_arena_loan:1b},minecraft:custom_name={text:"Kit de Práctica",color:"yellow",italic:false}]
execute if score #tier so_ar matches 1 run give @s leather_helmet[minecraft:custom_data={so_arena_loan:1b}]
execute if score #tier so_ar matches 1 run give @s leather_chestplate[minecraft:custom_data={so_arena_loan:1b}]
execute if score #tier so_ar matches 1 run give @s leather_leggings[minecraft:custom_data={so_arena_loan:1b}]
execute if score #tier so_ar matches 1 run give @s leather_boots[minecraft:custom_data={so_arena_loan:1b}]
execute if score #tier so_ar matches 1 run give @s bread[minecraft:custom_data={so_arena_loan:1b}] 8
execute if score #tier so_ar matches 2 run give @s iron_sword[minecraft:custom_data={so_arena_loan:1b},minecraft:custom_name={text:"Kit de Práctica",color:"yellow",italic:false}]
execute if score #tier so_ar matches 2 run give @s iron_chestplate[minecraft:custom_data={so_arena_loan:1b}]
execute if score #tier so_ar matches 2 run give @s leather_helmet[minecraft:custom_data={so_arena_loan:1b}]
execute if score #tier so_ar matches 2 run give @s bread[minecraft:custom_data={so_arena_loan:1b}] 8
execute if score #tier so_ar matches 2 run give @s bow[minecraft:custom_data={so_arena_loan:1b}]
execute if score #tier so_ar matches 2 run give @s arrow[minecraft:custom_data={so_arena_loan:1b}] 24
execute if score #tier so_ar matches 3 run give @s diamond_sword[minecraft:custom_data={so_arena_loan:1b},minecraft:custom_name={text:"Kit de Práctica",color:"yellow",italic:false}]
execute if score #tier so_ar matches 3 run give @s iron_chestplate[minecraft:custom_data={so_arena_loan:1b}]
execute if score #tier so_ar matches 3 run give @s iron_helmet[minecraft:custom_data={so_arena_loan:1b}]
execute if score #tier so_ar matches 3 run give @s bow[minecraft:custom_data={so_arena_loan:1b}]
execute if score #tier so_ar matches 3 run give @s arrow[minecraft:custom_data={so_arena_loan:1b}] 32
execute if score #tier so_ar matches 3 run give @s golden_apple[minecraft:custom_data={so_arena_loan:1b}] 2
execute if score #tier so_ar matches 4 run give @s diamond_sword[minecraft:custom_data={so_arena_loan:1b},minecraft:custom_name={text:"Kit de Práctica",color:"yellow",italic:false}]
execute if score #tier so_ar matches 4 run give @s golden_apple[minecraft:custom_data={so_arena_loan:1b}] 2
execute if score #tier so_ar matches 4 run give @s crossbow[minecraft:custom_data={so_arena_loan:1b}]
execute if score #tier so_ar matches 4 run give @s arrow[minecraft:custom_data={so_arena_loan:1b}] 48
tag @s add so_ar_loan
execute if score #loan so_ar matches 1 run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Kit prestado entregado. Vuelve con el botón o /trigger volver al terminar (se retira solo).", "color": "yellow", "bold": false}]
execute if score #loan so_ar matches 0 run tellraw @s [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Entrás con tu propio equipo: si morís, lo recuperás al volver a la isla.", "color": "yellow", "bold": false}]
