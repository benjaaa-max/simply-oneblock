tellraw @s {"text":""}
tellraw @s {"text":"══ BLOQUES FUNCIONALES ══","color":"gold","bold":true}
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Barril x4","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4011"}},{"text":"  —  4 E","color":"green"}]
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cama roja","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4021"}},{"text":"  —  4 E","color":"green"}]
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Soporte de armaduras x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4031"}},{"text":"  —  4 E","color":"green"}]
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Telar","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4041"}},{"text":"  —  4 E","color":"green"}]
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Alto horno","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4051"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Alto horno — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Ahumador","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4061"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Ahumador — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cortapiedras","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4071"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Cortapiedras — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Afilador","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4081"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Afilador — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Librería x8","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4091"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Librería x8 — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cofre de cobre encerado x2","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4101"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Cofre de cobre encerado x2 — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Mesa de herrería","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4111"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 2000.. run tellraw @s {"text":"  ✖ Mesa de herrería — 2.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Yunque","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4121"}},{"text":"  —  16 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Yunque — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Tocadiscos","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4131"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Tocadiscos — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Atril","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4141"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Atril — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 3500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Mesa de encantamientos","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4151"}},{"text":"  —  26 E","color":"green"}]
execute unless score #blocks so_shop matches 3500.. run tellraw @s {"text":"  ✖ Mesa de encantamientos — 3.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 5000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cofre de Ender","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4161"}},{"text":"  —  12 E","color":"green"}]
execute unless score #blocks so_shop matches 5000.. run tellraw @s {"text":"  ✖ Cofre de Ender — 5.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Soporte para pociones","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4171"}},{"text":"  —  12 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Soporte para pociones — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Nexo de reaparición","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 4181"}},{"text":"  —  24 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Nexo de reaparición — 6.667 bloques","color":"dark_gray"}
tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}
