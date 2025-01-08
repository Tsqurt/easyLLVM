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
#        | config_file_1_n(workflow 1.n) /
#   |-- config_file_2(workflow 2) /
#   |-- config_file_3(workflow 3) /
#   |-- ...
#   |-- config_file_n(workflow n) /

# demo :
# node = {
#     "config_file": "a.yaml",
#     "config_content": {}, // need to be parsed and computed during building the tree
#     "workflows": [], # List of workflow stages to execute in order
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
#     "objects": [], # List of objects to be processed, a workflow will execute on such objects
# }
#


def process(root):
    pass
