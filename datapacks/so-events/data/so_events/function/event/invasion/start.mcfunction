function so_events:lib/begin
scoreboard players set #active so_ev 5
scoreboard players set #stage so_ev 0
scoreboard players set #wave so_ev 0
function so_events:lib/no_grief
execute unless score #force_type so_ev matches 1..5 run function so_events:event/invasion/pick
execute if score #force_type so_ev matches 1..5 run scoreboard players operation #type so_ev = #force_type so_ev
scoreboard players set #force_type so_ev 0
bossbar set so_events:ev color red
bossbar set so_events:ev max 10
execute if score #type so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Horda de zombis!", "color": "dark_green", "bold": true}
execute if score #type so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Ataque de slimes!", "color": "green", "bold": true}
execute if score #type so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Oleada acorazada!", "color": "gray", "bold": true}
execute if score #type so_ev matches 4 run bossbar set so_events:ev name {"text": "¡Raid de saqueadores!", "color": "dark_red", "bold": true}
execute if score #type so_ev matches 5 run bossbar set so_events:ev name {"text": "¡Invasión del Nether!", "color": "dark_purple", "bold": true}
execute if score #type so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Horda de zombis en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Ataque de slimes en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Oleada acorazada en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 4 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Raid de saqueadores en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 5 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Invasión del Nether en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
playsound minecraft:event.raid.horn master @a ~ ~ ~ 1 1
