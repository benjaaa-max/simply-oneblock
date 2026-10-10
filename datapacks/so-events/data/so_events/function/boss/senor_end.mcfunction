summon minecraft:enderman ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Señor del End",color:"light_purple",bold:true},attributes:[{id:"minecraft:max_health",base:160d},{id:"minecraft:knockback_resistance",base:0.6d},{id:"minecraft:scale",base:1.6d}],Health:160f}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Señor del End", "color": "light_purple", "bold": true}
bossbar set so_events:boss max 160
bossbar set so_events:boss value 160
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Señor del End!", "color": "red", "bold": false}]
