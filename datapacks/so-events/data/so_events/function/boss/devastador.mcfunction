summon minecraft:ravager ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Devastador",color:"dark_red",bold:true},attributes:[{id:"minecraft:max_health",base:150d},{id:"minecraft:knockback_resistance",base:0.6d}],Health:150f}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Devastador", "color": "dark_red", "bold": true}
bossbar set so_events:boss max 150
bossbar set so_events:boss value 150
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Devastador!", "color": "red", "bold": false}]
