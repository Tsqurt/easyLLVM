
# config_tree.py
# config_tree:
# root(default)
#   |
#   |-- config_file_1(workflow 1) /
#        |
#        ...
#        | config_file_1_1(workflow 1.1) /
#        | config_file_1_2(workflow 1.2) /
#        | ...
    # two cases:
    # 1. easyLLVM <config_file / input_file_with_config>
    # 2. easyLLVM -<options> <input_file>
    # root = resolve_config(args)
    # process(root)
    # pprint.pprint(root["objects"], indent=4, width=80)
    # pprint.pprint(root["children"], indent=4, width=80)

# demo :
# node = {
#     "config_file": "a.yaml",
#     "config_content": {}, // need to be parsed and computed during building the tree
#     "workflow": [], # List of workflow stages to execute in order
    # Example workflow:
    # [
    #   "frontend",    # Stage 1: Parse source code into AST and generate LLVM IR
    #   "override",    # Stage 2: Apply any configuration overrides to frontend output
    #   "optimize",    # Stage 3: Run LLVM optimization passes on IR
    #   "llvm_link",   # Stage 4: Link multiple LLVM IR modules together
    #   "optimize",    # Stage 5: Run additional optimization passes on linked IR
    #   "lower",       # Stage 6: Lower IR to target-specific machine code
    #   "target_link", # Stage 7: Link object files and libraries into final binary
    #   "done",        # Stage 8: Mark compilation workflow as complete, this stage will send the output to the parent workflow
    # ]
#     "children": [], # List of children to be processed, a workflow will execute on such children
#     "objects": [], # List of objects to be processed, a workflow will execute on such objects
#     
# }
#
import pprint
import tempfile
import os
import atexit
import subprocess
def create_temp_file():
    # 在系统临时目录创建文件，但不会自动删除
    temp_fd, temp_path = tempfile.mkstemp(text=True)
    
    # 关闭文件描述符
    os.close(temp_fd)
    
    # 注册程序退出时的清理函数
    def cleanup():
        try:
            os.remove(temp_path)
        except FileNotFoundError:
            pass  # 文件可能已被系统清理，忽略错误
    
    atexit.register(cleanup)
    
    return temp_path


def frontend(list_of_objects, config_content) -> list:
    print("TODO: frontend!")
    print(list_of_objects)
    processed_c_files = frontend_c(list_of_objects, config_content)
    return processed_c_files

def frontend_c(list_of_objects, config_content) -> list:
    print("TODO: frontend_c!")
    print(list_of_objects)

    # return: a path to the processed c file
    def process_c_file(obj):
        print(f"Processing C file: {obj}")
        temp_file = create_temp_file()
        temp_file = temp_file + ".bc"
        subprocess.run(["clang", "-c", "-emit-llvm", obj, "-o", temp_file])
        return temp_file
    return [process_c_file(obj) for obj in list_of_objects]

def override(list_of_objects, config_content) -> list:
    print("TODO: override!")
    print(list_of_objects)
    return list_of_objects   

def optimize(list_of_objects, config_content) -> list:
    print("TODO: optimize!")
    print(list_of_objects)
    return list_of_objects

def llvm_link(list_of_objects, config_content) -> list:
    print("TODO: llvm_link!")
    print(list_of_objects)
    return list_of_objects

def lower(list_of_objects, config_content) -> list:
    print("TODO: lower!")
    print(list_of_objects)
    return list_of_objects

def target_link(list_of_objects, config_content) -> list:
    print("TODO: target_link!")
    print(list_of_objects)
    return list_of_objects

def done(list_of_objects) -> list:
    print("TODO: done!")
    print(list_of_objects)
    return list_of_objects

def process(root):
    # for each workflow stage, execute it
    for stage in root["workflow"]["process_sequence"]:
        # Get the corresponding function for this workflow stage
        if stage != "done":
            stage_func = globals()[stage]
            # Execute the stage function on objects with config
            root["objects"] = stage_func(root["objects"], root["config_content"])
        else:
            print("TODO: DONE!")
    pass
