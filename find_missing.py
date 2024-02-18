print("")

func_num = 0
with open("sa3_europe.s") as code_file:
    func = None
    num_bytes = 0
    for line in code_file.readlines():
        line = line.strip()
        if line.startswith("_"):
            func = line.replace('_', '').replace(':', '')
            num_bytes = 0
            continue

        if line.startswith(".byte") and func :
            num_bytes += len(line.split(","))
            for byte in line.split(","):
                if "0x00" in byte:
                    num_bytes -= 1 
            
            if num_bytes > 5:
                func_num += 1
                if func_num >= 2:
                    print(f"thumb_func 0x{func} sub_{func[1:].upper()}")
                func = None
