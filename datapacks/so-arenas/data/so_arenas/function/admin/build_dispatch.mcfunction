function so_arenas:admin/build_01
function so_arenas:admin/build_02
function so_arenas:admin/build_03
function so_arenas:admin/build_04
function so_arenas:admin/build_05
function so_arenas:admin/build_06
function so_arenas:admin/build_07
function so_arenas:admin/build_08
function so_arenas:admin/build_09
function so_arenas:admin/build_10
summon minecraft:villager -5003 95 -4929 {NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomNameVisible:1b,CustomName:{text:"Comandante de Contratos",color:"aqua",bold:true}}
summon minecraft:villager -4997 95 -4929 {NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,CustomNameVisible:1b,CustomName:{text:"Maestro de Armas",color:"yellow",bold:true}}
execute positioned -5000 96 -5000 run setblock ~ 96 ~ minecraft:crying_obsidian
execute positioned -5000 96 -5000 run setblock ~ 96 ~ minecraft:air
tellraw @a [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "¡El Coliseo VorNeX está listo!", "color": "green", "bold": false}]
playsound minecraft:ui.toast.challenge_complete master @a ~ ~ ~ 1 1
