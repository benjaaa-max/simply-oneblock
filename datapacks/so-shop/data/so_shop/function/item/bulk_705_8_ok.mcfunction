clear @s minecraft:emerald 184
give @s minecraft:paper[minecraft:item_name='{"text":"Contrato de Invasión","color":"red","italic":false}',minecraft:lore=['{"text":"Activa una invasión de mobs en tu base","color":"gray","italic":true}','{"text":"Rareza: Rara","color":"gold","italic":false}'],minecraft:custom_data={so_contract:"invasion"},minecraft:enchantment_glint_override=true] 8
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x8 (8 objetos) por 184 esmeraldas. Ahorraste 40.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
