execute if score #rec1 so_ar matches 1..999998 store result storage so_arenas:dg r1 int 1 run scoreboard players get #rec1 so_ar
execute if score #rec2 so_ar matches 1..999998 store result storage so_arenas:dg r2 int 1 run scoreboard players get #rec2 so_ar
execute if score #rec3 so_ar matches 1..999998 store result storage so_arenas:dg r3 int 1 run scoreboard players get #rec3 so_ar
execute unless score #rec1 so_ar matches 1..999998 run data modify storage so_arenas:dg r1 set value "—"
execute unless score #rec2 so_ar matches 1..999998 run data modify storage so_arenas:dg r2 set value "—"
execute unless score #rec3 so_ar matches 1..999998 run data modify storage so_arenas:dg r3 set value "—"
function so_arenas:dg/board_set with storage so_arenas:dg
