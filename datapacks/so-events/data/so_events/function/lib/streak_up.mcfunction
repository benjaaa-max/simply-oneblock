scoreboard players add #streak so_ev 1
# Bonus: 1 rollo extra de reward_small por cada 2 de racha (tope 3).
execute if score #streak so_ev matches 2..3 as @a[tag=so_ev_in] at @s run function so_events:lib/chest {t:"reward_small"}
execute if score #streak so_ev matches 4..5 as @a[tag=so_ev_in] at @s run function so_events:lib/chest {t:"reward_small"}
execute if score #streak so_ev matches 4..5 as @a[tag=so_ev_in] at @s run function so_events:lib/chest {t:"reward_small"}
execute if score #streak so_ev matches 6.. as @a[tag=so_ev_in] at @s run function so_events:lib/chest {t:"reward_small"}
execute if score #streak so_ev matches 6.. as @a[tag=so_ev_in] at @s run function so_events:lib/chest {t:"reward_small"}
execute if score #streak so_ev matches 6.. as @a[tag=so_ev_in] at @s run function so_events:lib/chest {t:"reward_small"}
execute if score #streak so_ev matches 2.. run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Racha de eventos: x", "color": "gold", "bold": false}, {"score": {"name": "#streak", "objective": "so_ev"}, "color": "white", "bold": true}, {"text": " — recompensa mejorada.", "color": "gold"}]
