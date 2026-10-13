$execute positioned ~$(dx) ~ ~$(dz) over motion_blocking_no_leaves run summon minecraft:falling_block ~ ~14 ~ {BlockState:{Name:"minecraft:magma_block"},Time:1,Tags:["so_ev_meteor"]}
$execute positioned ~$(dx) ~ ~$(dz) over motion_blocking_no_leaves run particle minecraft:flame ~ ~2 ~ 0.3 1 0.3 0.02 30
$execute positioned ~$(dx) ~ ~$(dz) over motion_blocking_no_leaves run loot spawn ~ ~1 ~ loot so_events:meteor
$execute positioned ~$(dx) ~ ~$(dz) over motion_blocking_no_leaves run playsound minecraft:entity.generic.explode master @a ~ ~ ~ 0.7 1.2
