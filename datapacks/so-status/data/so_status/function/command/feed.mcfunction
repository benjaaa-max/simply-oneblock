execute unless entity @s[team=so_nexlord] run return run tellraw @s {"text":"[SO Status] Feed es exclusivo de NeXLord.","color":"red"}
execute if score @s so_cd_feed matches 1.. run return run tellraw @s {"text":"[SO Status] Feed todavía está enfriándose.","color":"yellow"}
effect give @s minecraft:saturation 1 4 true
scoreboard players set @s so_cd_feed 6000
playsound minecraft:entity.generic.eat player @s ~ ~ ~ 0.7 1
tellraw @s {"text":"[SO Status] Comida restaurada. Enfriamiento: 5 minutos.","color":"green"}
