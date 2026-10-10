# $(mob): nombre de mob/ o boss/. Busca suelo cerca del jugador (nunca en el vacío).
scoreboard players set #ok so_ev 0
$data modify storage so_events:tmp mob set value "$(mob)"
function so_events:lib/spawn_roll
function so_events:lib/spawn_try with storage so_events:tmp
execute if score #ok so_ev matches 0 run function so_events:lib/spawn_roll
execute if score #ok so_ev matches 0 run function so_events:lib/spawn_try with storage so_events:tmp
execute if score #ok so_ev matches 0 run function so_events:lib/spawn_roll
execute if score #ok so_ev matches 0 run function so_events:lib/spawn_try with storage so_events:tmp
execute if score #ok so_ev matches 0 run function so_events:lib/spawn_here with storage so_events:tmp
