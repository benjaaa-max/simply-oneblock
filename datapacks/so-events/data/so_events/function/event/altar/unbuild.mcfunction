fill ~-1 ~ ~-1 ~1 ~ ~1 minecraft:air replace minecraft:iron_block
execute if block ~ ~1 ~ minecraft:beacon run setblock ~ ~1 ~ minecraft:air
execute if block ~ ~2 ~ #minecraft:impermeable run setblock ~ ~2 ~ minecraft:air
playsound minecraft:block.beacon.deactivate master @a ~ ~ ~ 2 1
kill @s
