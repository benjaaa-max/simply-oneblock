summon minecraft:iron_golem ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss","so_ev_golem"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Gólem Furioso",color:"gray",bold:true},attributes:[{id:"minecraft:max_health",base:140d},{id:"minecraft:knockback_resistance",base:0.6d}],Health:140f}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Gólem Furioso", "color": "gray", "bold": true}
bossbar set so_events:boss max 140
bossbar set so_events:boss value 140
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Gólem Furioso!", "color": "red", "bold": false}]
