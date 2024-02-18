import os

lines = []

arm_funcs = [
    "0x0203B000",
    "0x0203B03C",
    "0x0203B10C",
    "0x0203B14C"
]

def write_config():
     with open('subgame_loader.cfg', 'w') as config:
        config.write("\n".join(lines))

def test():
    return os.system("./gbadisasm mb_subgame_loader_2.gba -s -c subgame_loader.cfg > subgame_loader.s")

with open('subgame_loader_functions.csv') as functions_file:
    for line in functions_file.readlines():
        parsed = line.split(',')[1].split('\"')[1]
        address = f"0x{parsed.upper()}"
        print(address)

        type = "thumb_func" if address not in arm_funcs else "arm_func"
        lines.append(f"{type} {address} sub_{parsed.upper()}")

        write_config()
            
        error = test()
        if error:
            break
