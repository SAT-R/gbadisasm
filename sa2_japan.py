import os

lines = []

def write_config():
     with open('sa2_japan.cfg', 'w') as config:
        config.write("\n".join(lines))

def test():
    return os.system("./gbadisasm sa2_japan.gba -c sa2_japan.cfg > sa2_japan.s")

i = 1
multiplier = 1

with open('sa2_japan.csv') as functions_file:
    for line in functions_file.readlines():
        parsed = line.split(',')[1].split('\"')[1].upper()
        address = f"0x{parsed}"
        print(address)
        lines.append(f"thumb_func {address} sub_{parsed}")

        write_config()

        if multiplier == 0 or i % (multiplier) == 0:
            if i % (multiplier) == 0 and i > 20:
                multiplier *= 2
            error = test()
            if not error:
                i += 1
                continue

            if i > 20:
                print("Not good")
                exit(1)

            lines.pop(-1)
            lines.append(f"arm_func {address} sub_{parsed}\n")

            write_config()
            error = test()
            if not error:
                i = 0
                continue

            lines.pop(-1)
            lines.append(f"# thumb_func {address} sub_{parsed}\n")
        else:
            i += 1
    test()
