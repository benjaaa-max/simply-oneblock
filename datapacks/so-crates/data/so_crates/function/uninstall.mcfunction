execute as @a[tag=so_cr_in] run function so_crates:lib/leave
scoreboard objectives remove so_crates
scoreboard objectives remove crates
scoreboard objectives remove isla
scoreboard objectives remove so_cr_x
scoreboard objectives remove so_cr_y
scoreboard objectives remove so_cr_z
scoreboard objectives remove so_cr_saved
data remove storage so_crates:tmp x
tellraw @s {"text":"[SO Crates] desinstalado. Quitá la carpeta del datapack y /reload. El templo queda construido.","color":"yellow"}
