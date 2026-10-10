summon minecraft:skeleton ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Comandante Óseo",color:"white",bold:true},attributes:[{id:"minecraft:max_health",base:110d},{id:"minecraft:knockback_resistance",base:0.6d}],Health:110f,equipment:{head:{id:"minecraft:diamond_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1},mainhand:{id:"minecraft:bow",count:1}},drop_chances:{head:0.0f,chest:0.0f,mainhand:0.0f}}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Comandante Óseo", "color": "white", "bold": true}
bossbar set so_events:boss max 110
bossbar set so_events:boss value 110
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Comandante Óseo!", "color": "red", "bold": false}]
