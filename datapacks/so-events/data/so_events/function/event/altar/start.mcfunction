function so_events:lib/begin
scoreboard players set #active so_ev 9
scoreboard players set #paid so_ev 0
scoreboard players set #phase so_ev 0
bossbar set so_events:ev name {"text": "Altar místico", "color": "gold"}
bossbar set so_events:ev max 120
bossbar set so_events:ev color yellow
execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run function so_events:event/altar/place
execute as @e[tag=so_ev_altar,limit=1] at @s run playsound minecraft:music_disc.relic record @a ~ ~ ~ 3 1
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Apareció el Altar Místico. Tiren ofrendas durante 2 minutos: piedra y troncos suman poco, minerales más, gemas mucho. 3 fases de bendición.", "color": "gold", "bold": false}]
