playsound minecraft:block.bell.use master @a[tag=so_ar_zone] ~ ~ ~ 2 1
execute unless score #mode so_ar matches 9 run return run title @s actionbar {"text": "La campana suena cuando hay un desafío preparado.", "color": "gray"}
execute unless entity @s[tag=so_ar_ready] run return run title @s actionbar {"text": "Solo los gladiadores del túnel pueden tocarla.", "color": "gray"}
function so_arenas:lib/go_fight
