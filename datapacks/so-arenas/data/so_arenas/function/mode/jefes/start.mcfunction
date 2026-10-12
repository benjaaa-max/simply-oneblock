scoreboard players set #mode so_ar 6
scoreboard players set #champ so_ar 0
scoreboard players set #rest so_ar 0
execute if score #jt so_ar matches 1 run scoreboard players set #cmax so_ar 3
execute if score #jt so_ar matches 2 run scoreboard players set #cmax so_ar 5
execute if score #jt so_ar matches 2 run scoreboard players set #rew so_ar 11
bossbar set so_arenas:fight color red
execute if score #jt so_ar matches 1 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Duelo de Campeones: 3 minijefes seguidos con escoltas. 10 s de respiro entre cada uno.", "color": "red", "bold": false}]
execute if score #jt so_ar matches 2 run tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Desafío de Jefes: 5 jefes de tu fase en cadena. ¡Botín de jefe!", "color": "red", "bold": false}]
function so_arenas:mode/jefes/next
