function so_events:lib/begin
scoreboard players set #active so_ev 7
scoreboard players set #hits so_ev 0
bossbar set so_events:ev name {"text": "Caza del fugitivo", "color": "gold"}
bossbar set so_events:ev max 60
bossbar set so_events:ev color yellow
execute store result score #kind so_ev run random value 1..2
execute if score #kind so_ev matches 1 as @a[tag=so_ev_in,limit=1,sort=random] at @s run summon minecraft:chicken ~ ~ ~ {Tags:["so_ev_mob","so_ev_runner"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Pollo Dorado",color:"gold",bold:true},active_effects:[{id:"minecraft:speed",amplifier:1b,duration:-1,show_particles:1b}],attributes:[{id:"minecraft:movement_speed",base:0.42}]}
execute if score #kind so_ev matches 2 as @a[tag=so_ev_in,limit=1,sort=random] at @s run summon minecraft:fox ~ ~ ~ {Tags:["so_ev_mob","so_ev_runner"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Zorro Místico",color:"light_purple",bold:true},active_effects:[{id:"minecraft:speed",amplifier:1b,duration:-1,show_particles:1b}],attributes:[{id:"minecraft:movement_speed",base:0.6}]}
execute if score #kind so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡El Pollo Dorado apareció! Golpeenlo 5 veces en 60 segundos.", "color": "gold", "bold": true}]
execute if score #kind so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡El Zorro Místico apareció! Golpeenlo 5 veces en 60 segundos.", "color": "gold", "bold": true}]
execute as @e[tag=so_ev_runner,limit=1] at @s run playsound minecraft:entity.experience_orb.pickup master @a ~ ~ ~ 1 1.6
