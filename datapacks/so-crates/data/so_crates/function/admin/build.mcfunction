# Construye la zona de Crates. Párate en la zona antes (admin/goto) para que esté cargada.
fill 4984 200 4984 5016 204 5016 minecraft:barrier hollow
fill 4985 199 4985 5015 199 5015 minecraft:polished_blackstone_bricks
fill 4985 200 4985 5015 203 5015 minecraft:air
fill 4984 198 4984 5016 198 5016 minecraft:barrier
setblock 4987 199 4987 minecraft:sea_lantern
setblock 4987 199 4992 minecraft:sea_lantern
setblock 4987 199 4997 minecraft:sea_lantern
setblock 4987 199 5002 minecraft:sea_lantern
setblock 4987 199 5007 minecraft:sea_lantern
setblock 4987 199 5012 minecraft:sea_lantern
setblock 4992 199 4987 minecraft:sea_lantern
setblock 4992 199 4992 minecraft:sea_lantern
setblock 4992 199 4997 minecraft:sea_lantern
setblock 4992 199 5002 minecraft:sea_lantern
setblock 4992 199 5007 minecraft:sea_lantern
setblock 4992 199 5012 minecraft:sea_lantern
setblock 4997 199 4987 minecraft:sea_lantern
setblock 4997 199 4992 minecraft:sea_lantern
setblock 4997 199 4997 minecraft:sea_lantern
setblock 4997 199 5002 minecraft:sea_lantern
setblock 4997 199 5007 minecraft:sea_lantern
setblock 4997 199 5012 minecraft:sea_lantern
setblock 5002 199 4987 minecraft:sea_lantern
setblock 5002 199 4992 minecraft:sea_lantern
setblock 5002 199 4997 minecraft:sea_lantern
setblock 5002 199 5002 minecraft:sea_lantern
setblock 5002 199 5007 minecraft:sea_lantern
setblock 5002 199 5012 minecraft:sea_lantern
setblock 5007 199 4987 minecraft:sea_lantern
setblock 5007 199 4992 minecraft:sea_lantern
setblock 5007 199 4997 minecraft:sea_lantern
setblock 5007 199 5002 minecraft:sea_lantern
setblock 5007 199 5007 minecraft:sea_lantern
setblock 5007 199 5012 minecraft:sea_lantern
setblock 5012 199 4987 minecraft:sea_lantern
setblock 5012 199 4992 minecraft:sea_lantern
setblock 5012 199 4997 minecraft:sea_lantern
setblock 5012 199 5002 minecraft:sea_lantern
setblock 5012 199 5007 minecraft:sea_lantern
setblock 5012 199 5012 minecraft:sea_lantern
fill 4999 199 4999 5001 199 5001 minecraft:gilded_blackstone
setblock 4989 200 4990 minecraft:vault[facing=south,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":"Cemetery Key"}},loot_table:"so_crates:oneblock/cemetery"}} replace
setblock 4989 201 4990 minecraft:dark_oak_sign[rotation=0]{is_waxed:1b,front_text:{messages:["",{text:"OneBlock Crate",color:"gold",bold:true},{text:"Cemetery Key",color:"dark_gray"},""]}} replace
setblock 4991 200 4990 minecraft:vault[facing=south,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":"Graveyard Key"}},loot_table:"so_crates:oneblock/graveyard"}} replace
setblock 4991 201 4990 minecraft:dark_oak_sign[rotation=0]{is_waxed:1b,front_text:{messages:["",{text:"OneBlock Crate",color:"gold",bold:true},{text:"Graveyard Key",color:"dark_gray"},""]}} replace
setblock 4993 200 4990 minecraft:vault[facing=south,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":"Ossuary Key"}},loot_table:"so_crates:oneblock/ossuary"}} replace
setblock 4993 201 4990 minecraft:dark_oak_sign[rotation=0]{is_waxed:1b,front_text:{messages:["",{text:"OneBlock Crate",color:"gold",bold:true},{text:"Ossuary Key",color:"dark_gray"},""]}} replace
setblock 4995 200 4990 minecraft:vault[facing=south,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":"Old Tower Key"}},loot_table:"so_crates:oneblock/old_tower"}} replace
setblock 4995 201 4990 minecraft:dark_oak_sign[rotation=0]{is_waxed:1b,front_text:{messages:["",{text:"OneBlock Crate",color:"gold",bold:true},{text:"Old Tower Key",color:"dark_gray"},""]}} replace
setblock 4997 200 4990 minecraft:vault[facing=south,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":"Pyramid Key"}},loot_table:"so_crates:oneblock/pyramid"}} replace
setblock 4997 201 4990 minecraft:dark_oak_sign[rotation=0]{is_waxed:1b,front_text:{messages:["",{text:"OneBlock Crate",color:"gold",bold:true},{text:"Pyramid Key",color:"dark_gray"},""]}} replace
setblock 4999 200 4990 minecraft:vault[facing=south,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":"Rusty Mineshaft Key"}},loot_table:"so_crates:oneblock/rusty"}} replace
setblock 4999 201 4990 minecraft:dark_oak_sign[rotation=0]{is_waxed:1b,front_text:{messages:["",{text:"OneBlock Crate",color:"gold",bold:true},{text:"Rusty Mineshaft Key",color:"dark_gray"},""]}} replace
setblock 5001 200 4990 minecraft:vault[facing=south,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":"Treasure Room"}},loot_table:"so_crates:oneblock/treasure"}} replace
setblock 5001 201 4990 minecraft:dark_oak_sign[rotation=0]{is_waxed:1b,front_text:{messages:["",{text:"OneBlock Crate",color:"gold",bold:true},{text:"Treasure Room",color:"dark_gray"},""]}} replace
setblock 5003 200 4990 minecraft:vault[facing=south,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":"Deep_Key"}},loot_table:"so_crates:oneblock/deep"}} replace
setblock 5003 201 4990 minecraft:dark_oak_sign[rotation=0]{is_waxed:1b,front_text:{messages:["",{text:"OneBlock Crate",color:"gold",bold:true},{text:"Deep_Key",color:"dark_gray"},""]}} replace
setblock 5005 200 4990 minecraft:vault[facing=south,ominous=true]{config:{key_item:{id:"minecraft:ominous_trial_key",count:1,components:{"minecraft:custom_name":"Elder Guardian Key"}},loot_table:"so_crates:oneblock/elder"}} replace
setblock 5005 201 4990 minecraft:dark_oak_sign[rotation=0]{is_waxed:1b,front_text:{messages:["",{text:"OneBlock Crate",color:"gold",bold:true},{text:"Elder Guardian Key",color:"dark_gray"},""]}} replace
setblock 5007 200 4990 minecraft:vault[facing=south,ominous=true]{config:{key_item:{id:"minecraft:ominous_trial_key",count:1,components:{"minecraft:custom_name":"Warden_Key"}},loot_table:"so_crates:oneblock/warden"}} replace
setblock 5007 201 4990 minecraft:dark_oak_sign[rotation=0]{is_waxed:1b,front_text:{messages:["",{text:"OneBlock Crate",color:"gold",bold:true},{text:"Warden_Key",color:"dark_gray"},""]}} replace
setblock 5009 200 4990 minecraft:vault[facing=south,ominous=true]{config:{key_item:{id:"minecraft:ominous_trial_key",count:1,components:{"minecraft:custom_name":"Wither Arena"}},loot_table:"so_crates:oneblock/wither"}} replace
setblock 5009 201 4990 minecraft:dark_oak_sign[rotation=0]{is_waxed:1b,front_text:{messages:["",{text:"OneBlock Crate",color:"gold",bold:true},{text:"Wither Arena",color:"dark_gray"},""]}} replace
setblock 5011 200 4990 minecraft:vault[facing=south,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":"To the End"}},loot_table:"so_crates:oneblock/to_the_end"}} replace
setblock 5011 201 4990 minecraft:dark_oak_sign[rotation=0]{is_waxed:1b,front_text:{messages:["",{text:"OneBlock Crate",color:"gold",bold:true},{text:"To the End",color:"dark_gray"},""]}} replace
setblock 4990 200 5010 minecraft:vault[facing=north,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":{text:"Llave del Arquitecto",color:"aqua",italic:false},"minecraft:lore":[{text:"Abre: Crate del Constructor",color:"gray",italic:false}]}},loot_table:"so_crates:builder"}} replace
setblock 4990 201 5010 minecraft:dark_oak_sign[rotation=8]{is_waxed:1b,front_text:{messages:["",{text:"Crate del Constructor",color:"gold",bold:true},{text:"Llave del Arquitecto",color:"dark_gray"},""]}} replace
setblock 4994 200 5010 minecraft:vault[facing=north,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":{text:"Llave Subterránea",color:"gray",italic:false},"minecraft:lore":[{text:"Abre: Crate del Minero",color:"gray",italic:false}]}},loot_table:"so_crates:miner"}} replace
setblock 4994 201 5010 minecraft:dark_oak_sign[rotation=8]{is_waxed:1b,front_text:{messages:["",{text:"Crate del Minero",color:"gold",bold:true},{text:"Llave Subterránea",color:"dark_gray"},""]}} replace
setblock 4998 200 5010 minecraft:vault[facing=north,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":{text:"Llave Silvestre",color:"green",italic:false},"minecraft:lore":[{text:"Abre: Crate de la Naturaleza",color:"gray",italic:false}]}},loot_table:"so_crates:nature"}} replace
setblock 4998 201 5010 minecraft:dark_oak_sign[rotation=8]{is_waxed:1b,front_text:{messages:["",{text:"Crate de la Naturaleza",color:"gold",bold:true},{text:"Llave Silvestre",color:"dark_gray"},""]}} replace
setblock 5002 200 5010 minecraft:vault[facing=north,ominous=false]{config:{key_item:{id:"minecraft:trial_key",count:1,components:{"minecraft:custom_name":{text:"Llave de Batalla",color:"red",italic:false},"minecraft:lore":[{text:"Abre: Crate de Combate",color:"gray",italic:false}]}},loot_table:"so_crates:combat"}} replace
setblock 5002 201 5010 minecraft:dark_oak_sign[rotation=8]{is_waxed:1b,front_text:{messages:["",{text:"Crate de Combate",color:"gold",bold:true},{text:"Llave de Batalla",color:"dark_gray"},""]}} replace
setblock 5006 200 5010 minecraft:vault[facing=north,ominous=true]{config:{key_item:{id:"minecraft:ominous_trial_key",count:1,components:{"minecraft:custom_name":{text:"Llave Abisal",color:"dark_purple",italic:false},"minecraft:lore":[{text:"Abre: Crate Místico",color:"gray",italic:false}]}},loot_table:"so_crates:mystic"}} replace
setblock 5006 201 5010 minecraft:dark_oak_sign[rotation=8]{is_waxed:1b,front_text:{messages:["",{text:"Crate Místico",color:"gold",bold:true},{text:"Llave Abisal",color:"dark_gray"},""]}} replace
setblock 5010 200 5010 minecraft:vault[facing=north,ominous=true]{config:{key_item:{id:"minecraft:ominous_trial_key",count:1,components:{"minecraft:custom_name":{text:"Llave del Vacío",color:"gold",italic:false},"minecraft:lore":[{text:"Abre: Crate Legendario",color:"gray",italic:false}]}},loot_table:"so_crates:legend"}} replace
setblock 5010 201 5010 minecraft:dark_oak_sign[rotation=8]{is_waxed:1b,front_text:{messages:["",{text:"Crate Legendario",color:"gold",bold:true},{text:"Llave del Vacío",color:"dark_gray"},""]}} replace
setblock 5000 200 5003 minecraft:dark_oak_sign[rotation=8]{is_waxed:1b,front_text:{messages:["",{text:"« Volver a la isla",color:"dark_green",bold:true,click_event:{action:"run_command",command:"/trigger isla"}},{text:"(toca el cartel)",color:"gray"},""]}} replace
tellraw @s [{"text":"[SO Crates] ","color":"gold"},{"text":"Zona construida: 18 bóvedas.","color":"green"}]
