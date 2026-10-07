tellraw @s {"text":""}
tellraw @s {"text":"══ LLAVES Y CONTRATOS ══","color":"gold","bold":true}
execute if score #blocks so_shop matches 5000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Llave de prueba","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 11011"}},{"text":"  —  14 E","color":"green"}]
execute unless score #blocks so_shop matches 5000.. run tellraw @s {"text":"  ✖ Llave de prueba — 5.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Llave ominosa","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 11021"}},{"text":"  —  26 E","color":"green"}]
execute unless score #blocks so_shop matches 7000.. run tellraw @s {"text":"  ✖ Llave ominosa — 7.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Botella ominosa","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 11031"}},{"text":"  —  18 E","color":"green"}]
execute unless score #blocks so_shop matches 6000.. run tellraw @s {"text":"  ✖ Botella ominosa — 6.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Llave del Arquitecto","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 11041"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Llave del Arquitecto — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Llave Silvestre","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 11051"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Llave Silvestre — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Llave Subterránea","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 11061"}},{"text":"  —  12 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Llave Subterránea — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Llave de Batalla","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 11071"}},{"text":"  —  12 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Llave de Batalla — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 5000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Llave Abisal","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 11081"}},{"text":"  —  20 E","color":"green"}]
execute unless score #blocks so_shop matches 5000.. run tellraw @s {"text":"  ✖ Llave Abisal — 5.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Llave del Vacío","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 11091"}},{"text":"  —  26 E","color":"green"}]
execute unless score #blocks so_shop matches 7000.. run tellraw @s {"text":"  ✖ Llave del Vacío — 7.000 bloques","color":"dark_gray"}
tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}
