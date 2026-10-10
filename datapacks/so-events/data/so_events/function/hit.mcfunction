advancement revoke @s only so_events:hit
scoreboard players add #hits so_ev 1
execute if score #hits so_ev matches 5.. run function so_events:event/runner/win
execute unless score #hits so_ev matches 5.. run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.2
