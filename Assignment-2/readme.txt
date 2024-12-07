Assignment 2: Zipping a Folder

Overview:
This Python script compresses a folder into a password-protected zip file using the pyminizip library for zipping and adding password protection, 
as the built-in zipfile module in Python does not support creating password-encrypted zip files.
Additionally, the tqdm library is used to provide a progress bar during the zipping process.

Library to Install:
pip install pyminizip tqdm

How It Works:
1. Folder Path: You provide the path of the folder you want to zip.
2. Output File Name: You can specify a custom name for the zip file, or it will default to the folder's name.
3. Password Protection: You have the option to password-protect the zip file. If chosen, the script will prompt you for a password.
4. Compression Level: The script uses a default compression level of 5, but you can adjust it if needed.

Input:
1. Folder Path: Provide the folder that you want to zip.
2. Custom Zip Name: Optionally, enter a custom name for the zip file.
3. Password: Optionally, set a password for the zip file.

Output:
1. The folder is compressed into a zip file.
2. If you set a password, the zip file is password-protected.

Example Usage:
Please enter the path to the folder to be zipped: /path/to/your/folder
Enter a custom name for the zip file (leave blank to use default): my_folder
Enter a password for the zip file (leave blank to not set password): mySecurePassword
Compressing folder '/path/to/your/folder' into '/path/to/your/my_folder.zip'...
Folder '/path/to/your/folder' successfully compressed into '/path/to/your/my_folder.zip'.