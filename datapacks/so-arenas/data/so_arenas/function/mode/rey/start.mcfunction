# Colina física en el centro (dentro del óvalo que se limpia: desaparece al cerrar el foso).
fill -5006 96 -5001 -5006 96 -4999 minecraft:moss_block
fill -5005 96 -5003 -5005 96 -4997 minecraft:moss_block
fill -5004 96 -5004 -5004 96 -4996 minecraft:moss_block
fill -5003 96 -5005 -5003 96 -4995 minecraft:moss_block
fill -5002 96 -5005 -5002 96 -4995 minecraft:moss_block
fill -5001 96 -5006 -5001 96 -4994 minecraft:moss_block
fill -5000 96 -5006 -5000 96 -4994 minecraft:moss_block
fill -4999 96 -5006 -4999 96 -4994 minecraft:moss_block
fill -4998 96 -5005 -4998 96 -4995 minecraft:moss_block
fill -4997 96 -5005 -4997 96 -4995 minecraft:moss_block
fill -4996 96 -5004 -4996 96 -4996 minecraft:moss_block
fill -4995 96 -5003 -4995 96 -4997 minecraft:moss_block
fill -4994 96 -5001 -4994 96 -4999 minecraft:moss_block
fill -5004 97 -5001 -5004 97 -4999 minecraft:mud_bricks
fill -5003 97 -5003 -5003 97 -4997 minecraft:mud_bricks
fill -5002 97 -5003 -5002 97 -4997 minecraft:mud_bricks
fill -5001 97 -5004 -5001 97 -4996 minecraft:mud_bricks
fill -5000 97 -5004 -5000 97 -4996 minecraft:mud_bricks
fill -4999 97 -5004 -4999 97 -4996 minecraft:mud_bricks
fill -4998 97 -5003 -4998 97 -4997 minecraft:mud_bricks
fill -4997 97 -5003 -4997 97 -4997 minecraft:mud_bricks
fill -4996 97 -5001 -4996 97 -4999 minecraft:mud_bricks
fill -5002 98 -5001 -5002 98 -4999 minecraft:smooth_quartz
fill -5001 98 -5002 -5001 98 -4998 minecraft:smooth_quartz
fill -5000 98 -5002 -5000 98 -4998 minecraft:smooth_quartz
fill -4999 98 -5002 -4999 98 -4998 minecraft:smooth_quartz
fill -4998 98 -5001 -4998 98 -4999 minecraft:smooth_quartz
setblock -5002 98 -5001 minecraft:gold_block
setblock -5002 98 -5000 minecraft:gold_block
setblock -5002 98 -4999 minecraft:gold_block
setblock -5001 98 -5002 minecraft:gold_block
setblock -5001 98 -4998 minecraft:gold_block
setblock -5000 98 -5002 minecraft:gold_block
setblock -5000 98 -4998 minecraft:gold_block
setblock -4999 98 -5002 minecraft:gold_block
setblock -4999 98 -4998 minecraft:gold_block
setblock -4998 98 -5001 minecraft:gold_block
setblock -4998 98 -5000 minecraft:gold_block
setblock -4998 98 -4999 minecraft:gold_block
setblock -5000 98 -5000 minecraft:pearlescent_froglight
scoreboard players set #mode so_ar 5
scoreboard players set #hold so_ar 0
scoreboard players set #anticamp so_ar 0
bossbar set so_arenas:fight color yellow
bossbar set so_arenas:fight max 90
bossbar set so_arenas:fight value 0
bossbar set so_arenas:fight name [{"text": "Captura ", "color": "gold", "bold": true}, {"score": {"name": "#hold", "objective": "so_ar"}, "color": "white"}, {"text": "/90", "color": "gold"}]
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "Contrato: subí a la colina del centro y dominá la cima del anillo dorado 90 s en total (límite: 120 s). Sin anti-camping.", "color": "gold", "bold": false}]
function so_arenas:mode/rey/wave
