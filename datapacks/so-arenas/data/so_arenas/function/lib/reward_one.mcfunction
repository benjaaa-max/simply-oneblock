execute if score #rew so_ar matches 1 run loot insert -4997 96 -4938 loot so_arenas:practice_t1
execute if score #rew so_ar matches 2 run loot insert -4997 96 -4938 loot so_arenas:practice_t2
execute if score #rew so_ar matches 3 run loot insert -4997 96 -4938 loot so_arenas:practice_t3
execute if score #rew so_ar matches 4 run loot insert -4997 96 -4938 loot so_arenas:practice_t4
execute if score #rew so_ar matches 10 run loot insert -4997 96 -4938 loot so_arenas:contract
execute if score #rew so_ar matches 11 run loot insert -4997 96 -4938 loot so_arenas:boss
# mutadores: botín doble
execute if score #mutc so_ar matches 1.. if score #rew so_ar matches 1 run loot insert -4997 96 -4938 loot so_arenas:practice_t1
execute if score #mutc so_ar matches 1.. if score #rew so_ar matches 2 run loot insert -4997 96 -4938 loot so_arenas:practice_t2
execute if score #mutc so_ar matches 1.. if score #rew so_ar matches 3 run loot insert -4997 96 -4938 loot so_arenas:practice_t3
execute if score #mutc so_ar matches 1.. if score #rew so_ar matches 4 run loot insert -4997 96 -4938 loot so_arenas:practice_t4
execute if score #mutc so_ar matches 1.. if score #rew so_ar matches 10 run loot insert -4997 96 -4938 loot so_arenas:contract
execute if score #mutc so_ar matches 1.. if score #rew so_ar matches 11 run loot insert -4997 96 -4938 loot so_arenas:boss
# racha
execute if score @s so_ar_streak matches 3 run loot insert -4997 96 -4938 loot so_arenas:streak
execute if score @s so_ar_streak matches 5 run loot insert -4997 96 -4938 loot so_arenas:streak
execute if score @s so_ar_streak matches 10.. run loot insert -4997 96 -4938 loot so_arenas:streak
execute if score @s so_ar_streak matches 3 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "¡Racha de 3 victorias! Cofre extra.", "color": "gold", "bold": false}]
execute if score @s so_ar_streak matches 5 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "¡Racha de 5 victorias! Cofre extra.", "color": "gold", "bold": false}]
execute if score @s so_ar_streak matches 10.. run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "¡Racha legendaria! Cofre extra.", "color": "gold", "bold": false}]
