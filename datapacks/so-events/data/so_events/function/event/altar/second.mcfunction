scoreboard players add #t so_ev 1
execute store result bossbar so_events:ev value run scoreboard players get #t so_ev
execute as @e[tag=so_ev_altar,limit=1] at @s run particle minecraft:end_rod ~ ~1.2 ~ 0.2 0.4 0.2 0.02 8
execute as @e[tag=so_ev_altar,limit=1] at @s run function so_events:event/altar/take
execute if score #t so_ev matches 45.. run title @a[tag=so_ev_in] actionbar {"text": "¡Tributo al altar: 32 piedra o 16 troncos!", "color": "gold", "bold": true}
execute if score #paid so_ev matches 32.. run function so_events:event/altar/win
execute if score #t so_ev matches 90.. run function so_events:event/altar/fail
