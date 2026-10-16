$setblock ~ ~ ~ minecraft:chest{LootTable:"so_events:$(t)",CustomName:{text:"Cofre de Recompensa",color:"gold",bold:true}}
summon minecraft:text_display ~0.5 ~1.4 ~0.5 {Tags:["so_ev_chestlbl"],billboard:"center",text:{text:"✦ COFRE DE RECOMPENSA ✦",color:"gold",bold:true},background:0}
particle minecraft:totem_of_undying ~0.5 ~1 ~0.5 0.3 0.4 0.3 0.2 30
playsound minecraft:block.chest.open master @a ~ ~ ~ 1 0.7
playsound minecraft:entity.player.levelup master @a ~ ~ ~ 0.8 1.2
scoreboard players set #pl so_ev 1
