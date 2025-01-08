import os
import sys
from resolve_config import resolve_config
from configtree import process

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: easyLLVM <config_file>")
        sys.exit(1)
    # two cases:
    # 1. easyLLVM <config_file / input_file_with_config>
    # 2. easyLLVM -<options> <input_file>
    root = resolve_config(args)
    process(root)

if __name__ == "__main__":
    main()
