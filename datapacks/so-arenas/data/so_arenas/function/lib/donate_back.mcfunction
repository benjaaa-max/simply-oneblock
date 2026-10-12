$execute positioned $(x) $(y) $(z) unless entity @p[tag=so_ar_zone,distance=..10] run return 0
$execute positioned $(x) $(y) $(z) as @p[tag=so_ar_zone,distance=..10] at @s run summon minecraft:item ~ ~1.8 ~ {Tags:["so_ar_gift"],PickupDelay:0s,Item:{id:"minecraft:stone",count:1}}
$data modify entity @e[type=minecraft:item,tag=so_ar_gift,limit=1] Item set from block $(x) $(y) $(z) Items[0]
data remove entity @e[type=minecraft:item,tag=so_ar_gift,limit=1] Item.Slot
tag @e[type=minecraft:item,tag=so_ar_gift] remove so_ar_gift
$data remove block $(x) $(y) $(z) Items[0]
$execute positioned $(x) $(y) $(z) as @p[tag=so_ar_zone,distance=..10] at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 0.7
$execute positioned $(x) $(y) $(z) run title @p[tag=so_ar_zone,distance=..10] actionbar {"text": "Solo se puede donar durante un combate: te lo devolvemos.", "color": "yellow"}
