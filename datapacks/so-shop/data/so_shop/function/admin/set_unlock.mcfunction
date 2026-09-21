# Uso: function so_shop:admin/set_unlock {cat:3,value:2500}
$scoreboard players set #t$(cat) so_shop $(value)
$tellraw @a [{"text":"[SO Shop] ","color":"gold"},{"text":"Sección $(cat) se abre a $(value) bloques.","color":"yellow"}]
