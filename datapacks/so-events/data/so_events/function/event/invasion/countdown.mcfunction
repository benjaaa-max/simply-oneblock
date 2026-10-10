scoreboard players set #cd so_ev 10
scoreboard players operation #cd so_ev -= #t so_ev
execute store result bossbar so_events:ev value run scoreboard players get #cd so_ev
execute if score #cd so_ev matches 1.. run title @a[tag=so_ev_in] actionbar [{"text": "La invasión empieza en ", "color": "red"}, {"score": {"name": "#cd", "objective": "so_ev"}, "color": "white", "bold": true}]
execute if score #cd so_ev matches ..0 run function so_events:event/invasion/next
