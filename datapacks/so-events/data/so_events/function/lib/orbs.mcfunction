execute store result storage so_events:tmp dx int 1 run random value -6..6
execute store result storage so_events:tmp dz int 1 run random value -6..6
function so_events:lib/orb_spawn with storage so_events:tmp
