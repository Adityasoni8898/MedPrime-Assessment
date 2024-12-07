Assignment 1: Renaming All Files in a Folder Sequentially

Overview:
This Python script helps you rename all the files in a folder to a sequential order, like 1.ext, 2.ext, 3.ext, and so on. It keeps the original file extensions (like .jpg, .txt, .pdf) intact. 
It also handles hidden files by skipping them and provides error messages if a file cannot be renamed due to permission issues or file conflicts.

Libraries to install:
None

How It Works:
1. Folder Path: You'll be asked to provide the path to the folder you want to rename the files in.
2. Sorting Order: You can choose whether to sort the files in ascending order (default) or reverse order.
3. Preview: Before making the changes, script will preview you how the files will look after renaming.
4. Confirmation: If all correct, confirm the renaming, and the script will go ahead and rename the files.

# The script will also rename files in any subfolders within the provided folder using recursion.

Input:
1. Folder Path: Provide the path to the folder that contains the files you want to rename.
2. Sorting Option: Choose if the files should be in ascending order or reverse order.
3. Confirmation: You'll confirm whether to proceed with renaming the files.

Output:
1. Preview: A preview will show how the renamed files will look.
2. Renaming Result: The script will show whether the renaming was successful or if there were any errors.

Example Usage:
Enter the path to the folder: /path/to/your/folder
In reverse order? (yes or no): no
Preview of new names:
Inside the folder: /path/to/your/folder
  file1.jpg -> 1.jpg
  file2.txt -> 2.txt
  file3.pdf -> 3.pdf
Proceed with renaming? (yes or no): yes
Renaming Completed
 'file1.jpg' in folder '/path/to/your/folder' renamed to '1.jpg'
 'file2.txt' in folder '/path/to/your/folder' renamed to '2.txt'
 'file3.pdf' in folder '/path/to/your/folder' renamed to '3.pdf'
Completed