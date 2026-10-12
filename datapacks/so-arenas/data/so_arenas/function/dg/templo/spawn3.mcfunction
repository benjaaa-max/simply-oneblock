execute positioned -4989.5 60 -4986.5 run function so_events:api/mob {id:"drowned_trident"}
execute positioned -4989.5 60 -4980.5 run function so_events:api/mob {id:"drowned_trident"}
execute positioned -4991.5 60 -4986.5 run function so_events:api/mob {id:"drowned"}
summon minecraft:guardian -4993.5 57 -4983.5 {Tags:["so_ar_dgm"],PersistenceRequired:1b}
summon minecraft:guardian -4992.5 57 -4984.5 {Tags:["so_ar_dgm"],PersistenceRequired:1b}
execute as @e[tag=so_ev_mob,x=-5001,y=59,z=-4991,dx=14,dy=7,dz=14] run function so_arenas:dg/claim
