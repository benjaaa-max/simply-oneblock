scoreboard players remove @a[scores={so_cd_heal=1..}] so_cd_heal 1
scoreboard players remove @a[scores={so_cd_feed=1..}] so_cd_feed 1
execute as @a[scores={heal=1..}] at @s run function so_status:command/heal
execute as @a[scores={feed=1..}] at @s run function so_status:command/feed
execute as @a[scores={craft=1..}] at @s anchored eyes run function so_status:command/craft
execute as @a[scores={enderchest=1..}] at @s anchored eyes run function so_status:command/enderchest
execute as @a[scores={hat=1..}] at @s run function so_status:command/hat
execute as @a[scores={afk=1..}] at @s run function so_status:command/afk
scoreboard players reset @a heal
scoreboard players reset @a feed
scoreboard players reset @a craft
scoreboard players reset @a enderchest
scoreboard players reset @a hat
scoreboard players reset @a afk
scoreboard players enable @a heal
scoreboard players enable @a feed
scoreboard players enable @a craft
scoreboard players enable @a enderchest
scoreboard players enable @a hat
scoreboard players enable @a afk
