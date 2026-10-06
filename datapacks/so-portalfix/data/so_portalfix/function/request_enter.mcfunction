scoreboard players set @s spf_enter 0
function so_portalfix:search_far
execute if score @s spf_found matches 0 run tellraw @s [{"text":"[SO PortalFix] ","color":"gold"},{"text":"No hay ningún portal a menos de 3 bloques. Acércate al portal y vuelve a intentarlo.","color":"red"}]
