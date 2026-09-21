scoreboard players operation #falta so_shop = #cost so_shop
scoreboard players operation #falta so_shop -= #have so_shop
tellraw @s [{"text":"[SO Shop] ","color":"gold"},{"text":"No te alcanza. Te faltan ","color":"red"},{"score":{"name":"#falta","objective":"so_shop"},"color":"yellow"},{"text":" unidades del pago.","color":"red"}]
playsound minecraft:entity.villager.no master @s ~ ~ ~ 1 1
