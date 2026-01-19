class FileError(Exception):
    pass

class SyntaxError(FileError):
    pass

file_path = "config.txt"

requirements = ["width", "height", "entry", "exit", "exit", "output_file", "perfect"]
config = {}

def change_value(config_dic: dict):
    try:
        config_dic["width"] = int(config_dic["width"])
        config_dic["height"] = int(config_dic["height"])
        if config_dic["width"] < 8 or config_dic["width"] > 20:
            raise ValueError("impossible maze arguments")
        elif config_dic["height"] < 8 or config_dic["height"] > 20:
            raise ValueError("impossible maze arguments")
    except ValueError as e:
        print(f"{e}")

    try: 
        entry = [int(i) for i in config_dic["entry"].split(',')]
        exit_p = [int(i) for i in config_dic["exit"].split(',')]
        if len(entry) > 2 or len(exit_p) > 2:
            raise ValueError("impossible maze arguments")
    except ValueError as e:
        print(f"{e}")

    try:
        if config_dic["perfect"].lower() == "true":
            config_dic["perfect"] = True
        elif config_dic["perfect"].lower() == "false":
            config.dic["perfect"] = False
        else:
            raise ValueError("impossible maze arguments")
    except ValueError as e:
        print(f"{e}")

try:
    fd = open(file_path, 'r')
    for line in fd:
        if line.startswith("#") is False:
            temp = [x.strip() for x in line.split("=")]
            if "=" not in line and len(temp) != 2:
                raise SyntaxError("bad syntax")
            config.update({temp[0]: temp[1]})

    for c in list(config.keys()):
        config[c.lower()] = config.pop(c)

    for req in requirements:
        if req not in config.keys():
            raise FileError(f"{req} not found")
    change_value(config)
except (FileError, FileNotFoundError) as e:
    print(f"{e}")
finally:
    if fd:
        fd.close()
