import os

lines = []

arm_funcs = [
    "0x02000180",
]

def write_config():
     with open('collect_rings.cfg', 'w') as config:
        config.write("\n".join(lines))

def test():
    return os.system("./gbadisasm collect_rings.gba -c collect_rings.cfg > collect_rings.s")

with open('collect_rings_functions.csv') as functions_file:
    for line in functions_file.readlines():
        parsed = line.split(',')[1].split('\"')[1]
        address = f"0x{parsed}"
        print(address)

        type = "thumb_func" if address not in arm_funcs else "arm_func"
        lines.append(f"{type} {address} sub_{parsed}")

    write_config()
        
    error = test()
    if error:
        print("error")
