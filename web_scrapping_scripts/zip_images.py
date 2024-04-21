import os
import zipfile

def zip_folder(folder_path, output_path):
    # Create a ZipFile object in write mode
    with zipfile.ZipFile(output_path, 'w') as zipf:
        # Walk through directory
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Create a complete path of file
                file_path = os.path.join(root, file)
                # Add file to zip
                zipf.write(file_path, os.path.relpath(file_path, os.path.dirname(folder_path)))

# Usage
zip_folder('./images', 'social_media_screenshots.zip')
