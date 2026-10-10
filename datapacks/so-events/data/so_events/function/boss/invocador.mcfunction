summon minecraft:ravager ~ ~ ~ {Tags:["so_ev_mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:evoker",Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Invocador Supremo",color:"dark_red",bold:true},attributes:[{id:"minecraft:max_health",base:120d},{id:"minecraft:knockback_resistance",base:0.6d}],Health:120f}]}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Invocador Supremo", "color": "dark_red", "bold": true}
bossbar set so_events:boss max 120
bossbar set so_events:boss value 120
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Invocador Supremo!", "color": "red", "bold": false}]
