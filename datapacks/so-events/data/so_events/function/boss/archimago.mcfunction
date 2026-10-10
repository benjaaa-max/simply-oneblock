summon minecraft:illusioner ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Archimago Espectral",color:"dark_blue",bold:true},attributes:[{id:"minecraft:max_health",base:140d},{id:"minecraft:knockback_resistance",base:0.6d},{id:"minecraft:scale",base:1.4d}],Health:140f,equipment:{mainhand:{id:"minecraft:bow",count:1,components:{"minecraft:enchantments":{"minecraft:power":3}}}},drop_chances:{mainhand:0.0f}}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Archimago Espectral", "color": "dark_blue", "bold": true}
bossbar set so_events:boss max 140
bossbar set so_events:boss value 140
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Archimago Espectral!", "color": "red", "bold": false}]
