scoreboard players set #done_533 sq_group 1
tellraw @a [{"text": "[Misiones] ", "color": "gold"}, {"text": "¡Meta de la Isla completada! ", "color": "light_purple"}, {"text": "Correr 50.000 bloques", "color": "white"}, {"text": " — todos pueden reclamar su parte con /trigger quests", "color": "gray"}]
title @a actionbar {text:"¡Meta de la Isla completada!",color:"light_purple"}
execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.7 1
