# Se activa cuando los bloques minados avanzan #bless_every (200) desde #bless_next.
execute positioned 0 64 0 store result score #n so_ev if entity @a[distance=..64,gamemode=!spectator]
execute if score #n so_ev matches 0 run return 0
scoreboard players operation #diff so_ev = #blk so_ev
scoreboard players operation #diff so_ev -= #bless_next so_ev
execute if score #diff so_ev matches ..-1 run scoreboard players operation #bless_next so_ev = #blk so_ev
execute if score #diff so_ev matches ..-1 run return 0
execute if score #diff so_ev matches 200.. run scoreboard players operation #bless_next so_ev = #blk so_ev
execute if score #diff so_ev matches 200.. run execute store result score #r so_ev run random value 1..5
execute if score #diff so_ev matches 200.. run function so_events:admin/bless
