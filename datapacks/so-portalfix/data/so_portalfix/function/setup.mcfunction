scoreboard objectives add spf_escape trigger
scoreboard objectives add spf_deaths deathCount
scoreboard objectives add spf_seen dummy
scoreboard objectives add spf_return dummy
scoreboard objectives add spf_tries dummy
data modify storage so_portalfix:runtime initialized set value 1b
tellraw @a [{"text":"[SO PortalFix] ","color":"gold"},{"text":"Salida segura cargada. Usa /trigger spf_escape set 1 si quedas atrapado.","color":"green"}]
scoreboard objectives add spf_enter trigger
scoreboard objectives add spf_cd dummy
scoreboard objectives add spf_found dummy
