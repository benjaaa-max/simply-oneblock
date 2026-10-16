title @a[tag=so_ev_in] title {"text": "¡El altar los bendice!", "color": "gold", "bold": true}
execute as @a[tag=so_ev_in] at @s run summon minecraft:lightning_bolt ~ ~ ~ {visual_only:1b}
execute if score #phase so_ev matches 1 as @a[tag=so_ev_in] at @s run function so_events:lib/chest {t:"altar_1"}
execute if score #phase so_ev matches 2 as @a[tag=so_ev_in] at @s run function so_events:lib/chest {t:"altar_2"}
execute if score #phase so_ev matches 3.. as @a[tag=so_ev_in] at @s run function so_events:lib/chest {t:"altar_3"}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "El altar dejó un Cofre de Recompensa junto a cada participante.", "color": "gold", "bold": false}]
scoreboard players add @a[tag=so_ev_in] so_ev_win 1
scoreboard players add @a[tag=so_ev_in] so_ev_pos 1
function so_events:lib/streak_up
function so_events:lib/cleanup
