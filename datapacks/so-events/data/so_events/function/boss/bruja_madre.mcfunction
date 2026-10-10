summon minecraft:witch ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Gran Bruja Madre",color:"dark_purple",bold:true},attributes:[{id:"minecraft:max_health",base:150d},{id:"minecraft:knockback_resistance",base:0.6d},{id:"minecraft:scale",base:1.5d}],Health:150f,active_effects:[{id:"minecraft:resistance",amplifier:0b,duration:-1,show_particles:1b}]}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Gran Bruja Madre", "color": "dark_purple", "bold": true}
bossbar set so_events:boss max 150
bossbar set so_events:boss value 150
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Gran Bruja Madre!", "color": "red", "bold": false}]
