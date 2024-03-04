import os
import cv2
import imghdr

def rename_files_in_subfolders(folder_path):
    """
    Renames images into consecutive numbered files, e.g. {category}1.jpg, {category}2.jpg...
    
    Parameters:
        folder_path: path to parent directory containing image folders
    Returns:
        None
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

def remove_problematic_images(folder_path,image_exts):
    """
    Iterates over all subfolders and check whether file opens and extension is accepted
    
    Parameters:
        folder_path: Path to the parent directory containing image folders.
        image_exts: List of valid image extensions.
    Returns:
        None
    """

    for root, dirs, files in os.walk(folder_path):
        for image in files:
            image_path = os.path.join(root, image)
            try:
                img = cv2.imread(image_path)
                ext = imghdr.what(image_path)
                if ext not in image_exts:
                    print('File type not accepted {}'.format(image_path))
                    os.remove(image_path)
            except Exception as e:
                print('File won\'t open {}'.format(image_path))
                os.remove(image_path)

def main():
    folder_path = "raw_images/"
    image_exts = ['jpeg','jpg', 'bmp', 'png', None]
    remove_problematic_images(folder_path, image_exts)
    rename_files_in_subfolders(folder_path)

if __name__ == "__main__":
    main()

