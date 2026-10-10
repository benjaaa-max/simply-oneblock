# $(mob): mob/, boss/ o npc/. Busca suelo con 2 de aire (nunca en el vacío).
scoreboard players set #ok so_ev 0
$data modify storage so_events:tmp mob set value "$(mob)"
function so_events:lib/spawn_roll
execute if score #ok so_ev matches 0 run function so_events:lib/spawn_try with storage so_events:tmp
function so_events:lib/spawn_roll
execute if score #ok so_ev matches 0 run function so_events:lib/spawn_try with storage so_events:tmp
function so_events:lib/spawn_roll
execute if score #ok so_ev matches 0 run function so_events:lib/spawn_try with storage so_events:tmp
function so_events:lib/spawn_roll
execute if score #ok so_ev matches 0 run function so_events:lib/spawn_try with storage so_events:tmp
function so_events:lib/spawn_roll
execute if score #ok so_ev matches 0 run function so_events:lib/spawn_try with storage so_events:tmp
function so_events:lib/spawn_roll
execute if score #ok so_ev matches 0 run function so_events:lib/spawn_try with storage so_events:tmp
execute if score #ok so_ev matches 0 run function so_events:lib/spawn_here with storage so_events:tmp
