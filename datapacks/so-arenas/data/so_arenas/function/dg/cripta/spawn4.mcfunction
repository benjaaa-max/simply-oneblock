execute positioned -4965.5 60 -5039.5 run function so_events:api/boss {id:"caballero"}
execute positioned -4967.5 60 -5042.5 run function so_events:api/mob {id:"skeleton"}
execute positioned -4967.5 60 -5036.5 run function so_events:api/mob {id:"skeleton_armor"}
execute as @e[tag=so_ev_mob,x=-4980,y=59,z=-5050,dx=20,dy=11,dz=20] run function so_arenas:dg/claim
data modify entity @e[tag=so_ar_dgboss,limit=1] CustomName set value {text:"Caballero No-Muerto",color:"dark_red",bold:true}
execute unless entity @e[tag=so_ev_boss] run bossbar set so_events:boss visible false
bossbar set so_arenas:dg name {"text": "Caballero No-Muerto", "color": "dark_red", "bold": true}
