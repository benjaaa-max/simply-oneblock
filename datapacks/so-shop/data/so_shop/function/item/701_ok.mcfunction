clear @s minecraft:emerald 16
give @s minecraft:trial_key 1
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste ","color":"green"},{"text":"Llave de prueba","color":"white"},{"text":" por 16 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4
