# $(m): id de mob de so_events. Spawnea cerca del jugador sobre suelo firme.
scoreboard players set #ok so_ar 0
$data modify storage so_arenas:tmp m set value "$(m)"
function so_arenas:lib/spawn_roll
execute if score #ok so_ar matches 0 run function so_arenas:lib/spawn_try with storage so_arenas:tmp
function so_arenas:lib/spawn_roll
execute if score #ok so_ar matches 0 run function so_arenas:lib/spawn_try with storage so_arenas:tmp
function so_arenas:lib/spawn_roll
execute if score #ok so_ar matches 0 run function so_arenas:lib/spawn_try with storage so_arenas:tmp
function so_arenas:lib/spawn_roll
execute if score #ok so_ar matches 0 run function so_arenas:lib/spawn_try with storage so_arenas:tmp
execute if score #ok so_ar matches 0 run function so_arenas:lib/spawn_here with storage so_arenas:tmp
