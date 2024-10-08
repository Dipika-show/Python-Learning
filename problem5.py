import os

def print_directory_contents(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    # Print directory contents
    print(f"Contents of directory '{directory}':")
    for item in os.listdir(directory):
        print(item)
        # Example usage:
directory_path = '/'  # Replace with your directory path
print_directory_contents(directory_path)