tellraw @s {"text":""}
tellraw @s {"text":"══ BLOQUES DE CONSTRUCCIÓN ══","color":"green","bold":true}
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Tronco de roble x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1011"}},{"text":"  —  4 E","color":"green"}]
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Tronco de abedul x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1021"}},{"text":"  —  4 E","color":"green"}]
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Tronco de abeto x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1031"}},{"text":"  —  4 E","color":"green"}]
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Tronco de jungla x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1041"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Tronco de jungla x32 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Tronco de acacia x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1051"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Tronco de acacia x32 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Tronco de roble oscuro x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1061"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Tronco de roble oscuro x32 — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Tronco de cerezo x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1071"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Tronco de cerezo x32 — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Tronco de mangle x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1081"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Tronco de mangle x32 — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Bloque de bambú x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1091"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Bloque de bambú x32 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Tallo carmesí x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1101"}},{"text":"  —  7 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Tallo carmesí x32 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Tallo distorsionado x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1111"}},{"text":"  —  7 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Tallo distorsionado x32 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Ladrillos de piedra x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1121"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Ladrillos de piedra x64 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Pizarra profunda pulida x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1131"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Pizarra profunda pulida x64 — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Ladrillos x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1141"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Ladrillos x64 — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Bloque de cuarzo x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1151"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Bloque de cuarzo x32 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Ladrillos del Nether x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1161"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Ladrillos del Nether x64 — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 4000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Prismarina x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1171"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 4000.. run tellraw @s {"text":"  ✖ Prismarina x32 — 4.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 8500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Ladrillos de piedra del End x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1181"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 8500.. run tellraw @s {"text":"  ✖ Ladrillos de piedra del End x32 — 8.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 8500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Bloque de púrpur x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1191"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 8500.. run tellraw @s {"text":"  ✖ Bloque de púrpur x32 — 8.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cobre encerado x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1201"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Cobre encerado x64 — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cobre expuesto encerado x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1211"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Cobre expuesto encerado x64 — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cobre desgastado encerado x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1221"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Cobre desgastado encerado x64 — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cobre oxidado encerado x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 1231"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Cobre oxidado encerado x64 — 1.500 bloques","color":"dark_gray"}
tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}
