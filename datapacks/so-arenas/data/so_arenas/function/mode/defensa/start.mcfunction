setblock -5000 96 -5000 minecraft:crying_obsidian
summon minecraft:villager -4999.5 97 -4999.5 {Tags:["so_ar_bait"],NoAI:1b,Silent:1b,PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Núcleo Vivo",color:"dark_purple",bold:true},VillagerData:{profession:"minecraft:cleric",level:5,type:"minecraft:plains"},attributes:[{id:"minecraft:max_health",base:1024d},{id:"minecraft:knockback_resistance",base:1d}],Health:1024f,active_effects:[{id:"minecraft:glowing",amplifier:0b,duration:-1,show_particles:0b}]}
scoreboard players set #mode so_ar 3
scoreboard players set #hp so_ar 100
scoreboard players set #anticamp so_ar 0
bossbar set so_arenas:fight color purple
bossbar set so_arenas:fight max 100
bossbar set so_arenas:fight value 100
bossbar set so_arenas:fight name {"text": "Núcleo", "color": "dark_purple"}
execute as @a[tag=so_ar_in] run function so_arenas:lib/kit_def
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Contrato: protegé al Núcleo Vivo 2 minutos. Cada golpe que recibe baja la vida del núcleo (no le pegues vos). Usá las barricadas; acá la altura está permitida.", "color": "dark_purple", "bold": false}]
function so_arenas:mode/defensa/wave
