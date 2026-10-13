execute positioned -4965.5 60 -5011.5 run function so_events:api/boss {id:"arana_colosal"}
execute positioned -4967.5 60 -5014.5 run function so_events:api/mob {id:"cave_spider"}
execute positioned -4967.5 60 -5008.5 run function so_events:api/mob {id:"cave_spider"}
execute positioned -4961.5 60 -5011.5 run function so_events:api/mob {id:"cave_spider"}
execute as @e[tag=so_ev_mob,x=-4980,y=59,z=-5022,dx=20,dy=11,dz=20] run function so_arenas:dg/claim
data modify entity @e[tag=so_ar_dgboss,x=-4980,y=59,z=-5022,dx=20,dy=11,dz=20,limit=1] CustomName set value {text:"Rey Araña",color:"dark_red",bold:true}
execute unless entity @e[tag=so_ev_boss] run bossbar set so_events:boss visible false
bossbar set so_arenas:dg name {"text": "Rey Araña", "color": "dark_red", "bold": true}
