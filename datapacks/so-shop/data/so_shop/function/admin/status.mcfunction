# Diagnóstico rápido de la tienda. Uso: /function so_shop:admin/status
tellraw @s [{"text":"=== SO Shop: estado ===","color":"gold","bold":true}]
tellraw @s [{"text":"Activa: ","color":"yellow"},{"score":{"name":"#enabled","objective":"so_shop"},"color":"white"},{"text":"  Conteo leído: ","color":"yellow"},{"score":{"name":"#blocks","objective":"so_shop"},"color":"white"},{"text":"  Límite diario (transacciones): ","color":"yellow"},{"score":{"name":"#sell_limit","objective":"so_shop"},"color":"white"}]
execute if score #src so_shop matches 0 run tellraw @s {"text":"AVISO: no se encontro el contador de Simply OneBlock (fake_player ib_minedcount). Revisa que este instalado y activo.","color":"red","bold":true}
execute if score #src so_shop matches 1 run tellraw @s {"text":"Fuente del conteo: so_core","color":"dark_gray"}
execute if score #src so_shop matches 2 run tellraw @s [{"text":"Fuente del conteo: Simply OneBlock directo (ib_minedcount = ","color":"dark_gray"},{"score":{"name":"fake_player","objective":"ib_minedcount"},"color":"white"},{"text":")","color":"dark_gray"}]
tellraw @s [{"text":"Tu cooldown restante: ","color":"yellow"},{"score":{"name":"@s","objective":"so_shop_cd"},"color":"white"},{"text":" ticks","color":"yellow"}]
tellraw @s [{"text":"Tus ventas hoy: ","color":"yellow"},{"score":{"name":"@s","objective":"so_sold"},"color":"white"},{"text":" / ","color":"yellow"},{"score":{"name":"#sell_limit","objective":"so_shop"},"color":"white"}]
tellraw @s [{"text":"Modo desbloqueo total: ","color":"yellow"},{"score":{"name":"#bypass","objective":"so_shop"},"color":"white"}]
