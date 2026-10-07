execute if items entity @s armor.head * run return run tellraw @s {"text":"[SO Status] Primero dejá libre el espacio del casco.","color":"red"}
execute unless items entity @s weapon.mainhand * run return run tellraw @s {"text":"[SO Status] Tené en la mano el ítem que querés usar como sombrero.","color":"red"}
item replace entity @s armor.head from entity @s weapon.mainhand
item replace entity @s weapon.mainhand with minecraft:air
playsound minecraft:item.armor.equip_generic player @s ~ ~ ~ 0.7 1.1
tellraw @s {"text":"[SO Status] Sombrero equipado.","color":"green"}
