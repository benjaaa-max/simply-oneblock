summon minecraft:zombie ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Rey Zombi",color:"dark_green",bold:true},attributes:[{id:"minecraft:max_health",base:120d},{id:"minecraft:knockback_resistance",base:0.6d}],Health:120f,equipment:{head:{id:"minecraft:golden_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1},mainhand:{id:"minecraft:iron_sword",count:1,components:{"minecraft:enchantments":{"minecraft:sharpness":2}}}},drop_chances:{head:0.0f,chest:0.0f,mainhand:0.0f}}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Rey Zombi", "color": "dark_green", "bold": true}
bossbar set so_events:boss max 120
bossbar set so_events:boss value 120
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Rey Zombi!", "color": "red", "bold": false}]
