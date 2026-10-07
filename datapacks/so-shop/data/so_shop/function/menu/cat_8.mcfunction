tellraw @s {"text":""}
tellraw @s {"text":"══ DECORACIÓN Y TINTES ══","color":"dark_aqua","bold":true}
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Pack de 16 tintes (x4 c/u)","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8011"}},{"text":"  —  6 E","color":"green"}]
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Lana blanca x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8021"}},{"text":"  —  4 E","color":"green"}]
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Hormigón blanco x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8031"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Hormigón blanco x64 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Terracota blanca x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8041"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Terracota blanca x64 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Vidrio blanco x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8051"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Vidrio blanco x64 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Panel de vidrio blanco x64","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8061"}},{"text":"  —  3 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Panel de vidrio blanco x64 — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Vidrio tintado x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8071"}},{"text":"  —  8 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Vidrio tintado x32 — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Azulejos vidriados 1 (4 colores x4)","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8081"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Azulejos vidriados 1 (4 colores x4) — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Azulejos vidriados 2 (4 colores x4)","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8091"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Azulejos vidriados 2 (4 colores x4) — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Azulejos vidriados 3 (4 colores x4)","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8101"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Azulejos vidriados 3 (4 colores x4) — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Azulejos vidriados 4 (4 colores x4)","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8111"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Azulejos vidriados 4 (4 colores x4) — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Faroles x8 (normal y de almas)","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8121"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Faroles x8 (normal y de almas) — 500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cadena x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8131"}},{"text":"  —  4 E","color":"green"}]
execute unless score #blocks so_shop matches 500.. run tellraw @s {"text":"  ✖ Cadena x32 — 500 bloques","color":"dark_gray"}
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cuadros y marcos brillantes x16","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8141"}},{"text":"  —  4 E","color":"green"}]
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Maceta decorada x4","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8151"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Maceta decorada x4 — 1.000 bloques","color":"dark_gray"}
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Andamio x32","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 8161"}},{"text":"  —  4 E","color":"green"}]
tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}
