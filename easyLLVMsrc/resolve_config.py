import yaml

default_config_file = "~/.ez"

# node = {
#     "config_file": "a.yaml",
#     "config_content": {}, // need to be parsed and computed during building the tree
#     "workflows": [], # List of workflow stages to execute in order
#     "objects": [], # List of objects to be processed, a workflow will execute on such objects
# }
#

def parse_args(args, root):
    for i in range(len(args)):
        if args[i] == "-c":
            break
        if args[i] == "-o":
            i += 1
            break
        # else: a .yaml file
        if args[i].endswith(".ez"):
            break
        # else: a .c file
        if args[i].endswith(".c"):
            break

def presolve_yaml(node):
    with open(node["config_file"], 'r') as f:
        node["config_content"] = yaml.safe_load(f)

    # resolve the config content, workflows and objects
    node["workflows"] = node["config_content"]["workflows"]

def yaml_override(node_parent, node_child):
    pass

def resolve_yaml(node):
    pass

def resolve_config(args):
    # 0. parse args
    # 1. resolve config file
    # 2. parse config file
    root = {
        "config_file": default_config_file,
        "config_content": {},
        "workflows": [],
        "objects": [],
    }

    presolve_yaml(root)

    parse_args(args, root)

    resolve_yaml(root)

    return root

