execute unless score #enabled sq matches 1 run return 0
execute as @a[tag=!sq_init] run function so_quests:lib/init_player
scoreboard players add #t sq 1
execute if score #t sq matches 20.. run function so_quests:lib/check
execute if score #t sq matches 20.. run scoreboard players set #t sq 0
scoreboard players add #day sq 1
execute if score #day sq matches 24000.. run function so_quests:lib/new_day
execute if score #day sq matches 24000.. run scoreboard players set #day sq 0
execute as @a[scores={quests=1..}] at @s run dialog show @s so_quests:main
scoreboard players reset @a quests
scoreboard players enable @a quests
execute as @a[scores={quest_menu=1..6}] store result storage so_quests:tmp id int 1 run scoreboard players get @s quest_menu
execute as @a[scores={quest_menu=1..6}] run function so_quests:lib/open_cat with storage so_quests:tmp
scoreboard players reset @a quest_menu
scoreboard players enable @a quest_menu
execute as @a[scores={quest_view=1..}] at @s store result storage so_quests:tmp id int 1 run scoreboard players get @s quest_view
execute as @a[scores={quest_view=1..}] at @s run function so_quests:lib/view with storage so_quests:tmp
scoreboard players reset @a quest_view
scoreboard players enable @a quest_view
execute as @a[scores={quest_claim=1..}] at @s store result storage so_quests:tmp id int 1 run scoreboard players get @s quest_claim
execute as @a[scores={quest_claim=1..}] at @s run function so_quests:lib/claim with storage so_quests:tmp
scoreboard players reset @a quest_claim
scoreboard players enable @a quest_claim
