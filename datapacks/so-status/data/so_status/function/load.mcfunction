# so_status :: load -- idempotente, no reinicia nada en /reload.

scoreboard objectives add so_sys dummy
scoreboard objectives add so_cfg dummy
scoreboard objectives add so_playtime minecraft.custom:minecraft.play_time
scoreboard objectives add so_h dummy
scoreboard objectives add so_m dummy
scoreboard objectives add so_s dummy
scoreboard objectives add so_sidebar dummy

execute unless score #enabled so_cfg matches -2147483648.. run scoreboard players set #enabled so_cfg 1
execute unless score #hud_on so_cfg matches -2147483648.. run scoreboard players set #hud_on so_cfg 1
execute unless score #bar_on so_cfg matches -2147483648.. run scoreboard players set #bar_on so_cfg 1
execute unless score #beat so_sys matches -2147483648.. run scoreboard players set #beat so_sys 0
execute unless score #20 so_sys matches -2147483648.. run scoreboard players set #20 so_sys 20
execute unless score #60 so_sys matches -2147483648.. run scoreboard players set #60 so_sys 60
execute unless score #3600 so_sys matches -2147483648.. run scoreboard players set #3600 so_sys 3600
execute unless score #100 so_sys matches -2147483648.. run scoreboard players set #100 so_sys 100

# Salvaguarda: so_core siempre existe como OBJETIVO para consultarlo sin 'Unknown
# scoreboard objective', exista o no el datapack so_core real (pendiente).
scoreboard objectives add so_core dummy

bossbar add so_status:progress {"text":"Progreso del OneBlock","color":"green"}
bossbar set so_status:progress visible true
bossbar set so_status:progress players @a
bossbar set so_status:progress color green

# ----- equipos / rangos: un jugador solo puede estar en un equipo de Minecraft a la
# vez, así que el equipo ES el rango, sin necesitar un scoreboard aparte.
team add so_admin
team modify so_admin displayName {"text":"NeXAdmin"}
team modify so_admin prefix {"text":"[NeXAdmin] ","color":"red","bold":true}
team modify so_admin color red
team add so_vorlegend
team modify so_vorlegend displayName {"text":"VorLegend"}
team modify so_vorlegend prefix {"text":"[VorLegend] ","color":"gold","bold":true}
team modify so_vorlegend color gold
team add so_nexlord
team modify so_nexlord displayName {"text":"NeXLord"}
team modify so_nexlord prefix {"text":"[NeXLord] ","color":"light_purple","bold":true}
team modify so_nexlord color light_purple
team add so_voruser
team modify so_voruser displayName {"text":"VorUser"}
team modify so_voruser prefix {"text":""}
team modify so_voruser color white
