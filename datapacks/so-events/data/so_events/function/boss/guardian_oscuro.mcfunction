summon minecraft:warden ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Guardián de la Oscuridad",color:"dark_aqua",bold:true},attributes:[{id:"minecraft:max_health",base:180d},{id:"minecraft:knockback_resistance",base:1d},{id:"minecraft:attack_damage",base:10d}],Health:180f}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Guardián de la Oscuridad", "color": "dark_aqua", "bold": true}
bossbar set so_events:boss max 180
bossbar set so_events:boss value 180
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Guardián de la Oscuridad!", "color": "red", "bold": false}]
