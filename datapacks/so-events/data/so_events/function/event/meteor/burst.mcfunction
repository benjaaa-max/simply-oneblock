execute store result storage so_events:tmp dx int 1 run random value -10..10
execute store result storage so_events:tmp dz int 1 run random value -10..10
function so_events:event/meteor/fall with storage so_events:tmp
