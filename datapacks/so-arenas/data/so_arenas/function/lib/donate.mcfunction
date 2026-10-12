execute as @a[tag=so_ar_in,limit=1,sort=random] at @s run summon minecraft:item ~ ~1.5 ~ {Tags:["so_ar_gift"],PickupDelay:10s,Motion:[0.0d,0.2d,0.0d],Item:{id:"minecraft:stone",count:1}}
$data modify entity @e[type=minecraft:item,tag=so_ar_gift,limit=1] Item set from block $(x) $(y) $(z) Items[0]
data remove entity @e[type=minecraft:item,tag=so_ar_gift,limit=1] Item.Slot
execute as @e[type=minecraft:item,tag=so_ar_gift] at @s run particle minecraft:totem_of_undying ~ ~ ~ 0.3 0.3 0.3 0.2 20 force
execute as @e[type=minecraft:item,tag=so_ar_gift] at @s run playsound minecraft:entity.player.levelup master @a[distance=..20] ~ ~ ~ 0.6 1.6
tag @e[type=minecraft:item,tag=so_ar_gift] remove so_ar_gift
$data remove block $(x) $(y) $(z) Items[0]
execute as @a[tag=so_ar_zone] at @s run playsound minecraft:entity.villager.celebrate master @s ~ ~ ~ 0.6 1.1
tellraw @a[tag=so_ar_zone] [{"text": "[Arena] ", "color": "gold", "bold": true}, {"text": "¡Un espectador envía suministros al foso!", "color": "green", "bold": false}]
