# A death or manual request in the Overworld is already safe unless it landed on the gateway.
execute if dimension minecraft:overworld unless predicate simply_oneblock:portal run scoreboard players set @s spf_return 0
execute if score @s spf_return matches 1 if dimension minecraft:overworld if predicate simply_oneblock:portal run function so_portalfix:push_out

# Change dimension explicitly when outside the Overworld.
execute if score @s spf_return matches 1 unless dimension minecraft:overworld in minecraft:overworld run teleport @s -2.5 65.0 0.5 facing 0.5 65.0 0.5

# v4: close the home portal only when coming back from a phase dimension (never from the Overworld itself).
execute if score @s spf_return matches 1 if predicate so_portalfix:in_phase store result score #ob spf_tmp run scoreboard players get fake_player ib_minedcount
execute if score @s spf_return matches 1 if predicate so_portalfix:in_phase if score #ob spf_tmp matches ..15001 run scoreboard players set #pending spf_tmp 4

# Check the player's actual dimension after teleporting; stop once the return worked.
execute at @s if dimension minecraft:overworld run scoreboard players set @s spf_return 0
execute if score @s spf_return matches 1 run scoreboard players add @s spf_tries 1
execute if score @s spf_return matches 1 if score @s spf_tries matches 40.. run function so_portalfix:return_failed