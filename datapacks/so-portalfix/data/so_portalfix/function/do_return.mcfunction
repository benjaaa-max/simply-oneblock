# v4: emulate Simply OneBlock's return portal, but land beside the home gateway instead of on it.
scoreboard players set @s spf_found 1
scoreboard players set @s spf_cd 60
execute if dimension simply_oneblock:phase_3 run time set day
execute if dimension simply_oneblock:phase_10 run time set day
execute if dimension simply_oneblock:phase_13 run time set day
execute if dimension simply_oneblock:phase_18 run time set day
# Close the home portal like the original return does (only during phases 1-19, never the phase 20 permanent portal).
execute store result score #ob spf_tmp run scoreboard players get fake_player ib_minedcount
execute unless dimension simply_oneblock:phase_20 if score #ob spf_tmp matches ..15001 run scoreboard players set #pending spf_tmp 4
particle minecraft:reverse_portal ~ ~1 ~ 0.4 0.8 0.4 0.05 60 normal
playsound minecraft:block.portal.travel player @s ~ ~ ~ 0.3 1.6
execute in minecraft:overworld run teleport @s -2.5 65.0 0.5 facing 0.5 65.0 0.5
execute at @s run particle minecraft:reverse_portal ~ ~1 ~ 0.4 0.8 0.4 0.05 60 normal
