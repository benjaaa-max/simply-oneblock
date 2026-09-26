# Reloj interno: 24000 ticks = 1 dia de Minecraft. No usa /time.
scoreboard players add #daytick so_shop 1
execute if score #daytick so_shop matches 24000.. run function so_shop:lib/new_day
execute if score #daytick so_shop matches 24000.. run scoreboard players set #daytick so_shop 0
