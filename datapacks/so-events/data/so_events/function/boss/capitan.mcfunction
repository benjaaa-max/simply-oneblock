summon minecraft:vindicator ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Capitán Saqueador",color:"dark_red",bold:true},attributes:[{id:"minecraft:max_health",base:130d},{id:"minecraft:knockback_resistance",base:0.6d}],Health:130f,equipment:{head:{id:"minecraft:white_banner",count:1},mainhand:{id:"minecraft:{id:"minecraft:diamond_axe",count:1,components:{"minecraft:enchantments":{"minecraft:sharpness":1}}}",count:1}},drop_chances:{head:0.0f,mainhand:0.0f}}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Capitán Saqueador", "color": "dark_red", "bold": true}
bossbar set so_events:boss max 130
bossbar set so_events:boss value 130
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Capitán Saqueador!", "color": "red", "bold": false}]
