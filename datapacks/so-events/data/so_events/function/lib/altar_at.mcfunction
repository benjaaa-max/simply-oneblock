# Si hay lugar (3x3 libre y 3 de alto), arma el faro; si no, solo el altar flotante.
execute if block ~-1 ~ ~-1 #minecraft:air if block ~ ~ ~-1 #minecraft:air if block ~1 ~ ~-1 #minecraft:air if block ~-1 ~ ~ #minecraft:air if block ~ ~ ~ #minecraft:air if block ~1 ~ ~ #minecraft:air if block ~-1 ~ ~1 #minecraft:air if block ~ ~ ~1 #minecraft:air if block ~1 ~ ~1 #minecraft:air if block ~ ~1 ~ #minecraft:air if block ~ ~2 ~ #minecraft:air run function so_events:event/altar/build
execute unless entity @e[tag=so_ev_beacon] if block ~ ~ ~ #minecraft:air run summon minecraft:block_display ~-0.5 ~0.5 ~-0.5 {Tags:["so_ev_altar"],block_state:{Name:"minecraft:end_portal_frame"},brightness:{sky:15,block:15},glowing:1b}
particle minecraft:flame ~ ~1 ~ 0.4 0.4 0.4 0.02 30
