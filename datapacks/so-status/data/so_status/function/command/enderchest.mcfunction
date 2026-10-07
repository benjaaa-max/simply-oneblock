execute unless entity @s[team=so_vorlegend] unless entity @s[team=so_nexlord] run return run tellraw @s {"text":"[SO Status] Enderchest requiere NeXLord o VorLegend.","color":"red"}
execute positioned ^ ^ ^2 align xyz unless block ~ ~ ~ minecraft:air run return run tellraw @s {"text":"[SO Status] Mirá hacia un espacio libre cercano e intentá otra vez.","color":"red"}
execute positioned ^ ^ ^2 align xyz run summon minecraft:marker ~0.5 ~ ~0.5 {Tags:["so_status_temp","so_status_ender"]}
execute positioned ^ ^ ^2 align xyz run setblock ~ ~ ~ minecraft:ender_chest
playsound minecraft:block.ender_chest.open player @s ~ ~ ~ 0.8 1
tellraw @s {"text":"[SO Status] Cofre de Ender temporal creado por 15 segundos.","color":"green"}
