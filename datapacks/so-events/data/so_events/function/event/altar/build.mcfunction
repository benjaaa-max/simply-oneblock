fill ~-1 ~ ~-1 ~1 ~ ~1 minecraft:iron_block
setblock ~ ~1 ~ minecraft:beacon
setblock ~ ~2 ~ minecraft:purple_stained_glass
summon minecraft:marker ~ ~ ~ {Tags:["so_ev_beacon"]}
summon minecraft:block_display ~-0.5 ~3 ~-0.5 {Tags:["so_ev_altar"],block_state:{Name:"minecraft:end_portal_frame",Properties:{eye:"true"}},brightness:{sky:15,block:15},glowing:1b}
playsound minecraft:block.beacon.activate master @a ~ ~ ~ 2 1
