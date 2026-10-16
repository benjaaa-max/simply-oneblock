# Uso: execute as <jugador> at @s run function so_events:lib/chest {t:"tabla"}
scoreboard players set #pl so_ev 0
$execute unless score #pl so_ev matches 1 positioned ~1 ~ ~ if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:lib/chest_put {t:"$(t)"}
$execute unless score #pl so_ev matches 1 positioned ~-1 ~ ~ if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:lib/chest_put {t:"$(t)"}
$execute unless score #pl so_ev matches 1 positioned ~ ~ ~1 if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:lib/chest_put {t:"$(t)"}
$execute unless score #pl so_ev matches 1 positioned ~ ~ ~-1 if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:lib/chest_put {t:"$(t)"}
$execute unless score #pl so_ev matches 1 positioned ~1 ~ ~1 if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:lib/chest_put {t:"$(t)"}
$execute unless score #pl so_ev matches 1 positioned ~-1 ~ ~-1 if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:lib/chest_put {t:"$(t)"}
$execute unless score #pl so_ev matches 1 positioned ~1 ~ ~-1 if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:lib/chest_put {t:"$(t)"}
$execute unless score #pl so_ev matches 1 positioned ~-1 ~ ~1 if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:lib/chest_put {t:"$(t)"}
$execute unless score #pl so_ev matches 1 positioned ~2 ~ ~ if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:lib/chest_put {t:"$(t)"}
$execute unless score #pl so_ev matches 1 positioned ~-2 ~ ~ if block ~ ~ ~ #minecraft:air if block ~ ~1 ~ #minecraft:air unless block ~ ~-1 ~ #minecraft:air run function so_events:lib/chest_put {t:"$(t)"}
$execute unless score #pl so_ev matches 1 run loot give @s loot so_events:$(t)
