function so_events:lib/blocks
execute unless score #active so_ev matches 0 run function so_events:lib/cleanup
function so_events:event/mana/start
