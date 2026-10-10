scoreboard objectives add so_ev dummy
scoreboard objectives add evento trigger
execute unless score #enabled so_ev matches 0..1 run scoreboard players set #enabled so_ev 1
execute unless score #auto so_ev matches 0..1 run scoreboard players set #auto so_ev 1
execute unless score #every so_ev matches 1.. run scoreboard players set #every so_ev 400
execute unless score #min so_ev matches 0.. run scoreboard players set #min so_ev 300
execute unless score #mine_goal so_ev matches 1.. run scoreboard players set #mine_goal so_ev 150
execute unless score #active so_ev matches 0.. run scoreboard players set #active so_ev 0
bossbar add so_events:ev {"text": "Evento"}
bossbar add so_events:boss {"text": "Jefe"}
bossbar set so_events:ev color yellow
bossbar set so_events:boss color red
tellraw @a[tag=oneblock_admin] [{"text": "[SO Events] ", "color": "gold"}, {"text": "cargado. Ayuda: /function so_events:admin/help", "color": "gray"}]
scoreboard players set #twenty so_ev 20
scoreboard players set #five so_ev 5
scoreboard players set #near so_ev 0
function so_events:load_offers
