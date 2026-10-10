scoreboard players add #wt so_ev 1
execute store result score #alive so_ev if entity @e[tag=so_ev_mob]
title @a[tag=so_ev_in] actionbar [{"text": "Enemigos restantes: ", "color": "red"}, {"score": {"name": "#alive", "objective": "so_ev"}, "color": "white", "bold": true}]
execute if score #alive so_ev matches 0 if score #wt so_ev matches 3.. run function so_events:event/invasion/next
execute if score #wt so_ev matches 90.. run function so_events:event/invasion/next
