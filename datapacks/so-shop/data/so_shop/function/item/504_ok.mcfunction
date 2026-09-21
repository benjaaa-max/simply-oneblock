clear @s minecraft:emerald 24
give @s minecraft:enchanted_book[minecraft:stored_enchantments={"minecraft:efficiency":4}] 1
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste ","color":"green"},{"text":"Libro: Eficiencia IV","color":"white"},{"text":" por 24 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4
