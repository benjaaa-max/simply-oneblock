clear @s minecraft:emerald 20
give @s minecraft:ominous_bottle 1
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste ","color":"green"},{"text":"Botella ominosa","color":"white"},{"text":" por 20 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4
