# Comun a todo evento: participantes, alerta, temporizador y nivel (1 <5000, 2 <10000, 3 desde 10000).
tag @a remove so_ev_in
execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in
scoreboard players set #t so_ev 0
scoreboard players set #tier so_ev 1
execute if score #blk so_ev matches 5000.. run scoreboard players set #tier so_ev 2
execute if score #blk so_ev matches 10000.. run scoreboard players set #tier so_ev 3
bossbar set so_events:ev players @a[tag=so_ev_in]
bossbar set so_events:ev visible true
playsound minecraft:block.bell.use master @a ~ ~ ~ 1 0.8
