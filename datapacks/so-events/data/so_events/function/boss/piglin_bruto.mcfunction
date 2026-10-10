summon minecraft:piglin_brute ~ ~ ~ {Tags:["so_ev_mob","so_ev_boss"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Bruto del Nether",color:"gold",bold:true},attributes:[{id:"minecraft:max_health",base:120d},{id:"minecraft:knockback_resistance",base:0.6d}],Health:120f,IsImmuneToZombification:1b,equipment:{mainhand:{id:"minecraft:golden_axe",count:1,components:{"minecraft:enchantments":{"minecraft:sharpness":2}}}},drop_chances:{mainhand:0.0f}}
scoreboard players set #ok so_ev 1
bossbar set so_events:boss name {"text": "Bruto del Nether", "color": "gold", "bold": true}
bossbar set so_events:boss max 120
bossbar set so_events:boss value 120
bossbar set so_events:boss players @a
bossbar set so_events:boss visible true
playsound minecraft:entity.wither.spawn hostile @a ~ ~ ~ 0.6 1.3
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡Apareció Bruto del Nether!", "color": "red", "bold": false}]
