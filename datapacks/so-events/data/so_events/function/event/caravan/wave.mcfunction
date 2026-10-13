execute as @a[tag=so_ev_in] at @s run function so_events:lib/spawn {mob:"mob/saqueador_caravana"}
execute as @a[tag=so_ev_in] at @s run function so_events:lib/spawn {mob:"mob/saqueador_caravana"}
execute as @a[tag=so_ev_in] at @s run function so_events:lib/spawn {mob:"mob/pillager"}
execute as @a[tag=so_ev_in] at @s run function so_events:lib/spawn {mob:"mob/vindicator"}
function so_events:lib/tier_up
title @a[tag=so_ev_in] actionbar {"text": "¡Saqueadores atacan la caravana!", "color": "red", "bold": true}
