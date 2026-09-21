# Uso: function so_shop:admin/set_sell_limit {value:6}
$scoreboard players set #sell_limit so_shop $(value)
$tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Límite diario de ventas: $(value).","color":"yellow"}]
