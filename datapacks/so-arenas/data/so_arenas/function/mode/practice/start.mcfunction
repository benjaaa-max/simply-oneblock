scoreboard players set #mode so_ar 1
scoreboard players set #wave so_ar 0
scoreboard players set #t so_ar 0
scoreboard players set #anticamp so_ar 1
scoreboard players operation #rew so_ar = #tier so_ar
bossbar set so_arenas:fight name {"text": "Práctica", "color": "yellow"}
bossbar set so_arenas:fight color yellow
bossbar set so_arenas:fight max 2
bossbar set so_arenas:fight value 0
bossbar set so_arenas:fight players @a[tag=so_ar_in]
bossbar set so_arenas:fight visible true
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "La práctica comienza: 2 oleadas. ¡Golpeá, esquivá y sobreviví!", "color": "yellow", "bold": false}]
function so_arenas:mode/practice/wave
