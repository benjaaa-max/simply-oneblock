execute if score #enabled so_shop matches 1 run function so_shop:lib/progress
execute if score #enabled so_shop matches 1 as @a[scores={shop=1..}] at @s run function so_shop:menu/main
scoreboard players reset @a shop
scoreboard players enable @a shop
execute if score #enabled so_shop matches 1 as @a[scores={shop_menu=1..}] at @s run function so_shop:lib/open_cat
scoreboard players reset @a shop_menu
scoreboard players enable @a shop_menu
# Cooldown anti-abuso: decrementa 1 por tick para todos (no cuesta nada si ya está en 0)
execute if score #enabled so_shop matches 1 as @a if score @s so_shop_cd matches 1.. run scoreboard players remove @s so_shop_cd 1

execute if score #enabled so_shop matches 1 as @a[scores={shop_buy=1..}] at @s if score @s so_shop_cd matches 1.. run function so_shop:lib/cooldown
execute if score #enabled so_shop matches 1 as @a[scores={shop_buy=1..}] at @s unless score @s so_shop_cd matches 1.. run function so_shop:lib/dispatch
scoreboard players reset @a shop_buy
scoreboard players enable @a shop_buy
