execute unless entity @s[team=so_vorlegend] run return run tellraw @s {"text":"[SO Status] Heal es exclusivo de VorLegend.","color":"red"}
execute if score @s so_cd_heal matches 1.. run return run tellraw @s [{"text":"[SO Status] Heal estará listo en ","color":"yellow"},{"score":{"name":"@s","objective":"so_cd_heal"},"color":"white"},{"text":" ticks.","color":"yellow"}]
effect give @s minecraft:instant_health 1 4 true
effect give @s minecraft:saturation 1 4 true
scoreboard players set @s so_cd_heal 6000
playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.4
tellraw @s {"text":"[SO Status] Vida y comida restauradas. Enfriamiento: 5 minutos.","color":"green"}
