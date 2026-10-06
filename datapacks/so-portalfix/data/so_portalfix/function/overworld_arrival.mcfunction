# This advancement fires on every dimension change into the Overworld.
# Only redirect if the arrival point is the active OneBlock gateway.
execute if dimension minecraft:overworld if predicate simply_oneblock:portal run function so_portalfix:push_out
advancement revoke @s only so_portalfix:overworld_arrival