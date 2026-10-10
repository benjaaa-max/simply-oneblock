summon minecraft:slime ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Slime Rey",color:"green",bold:true},attributes:[{id:"minecraft:max_health",base:64d},{id:"minecraft:knockback_resistance",base:0.6d}],Health:64f,Size:5}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Slime Rey", "color": "green", "bold": true}
bossbar set so_events:boss max 64
bossbar set so_events:boss value 64
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Slime Rey!", "color": "red", "bold": false}]
