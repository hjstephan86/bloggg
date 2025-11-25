import os
import sys

def print_html_contents(root_dir):
    """
    Recursively searches for and prints the content of all .html files
    starting from the given root directory.

    Args:
        root_dir (str): The path to the starting directory.
    """
    print(f"--- Starting recursive search in: {root_dir} ---")
    
    # Check if the directory exists
    if not os.path.isdir(root_dir):
        print(f"Error: Directory not found at path: {root_dir}", file=sys.stderr)
        return

    # os.walk generates the file names in a directory tree 
    # by walking the tree top-down or bottom-up.
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # dirpath is a string, the path to the directory.
        # dirnames is a list of the names of the subdirectories in dirpath.
        # filenames is a list of the names of the non-directory files in dirpath.
        
        for filename in filenames:
            # Check if the file is an HTML file (case-insensitive)
            if filename.lower().endswith('.html') or filename.lower().endswith('.htm'):
                # Construct the full file path
                filepath = os.path.join(dirpath, filename)
                
                # print("\n" + "="*80)
                print(f"File: {filepath}")
                # print("="*80)
                
                try:
                    # Open the file and read its content.
                    # 'r' mode is for reading. We use 'utf-8' encoding 
                    # as it is standard for HTML files.
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # print(content)
                        
                except FileNotFoundError:
                    # This should generally not happen with os.walk, 
                    # but good for robust scripts.
                    print(f"Error: File not found (concurrent deletion?): {filepath}", file=sys.stderr)
                except UnicodeDecodeError as e:
                    # Handle files that might not be correctly encoded in utf-8
                    print(f"Error reading file {filepath}: Encoding issue ({e}). Skipping.", file=sys.stderr)
                except Exception as e:
                    # Catch any other unexpected errors
                    print(f"An unexpected error occurred while processing {filepath}: {e}", file=sys.stderr)

    print("\n--- Search and printing complete. ---")


if __name__ == "__main__":
    # The script can be run in two ways:
    # 1. Provide the path as a command-line argument: 
    #    python html_reader.py /path/to/your/folder
    # 2. If no argument is provided, use the current working directory.

    if len(sys.argv) > 1:
        # Use the first command-line argument as the root directory
        target_directory = sys.argv[1]
    else:
        # Use the current directory if no argument is provided
        target_directory = os.getcwd()
        print(f"No directory provided. Using current directory: {target_directory}")

    print_html_contents(target_directory)

