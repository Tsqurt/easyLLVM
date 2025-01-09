import yaml
import pprint
default_config_file = "/home/nanami/.ez"

# node = {
#     "config_file": "a.yaml",
#     "config_content": {}, // need to be parsed and computed during building the tree
#     "workflow": [], # List of workflow stages to execute in order
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
            if isinstance(root["config_content"]["workflow"]["unit_add"], list):
                    root["config_content"]["workflow"]["unit_add"].append(args[i])
            elif root["config_content"]["workflow"]["unit_add"] == "all":
                    TODO 
            elif root["config_content"]["workflow"]["unit_add"] == "nil":
                    root["config_content"]["workflow"]["unit_add"] = [args[i]]
            else:
                root["config_content"]["workflow"]["unit_add"] = [args[i]]
            break

def presolve_yaml(node):
    with open(node["config_file"], 'r') as f:
        node["config_content"] = yaml.safe_load(f)

    # resolve the config content, workflow and objects
    node["workflow"] = node["config_content"]["workflow"]

def yaml_override(node_parent_content, node_child_content):
    # child will inherit parent's all config_content
    # Inherit all config content from parent except workflow
    list_plain_inherit = ['host', 'frontend_c', 'llvm_link', 'lower', 'optimize', 'override', 'target_link']
    for attr in list_plain_inherit:
        src = node_parent_content[attr]
        dst = node_child_content[attr]
        for key, value in src.items():
            if key not in dst:
                dst[key] = value

    # Inherit workflow from parent
    # TODO
    print("TODO: Inherit workflow from parent")

def resolve_yaml(node):
    # find resources and children
    print("TODO: find children")
    # TODO: 
    print("TODO: match")
    for unit_add in node["config_content"]["workflow"]["unit_add"]:
        node["objects"].append(unit_add)
    
    if "process_sequence" not in node["config_content"]["workflow"]:
        node["workflow"]["process_sequence"] = node["config_content"]["workflow"]["process_sequence_default"]
        
def resolve_config(args):
    # 0. parse args
    # 1. resolve config file
    # 2. parse config file
    root = {
        "config_file": default_config_file,
        "config_content": {},
        "workflow": [],
        "objects": [],
        "children": [],
    }

    presolve_yaml(root)

    pprint.pprint(root["config_content"], indent=4, width=80)

    parse_args(args, root)

    resolve_yaml(root)
    
    pprint.pprint(root["config_content"], indent=4, width=80)

    return root
