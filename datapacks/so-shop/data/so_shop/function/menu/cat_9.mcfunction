tellraw @s {"text":""}
tellraw @s {"text":"══ HUEVOS GENERADORES ══","color":"white","bold":true}
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de oveja","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9011"}},{"text":"  —  8 E","color":"green"}]
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de vaca","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9021"}},{"text":"  —  8 E","color":"green"}]
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de cerdo","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9031"}},{"text":"  —  8 E","color":"green"}]
tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de gallina","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9041"}},{"text":"  —  6 E","color":"green"}]
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de caballo","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9051"}},{"text":"  —  14 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Huevo de caballo — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de lobo","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9061"}},{"text":"  —  12 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Huevo de lobo — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de gato","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9071"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 1000.. run tellraw @s {"text":"  ✖ Huevo de gato — 1.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de abeja","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9081"}},{"text":"  —  12 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Huevo de abeja — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 1500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de gólem de cobre","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9091"}},{"text":"  —  14 E","color":"green"}]
execute unless score #blocks so_shop matches 1500.. run tellraw @s {"text":"  ✖ Huevo de gólem de cobre — 1.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de aldeano","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9101"}},{"text":"  —  20 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Huevo de aldeano — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 3500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de gólem de hierro","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9111"}},{"text":"  —  20 E","color":"green"}]
execute unless score #blocks so_shop matches 3500.. run tellraw @s {"text":"  ✖ Huevo de gólem de hierro — 3.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 4000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de allay","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9121"}},{"text":"  —  20 E","color":"green"}]
execute unless score #blocks so_shop matches 4000.. run tellraw @s {"text":"  ✖ Huevo de allay — 4.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 5000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de Happy Ghast","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9131"}},{"text":"  —  20 E","color":"green"}]
execute unless score #blocks so_shop matches 5000.. run tellraw @s {"text":"  ✖ Huevo de Happy Ghast — 5.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de enderman","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9141"}},{"text":"  —  18 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Huevo de enderman — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 6667.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de blaze","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9151"}},{"text":"  —  18 E","color":"green"}]
execute unless score #blocks so_shop matches 6667.. run tellraw @s {"text":"  ✖ Huevo de blaze — 6.667 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Huevo de esqueleto wither","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 9161"}},{"text":"  —  20 E","color":"green"}]
execute unless score #blocks so_shop matches 7500.. run tellraw @s {"text":"  ✖ Huevo de esqueleto wither — 7.500 bloques","color":"dark_gray"}
tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}
