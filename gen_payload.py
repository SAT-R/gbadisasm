import os

lines = []

arm_funcs = [
    "0x0203b000",
    "0x0203b03c",
    "0x0203b10c",
    "0x0203b14c"
]

def write_config():
     with open('payload.cfg', 'w') as config:
        config.write("\n".join(lines))

def test():
    return os.system("./gbadisasm payload.gba -c payload.cfg > payload.s")

with open('payload_functions.csv') as functions_file:
    for line in functions_file.readlines():
        parsed = line.split(',')[1].split('\"')[1]
        address = f"0x{parsed}"
        print(address)

        type = "thumb_func" if address not in arm_funcs else "arm_func"
        lines.append(f"{type} {address} sub_{parsed}")

        write_config()
        
        error = test()
        if error:
            break
