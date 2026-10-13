scoreboard players add #t so_ev 1
execute positioned 0 64 0 as @a[distance=..64,gamemode=!spectator] run tag @s add so_ev_in
bossbar set so_events:ev players @a[tag=so_ev_in]
execute if score #stage so_ev matches 0 run function so_events:event/invasion/countdown
execute if score #stage so_ev matches 1 run function so_events:event/invasion/waves
execute if score #stage so_ev matches 2 unless entity @e[tag=so_ev_boss] run function so_events:event/invasion/win
# Golems enfurecidos: un roce minimo atribuido al jugador mas cercano los vuelve hostiles.
scoreboard players operation #m so_ev = #t so_ev
scoreboard players operation #m so_ev %= #five so_ev
execute if score #m so_ev matches 0 as @e[tag=so_ev_golem] at @s if entity @a[tag=so_ev_in,distance=..32] run damage @s 0.01 minecraft:player_attack by @p[tag=so_ev_in]
# Warden: se renueva el bloqueo de excavación y un golpe real del jugador más cercano le sube la ira al tope.
execute as @e[tag=so_ev_boss,type=minecraft:warden] run function so_events:lib/warden_keep
execute if score #m so_ev matches 0 as @e[tag=so_ev_boss,type=minecraft:warden] at @s if entity @a[tag=so_ev_in,distance=..48] run damage @s 0.1 minecraft:player_attack by @p[tag=so_ev_in]
# Invasión alfa: aura del jefe.
execute if score #alpha so_ev matches 1 as @e[tag=so_ev_boss] at @s run particle minecraft:soul_fire_flame ~ ~1 ~ 0.4 0.6 0.4 0.02 12
execute if score #active so_ev matches 5 if score #t so_ev matches 420.. run function so_events:event/invasion/fail
execute if score #active so_ev matches 5 unless entity @a[tag=so_ev_in] run function so_events:event/invasion/fail
