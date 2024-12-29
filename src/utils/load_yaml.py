import yaml
from pathlib import Path

# Define the root directory by resolving the path three levels up from the current file
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# Define the parameter directory path for the YAML file
PARAM_DIR = ROOT_DIR / 'params.yaml'

def yaml_loader()->dict:
    """
    Function to load and parse a YAML file.
    
    This function reads the contents of the YAML file located at PARAM_DIR
    and returns it as a dictionary.
    
    Returns:
        dict: Parsed content of the YAML file.
    """
    with open(PARAM_DIR, 'r') as yaml_file:
        yaml_content = yaml.safe_load(yaml_file)
    return yaml_content

if __name__ == "__main__":
    # Call the yaml_loader function to load YAML content
    yaml_loader()
