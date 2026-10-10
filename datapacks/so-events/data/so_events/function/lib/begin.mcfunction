# Comun a todo evento: participantes, alerta y temporizador.
tag @a remove so_ev_in
execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in
scoreboard players set #t so_ev 0
bossbar set so_events:ev players @a[tag=so_ev_in]
bossbar set so_events:ev visible true
playsound minecraft:block.bell.use master @a ~ ~ ~ 1 0.8
