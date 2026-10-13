execute as @a[tag=so_ev_in] run loot give @s loot so_events:reward_eclipse
execute as @a[tag=so_ev_in] run loot give @s loot so_events:reward_big
scoreboard players add @a[tag=so_ev_in] so_ev_win 1
scoreboard players add @a[tag=so_ev_in] so_ev_inv 1
function so_events:lib/streak_up
execute as @a[tag=so_ev_in] at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:30,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{explosions:[{shape:"large_ball",colors:[I;11141290,16777215],has_trail:1b}]}}}}
tellraw @a [{"text": "[Evento] ", "color": "gold", "bold": true}, {"text": "El eclipse terminó. Los sobrevivientes recibieron el botín legendario del eclipse.", "color": "green", "bold": false}]
function so_events:lib/cleanup
