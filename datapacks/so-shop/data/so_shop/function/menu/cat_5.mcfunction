tellraw @s {"text":""}
tellraw @s {"text":"══ MECANISMOS Y REDSTONE ══","color":"red","bold":true}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Polvo de redstone x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5011"}},{"text":"  —  4 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Polvo de redstone x32 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Pistón x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5021"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Pistón x8 — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Pistón pegajoso x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5031"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Pistón pegajoso x8 — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Observador x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5041"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 2000.. run tellraw @s {"text":"  ✖ Observador x8 — 2.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Repetidor x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5051"}},{"text":"  —  4 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Repetidor x8 — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Comparador x4","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5061"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Comparador x4 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Tolva x4","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5071"}},{"text":"  —  12 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Tolva x4 — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Dispensador x4","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5081"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Dispensador x4 — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Soltador x4","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5091"}},{"text":"  —  4 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Soltador x4 — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Lámpara de redstone x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5101"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Lámpara de redstone x8 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Sensor de luz solar x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5111"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Sensor de luz solar x2 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Diana x4","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5121"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Diana x4 — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Bloque de slime x4","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5131"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Bloque de slime x4 — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Riel propulsor x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 5141"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Riel propulsor x8 — 1.500 bloques","color":"dark_gray"}
tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}
