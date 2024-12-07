import os

def list_files(path):
    files = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)) and not f.startswith('.'):
            files.append(f)
    return files

def list_dirs(path):
    dirs = []
    for d in os.listdir(path):
        if os.path.isdir(os.path.join(path, d))  and not d.startswith('.'):
            dirs.append(d)
    return dirs

def preview(path, rev: bool):
    files = list_files(path)
    files.sort(reverse=rev)
    i = 1
    print(f"\nInside {path}: ")
    for filename in files:
        file_extension = os.path.splitext(filename)[1]
        print(f"{filename} -> {i}{file_extension}")
        i = i + 1

    # dirs
    dirs = list_dirs(path)
    for directory in dirs:
        preview(os.path.join(path, directory), rev)


def rename_files(path, rev: bool):
    files = list_files(path)
    files.sort(reverse=rev)
    i = 1

    renamed_files = set() 

    for filename in files:
        old_name = os.path.join(path, filename)
        file_extension = os.path.splitext(filename)[1]
        new_filename = f"{i}{file_extension}"
        new_name = os.path.join(path, new_filename)

        # check if the new filename already exists in the dir or has been renamed
        if os.path.exists(new_name) or new_filename in renamed_files:
            print(f"Skipping '{filename}' as it would result in a name conflict with an existing file.")
            continue

        try:
            os.rename(old_name, new_name)
            renamed_files.add(new_filename)
            # for process logging
            print(f" '{filename}' renamed to '{new_filename}'")
        except PermissionError:
            print(f"Error, unable to rename '{filename}' inside the folder '{path}' because of permission issues")
        except Exception as e:
            print(f"Error, unable to rename '{filename}' in the folder '{path}' because of: {e}")

        i = i + 1
        
    # for sub dir
    dirs = list_dirs(path)
    for directory in dirs:
        rename_files(os.path.join(path, directory), rev)


if __name__ == "__main__":
    try:
        path = input("Enter the path to the folder to be renamed: ").strip()
        if not os.path.exists(path):
            # if path is valid
            print(f"Error: The folder '{path}' does not exist.")
        else:
            # to reverse or not
            while True:
                reverse = input("In reverse order? (yes or no): ").strip().lower()
                if reverse in ['yes', 'no']:
                    rev = reverse == 'yes'
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            # preview changes
            preview(path, rev)

            # confirm renaming
            while True:
                confirm = input("\nProceed with renaming? (yes or no): ").strip().lower()
                if confirm == "yes":
                    print("Renaming files...")
                    rename_files(path, rev)
                    print("Renaming completed successfully.")
                    break
                elif confirm == "no":
                    print("Renaming cancelled.")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

    except Exception as e:
        print(f"An error occurred: {e}")