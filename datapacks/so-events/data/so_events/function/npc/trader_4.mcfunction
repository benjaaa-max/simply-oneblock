summon minecraft:wandering_trader ~ ~ ~ {Tags:["so_ev_mob","so_ev_new"],Invulnerable:1b,NoAI:1b,PersistenceRequired:1b,CustomNameVisible:1b,CustomName:{text:"Minero Ambulante",color:"gray",bold:true},Offers:{Recipes:[]}}
scoreboard players set #ok so_ev 1
data modify storage so_events:tmp pool set from storage so_events:offers min
function so_events:lib/offer_pick
function so_events:lib/offer_pick
function so_events:lib/offer_pick
function so_events:lib/offer_pick
function so_events:lib/offer_pick
function so_events:lib/offer_pick
function so_events:lib/offer_pick
function so_events:lib/offer_pick
particle minecraft:happy_villager ~ ~1 ~ 0.5 1 0.5 0 20
tag @e[tag=so_ev_new] remove so_ev_new
