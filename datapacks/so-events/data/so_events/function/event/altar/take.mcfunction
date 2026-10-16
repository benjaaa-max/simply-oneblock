execute as @e[type=minecraft:item,distance=..4] if items entity @s contents #so_events:altar_tribute run function so_events:event/altar/add {m:1}
execute as @e[type=minecraft:item,distance=..4] if items entity @s contents #so_events:altar_ore run function so_events:event/altar/add {m:4}
execute as @e[type=minecraft:item,distance=..4] if items entity @s contents #so_events:altar_gem run function so_events:event/altar/add {m:16}
