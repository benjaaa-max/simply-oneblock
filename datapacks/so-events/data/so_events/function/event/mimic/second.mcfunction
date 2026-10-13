scoreboard players add #t so_ev 1
execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in
execute store result bossbar so_events:ev value run scoreboard players get #t so_ev
execute if score #mimic so_ev matches 0 as @e[tag=so_ev_mimic] at @s run particle minecraft:witch ~ ~0.7 ~ 0.3 0.3 0.3 0.01 4
execute if score #mimic so_ev matches 0 as @e[tag=so_ev_mimic] at @s run particle minecraft:enchant ~ ~1.2 ~ 0.3 0.3 0.3 0.5 6
# Antitrampa: romper el cofre también cuenta como elegirlo.
execute if score #mimic so_ev matches 0 as @e[tag=so_ev_mim_real] at @s unless block ~ ~ ~ minecraft:chest run function so_events:event/mimic/treasure
execute if score #mimic so_ev matches 0 as @e[tag=so_ev_mim_fake] at @s unless block ~ ~ ~ minecraft:chest run function so_events:event/mimic/trap
execute if score #mimic so_ev matches 1 run function so_events:event/mimic/end
# Trampa: el evento sigue hasta derrotar a los vexes.
execute if score #mimic so_ev matches 2 run title @a[tag=so_ev_in] actionbar {"text": "¡Derrotá a los vexes y phantoms de la trampa!", "color": "red", "bold": true}
execute if score #mimic so_ev matches 2 unless entity @e[tag=so_ev_mob] run function so_events:event/mimic/trap_win
execute if score #t so_ev matches 120.. run function so_events:event/mimic/vanish
