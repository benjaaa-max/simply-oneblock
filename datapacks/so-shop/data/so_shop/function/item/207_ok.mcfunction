clear @s minecraft:emerald 6
give @s minecraft:cyan_stained_glass 64
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste ","color":"green"},{"text":"Cristal coloreado x64 (cian)","color":"white"},{"text":" por 6 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4
