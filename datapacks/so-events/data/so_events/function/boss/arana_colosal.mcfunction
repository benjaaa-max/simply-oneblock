summon minecraft:spider ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Araña Colosal",color:"dark_red",bold:true},attributes:[{id:"minecraft:max_health",base:220d},{id:"minecraft:knockback_resistance",base:0.6d},{id:"minecraft:scale",base:5d},{id:"minecraft:attack_damage",base:8d}],Health:220f}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Araña Colosal", "color": "dark_red", "bold": true}
bossbar set so_events:boss max 220
bossbar set so_events:boss value 220
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Araña Colosal!", "color": "red", "bold": false}]
