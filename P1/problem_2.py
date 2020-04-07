## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("./testdir"))

# # Let us check if this file is indeed a file!
# print (os.path.isfile("./ex.py"))

# # Does the file end with .py?
# print ("./ex.py".endswith(".py"))

print (os.path.join('./testdir', ''))

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    def rec_find_files(suffix, path, file_paths):
      if os.path.isfile(path) and path.endswith(suffix):
        file_paths.append(path)
        return file_paths
      elif os.path.isdir(path):
        for cur_val in os.listdir(path):
          sub_path = os.path.join(path, cur_val)
          if  os.path.isfile(sub_path) and sub_path.endswith(suffix):
            file_paths.append(sub_path)
          elif os.path.isdir(sub_path):
            rec_find_files(suffix, sub_path, file_paths)
        return file_paths

    return rec_find_files(suffix, path, [])


print(find_files(".c", "./testdir"))