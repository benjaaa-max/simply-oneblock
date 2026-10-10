function so_events:lib/begin
scoreboard players set #active so_ev 4
bossbar set so_events:ev name {"text": "Mercader errante", "color": "aqua"}
bossbar set so_events:ev max 300
bossbar set so_events:ev color blue
execute as @a[tag=so_ev_in,limit=1,sort=random] at @s run summon minecraft:wandering_trader ~ ~ ~ {Tags:["so_ev_mob"],Invulnerable:1b,NoAI:1b,PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Mercader de Eventos",color:"aqua",bold:true},Offers:{Recipes:[{buy:{id:"minecraft:emerald",count:10},sell:{id:"minecraft:diamond",count:1},maxUses:4},{buy:{id:"minecraft:emerald",count:6},sell:{id:"minecraft:golden_apple",count:1},maxUses:3},{buy:{id:"minecraft:emerald",count:4},sell:{id:"minecraft:ender_pearl",count:2},maxUses:4},{buy:{id:"minecraft:emerald",count:8},sell:{id:"minecraft:experience_bottle",count:16},maxUses:3},{buy:{id:"minecraft:emerald",count:16},sell:{id:"minecraft:netherite_scrap",count:1},maxUses:1},{buy:{id:"minecraft:emerald",count:12},sell:{id:"minecraft:heart_of_the_sea",count:1},maxUses:1},{buy:{id:"minecraft:diamond",count:2},sell:{id:"minecraft:emerald",count:24},maxUses:4},{buy:{id:"minecraft:emerald",count:20},sell:{id:"minecraft:totem_of_undying",count:1},maxUses:1}]}}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "Un mercader especial apareció en la isla por 5 minutos.", "color": "aqua", "bold": false}]
