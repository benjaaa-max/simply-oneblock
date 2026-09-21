clear @s minecraft:emerald 14
give @s minecraft:iron_pickaxe[minecraft:enchantments={"minecraft:efficiency":3}] 1
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste ","color":"green"},{"text":"Pico de hierro (Eficiencia III)","color":"white"},{"text":" por 14 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4
