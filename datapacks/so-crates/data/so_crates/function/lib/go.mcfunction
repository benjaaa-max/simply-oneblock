execute unless dimension minecraft:overworld run return run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Solo podés viajar desde el mundo normal (no desde el Nether, el End ni las dimensiones de fase).","color":"red"}]
execute if entity @s[tag=so_cr_in] run return run tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Ya estás en el templo. Para volver: /trigger isla","color":"yellow"}]
execute store result score @s so_cr_x run data get entity @s Pos[0]
execute store result score @s so_cr_y run data get entity @s Pos[1]
execute store result score @s so_cr_z run data get entity @s Pos[2]
scoreboard players set @s so_cr_saved 1
tp @s 5000.5 101 5012.5 180 0
playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 1 1
tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Bienvenido al Templo de las Bóvedas. Oeste: llaves Simply · Este: especiales · Norte: Forja de Llaves. Volver: ","color":"green"},{"text":"/trigger isla","color":"yellow","click_event":{"action":"run_command","command":"/trigger isla"}}]
