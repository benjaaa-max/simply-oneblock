scoreboard players add #t so_ev 1
execute store result bossbar so_events:ev value run scoreboard players get #t so_ev
scoreboard players operation #m so_ev = #t so_ev
scoreboard players operation #m so_ev %= #three so_ev
execute if score #m so_ev matches 0 run function so_events:event/mana/burst
execute if score #t so_ev matches 45.. run function so_events:lib/cleanup
