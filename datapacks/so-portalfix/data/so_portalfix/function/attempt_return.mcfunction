# A death or manual request in the Overworld is already safe unless it landed on the gateway.
execute if dimension minecraft:overworld unless predicate simply_oneblock:portal run scoreboard players set @s spf_return 0
execute if score @s spf_return matches 1 if dimension minecraft:overworld if predicate simply_oneblock:portal run function so_portalfix:push_out

# Change dimension explicitly when outside the Overworld.
execute if score @s spf_return matches 1 unless dimension minecraft:overworld run execute in minecraft:overworld run teleport @s -2.5 65.0 0.5 facing 0.5 65.0 0.5

#Remove the temporary portal column from the overworld.
execute if score @s spf_return matches 1 run execute in minecraft:overworld run fill 0 64 0 0 66 0 minecraft:air replace

# Check the player's actual dimension after teleporting; stop once the return worked.
execute at @s if dimension minecraft:overworld run scoreboard players set @s spf_return 0
execute if score @s spf_return matches 1 run scoreboard players add @s spf_tries 1
execute if score @s spf_return matches 1 if score @s spf_tries matches 40.. run function so_portalfix:return_failed