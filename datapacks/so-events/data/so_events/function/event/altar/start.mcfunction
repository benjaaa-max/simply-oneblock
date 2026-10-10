function so_events:lib/begin
scoreboard players set #active so_ev 9
scoreboard players set #paid so_ev 0
scoreboard players set #need so_ev 32
bossbar set so_events:ev name {"text": "Altar del sacrificio", "color": "gold"}
bossbar set so_events:ev max 90
bossbar set so_events:ev color yellow
scoreboard players set #near so_ev 1
execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function so_events:event/altar/place
scoreboard players set #near so_ev 0
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "El Altar del Sacrificio apareció. Tirenle encima 32 bloques de piedra o 16 troncos para bendecir la isla.", "color": "gold", "bold": false}]
