scoreboard players add #t so_ev 1
execute store result bossbar so_events:ev value run scoreboard players get #t so_ev
execute as @e[tag=so_ev_runner,limit=1] at @s run particle minecraft:end_rod ~ ~0.5 ~ 0.2 0.2 0.2 0.02 6
execute as @e[tag=so_ev_runner,limit=1] at @s run title @a[tag=so_ev_in,distance=..40] actionbar [{"text": "Golpes: ", "color": "gold"}, {"score": {"name": "#hits", "objective": "so_ev"}, "color": "white", "bold": true}, {"text": "/5", "color": "gray"}]
execute unless entity @e[tag=so_ev_runner] run function so_events:event/runner/fail
execute if score #t so_ev matches 60.. run function so_events:event/runner/fail
