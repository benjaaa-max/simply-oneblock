function so_quests:lib/read_count
tellraw @s [{"text": "[Misiones] ", "color": "gold"}, {"text": "Fuente (1=so_core 2=Simply OneBlock 0=ninguna): ", "color": "gray"}, {"score": {"name": "#src", "objective": "sq"}, "color": "yellow"}, {"text": "  Bloques: ", "color": "gray"}, {"score": {"name": "#blocks", "objective": "sq"}, "color": "yellow"}]
