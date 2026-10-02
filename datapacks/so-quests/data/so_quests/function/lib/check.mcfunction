function so_quests:lib/read_count
execute if score #blocks sq matches 100.. run execute as @a[scores={sqs_101=0}] run function so_quests:q/101/ready
execute if score #blocks sq matches 500.. run execute as @a[scores={sqs_102=0}] run function so_quests:q/102/ready
execute if score #blocks sq matches 1000.. run execute as @a[scores={sqs_103=0}] run function so_quests:q/103/ready
execute if score #blocks sq matches 2500.. run execute as @a[scores={sqs_104=0}] run function so_quests:q/104/ready
execute if score #blocks sq matches 5000.. run execute as @a[scores={sqs_105=0}] run function so_quests:q/105/ready
execute if score #blocks sq matches 7500.. run execute as @a[scores={sqs_106=0}] run function so_quests:q/106/ready
execute if score #blocks sq matches 10000.. run execute as @a[scores={sqs_107=0}] run function so_quests:q/107/ready
execute if score #blocks sq matches 12500.. run execute as @a[scores={sqs_108=0}] run function so_quests:q/108/ready
execute if score #blocks sq matches 15000.. run execute as @a[scores={sqs_109=0}] run function so_quests:q/109/ready
execute as @a[scores={sqs_110=0}] if score @s so_shop_seen matches 1.. run function so_quests:q/110/ready
execute as @a[scores={sqs_111=0}] if score @s so_shop_buys matches 10.. run function so_quests:q/111/ready
execute as @a[scores={sqs_112=0},advancements={so_quests:trade/any=true}] run function so_quests:q/112/ready
execute as @a[scores={sqs_113=0},advancements={so_quests:trade/mercader_de_la_llanura=true}] run function so_quests:q/113/ready
execute as @a[scores={sqs_114=0},advancements={so_quests:trade/buzo_mercante=true}] run function so_quests:q/114/ready
execute as @a[scores={sqs_115=0},advancements={so_quests:trade/comerciante_infernal=true}] run function so_quests:q/115/ready
execute as @a[scores={sqs_116=0},advancements={so_quests:trade/saqueador_de_tumbas=true}] run function so_quests:q/116/ready
execute as @a[scores={sqs_117=0},advancements={so_quests:trade/maestro_del_oneblock=true}] run function so_quests:q/117/ready
execute as @a[scores={sqs_201=0}] if score @s sqp_201 matches 500.. run function so_quests:q/201/ready
execute as @a[scores={sqs_202=0}] if score @s sqp_202 matches 100.. run function so_quests:q/202/ready
execute as @a[scores={sqs_203=0}] if score @s sqp_203 matches 64.. run function so_quests:q/203/ready
execute as @a[scores={sqs_204=0}] if score @s sqp_204 matches 64.. run function so_quests:q/204/ready
execute as @a[scores={sqs_205=0}] if score @s sqp_205 matches 32.. run function so_quests:q/205/ready
execute as @a[scores={sqs_206=0}] if score @s sqp_206 matches 16.. run function so_quests:q/206/ready
execute as @a[scores={sqs_207=0}] if score @s sqp_207 matches 5.. run function so_quests:q/207/ready
execute as @a[scores={sqs_208=0}] if score @s sqp_208 matches 128.. run function so_quests:q/208/ready
execute as @a[scores={sqs_209=0}] if score @s sqp_209 matches 4.. run function so_quests:q/209/ready
execute as @a[scores={sqs_210=0}] if score @s sqp_210 matches 128.. run function so_quests:q/210/ready
execute as @a[scores={sqs_211=0}] if score @s sqp_211 matches 1.. run function so_quests:q/211/ready
execute as @a[scores={sqs_212=0}] if score @s sqp_212 matches 1.. run function so_quests:q/212/ready
execute as @a[scores={sqs_213=0}] if score @s sqp_213 matches 32.. run function so_quests:q/213/ready
execute as @a[scores={sqs_214=0}] if score @s sqp_214 matches 8.. run function so_quests:q/214/ready
execute as @a[scores={sqs_215=0}] if score @s sqp_215 matches 1.. run function so_quests:q/215/ready
execute as @a[scores={sqs_216=0}] if score @s sqp_216 matches 64.. run function so_quests:q/216/ready
execute as @a[scores={sqs_217=0}] if score @s sqp_217 matches 64.. run function so_quests:q/217/ready
execute as @a[scores={sqs_218=0}] if score @s sqp_218 matches 1.. run function so_quests:q/218/ready
execute as @a[scores={sqs_301=0}] if score @s sqp_301 matches 50.. run function so_quests:q/301/ready
execute as @a[scores={sqs_302=0}] if score @s sqp_302 matches 50.. run function so_quests:q/302/ready
execute as @a[scores={sqs_303=0}] if score @s sqp_303 matches 30.. run function so_quests:q/303/ready
execute as @a[scores={sqs_304=0}] if score @s sqp_304 matches 25.. run function so_quests:q/304/ready
execute as @a[scores={sqs_305=0}] if score @s sqp_305 matches 15.. run function so_quests:q/305/ready
execute as @a[scores={sqs_306=0}] if score @s sqp_306 matches 10.. run function so_quests:q/306/ready
execute as @a[scores={sqs_307=0}] if score @s sqp_307 matches 10.. run function so_quests:q/307/ready
execute as @a[scores={sqs_308=0}] if score @s sqp_308 matches 20.. run function so_quests:q/308/ready
execute as @a[scores={sqs_309=0}] if score @s sqp_309 matches 300.. run function so_quests:q/309/ready
execute as @a[scores={sqs_310=0}] if score @s sqp_310 matches 1000000.. run function so_quests:q/310/ready
execute as @a run scoreboard players operation @s sqv_310 = @s sqp_310
execute as @a run scoreboard players operation @s sqv_310 /= #100 sq
execute as @a[scores={sqs_311=0}] if score @s sqp_311 matches 200000.. run function so_quests:q/311/ready
execute as @a run scoreboard players operation @s sqv_311 = @s sqp_311
execute as @a run scoreboard players operation @s sqv_311 /= #100 sq
execute as @a[scores={sqs_312=0}] if score @s sqp_312 matches 20.. run function so_quests:q/312/ready
execute as @a[scores={sqs_313=0}] if score @s sqp_313 matches 30.. run function so_quests:q/313/ready
execute as @a[scores={sqs_314=0}] if score @s sqp_314 matches 25.. run function so_quests:q/314/ready
execute as @a[scores={sqs_315=0}] if score @s sqp_315 matches 50000.. run function so_quests:q/315/ready
execute as @a run scoreboard players operation @s sqv_315 = @s sqp_315
execute as @a run scoreboard players operation @s sqv_315 /= #100 sq
execute as @a[scores={sqs_401=0},advancements={minecraft:story/mine_stone=true}] run function so_quests:q/401/ready
execute as @a[scores={sqs_402=0},advancements={minecraft:story/upgrade_tools=true}] run function so_quests:q/402/ready
execute as @a[scores={sqs_403=0},advancements={minecraft:story/smelt_iron=true}] run function so_quests:q/403/ready
execute as @a[scores={sqs_404=0},advancements={minecraft:story/obtain_armor=true}] run function so_quests:q/404/ready
execute as @a[scores={sqs_405=0},advancements={minecraft:story/lava_bucket=true}] run function so_quests:q/405/ready
execute as @a[scores={sqs_406=0},advancements={minecraft:story/iron_tools=true}] run function so_quests:q/406/ready
execute as @a[scores={sqs_407=0},advancements={minecraft:story/deflect_arrow=true}] run function so_quests:q/407/ready
execute as @a[scores={sqs_408=0},advancements={minecraft:story/form_obsidian=true}] run function so_quests:q/408/ready
execute as @a[scores={sqs_409=0},advancements={minecraft:story/mine_diamond=true}] run function so_quests:q/409/ready
execute as @a[scores={sqs_410=0},advancements={minecraft:story/enter_the_nether=true}] run function so_quests:q/410/ready
execute as @a[scores={sqs_411=0},advancements={minecraft:story/shiny_gear=true}] run function so_quests:q/411/ready
execute as @a[scores={sqs_412=0},advancements={minecraft:story/enchant_item=true}] run function so_quests:q/412/ready
execute as @a[scores={sqs_413=0},advancements={minecraft:story/cure_zombie_villager=true}] run function so_quests:q/413/ready
execute as @a[scores={sqs_414=0},advancements={minecraft:story/follow_ender_eye=true}] run function so_quests:q/414/ready
execute as @a[scores={sqs_415=0},advancements={minecraft:story/enter_the_end=true}] run function so_quests:q/415/ready
execute as @a[scores={sqs_416=0},advancements={minecraft:nether/find_fortress=true}] run function so_quests:q/416/ready
execute as @a[scores={sqs_417=0},advancements={minecraft:nether/obtain_blaze_rod=true}] run function so_quests:q/417/ready
execute as @a[scores={sqs_418=0},advancements={minecraft:nether/get_wither_skull=true}] run function so_quests:q/418/ready
execute as @a[scores={sqs_419=0},advancements={minecraft:nether/summon_wither=true}] run function so_quests:q/419/ready
execute as @a[scores={sqs_420=0},advancements={minecraft:nether/brew_potion=true}] run function so_quests:q/420/ready
execute as @a[scores={sqs_421=0},advancements={minecraft:end/kill_dragon=true}] run function so_quests:q/421/ready
execute as @a[scores={sqs_422=0},advancements={minecraft:end/find_end_city=true}] run function so_quests:q/422/ready
execute as @a[scores={sqs_423=0},advancements={minecraft:adventure/kill_a_mob=true}] run function so_quests:q/423/ready
execute as @a[scores={sqs_424=0},advancements={minecraft:adventure/trade=true}] run function so_quests:q/424/ready
execute as @a[scores={sqs_425=0},advancements={minecraft:adventure/totem_of_undying=true}] run function so_quests:q/425/ready
execute as @a[scores={sqs_426=0},advancements={minecraft:husbandry/plant_seed=true}] run function so_quests:q/426/ready
execute as @a[scores={sqs_427=0},advancements={minecraft:husbandry/breed_an_animal=true}] run function so_quests:q/427/ready
execute as @a[scores={sqs_428=0},advancements={minecraft:husbandry/tame_an_animal=true}] run function so_quests:q/428/ready
execute as @a[scores={sqc_501=1..}] run scoreboard players operation #raw_501 sq_group += @s sqc_501
scoreboard players set @a[scores={sqc_501=1..}] sqc_501 0
scoreboard players operation #g_501 sq_group = #raw_501 sq_group
execute unless score #done_501 sq_group matches 1 if score #g_501 sq_group matches 3000.. run function so_quests:q/501/ready
execute as @a[scores={sqc_502=1..}] run scoreboard players operation #raw_502 sq_group += @s sqc_502
scoreboard players set @a[scores={sqc_502=1..}] sqc_502 0
scoreboard players operation #g_502 sq_group = #raw_502 sq_group
execute unless score #done_502 sq_group matches 1 if score #g_502 sq_group matches 3000.. run function so_quests:q/502/ready
execute as @a[scores={sqc_503=1..}] run scoreboard players operation #raw_503 sq_group += @s sqc_503
scoreboard players set @a[scores={sqc_503=1..}] sqc_503 0
scoreboard players operation #g_503 sq_group = #raw_503 sq_group
execute unless score #done_503 sq_group matches 1 if score #g_503 sq_group matches 2000.. run function so_quests:q/503/ready
execute as @a[scores={sqc_504=1..}] run scoreboard players operation #raw_504 sq_group += @s sqc_504
scoreboard players set @a[scores={sqc_504=1..}] sqc_504 0
scoreboard players operation #g_504 sq_group = #raw_504 sq_group
execute unless score #done_504 sq_group matches 1 if score #g_504 sq_group matches 5000.. run function so_quests:q/504/ready
execute as @a[scores={sqc_505=1..}] run scoreboard players operation #raw_505 sq_group += @s sqc_505
scoreboard players set @a[scores={sqc_505=1..}] sqc_505 0
scoreboard players operation #g_505 sq_group = #raw_505 sq_group
execute unless score #done_505 sq_group matches 1 if score #g_505 sq_group matches 1000.. run function so_quests:q/505/ready
execute as @a[scores={sqc_506=1..}] run scoreboard players operation #raw_506 sq_group += @s sqc_506
scoreboard players set @a[scores={sqc_506=1..}] sqc_506 0
scoreboard players operation #g_506 sq_group = #raw_506 sq_group
execute unless score #done_506 sq_group matches 1 if score #g_506 sq_group matches 500.. run function so_quests:q/506/ready
execute as @a[scores={sqc_507=1..}] run scoreboard players operation #raw_507 sq_group += @s sqc_507
scoreboard players set @a[scores={sqc_507=1..}] sqc_507 0
scoreboard players operation #g_507 sq_group = #raw_507 sq_group
execute unless score #done_507 sq_group matches 1 if score #g_507 sq_group matches 800.. run function so_quests:q/507/ready
execute as @a[scores={sqc_508=1..}] run scoreboard players operation #raw_508 sq_group += @s sqc_508
scoreboard players set @a[scores={sqc_508=1..}] sqc_508 0
scoreboard players operation #g_508 sq_group = #raw_508 sq_group
execute unless score #done_508 sq_group matches 1 if score #g_508 sq_group matches 300.. run function so_quests:q/508/ready
execute as @a[scores={sqc_509=1..}] run scoreboard players operation #raw_509 sq_group += @s sqc_509
scoreboard players set @a[scores={sqc_509=1..}] sqc_509 0
scoreboard players operation #g_509 sq_group = #raw_509 sq_group
execute unless score #done_509 sq_group matches 1 if score #g_509 sq_group matches 500.. run function so_quests:q/509/ready
execute as @a[scores={sqc_510=1..}] run scoreboard players operation #raw_510 sq_group += @s sqc_510
scoreboard players set @a[scores={sqc_510=1..}] sqc_510 0
scoreboard players operation #g_510 sq_group = #raw_510 sq_group
execute unless score #done_510 sq_group matches 1 if score #g_510 sq_group matches 300.. run function so_quests:q/510/ready
execute as @a[scores={sqc_511=1..}] run scoreboard players operation #raw_511 sq_group += @s sqc_511
scoreboard players set @a[scores={sqc_511=1..}] sqc_511 0
scoreboard players operation #g_511 sq_group = #raw_511 sq_group
execute unless score #done_511 sq_group matches 1 if score #g_511 sq_group matches 150.. run function so_quests:q/511/ready
execute as @a[scores={sqc_512=1..}] run scoreboard players operation #raw_512 sq_group += @s sqc_512
scoreboard players set @a[scores={sqc_512=1..}] sqc_512 0
scoreboard players operation #g_512 sq_group = #raw_512 sq_group
execute unless score #done_512 sq_group matches 1 if score #g_512 sq_group matches 300.. run function so_quests:q/512/ready
execute as @a[scores={sqc_513=1..}] run scoreboard players operation #raw_513 sq_group += @s sqc_513
scoreboard players set @a[scores={sqc_513=1..}] sqc_513 0
scoreboard players operation #g_513 sq_group = #raw_513 sq_group
execute unless score #done_513 sq_group matches 1 if score #g_513 sq_group matches 300.. run function so_quests:q/513/ready
execute as @a[scores={sqc_514=1..}] run scoreboard players operation #raw_514 sq_group += @s sqc_514
scoreboard players set @a[scores={sqc_514=1..}] sqc_514 0
scoreboard players operation #g_514 sq_group = #raw_514 sq_group
execute unless score #done_514 sq_group matches 1 if score #g_514 sq_group matches 300.. run function so_quests:q/514/ready
execute as @a[scores={sqc_515=1..}] run scoreboard players operation #raw_515 sq_group += @s sqc_515
scoreboard players set @a[scores={sqc_515=1..}] sqc_515 0
scoreboard players operation #g_515 sq_group = #raw_515 sq_group
execute unless score #done_515 sq_group matches 1 if score #g_515 sq_group matches 300.. run function so_quests:q/515/ready
execute as @a[scores={sqc_516=1..}] run scoreboard players operation #raw_516 sq_group += @s sqc_516
scoreboard players set @a[scores={sqc_516=1..}] sqc_516 0
scoreboard players operation #g_516 sq_group = #raw_516 sq_group
execute unless score #done_516 sq_group matches 1 if score #g_516 sq_group matches 300.. run function so_quests:q/516/ready
execute as @a[scores={sqc_517=1..}] run scoreboard players operation #raw_517 sq_group += @s sqc_517
scoreboard players set @a[scores={sqc_517=1..}] sqc_517 0
scoreboard players operation #g_517 sq_group = #raw_517 sq_group
execute unless score #done_517 sq_group matches 1 if score #g_517 sq_group matches 300.. run function so_quests:q/517/ready
execute as @a[scores={sqc_518=1..}] run scoreboard players operation #raw_518 sq_group += @s sqc_518
scoreboard players set @a[scores={sqc_518=1..}] sqc_518 0
scoreboard players operation #g_518 sq_group = #raw_518 sq_group
execute unless score #done_518 sq_group matches 1 if score #g_518 sq_group matches 200.. run function so_quests:q/518/ready
execute as @a[scores={sqc_519=1..}] run scoreboard players operation #raw_519 sq_group += @s sqc_519
scoreboard players set @a[scores={sqc_519=1..}] sqc_519 0
scoreboard players operation #g_519 sq_group = #raw_519 sq_group
execute unless score #done_519 sq_group matches 1 if score #g_519 sq_group matches 200.. run function so_quests:q/519/ready
execute as @a[scores={sqc_520=1..}] run scoreboard players operation #raw_520 sq_group += @s sqc_520
scoreboard players set @a[scores={sqc_520=1..}] sqc_520 0
scoreboard players operation #g_520 sq_group = #raw_520 sq_group
execute unless score #done_520 sq_group matches 1 if score #g_520 sq_group matches 3000.. run function so_quests:q/520/ready
execute as @a[scores={sqc_521=1..}] run scoreboard players operation #raw_521 sq_group += @s sqc_521
scoreboard players set @a[scores={sqc_521=1..}] sqc_521 0
scoreboard players operation #g_521 sq_group = #raw_521 sq_group
execute unless score #done_521 sq_group matches 1 if score #g_521 sq_group matches 1000.. run function so_quests:q/521/ready
execute as @a[scores={sqc_522=1..}] run scoreboard players operation #raw_522 sq_group += @s sqc_522
scoreboard players set @a[scores={sqc_522=1..}] sqc_522 0
scoreboard players operation #g_522 sq_group = #raw_522 sq_group
execute unless score #done_522 sq_group matches 1 if score #g_522 sq_group matches 500.. run function so_quests:q/522/ready
execute as @a[scores={sqc_523=1..}] run scoreboard players operation #raw_523 sq_group += @s sqc_523
scoreboard players set @a[scores={sqc_523=1..}] sqc_523 0
scoreboard players operation #g_523 sq_group = #raw_523 sq_group
execute unless score #done_523 sq_group matches 1 if score #g_523 sq_group matches 100.. run function so_quests:q/523/ready
execute as @a[scores={sqc_524=1..}] run scoreboard players operation #raw_524 sq_group += @s sqc_524
scoreboard players set @a[scores={sqc_524=1..}] sqc_524 0
scoreboard players operation #g_524 sq_group = #raw_524 sq_group
execute unless score #done_524 sq_group matches 1 if score #g_524 sq_group matches 200.. run function so_quests:q/524/ready
execute as @a[scores={sqc_525=1..}] run scoreboard players operation #raw_525 sq_group += @s sqc_525
scoreboard players set @a[scores={sqc_525=1..}] sqc_525 0
scoreboard players operation #g_525 sq_group = #raw_525 sq_group
execute unless score #done_525 sq_group matches 1 if score #g_525 sq_group matches 100.. run function so_quests:q/525/ready
execute as @a[scores={sqc_526=1..}] run scoreboard players operation #raw_526 sq_group += @s sqc_526
scoreboard players set @a[scores={sqc_526=1..}] sqc_526 0
scoreboard players operation #g_526 sq_group = #raw_526 sq_group
execute unless score #done_526 sq_group matches 1 if score #g_526 sq_group matches 2000.. run function so_quests:q/526/ready
execute as @a[scores={sqc_527=1..}] run scoreboard players operation #raw_527 sq_group += @s sqc_527
scoreboard players set @a[scores={sqc_527=1..}] sqc_527 0
scoreboard players operation #g_527 sq_group = #raw_527 sq_group
execute unless score #done_527 sq_group matches 1 if score #g_527 sq_group matches 500.. run function so_quests:q/527/ready
execute as @a[scores={sqc_528=1..}] run scoreboard players operation #raw_528 sq_group += @s sqc_528
scoreboard players set @a[scores={sqc_528=1..}] sqc_528 0
scoreboard players operation #g_528 sq_group = #raw_528 sq_group
execute unless score #done_528 sq_group matches 1 if score #g_528 sq_group matches 500.. run function so_quests:q/528/ready
execute as @a[scores={sqc_529=1..}] run scoreboard players operation #raw_529 sq_group += @s sqc_529
scoreboard players set @a[scores={sqc_529=1..}] sqc_529 0
scoreboard players operation #g_529 sq_group = #raw_529 sq_group
execute unless score #done_529 sq_group matches 1 if score #g_529 sq_group matches 500.. run function so_quests:q/529/ready
execute as @a[scores={sqc_530=1..}] run scoreboard players operation #raw_530 sq_group += @s sqc_530
scoreboard players set @a[scores={sqc_530=1..}] sqc_530 0
scoreboard players operation #g_530 sq_group = #raw_530 sq_group
execute unless score #done_530 sq_group matches 1 if score #g_530 sq_group matches 300.. run function so_quests:q/530/ready
execute as @a[scores={sqc_531=1..}] run scoreboard players operation #raw_531 sq_group += @s sqc_531
scoreboard players set @a[scores={sqc_531=1..}] sqc_531 0
scoreboard players operation #g_531 sq_group = #raw_531 sq_group
execute unless score #done_531 sq_group matches 1 if score #g_531 sq_group matches 200.. run function so_quests:q/531/ready
execute as @a[scores={sqc_532=1..}] run scoreboard players operation #raw_532 sq_group += @s sqc_532
scoreboard players set @a[scores={sqc_532=1..}] sqc_532 0
scoreboard players operation #g_532 sq_group = #raw_532 sq_group
execute unless score #done_532 sq_group matches 1 if score #g_532 sq_group matches 3000.. run function so_quests:q/532/ready
execute as @a[scores={sqc_533=1..}] run scoreboard players operation #raw_533 sq_group += @s sqc_533
scoreboard players set @a[scores={sqc_533=1..}] sqc_533 0
scoreboard players operation #g_533 sq_group = #raw_533 sq_group
scoreboard players operation #g_533 sq_group /= #100 sq
execute unless score #done_533 sq_group matches 1 if score #g_533 sq_group matches 50000.. run function so_quests:q/533/ready
execute as @a[scores={sqc_534=1..}] run scoreboard players operation #raw_534 sq_group += @s sqc_534
scoreboard players set @a[scores={sqc_534=1..}] sqc_534 0
scoreboard players operation #g_534 sq_group = #raw_534 sq_group
scoreboard players operation #g_534 sq_group /= #100 sq
execute unless score #done_534 sq_group matches 1 if score #g_534 sq_group matches 20000.. run function so_quests:q/534/ready
execute as @a[scores={sqc_535=1..}] run scoreboard players operation #raw_535 sq_group += @s sqc_535
scoreboard players set @a[scores={sqc_535=1..}] sqc_535 0
scoreboard players operation #g_535 sq_group = #raw_535 sq_group
scoreboard players operation #g_535 sq_group /= #100 sq
execute unless score #done_535 sq_group matches 1 if score #g_535 sq_group matches 10000.. run function so_quests:q/535/ready
execute as @a[scores={sqc_536=1..}] run scoreboard players operation #raw_536 sq_group += @s sqc_536
scoreboard players set @a[scores={sqc_536=1..}] sqc_536 0
scoreboard players operation #g_536 sq_group = #raw_536 sq_group
scoreboard players operation #g_536 sq_group /= #100 sq
execute unless score #done_536 sq_group matches 1 if score #g_536 sq_group matches 10000.. run function so_quests:q/536/ready
execute as @a[scores={sqs_601=0}] if score @s sqp_601 matches 20.. run function so_quests:q/601/ready
execute as @a[scores={sqs_602=0}] if score @s sqp_602 matches 128.. run function so_quests:q/602/ready
