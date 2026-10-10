summon minecraft:piglin_brute ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Caudillo Bruto",color:"gold",bold:true},attributes:[{id:"minecraft:max_health",base:180d},{id:"minecraft:knockback_resistance",base:0.6d}],Health:180f,IsImmuneToZombification:1b,equipment:{chest:{id:"minecraft:netherite_chestplate",count:1},mainhand:{id:"minecraft:golden_axe",count:1,components:{"minecraft:enchantments":{"minecraft:sharpness":3}}}},drop_chances:{chest:0.0f,mainhand:0.0f}}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Caudillo Bruto", "color": "gold", "bold": true}
bossbar set so_events:boss max 180
bossbar set so_events:boss value 180
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Caudillo Bruto!", "color": "red", "bold": false}]
