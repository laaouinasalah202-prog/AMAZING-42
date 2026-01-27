class FileError(Exception):
    pass

class SyntaxError(FileError):
    pass

def change_value(config_dic: dict):
    try:
        config_dic["WIDTH"] = int(config_dic["WIDTH"])
        config_dic["HEIGHT"] = int(config_dic["HEIGHT"])
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    try:  
        exit_p = [int(i) for i in config_dic["EXIT"].split(',')]
        entry = [int(i) for i in config_dic["ENTRY"].split(',')]
        if len(entry) != 2:
            raise ValueError(f"Invalid Entry Value: {entry}")
        elif len(exit_p) != 2:
            raise ValueError(f"Invalid Exit Value: {exit_p}")
        config_dic["ENTRY"] = tuple(entry)
        config_dic["EXIT"] = tuple(exit_p)
    except ValueError as e:
        print(f"{e}")
        exit(1)
    try:
        if config_dic["PERFECT"].lower() == "true":
            config_dic["PERFECT"] = True
        elif config_dic["PERFECT"].lower() == "false":
            config_dic["PERFECT"] = False
        else:
            raise ValueError("impossible maze arguments")
    except ValueError as e:
        print(f"{e}")

def parssing(file_path) -> dict:
    config = {}
    requirements = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]
    try:
        fd = open(file_path)
        with open(file_path) as fd: 
            for line in fd:
                if "output_file" not in line.lower():
                    line = line.upper()
                if line == '\n':
                    continue
                if line.startswith("#") is False:
                    temp = [x.strip() for x in line.split("=")]
                    if "=" not in line or len(temp) != 2: 
                        raise SyntaxError(f"Error: Invalid config format - '{temp[0]}'")
                    config.update({temp[0]: temp[1]})
            
            for req in requirements:
                if req not in config.keys():
                    raise FileError(f"Error: Invalid config format - '{req}'")
            change_value(config)
            return config
    except (FileError, FileNotFoundError) as e:
        print(f"{e}")
        exit(1)
