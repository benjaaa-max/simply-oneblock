clear @s minecraft:emerald 28
give @s minecraft:paper[minecraft:item_name='{"text":"Contrato de Invasión","color":"red","italic":false}',minecraft:custom_data={so_contract:"invasion"},minecraft:enchantment_glint_override=true] 1
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste ","color":"green"},{"text":"Contrato de Invasión","color":"white"},{"text":" por 28 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4
