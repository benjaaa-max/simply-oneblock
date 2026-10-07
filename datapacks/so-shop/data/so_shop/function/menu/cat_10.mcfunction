tellraw @s {"text":""}
tellraw @s {"text":"══ LIBROS ENCANTADOS ══","color":"light_purple","bold":true}
execute if score #blocks so_shop matches 4000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Reparación","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 10011"}},{"text":"  —  34 E","color":"green"}]
execute unless score #blocks so_shop matches 4000.. run tellraw @s {"text":"  ✖ Reparación — 4.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 3500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Fortuna III","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 10021"}},{"text":"  —  28 E","color":"green"}]
execute unless score #blocks so_shop matches 3500.. run tellraw @s {"text":"  ✖ Fortuna III — 3.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 3500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Toque de seda","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 10031"}},{"text":"  —  26 E","color":"green"}]
execute unless score #blocks so_shop matches 3500.. run tellraw @s {"text":"  ✖ Toque de seda — 3.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 3500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Eficiencia V","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 10041"}},{"text":"  —  26 E","color":"green"}]
execute unless score #blocks so_shop matches 3500.. run tellraw @s {"text":"  ✖ Eficiencia V — 3.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Irrompibilidad III","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 10051"}},{"text":"  —  20 E","color":"green"}]
execute unless score #blocks so_shop matches 2000.. run tellraw @s {"text":"  ✖ Irrompibilidad III — 2.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 4000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Filo V","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 10061"}},{"text":"  —  28 E","color":"green"}]
execute unless score #blocks so_shop matches 4000.. run tellraw @s {"text":"  ✖ Filo V — 4.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 3000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Protección IV","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 10071"}},{"text":"  —  24 E","color":"green"}]
execute unless score #blocks so_shop matches 3000.. run tellraw @s {"text":"  ✖ Protección IV — 3.000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 3500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Botín III","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 10081"}},{"text":"  —  24 E","color":"green"}]
execute unless score #blocks so_shop matches 3500.. run tellraw @s {"text":"  ✖ Botín III — 3.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Caída de pluma IV","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 10091"}},{"text":"  —  18 E","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Caída de pluma IV — 2.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 3500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Poder V","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 10101"}},{"text":"  —  22 E","color":"green"}]
execute unless score #blocks so_shop matches 3500.. run tellraw @s {"text":"  ✖ Poder V — 3.500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 3000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Infinidad","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 10111"}},{"text":"  —  20 E","color":"green"}]
execute unless score #blocks so_shop matches 3000.. run tellraw @s {"text":"  ✖ Infinidad — 3.000 bloques","color":"dark_gray"}
tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop set 2"}}
