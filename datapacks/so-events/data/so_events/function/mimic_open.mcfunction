advancement revoke @s only so_events:mimic
execute if score #active so_ev matches 12 if score #mimic so_ev matches 0 run function so_events:event/mimic/treasure
