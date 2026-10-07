tellraw @s {"text":""}
tellraw @s {"text":"══ NATURALEZA Y GRANJA ══","color":"dark_green","bold":true}
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Bloque de pasto x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6011"}},{"text":"  —  4 E","color":"green"}]
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Podzol x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6021"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Podzol x16 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Micelio x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6031"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Micelio x16 — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Bloque de musgo x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6041"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Bloque de musgo x16 — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Nylium carmesí x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6051"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Nylium carmesí x16 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Nylium distorsionado x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6061"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Nylium distorsionado x16 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Estalactita puntiaguda x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6071"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 2000.. run tellraw @s {"text":"  ✖ Estalactita puntiaguda x16 — 2.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 4500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Esponja x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6081"}},{"text":"  —  16 E","color":"green"}]
execute unless score #blocks so_shop matches 4500.. run tellraw @s {"text":"  ✖ Esponja x2 — 4.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Obsidiana llorosa x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6091"}},{"text":"  —  12 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Obsidiana llorosa x8 — 6.667 bloques","color":"dark_gray"}
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Pack de brotes (7 árboles x2)","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6101"}},{"text":"  —  6 E","color":"green"}]
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Propágulo de mangle x4","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6111"}},{"text":"  —  4 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Propágulo de mangle x4 — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Hongos del Overworld x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6121"}},{"text":"  —  4 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Hongos del Overworld x8 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Hongos del Nether x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6131"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Hongos del Nether x8 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Verruga del Nether x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6141"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Verruga del Nether x8 — 6.667 bloques","color":"dark_gray"}
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Caña de azúcar x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6151"}},{"text":"  —  3 E","color":"green"}]
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cactus x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6161"}},{"text":"  —  3 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Cactus x8 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Bambú x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6171"}},{"text":"  —  4 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Bambú x16 — 500 bloques","color":"dark_gray"}
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Semillas surtidas x24","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6181"}},{"text":"  —  4 E","color":"green"}]
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Granos de cacao x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6191"}},{"text":"  —  4 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Granos de cacao x8 — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Bayas dulces x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 6201"}},{"text":"  —  3 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Bayas dulces x8 — 500 bloques","color":"dark_gray"}
tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}
