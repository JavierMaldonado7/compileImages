import os
import shutil

# define the path to the file containing the names of the files you want to search for
filename_list_path = "names.txt"

# define the path to the directory you want to copy the files to
path_to_copy = os.path.expanduser("~/Desktop/Compiled")

# create the directory if it doesn't already exist
if not os.path.exists(path_to_copy):
    os.makedirs(path_to_copy)

# define a function to read in filenames from a text file and add them to the list of filenames to search for
def add_filenames_from_file(filepath, filenames_to_search):
    with open(filepath, "r") as f:
        filenames = f.read().splitlines()
        filenames_to_search.extend(filenames)

# create an empty list to store the filenames to search for
filenames_to_search = []

# add the filenames from the text file to the list
add_filenames_from_file(filename_list_path, filenames_to_search)

# iterate through all the files in the file system
for root, dirs, files in os.walk("/"):
    for file in files:
        # check if the file name is in the list of names you're looking for
        if file in filenames_to_search:
            # construct the full path to the file
            full_path = os.path.join(root, file)
            # construct the full path to the destination directory
            destination_path = os.path.join(path_to_copy, file)
            # copy the file to the destination directory
            shutil.copy(full_path, destination_path)
