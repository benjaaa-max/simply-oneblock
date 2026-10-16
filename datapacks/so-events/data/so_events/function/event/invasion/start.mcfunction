function so_events:lib/begin
scoreboard players set #active so_ev 5
execute as @a[tag=so_ev_in] at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 1 1
execute as @a[tag=so_ev_in] at @s run playsound minecraft:music_disc.pigstep record @s ~ ~ ~ 0.6 1
execute if score #force_tier so_ev matches 1..3 run scoreboard players operation #tier so_ev = #force_tier so_ev
scoreboard players set #force_tier so_ev 0
scoreboard players set #stage so_ev 0
scoreboard players set #wave so_ev 0
function so_events:lib/no_grief
execute unless score #force_type so_ev matches 1..20 run function so_events:event/invasion/pick
execute if score #force_type so_ev matches 1..20 run scoreboard players operation #type so_ev = #force_type so_ev
scoreboard players set #force_type so_ev 0
# Invasión alfa: 10% de chance (o forzada por admin).
execute store result score #alpha so_ev run random value 1..10
execute if score #alpha_force so_ev matches 1 run scoreboard players set #alpha so_ev 1
execute if score #alpha so_ev matches 2.. run scoreboard players set #alpha so_ev 0
bossbar set so_events:ev color red
bossbar set so_events:ev max 10
execute if score #type so_ev matches 1 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Horda de zombis!", "color": "dark_green", "bold": true}
execute if score #type so_ev matches 1 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Horda de zombis! [Nivel II]", "color": "dark_green", "bold": true}
execute if score #type so_ev matches 1 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Horda de zombis! [Nivel III]", "color": "dark_green", "bold": true}
execute if score #type so_ev matches 2 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Ataque de slimes!", "color": "green", "bold": true}
execute if score #type so_ev matches 2 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Ataque de slimes! [Nivel II]", "color": "green", "bold": true}
execute if score #type so_ev matches 2 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Ataque de slimes! [Nivel III]", "color": "green", "bold": true}
execute if score #type so_ev matches 3 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Oleada acorazada!", "color": "gray", "bold": true}
execute if score #type so_ev matches 3 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Oleada acorazada! [Nivel II]", "color": "gray", "bold": true}
execute if score #type so_ev matches 3 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Oleada acorazada! [Nivel III]", "color": "gray", "bold": true}
execute if score #type so_ev matches 4 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Raid de saqueadores!", "color": "dark_red", "bold": true}
execute if score #type so_ev matches 4 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Raid de saqueadores! [Nivel II]", "color": "dark_red", "bold": true}
execute if score #type so_ev matches 4 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Raid de saqueadores! [Nivel III]", "color": "dark_red", "bold": true}
execute if score #type so_ev matches 5 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Invasión del Nether!", "color": "dark_purple", "bold": true}
execute if score #type so_ev matches 5 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Invasión del Nether! [Nivel II]", "color": "dark_purple", "bold": true}
execute if score #type so_ev matches 5 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Invasión del Nether! [Nivel III]", "color": "dark_purple", "bold": true}
execute if score #type so_ev matches 6 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Invasión del End!", "color": "light_purple", "bold": true}
execute if score #type so_ev matches 6 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Invasión del End! [Nivel II]", "color": "light_purple", "bold": true}
execute if score #type so_ev matches 6 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Invasión del End! [Nivel III]", "color": "light_purple", "bold": true}
execute if score #type so_ev matches 7 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Plaga de artrópodos!", "color": "dark_red", "bold": true}
execute if score #type so_ev matches 7 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Plaga de artrópodos! [Nivel II]", "color": "dark_red", "bold": true}
execute if score #type so_ev matches 7 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Plaga de artrópodos! [Nivel III]", "color": "dark_red", "bold": true}
execute if score #type so_ev matches 8 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Asedio marino!", "color": "aqua", "bold": true}
execute if score #type so_ev matches 8 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Asedio marino! [Nivel II]", "color": "aqua", "bold": true}
execute if score #type so_ev matches 8 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Asedio marino! [Nivel III]", "color": "aqua", "bold": true}
execute if score #type so_ev matches 9 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Prueba ominosa!", "color": "dark_aqua", "bold": true}
execute if score #type so_ev matches 9 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Prueba ominosa! [Nivel II]", "color": "dark_aqua", "bold": true}
execute if score #type so_ev matches 9 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Prueba ominosa! [Nivel III]", "color": "dark_aqua", "bold": true}
execute if score #type so_ev matches 10 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Tormenta de huesos!", "color": "white", "bold": true}
execute if score #type so_ev matches 10 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Tormenta de huesos! [Nivel II]", "color": "white", "bold": true}
execute if score #type so_ev matches 10 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Tormenta de huesos! [Nivel III]", "color": "white", "bold": true}
execute if score #type so_ev matches 11 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Rebelión de gólems!", "color": "gray", "bold": true}
execute if score #type so_ev matches 11 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Rebelión de gólems! [Nivel II]", "color": "gray", "bold": true}
execute if score #type so_ev matches 11 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Rebelión de gólems! [Nivel III]", "color": "gray", "bold": true}
execute if score #type so_ev matches 12 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Ilusionismo oscuro!", "color": "dark_aqua", "bold": true}
execute if score #type so_ev matches 12 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Ilusionismo oscuro! [Nivel II]", "color": "dark_aqua", "bold": true}
execute if score #type so_ev matches 12 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Ilusionismo oscuro! [Nivel III]", "color": "dark_aqua", "bold": true}
execute if score #type so_ev matches 13 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Asalto del Bastión!", "color": "gold", "bold": true}
execute if score #type so_ev matches 13 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Asalto del Bastión! [Nivel II]", "color": "gold", "bold": true}
execute if score #type so_ev matches 13 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Asalto del Bastión! [Nivel III]", "color": "gold", "bold": true}
execute if score #type so_ev matches 14 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Caza del Warden!", "color": "dark_blue", "bold": true}
execute if score #type so_ev matches 14 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Caza del Warden! [Nivel II]", "color": "dark_blue", "bold": true}
execute if score #type so_ev matches 14 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Caza del Warden! [Nivel III]", "color": "dark_blue", "bold": true}
execute if score #type so_ev matches 15 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Enjambre del cielo!", "color": "dark_gray", "bold": true}
execute if score #type so_ev matches 15 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Enjambre del cielo! [Nivel II]", "color": "dark_gray", "bold": true}
execute if score #type so_ev matches 15 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Enjambre del cielo! [Nivel III]", "color": "dark_gray", "bold": true}
execute if score #type so_ev matches 16 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Marea anciana!", "color": "aqua", "bold": true}
execute if score #type so_ev matches 16 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Marea anciana! [Nivel II]", "color": "aqua", "bold": true}
execute if score #type so_ev matches 16 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Marea anciana! [Nivel III]", "color": "aqua", "bold": true}
execute if score #type so_ev matches 17 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Aquelarre de brujas!", "color": "dark_purple", "bold": true}
execute if score #type so_ev matches 17 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Aquelarre de brujas! [Nivel II]", "color": "dark_purple", "bold": true}
execute if score #type so_ev matches 17 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Aquelarre de brujas! [Nivel III]", "color": "dark_purple", "bold": true}
execute if score #type so_ev matches 18 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Furia de llamas!", "color": "red", "bold": true}
execute if score #type so_ev matches 18 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Furia de llamas! [Nivel II]", "color": "red", "bold": true}
execute if score #type so_ev matches 18 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Furia de llamas! [Nivel III]", "color": "red", "bold": true}
execute if score #type so_ev matches 19 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Horda zombificada!", "color": "dark_green", "bold": true}
execute if score #type so_ev matches 19 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Horda zombificada! [Nivel II]", "color": "dark_green", "bold": true}
execute if score #type so_ev matches 19 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Horda zombificada! [Nivel III]", "color": "dark_green", "bold": true}
execute if score #type so_ev matches 20 if score #tier so_ev matches 1 run bossbar set so_events:ev name {"text": "¡Vanguardia del Mal!", "color": "dark_red", "bold": true}
execute if score #type so_ev matches 20 if score #tier so_ev matches 2 run bossbar set so_events:ev name {"text": "¡Vanguardia del Mal! [Nivel II]", "color": "dark_red", "bold": true}
execute if score #type so_ev matches 20 if score #tier so_ev matches 3 run bossbar set so_events:ev name {"text": "¡Vanguardia del Mal! [Nivel III]", "color": "dark_red", "bold": true}
execute if score #type so_ev matches 1 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Horda de zombis en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 1 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Horda de zombis [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 1 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Horda de zombis [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 2 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Ataque de slimes en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 2 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Ataque de slimes [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 2 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Ataque de slimes [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 3 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Oleada acorazada en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 3 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Oleada acorazada [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 3 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Oleada acorazada [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 4 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Raid de saqueadores en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 4 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Raid de saqueadores [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 4 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Raid de saqueadores [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 5 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Invasión del Nether en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 5 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Invasión del Nether [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 5 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Invasión del Nether [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 6 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Invasión del End en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 6 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Invasión del End [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 6 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Invasión del End [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 7 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Plaga de artrópodos en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 7 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Plaga de artrópodos [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 7 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Plaga de artrópodos [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 8 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Asedio marino en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 8 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Asedio marino [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 8 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Asedio marino [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 9 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Prueba ominosa en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 9 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Prueba ominosa [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 9 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Prueba ominosa [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 10 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Tormenta de huesos en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 10 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Tormenta de huesos [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 10 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Tormenta de huesos [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 11 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Rebelión de gólems en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 11 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Rebelión de gólems [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 11 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Rebelión de gólems [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 12 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Ilusionismo oscuro en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 12 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Ilusionismo oscuro [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 12 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Ilusionismo oscuro [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 13 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Asalto del Bastión en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 13 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Asalto del Bastión [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 13 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Asalto del Bastión [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 14 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Caza del Warden en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 14 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Caza del Warden [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 14 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Caza del Warden [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 15 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Enjambre del cielo en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 15 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Enjambre del cielo [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 15 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Enjambre del cielo [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 16 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Marea anciana en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 16 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Marea anciana [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 16 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Marea anciana [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 17 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Aquelarre de brujas en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 17 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Aquelarre de brujas [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 17 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Aquelarre de brujas [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 18 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Furia de llamas en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 18 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Furia de llamas [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 18 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Furia de llamas [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 19 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Horda zombificada en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 19 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Horda zombificada [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 19 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Horda zombificada [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 20 if score #tier so_ev matches 1 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Vanguardia del Mal en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 20 if score #tier so_ev matches 2 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Vanguardia del Mal [Nivel II] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #type so_ev matches 20 if score #tier so_ev matches 3 run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "¡ALERTA! Vanguardia del Mal [Nivel III] en 10 segundos. Defiendan la isla.", "color": "red", "bold": true}]
execute if score #tier so_ev matches 2.. run tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "La isla ya es fuerte: los invasores vienen reforzados y la recompensa es mayor.", "color": "gold", "bold": false}]
playsound minecraft:event.raid.horn master @a ~ ~ ~ 1 1
