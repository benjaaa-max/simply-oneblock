execute unless entity @s[team=so_vorlegend] run return run tellraw @s {"text":"[SO Status] Craft es exclusivo de VorLegend.","color":"red"}
execute positioned ^ ^ ^2 align xyz unless block ~ ~ ~ minecraft:air run return run tellraw @s {"text":"[SO Status] Mirá hacia un espacio libre cercano e intentá otra vez.","color":"red"}
execute positioned ^ ^ ^2 align xyz run summon minecraft:marker ~0.5 ~ ~0.5 {Tags:["so_status_temp","so_status_craft"]}
execute positioned ^ ^ ^2 align xyz run setblock ~ ~ ~ minecraft:crafting_table
playsound minecraft:block.wood.place player @s ~ ~ ~ 0.8 1
tellraw @s {"text":"[SO Status] Mesa temporal creada por 15 segundos.","color":"green"}
