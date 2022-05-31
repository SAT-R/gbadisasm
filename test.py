import os

lines = []

def write_config():
     with open('test.cfg', 'w') as config:
        config.write("\n".join(lines))

def test():
    return os.system("./gbadisasm mb_chao_garden.gba -c test.cfg > test.s")

with open('functions.csv') as functions_file:
    for line in functions_file.readlines():
        parsed = line.split(',')[1].split('\"')[1]
        address = f"0x{parsed}"
        print(address)
        lines.append(f"thumb_func {address} sub_{parsed}")

        write_config()
        
        error = test()
        if not error:
            continue

        lines.pop(-1)
        lines.append(f"arm_func {address} sub_{parsed}")

        write_config()
        error = test()
        if not error:
            continue

        lines.pop(-1)
        lines.append(f"# thumb_func {address} sub_{parsed}")
