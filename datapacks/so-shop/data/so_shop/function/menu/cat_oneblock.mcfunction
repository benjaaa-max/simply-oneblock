tellraw @s {"text":""}
tellraw @s {"text":"══ LLAVES ONEBLOCK ══","color":"gold","bold":true}
execute if score #blocks so_shop matches 434.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Cemetery Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 711"}},{"text":"  —  ","color":"dark_gray"},{"text":"5 esmeraldas · 434 bloques","color":"green"}]
execute unless score #blocks so_shop matches 434.. run tellraw @s {"text":"  ✖ Cemetery Key — 434 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 434.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Graveyard Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 712"}},{"text":"  —  ","color":"dark_gray"},{"text":"5 esmeraldas · 434 bloques","color":"green"}]
execute unless score #blocks so_shop matches 434.. run tellraw @s {"text":"  ✖ Graveyard Key — 434 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 434.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Ossuary Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 713"}},{"text":"  —  ","color":"dark_gray"},{"text":"6 esmeraldas · 434 bloques","color":"green"}]
execute unless score #blocks so_shop matches 434.. run tellraw @s {"text":"  ✖ Ossuary Key — 434 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 434.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Old Tower Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 714"}},{"text":"  —  ","color":"dark_gray"},{"text":"7 esmeraldas · 434 bloques","color":"green"}]
execute unless score #blocks so_shop matches 434.. run tellraw @s {"text":"  ✖ Old Tower Key — 434 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Pyramid Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 715"}},{"text":"  —  ","color":"dark_gray"},{"text":"10 esmeraldas · 2500 bloques","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Pyramid Key — 2500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Rusty Mineshaft Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 716"}},{"text":"  —  ","color":"dark_gray"},{"text":"11 esmeraldas · 2500 bloques","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Rusty Mineshaft Key — 2500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Treasure Room","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 717"}},{"text":"  —  ","color":"dark_gray"},{"text":"12 esmeraldas · 2500 bloques","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Treasure Room — 2500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 2500.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Deep_Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 718"}},{"text":"  —  ","color":"dark_gray"},{"text":"14 esmeraldas · 2500 bloques","color":"green"}]
execute unless score #blocks so_shop matches 2500.. run tellraw @s {"text":"  ✖ Deep_Key — 2500 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Elder Guardian Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 719"}},{"text":"  —  ","color":"dark_gray"},{"text":"22 esmeraldas · 7000 bloques","color":"green"}]
execute unless score #blocks so_shop matches 7000.. run tellraw @s {"text":"  ✖ Elder Guardian Key — 7000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Warden_Key","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 720"}},{"text":"  —  ","color":"dark_gray"},{"text":"26 esmeraldas · 7000 bloques","color":"green"}]
execute unless score #blocks so_shop matches 7000.. run tellraw @s {"text":"  ✖ Warden_Key — 7000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"Wither Arena","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 721"}},{"text":"  —  ","color":"dark_gray"},{"text":"30 esmeraldas · 7000 bloques","color":"green"}]
execute unless score #blocks so_shop matches 7000.. run tellraw @s {"text":"  ✖ Wither Arena — 7000 bloques","color":"dark_gray"}
execute if score #blocks so_shop matches 7000.. run tellraw @s [{"text":"  ▸ ","color":"dark_gray"},{"text":"To the End","color":"white","click_event":{"action":"run_command","command":"/trigger shop_buy set 722"}},{"text":"  —  ","color":"dark_gray"},{"text":"28 esmeraldas · 7000 bloques","color":"green"}]
execute unless score #blocks so_shop matches 7000.. run tellraw @s {"text":"  ✖ To the End — 7000 bloques","color":"dark_gray"}
tellraw @s {"text":"  « Volver","color":"yellow","click_event":{"action":"run_command","command":"/trigger shop_menu set 7"}}
playsound minecraft:item.book.page_turn master @s ~ ~ ~ 0.6 1.2
