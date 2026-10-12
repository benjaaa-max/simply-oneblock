scoreboard players set #dgs so_ar 6
give @a[tag=so_ar_dgp] minecraft:tripwire_hook[custom_name={text:"Llave de Sala",color:"gold",italic:false},custom_data={so_ar_dgkey:1b},lore=[{text:"Abre la reja del jefe",color:"gray",italic:false}]] 1
execute store result score #r so_ar run random value 1..10
setblock -4994 60 -5044 minecraft:barrel[facing=up]
execute if score #r so_ar matches ..4 run loot insert -4994 60 -5044 loot so_arenas:dg_secret
execute if score #r so_ar matches 5.. run loot insert -4994 60 -5044 loot so_arenas:dg_room
execute if score #r so_ar matches ..4 run tellraw @a[tag=so_ar_dgp] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "¡Barril secreto! Algo brilla adentro.", "color": "gold", "bold": false}]
execute as @a[tag=so_ar_dgp] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.2
title @a[tag=so_ar_dgp] title {"text": "¡Llave de Sala!", "color": "gold", "bold": true}
tellraw @a[tag=so_ar_dgp] [{"text": "[Catacumbas] ", "color": "dark_purple", "bold": true}, {"text": "Sala despejada: recibieron la Llave de Sala. Acercate con ella a la reja del jefe (al este).", "color": "gold", "bold": false}]
