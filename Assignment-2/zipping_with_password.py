import os
import zipfile
import pyminizip
from tqdm import tqdm

def zip_directory_with_password(path, output_zip_path, password):
    try:
        if not os.path.isdir(path):
            raise ValueError(f"The specified path '{path}' is not a valid directory.")

        # create a temporary zip file
        temp_zip_path = output_zip_path + "_temp.zip"

        all_files = []
        # used os.walk() function for accessing all sub_dirs
        for root, dirs, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, path)
                all_files.append((full_path, arcname))

        with zipfile.ZipFile(temp_zip_path, 'w', zipfile.ZIP_DEFLATED) as z, tqdm(total=len(all_files), desc="Zipping files") as t:
            for full_path, arcname in all_files:
                #writing files to zip file
                z.write(full_path, arcname)
                # updating progress bar
                t.update(1)

        # password protecting the zip file
        print("Adding password protection...")
        pyminizip.compress(temp_zip_path, None, output_zip_path, password, 5)

        # remove the temporary zip file
        os.remove(temp_zip_path)
    except ValueError as e:
        print(f"ValueError occurred: {e}")
    except PermissionError as pe:
        print(f"PermissionError occurred: {pe}")

if __name__ == "__main__":
    try:
        path = input("Enter the path of the folder: ").strip()
        if not os.path.exists(path):
            print(f"Error: The folder '{path}' does not exist.")
        else:
            # Determine output zip file name
            output_zip_path = input("Enter a custom name for the zip file (leave blank to use default): ").strip()
            if not output_zip_path:
                folder_name = os.path.basename(path.rstrip('/\\'))
                output_zip_path = os.path.join(os.path.dirname(path), f"{folder_name}.zip")
            else:
                if not output_zip_path.lower().endswith('.zip'):
                    output_zip_path += '.zip'
                output_zip_path = os.path.join(os.path.dirname(path), output_zip_path)

            zip_password = input("Enter a password for the zip file (leave blank to not set password): ").strip()

            zip_directory_with_password(path, output_zip_path, zip_password)
            print(f"Successfully created zip file: {output_zip_path}")

    except Exception as e:
        print(f"An error occurred: {e}")