import yaml
import os
import sys

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: easyLLVM <config_file>")
        sys.exit(1)
    
    # two cases:
    # 1. easyLLVM <config_file / input_file_with_config>
    # 2. easyLLVM -<options> <input_file>

    # if the first argument is a yaml file, then we use it as the config file
    if args[0].endswith(".yaml"):
        with open(args[0], 'r') as file:
            data = yaml.safe_load(file)
        print(data)
    else:
        # if the first argument is not a yaml file, then we use it as the input file
        print(args[0])

if __name__ == "__main__":
    main()
