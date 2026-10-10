# $(m): id de so_events:api/mob · $(t): 1 = objetivo de caza. Punto al azar dentro del foso.
$data modify storage so_arenas:tmp m set value "$(m)"
execute store result storage so_arenas:tmp a int 1 run random value 0..359
execute store result storage so_arenas:tmp d int 1 run random value 5..20
function so_arenas:lib/spawn_at with storage so_arenas:tmp
$scoreboard players set #tg so_ar $(t)
execute as @e[tag=so_ev_mob,x=-5032,y=88,z=-5038,dx=64,dy=60,dz=76] run function so_arenas:lib/claim
