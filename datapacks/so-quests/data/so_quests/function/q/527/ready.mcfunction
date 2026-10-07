scoreboard players set #done_527 sq_group 1
tellraw @a [{"text": "[Misiones] ", "color": "gold"}, {"text": "¡Meta de la Isla completada! ", "color": "light_purple"}, {"text": "Hornear 500 panes", "color": "white"}, {"text": " — todos pueden reclamar su parte con /trigger quests", "color": "gray"}]
title @a actionbar {text:"¡Meta de la Isla completada!",color:"light_purple"}
execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.7 1
