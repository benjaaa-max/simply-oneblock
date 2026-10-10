summon minecraft:guardian ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Guardián del Abismo",color:"aqua",bold:true},attributes:[{id:"minecraft:max_health",base:60d},{id:"minecraft:knockback_resistance",base:0.6d}],Health:60f}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Guardián del Abismo", "color": "aqua", "bold": true}
bossbar set so_events:boss max 60
bossbar set so_events:boss value 60
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Guardián del Abismo!", "color": "red", "bold": false}]
