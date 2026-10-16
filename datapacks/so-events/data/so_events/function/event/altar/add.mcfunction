$execute store result score #cnt so_ev run data get entity @s Item.count $(m)
scoreboard players operation #paid so_ev += #cnt so_ev
particle minecraft:soul_fire_flame ~ ~0.3 ~ 0.2 0.2 0.2 0.05 12
playsound minecraft:block.respawn_anchor.charge master @a ~ ~ ~ 0.8 1.4
kill @s
