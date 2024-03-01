import os
from PIL import Image


def rename_files_in_subfolders(folder_path):
    """
    Parameters:
      folder_path: path to parent directory containing image folders
    """

    # Iterate over all subfolders and rename files
    for root, dirs, files in os.walk(folder_path):
        for i, file in enumerate(files):
            _, file_extension = os.path.splitext(file)
            new_name = f"{os.path.basename(root)}{i}{file_extension}"
            current_file_path = os.path.join(root, file)
            new_file_path = os.path.join(root, new_name)
            os.rename(current_file_path, new_file_path)


def convert_png_to_jpg(folder_path):
    """
    Parameters:
      folder_path: path to parent directory containing image folders
    """

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.png'):
                png_file_path = os.path.join(root, file)
                with Image.open(png_file_path) as img:
                    # Convert PNG to JPG format
                    jpg_file_path = os.path.splitext(png_file_path)[0] + ".jpg"
                    img = img.convert('RGB')
                    img.save(jpg_file_path)

                # Remove the original PNG file
                os.remove(png_file_path)


def main():
    folder_path = "raw_images/"
    rename_files_in_subfolders(folder_path)
    convert_png_to_jpg(folder_path)


if __name__ == "__main__":
    main()