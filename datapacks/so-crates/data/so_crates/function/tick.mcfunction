execute if score #enabled so_crates matches 1 as @a[scores={crates=1..}] at @s run function so_crates:lib/go
execute if score #enabled so_crates matches 1 as @a[scores={isla=1..}] at @s run function so_crates:lib/back
scoreboard players reset @a crates
scoreboard players enable @a crates
scoreboard players reset @a isla
scoreboard players enable @a isla
scoreboard players add #t so_crates 1
execute if score #t so_crates matches 10.. run function so_crates:lib/zone
