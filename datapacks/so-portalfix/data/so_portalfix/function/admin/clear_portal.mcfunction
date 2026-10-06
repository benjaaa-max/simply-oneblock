# v4 admin: force-close the home portal (same as returning through it).
scoreboard players set #pending spf_tmp 4
tellraw @s [{"text":"[SO PortalFix] ","color":"gold"},{"text":"Cerrando el portal de la isla...","color":"green"}]
