summon minecraft:phantom ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Espectro Alfa",color:"dark_gray",bold:true},attributes:[{id:"minecraft:max_health",base:100d},{id:"minecraft:knockback_resistance",base:0.6d},{id:"minecraft:scale",base:3d}],Health:100f,active_effects:[{id:"minecraft:fire_resistance",amplifier:0b,duration:-1,show_particles:1b}]}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Espectro Alfa", "color": "dark_gray", "bold": true}
bossbar set so_events:boss max 100
bossbar set so_events:boss value 100
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Espectro Alfa!", "color": "red", "bold": false}]
