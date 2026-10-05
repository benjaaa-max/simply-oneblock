clear @s minecraft:emerald 50
give @s minecraft:paper[minecraft:item_name='{"text":"Boleto de Arena","color":"aqua","italic":false}',minecraft:lore=['{"text":"Canjéalo para entrar a la arena de combate","color":"gray","italic":true}','{"text":"Rareza: Poco común","color":"yellow","italic":false}'],minecraft:custom_data={so_ticket:"arena"},minecraft:enchantment_glint_override=true] 3
scoreboard players set @s so_shop_cd 20
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"Compraste x3 (3 objetos) por 50 esmeraldas. Ahorraste 4.","color":"green"}]
playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
scoreboard players add @s so_shop_buys 1
