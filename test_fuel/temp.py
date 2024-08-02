# Convert fraction to string
        try:
            instr = infrac.split("/")
        except (ValueError,TypeError):
            continue
        try:
            x = int(instr[0])
        except (ValueError, TypeError):
            continue
        try:
            y = int(instr[1])
        except (ValueError, TypeError):
            continue
        if x > y:
            continue
        elif y == 0:
            continue
        else:
            return x, y
