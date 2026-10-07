# Se ejecuta COMO cada jugador conectado (ver tick.mcfunction).
scoreboard objectives setdisplay sidebar so_sidebar

# Línea 1: nombre del servidor (texto fijo, número oculto).
scoreboard players set "VorNeX - OneBlock" so_sidebar 3
scoreboard players display name "VorNeX - OneBlock" so_sidebar {"text":"VorNeX - OneBlock","color":"gold","bold":true}
scoreboard players display numberformat "VorNeX - OneBlock" so_sidebar blank

# Línea 2: nombre real + rango del jugador. {selector:@s} se resuelve al nombre real.
scoreboard players set @s so_sidebar 2
scoreboard players display numberformat @s so_sidebar blank
execute as @s[team=so_admin] run scoreboard players display name @s so_sidebar [{"text":"[NeXAdmin] ","color":"red","bold":true},{"selector":"@s","color":"white"}]
execute as @s[team=so_vorlegend] run scoreboard players display name @s so_sidebar [{"text":"[VorLegend] ","color":"gold","bold":true},{"selector":"@s","color":"white"}]
execute as @s[team=so_nexlord] run scoreboard players display name @s so_sidebar [{"text":"[NeXLord] ","color":"light_purple","bold":true},{"selector":"@s","color":"white"}]
execute as @s[team=so_voruser] run scoreboard players display name @s so_sidebar [{"text":"VorUser: ","color":"gray"},{"selector":"@s","color":"white"}]

# Línea 3: tiempo jugado real (minecraft.custom:minecraft.play_time, en ticks -> segundos -> h/m/s)
scoreboard players operation #secs so_sys = @s so_playtime
scoreboard players operation #secs so_sys /= #20 so_sys
scoreboard players operation @s so_h = #secs so_sys
scoreboard players operation @s so_h /= #3600 so_sys
scoreboard players operation #rem so_sys = @s so_h
scoreboard players operation #rem so_sys *= #3600 so_sys
scoreboard players operation #secs2 so_sys = #secs so_sys
scoreboard players operation #secs2 so_sys -= #rem so_sys
scoreboard players operation @s so_m = #secs2 so_sys
scoreboard players operation @s so_m /= #60 so_sys
scoreboard players operation #rem2 so_sys = @s so_m
scoreboard players operation #rem2 so_sys *= #60 so_sys
scoreboard players operation #secs2 so_sys -= #rem2 so_sys
scoreboard players operation @s so_s = #secs2 so_sys
scoreboard players set @s so_sidebar 1
execute if score @s so_h matches 0..9 if score @s so_m matches 0..9 if score @s so_s matches 0..9 run scoreboard players display name @s so_sidebar [{"text":"0"},{"score":{"name":"@s","objective":"so_h"},"color":"white"},{"text":"h ","color":"gray"},{"text":"0"},{"score":{"name":"@s","objective":"so_m"},"color":"white"},{"text":"m ","color":"gray"},{"text":"0"},{"score":{"name":"@s","objective":"so_s"},"color":"white"},{"text":"s","color":"gray"}]
execute if score @s so_h matches 0..9 if score @s so_m matches 0..9 if score @s so_s matches 10.. run scoreboard players display name @s so_sidebar [{"text":"0"},{"score":{"name":"@s","objective":"so_h"},"color":"white"},{"text":"h ","color":"gray"},{"text":"0"},{"score":{"name":"@s","objective":"so_m"},"color":"white"},{"text":"m ","color":"gray"},{"score":{"name":"@s","objective":"so_s"},"color":"white"},{"text":"s","color":"gray"}]
execute if score @s so_h matches 0..9 if score @s so_m matches 10.. if score @s so_s matches 0..9 run scoreboard players display name @s so_sidebar [{"text":"0"},{"score":{"name":"@s","objective":"so_h"},"color":"white"},{"text":"h ","color":"gray"},{"score":{"name":"@s","objective":"so_m"},"color":"white"},{"text":"m ","color":"gray"},{"text":"0"},{"score":{"name":"@s","objective":"so_s"},"color":"white"},{"text":"s","color":"gray"}]
execute if score @s so_h matches 0..9 if score @s so_m matches 10.. if score @s so_s matches 10.. run scoreboard players display name @s so_sidebar [{"text":"0"},{"score":{"name":"@s","objective":"so_h"},"color":"white"},{"text":"h ","color":"gray"},{"score":{"name":"@s","objective":"so_m"},"color":"white"},{"text":"m ","color":"gray"},{"score":{"name":"@s","objective":"so_s"},"color":"white"},{"text":"s","color":"gray"}]
execute if score @s so_h matches 10.. if score @s so_m matches 0..9 if score @s so_s matches 0..9 run scoreboard players display name @s so_sidebar [{"score":{"name":"@s","objective":"so_h"},"color":"white"},{"text":"h ","color":"gray"},{"text":"0"},{"score":{"name":"@s","objective":"so_m"},"color":"white"},{"text":"m ","color":"gray"},{"text":"0"},{"score":{"name":"@s","objective":"so_s"},"color":"white"},{"text":"s","color":"gray"}]
execute if score @s so_h matches 10.. if score @s so_m matches 0..9 if score @s so_s matches 10.. run scoreboard players display name @s so_sidebar [{"score":{"name":"@s","objective":"so_h"},"color":"white"},{"text":"h ","color":"gray"},{"text":"0"},{"score":{"name":"@s","objective":"so_m"},"color":"white"},{"text":"m ","color":"gray"},{"score":{"name":"@s","objective":"so_s"},"color":"white"},{"text":"s","color":"gray"}]
execute if score @s so_h matches 10.. if score @s so_m matches 10.. if score @s so_s matches 0..9 run scoreboard players display name @s so_sidebar [{"score":{"name":"@s","objective":"so_h"},"color":"white"},{"text":"h ","color":"gray"},{"score":{"name":"@s","objective":"so_m"},"color":"white"},{"text":"m ","color":"gray"},{"text":"0"},{"score":{"name":"@s","objective":"so_s"},"color":"white"},{"text":"s","color":"gray"}]
execute if score @s so_h matches 10.. if score @s so_m matches 10.. if score @s so_s matches 10.. run scoreboard players display name @s so_sidebar [{"score":{"name":"@s","objective":"so_h"},"color":"white"},{"text":"h ","color":"gray"},{"score":{"name":"@s","objective":"so_m"},"color":"white"},{"text":"m ","color":"gray"},{"score":{"name":"@s","objective":"so_s"},"color":"white"},{"text":"s","color":"gray"}]
