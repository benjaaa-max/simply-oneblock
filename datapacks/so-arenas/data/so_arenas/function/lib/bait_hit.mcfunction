advancement revoke @s only so_arenas:bait_hit
execute as @e[tag=so_ar_bait] run data modify entity @s Health set value 1024f
title @s actionbar {"text": "¡No le pegues al Núcleo Vivo! Defendelo.", "color": "red", "bold": true}
