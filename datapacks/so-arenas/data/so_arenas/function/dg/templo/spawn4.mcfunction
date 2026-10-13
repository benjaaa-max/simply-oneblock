execute positioned -4965.5 60 -4983.5 run function so_events:api/boss {id:"guardian_oscuro"}
execute positioned -4967.5 60 -4986.5 run function so_events:api/mob {id:"drowned_trident"}
execute positioned -4967.5 60 -4980.5 run function so_events:api/mob {id:"drowned_trident"}
execute as @e[tag=so_ev_mob,x=-4980,y=59,z=-4994,dx=20,dy=11,dz=20] run function so_arenas:dg/claim
data modify entity @e[tag=so_ar_dgboss,x=-4980,y=59,z=-4994,dx=20,dy=11,dz=20,limit=1] CustomName set value {text:"Guardián de la Oscuridad",color:"dark_red",bold:true}
execute unless entity @e[tag=so_ev_boss] run bossbar set so_events:boss visible false
bossbar set so_arenas:dg name {"text": "Guardián de la Oscuridad", "color": "dark_red", "bold": true}
