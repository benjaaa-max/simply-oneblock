$data modify entity @e[tag=so_ev_new,limit=1] Offers.Recipes append from storage so_events:tmp pool[$(i)]
$data remove storage so_events:tmp pool[$(i)]
