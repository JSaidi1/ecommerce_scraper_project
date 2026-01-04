import os


def search_file_in_parents(file_name: str, max_parents_level: int):
    """
    Return the file path if found, otherwise, it returns None.
    """
    # Get the directory where the script is executed
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Search in the current directory first
    if file_name in os.listdir(current_dir):
        return os.path.join(current_dir, file_name)
    # If not found, check the parent directories
    for i in range(max_parents_level):
        # Go up one level in the directory tree
        parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
        # Check if the file exists in the parent directory
        if file_name in os.listdir(parent_dir):
            return os.path.join(parent_dir, file_name)        
        # Update current_dir to the parent directory for the next iteration
        current_dir = parent_dir
    
    return None  # Return None if the file wasn't found
