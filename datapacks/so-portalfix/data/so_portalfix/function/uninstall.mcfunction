advancement revoke @a only so_portalfix:overworld_arrival
scoreboard objectives remove spf_escape
scoreboard objectives remove spf_deaths
scoreboard objectives remove spf_seen
scoreboard objectives remove spf_return
scoreboard objectives remove spf_tries
data remove storage so_portalfix:runtime initialized
tellraw @a [{"text":"[SO PortalFix] ","color":"gold"},{"text":"Datos del parche retirados. Desactiva y elimina el datapack.","color":"red"}]

scoreboard objectives remove spf_enter
scoreboard objectives remove spf_cd
scoreboard objectives remove spf_found
scoreboard objectives remove spf_tmp
advancement revoke @a only so_portalfix:dim_change
tag @a remove spf_noassist
