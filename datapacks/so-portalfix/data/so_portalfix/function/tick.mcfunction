# Keep the escape trigger available to every online player.
scoreboard players enable @a spf_escape

# Detect new deaths without treating an old death score as a new death after reload.
scoreboard players add @a spf_deaths 0
execute as @a unless score @s spf_seen matches -2147483648..2147483647 run scoreboard players operation @s spf_seen = @s spf_deaths
execute as @a if score @s spf_deaths > @s spf_seen run function so_portalfix:after_death
execute as @a run scoreboard players operation @s spf_seen = @s spf_deaths

# A player can request a return from any dimension with /trigger spf_escape set 1.
execute as @a[scores={spf_escape=1..}] at @s run function so_portalfix:request_escape

# Retry a requested/death-triggered return briefly if the host delays dimension changes.
execute as @a[scores={spf_return=1..}] at @s run function so_portalfix:attempt_return

# Backup for anyone who is still standing on the active home gateway.
execute as @a at @s if dimension minecraft:overworld if predicate simply_oneblock:portal run function so_portalfix:push_out

# v3 - Bedrock/Geyser portal assist.
scoreboard players enable @a spf_enter
scoreboard players remove @a[scores={spf_cd=1..}] spf_cd 1
execute as @a[scores={spf_enter=1..}] at @s run function so_portalfix:request_enter
execute as @a[tag=!spf_noassist] unless score @s spf_cd matches 1.. at @s run function so_portalfix:assist_near
