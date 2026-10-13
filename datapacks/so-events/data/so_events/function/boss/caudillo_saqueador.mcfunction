summon minecraft:ravager ~ ~ ~ {Tags:["so_ev_mob"],PersistenceRequired:1b,Passengers:[{id:"minecraft:pillager",Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Caudillo Saqueador",color:"red",bold:true},attributes:[{id:"minecraft:max_health",base:160d},{id:"minecraft:knockback_resistance",base:0.6d}],Health:160f,equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1},mainhand:{id:"minecraft:crossbow",count:1,components:{"minecraft:enchantments":{"minecraft:piercing":2}}}},drop_chances:{head:0.0f,chest:0.0f,mainhand:0.0f}}]}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Caudillo Saqueador", "color": "red", "bold": true}
bossbar set so_events:boss max 160
bossbar set so_events:boss value 160
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Caudillo Saqueador!", "color": "red", "bold": false}]
