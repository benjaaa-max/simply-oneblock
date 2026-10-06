# v4: remove the home gateway for a few ticks so Simply OneBlock advances past the milestone exactly once (its own air check does the +1).
execute in minecraft:overworld if block 0 65 0 minecraft:end_gateway if block 0 64 0 minecraft:bedrock run fill 0 64 0 0 66 0 minecraft:air
scoreboard players remove #pending spf_tmp 1
