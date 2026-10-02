# Abre la tienda en ventana (dialog). Fallback: /trigger shop set 2
dialog show @s so_shop:main
playsound minecraft:item.book.page_turn master @s ~ ~ ~ 0.6 1.4
scoreboard players set @s so_shop_seen 1
