tellraw @s {"text":""}
tellraw @s {"text":"══ MINERALES E INGREDIENTES ══","color":"aqua","bold":true}
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Carbón x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2011"}},{"text":"  —  4 E","color":"green"}]
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Lingote de cobre x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2021"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Lingote de cobre x32 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Lingote de hierro x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2031"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Lingote de hierro x16 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Lingote de oro x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2041"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Lingote de oro x16 — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 3500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Diamante x4","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2051"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 3500.. run tellraw @s {"text":"  ✖ Diamante x4 — 3.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Fragmento de netherita x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2061"}},{"text":"  —  12 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Fragmento de netherita x2 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Lingote de netherita","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2071"}},{"text":"  —  24 E","color":"green"}]
execute unless score #blocks so_shop matches 7500.. run tellraw @s {"text":"  ✖ Lingote de netherita — 7.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Lapislázuli x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2081"}},{"text":"  —  4 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Lapislázuli x32 — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Fragmento de amatista x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2091"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Fragmento de amatista x16 — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Polvo de piedra luminosa x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2101"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Polvo de piedra luminosa x32 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cuarzo del Nether x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2111"}},{"text":"  —  3 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Cuarzo del Nether x32 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Pólvora x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2121"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Pólvora x16 — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 5000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Perla de Ender x4","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2131"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 5000.. run tellraw @s {"text":"  ✖ Perla de Ender x4 — 5.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Vara de breeze x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 2141"}},{"text":"  —  14 E","color":"green"}]
execute unless score #blocks so_shop matches 7000.. run tellraw @s {"text":"  ✖ Vara de breeze x2 — 7.000 bloques","color":"dark_gray"}
tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}
