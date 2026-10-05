clear @s minecraft:emerald 46
give @s minecraft:tripwire_hook[minecraft:item_name='{"text":"Llave de Mazmorra","color":"gold","italic":false}',minecraft:lore=['{"text":"Abre las puertas de una mazmorra","color":"gray","italic":true}','{"text":"Rareza: Poco común","color":"yellow","italic":false}'],minecraft:custom_data={so_key:"dungeon"},minecraft:enchantment_glint_override=true] 2
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x2 (2 objetos) por 46 esmeraldas. Ahorraste 2.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
