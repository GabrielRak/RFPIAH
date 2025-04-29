import os 

def check_if_path_exists(path):
    """
        Checks if the path exists.
    """
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    