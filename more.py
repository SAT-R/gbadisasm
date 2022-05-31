import os
current_config_lines = open("new_test.cfg").readlines()

def test():
    return os.system("./gbadisasm mb_chao_garden.gba -c new_test.cfg > test.s")


def write_config():
     with open('new_test.cfg', 'w') as config:
        config.write("".join(current_config_lines))

more_found = True
while more_found:
    more_found = False
    potential_functions = []
    with open('test.s') as assembly:
        lines = assembly.readlines()
        for i in range(len(lines)):
            line = lines[i]
            if line.startswith("_02"):
                next_line = lines[i + 1]
                if ".byte" in next_line and not next_line.startswith("_02"):
                    potential_functions.append(line[1:-2])

    for func in potential_functions:
        already_found = False
        for config_line in current_config_lines:
            if func in config_line:
                already_found = True
        
        if already_found:
            continue

        more_found = True

        address = f"0x{func}"
        print(address)
        current_config_lines.append(f"thumb_func {address} sub_{func}\n")

        write_config()
        
        error = test()
        if not error:
            continue

        current_config_lines.pop(-1)
        current_config_lines.append(f"arm_func {address} sub_{func}\n")

        write_config()
        error = test()
        if not error:
            continue

        current_config_lines.pop(-1)
        current_config_lines.append(f"# thumb_func {address} sub_{func}\n")

    print(potential_functions)
