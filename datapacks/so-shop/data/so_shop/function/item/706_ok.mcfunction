clear @s minecraft:emerald 18
give @s minecraft:paper[minecraft:item_name='{"text":"Boleto de Arena","color":"aqua","italic":false}',minecraft:custom_data={so_ticket:"arena"},minecraft:enchantment_glint_override=true] 1
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste ","color":"green"},{"text":"Boleto de Arena","color":"white"},{"text":" por 18 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4
