tellraw @s {"text":""}
tellraw @s {"text":"══ ALIMENTOS Y POCIONES ══","color":"light_purple","bold":true}
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Pan x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7011"}},{"text":"  —  3 E","color":"green"}]
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Torta","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7021"}},{"text":"  —  4 E","color":"green"}]
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Filete cocinado x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7031"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Filete cocinado x16 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Chuleta cocinada x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7041"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Chuleta cocinada x16 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Zanahoria dorada x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7051"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Zanahoria dorada x16 — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 3500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Manzana dorada x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7061"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 3500.. run tellraw @s {"text":"  ✖ Manzana dorada x2 — 3.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Manzana de Notch","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7071"}},{"text":"  —  12 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Manzana de Notch — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Arrojadiza: Curación II x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7081"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Arrojadiza: Curación II x2 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Arrojadiza: Regeneración x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7091"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Arrojadiza: Regeneración x2 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Arrojadiza: Fuerza II x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7101"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Arrojadiza: Fuerza II x2 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Arrojadiza: Velocidad II x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7111"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Arrojadiza: Velocidad II x2 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Arrojadiza: Caída lenta x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7121"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Arrojadiza: Caída lenta x2 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Arrojadiza: Daño II x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7131"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Arrojadiza: Daño II x2 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Arrojadiza: Debilidad x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7141"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Arrojadiza: Debilidad x2 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Arrojadiza: Veneno x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7151"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Arrojadiza: Veneno x2 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Arrojadiza: Infestación x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 7161"}},{"text":"  —  12 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Arrojadiza: Infestación x2 — 6.667 bloques","color":"dark_gray"}
tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}
