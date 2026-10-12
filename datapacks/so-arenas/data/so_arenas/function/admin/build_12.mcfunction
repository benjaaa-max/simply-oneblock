# coliseo: paso 12/14
fill -5002 96 -4914 -5002 99 -4914 minecraft:deepslate_tiles
fill -4998 96 -4914 -4998 99 -4914 minecraft:deepslate_tiles
fill -5002 100 -4914 -4998 100 -4914 minecraft:polished_deepslate
fill -5001 96 -4913 -4999 99 -4913 minecraft:polished_blackstone_bricks
setblock -5000 96 -4913 minecraft:dark_oak_door[half=lower,facing=north]
setblock -5000 97 -4913 minecraft:dark_oak_door[half=upper,facing=north]
setblock -5002 101 -4914 minecraft:soul_lantern
setblock -4998 101 -4914 minecraft:soul_lantern
setblock -5000 95 -4915 minecraft:crying_obsidian
setblock -5000 96 -4915 minecraft:polished_blackstone_pressure_plate
setblock -5001 96 -4915 minecraft:oak_sign[rotation=8]{is_waxed:1b,front_text:{messages:[{text:"Entrada a",color:"black",bold:false},{text:"Catacumbas",color:"dark_purple",bold:true,click_event:{action:"run_command",command:"/trigger arena_dg set 20"}},{text:"pisá la placa",color:"black",bold:false},{text:"o tocá acá",color:"black",bold:false}]}}
fill -5046 58 -5048 -5030 67 -5032 minecraft:deepslate_tiles hollow
fill -5046 62 -5048 -5030 62 -5032 minecraft:mossy_stone_bricks replace minecraft:deepslate_tiles
fill -5024 58 -5048 -5008 67 -5032 minecraft:deepslate_tiles hollow
fill -5024 62 -5048 -5008 62 -5032 minecraft:mossy_stone_bricks replace minecraft:deepslate_tiles
fill -5002 58 -5048 -4986 67 -5032 minecraft:deepslate_tiles hollow
fill -5002 62 -5048 -4986 62 -5032 minecraft:mossy_stone_bricks replace minecraft:deepslate_tiles
fill -4981 58 -5051 -4959 71 -5029 minecraft:deepslate_tiles hollow
fill -4981 62 -5051 -4959 62 -5029 minecraft:mossy_stone_bricks replace minecraft:deepslate_tiles
fill -5030 58 -5042 -5024 64 -5038 minecraft:deepslate_tiles hollow
fill -5008 58 -5042 -5002 64 -5038 minecraft:deepslate_tiles hollow
fill -4986 58 -5042 -4981 64 -5038 minecraft:deepslate_tiles hollow
function so_arenas:dg/cripta/reset
