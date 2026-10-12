$data modify storage so_arenas:tmp b set value "$(b)"
execute store result storage so_arenas:tmp a int 1 run random value 0..359
execute store result storage so_arenas:tmp d int 1 run random value 8..14
function so_arenas:lib/spawn_boss_at with storage so_arenas:tmp
scoreboard players set #tg so_ar 0
execute as @e[tag=so_ev_mob,x=-5032,y=88,z=-5038,dx=64,dy=60,dz=76] run function so_arenas:lib/claim
execute unless entity @e[tag=so_ev_boss] run bossbar set so_events:boss visible false
