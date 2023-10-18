import os

# Specify the directory path you want to list files from
directory_path = r"C:\Users\kinla\Documents\All_github_repo\datasets\gutenberg\train"

# List all files in the specified directory
files = os.listdir(directory_path)

# Print the list of files
print("List of files in the directory:")
for file in files:
    print(file)
