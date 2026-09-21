clear @s minecraft:emerald 24
give @s minecraft:tripwire_hook[minecraft:item_name='{"text":"Llave de Mazmorra","color":"gold","italic":false}',minecraft:custom_data={so_key:"dungeon"},minecraft:enchantment_glint_override=true] 1
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste ","color":"green"},{"text":"Llave de Mazmorra","color":"white"},{"text":" por 24 esmeraldas.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.5 1.4
