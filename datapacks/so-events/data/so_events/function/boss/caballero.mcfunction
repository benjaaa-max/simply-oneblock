summon minecraft:wither_skeleton ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Caballero del Nether",color:"dark_purple",bold:true},attributes:[{id:"minecraft:max_health",base:160d},{id:"minecraft:knockback_resistance",base:0.6d}],Health:160f,equipment:{head:{id:"minecraft:netherite_helmet",count:1},mainhand:{id:"minecraft:netherite_sword",count:1,components:{"minecraft:enchantments":{"minecraft:sharpness":2}}}},drop_chances:{head:0.0f,mainhand:0.0f}}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Caballero del Nether", "color": "dark_purple", "bold": true}
bossbar set so_events:boss max 160
bossbar set so_events:boss value 160
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Caballero del Nether!", "color": "red", "bold": false}]
