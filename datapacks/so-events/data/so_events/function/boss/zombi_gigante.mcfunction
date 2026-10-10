summon minecraft:zombie ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Zombi Colosal",color:"dark_green",bold:true},attributes:[{id:"minecraft:max_health",base:200d},{id:"minecraft:knockback_resistance",base:0.6d},{id:"minecraft:scale",base:2d}],Health:200f,equipment:{head:{id:"minecraft:diamond_helmet",count:1,components:{"minecraft:enchantments":{"minecraft:protection":1,"minecraft:thorns":1}}},chest:{id:"minecraft:diamond_chestplate",count:1,components:{"minecraft:enchantments":{"minecraft:protection":1,"minecraft:thorns":1}}},legs:{id:"minecraft:diamond_leggings",count:1,components:{"minecraft:enchantments":{"minecraft:protection":1,"minecraft:thorns":1}}},feet:{id:"minecraft:diamond_boots",count:1,components:{"minecraft:enchantments":{"minecraft:protection":1,"minecraft:thorns":1}}},mainhand:{id:"minecraft:diamond_sword",count:1}},drop_chances:{head:0.0f,chest:0.0f,legs:0.0f,feet:0.0f,mainhand:0.0f}}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Zombi Colosal", "color": "dark_green", "bold": true}
bossbar set so_events:boss max 200
bossbar set so_events:boss value 200
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Zombi Colosal!", "color": "red", "bold": false}]
