# so_status :: carga idempotente; /reload no reinicia progreso ni enfriamientos.
scoreboard objectives add so_sys dummy
scoreboard objectives add so_cfg dummy
scoreboard objectives add so_playtime minecraft.custom:minecraft.play_time
scoreboard objectives add so_sidebar dummy {"text":"VorNeX • Tiempo (min)","color":"gold","bold":true}
scoreboard objectives add so_core dummy
scoreboard objectives add so_cd_heal dummy
scoreboard objectives add so_cd_feed dummy
scoreboard objectives add so_temp_age dummy
scoreboard objectives add heal trigger
scoreboard objectives add feed trigger
scoreboard objectives add craft trigger
scoreboard objectives add enderchest trigger
scoreboard objectives add hat trigger
scoreboard objectives add afk trigger
execute unless score #enabled so_cfg matches -2147483648.. run scoreboard players set #enabled so_cfg 1
execute unless score #hud_on so_cfg matches -2147483648.. run scoreboard players set #hud_on so_cfg 1
execute unless score #bar_on so_cfg matches -2147483648.. run scoreboard players set #bar_on so_cfg 1
execute unless score #beat so_sys matches -2147483648.. run scoreboard players set #beat so_sys 0
scoreboard players set #20 so_sys 20
scoreboard players set #60 so_sys 60
scoreboard players set #100 so_sys 100
scoreboard players set #1200 so_sys 1200
bossbar add so_status:progress {"text":"Progreso del OneBlock","color":"green"}
bossbar set so_status:progress color green
bossbar set so_status:progress max 100
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
team modify so_voruser prefix {"text":"[VorUser] ","color":"gray"}
team modify so_voruser color gray
tellraw @a[tag=oneblock_admin] [{"text":"[SO Status] ","color":"gold"},{"text":"cargado. Ayuda: /function so_status:admin/help","color":"gray"}]
