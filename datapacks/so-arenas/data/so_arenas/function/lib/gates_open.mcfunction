function so_arenas:lib/gate_pit_open
fill -5003 96 -4940 -4997 100 -4940 minecraft:air replace minecraft:iron_bars
particle minecraft:wax_on -5000 98 -4940 3 2 0.3 0 30 force
playsound minecraft:block.iron_door.open master @a[tag=so_ar_zone] -5000 98 -4940 2 0.7
