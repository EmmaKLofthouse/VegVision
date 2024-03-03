import os
from PIL import Image


def rename_files_in_subfolders(folder_path):
    """
    Parameters:
      folder_path: path to parent directory containing image folders
    """

    # Iterate over all subfolders and rename files with dummy names to avoid conflicts
    for root, dirs, files in os.walk(folder_path):
        for i, file in enumerate(files):
            _, file_extension = os.path.splitext(file)
            dummy_name = f"{i}{file_extension}"
            current_file_path = os.path.join(root, file)
            dummy_file_path = os.path.join(root, dummy_name)
            os.rename(current_file_path, dummy_file_path)

    # Iterate over all subfolders and rename files
    for root, dirs, files in os.walk(folder_path):
        for i, file in enumerate(files):
            _, file_extension = os.path.splitext(file)
            new_name = f"{os.path.basename(root)}{i}{file_extension}"
            current_file_path = os.path.join(root, file)
            new_file_path = os.path.join(root, new_name)
            os.rename(current_file_path, new_file_path)

def main():
    folder_path = "raw_images/"
    rename_files_in_subfolders(folder_path)

if __name__ == "__main__":
    main()

