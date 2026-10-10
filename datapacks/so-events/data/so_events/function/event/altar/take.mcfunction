execute as @e[type=minecraft:item,distance=..2,nbt={Item:{id:'minecraft:cobblestone'}}] run function so_events:event/altar/add
execute as @e[type=minecraft:item,distance=..2,nbt={Item:{id:'minecraft:cobblestone'}}] run kill @s
execute as @e[type=minecraft:item,distance=..2,nbt={Item:{id:'minecraft:deepslate'}}] run function so_events:event/altar/add
execute as @e[type=minecraft:item,distance=..2,nbt={Item:{id:'minecraft:deepslate'}}] run kill @s
execute as @e[type=minecraft:item,distance=..2,nbt={Item:{id:'#minecraft:logs'}}] run function so_events:event/altar/add
execute as @e[type=minecraft:item,distance=..2,nbt={Item:{id:'#minecraft:logs'}}] run kill @s
