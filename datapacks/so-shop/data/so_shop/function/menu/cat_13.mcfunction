tellraw @s {"text":""}
tellraw @s {"text":"══ LLAVES ONEBLOCK ══","color":"gold","bold":true}
execute if score #blocks so_shop matches 434.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cemetery Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 13011"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 434.. run tellraw @s {"text":"  ✖ Cemetery Key — 434 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 434.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Graveyard Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 13021"}},{"text":"  —  5 E","color":"green"}]
execute unless score #blocks so_shop matches 434.. run tellraw @s {"text":"  ✖ Graveyard Key — 434 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 434.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Ossuary Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 13031"}},{"text":"  —  6 E","color":"green"}]
execute unless score #blocks so_shop matches 434.. run tellraw @s {"text":"  ✖ Ossuary Key — 434 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 434.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Old Tower Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 13041"}},{"text":"  —  7 E","color":"green"}]
execute unless score #blocks so_shop matches 434.. run tellraw @s {"text":"  ✖ Old Tower Key — 434 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Pyramid Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 13051"}},{"text":"  —  10 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Pyramid Key — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Rusty Mineshaft Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 13061"}},{"text":"  —  11 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Rusty Mineshaft Key — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Treasure Room","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 13071"}},{"text":"  —  12 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Treasure Room — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Deep_Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 13081"}},{"text":"  —  14 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Deep_Key — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Elder Guardian Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 13091"}},{"text":"  —  22 E","color":"green"}]
execute unless score #blocks so_shop matches 7000.. run tellraw @s {"text":"  ✖ Elder Guardian Key — 7.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Warden_Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 13101"}},{"text":"  —  26 E","color":"green"}]
execute unless score #blocks so_shop matches 7000.. run tellraw @s {"text":"  ✖ Warden_Key — 7.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Wither Arena","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 13111"}},{"text":"  —  30 E","color":"green"}]
execute unless score #blocks so_shop matches 7000.. run tellraw @s {"text":"  ✖ Wither Arena — 7.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"To the End","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 13121"}},{"text":"  —  28 E","color":"green"}]
execute unless score #blocks so_shop matches 7000.. run tellraw @s {"text":"  ✖ To the End — 7.000 bloques","color":"dark_gray"}
tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}
