# 'if items' sí acepta tags de ítem (las NBT con # no funcionan).
execute as @e[type=minecraft:item,distance=..3.5] if items entity @s contents #so_events:altar_tribute run function so_events:event/altar/add
