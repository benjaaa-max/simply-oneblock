# Devuelve el disco al piso del túnel (no desaparece) y apaga el tocadiscos para no duplicar la música.
summon minecraft:item -5003 97.2 -4964 {Tags:["so_ar_disc"],Age:-32768s,PickupDelay:10s,Item:{id:"minecraft:stone",count:1}}
data modify entity @e[type=minecraft:item,tag=so_ar_disc,limit=1] Item set from block -5003 96 -4965 RecordItem
tag @e[type=minecraft:item,tag=so_ar_disc] remove so_ar_disc
setblock -5003 96 -4965 minecraft:air
setblock -5003 96 -4965 minecraft:jukebox
