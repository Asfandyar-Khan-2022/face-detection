# Python program to rename all file
# names in your directory
import os

def change_names(files_location, rename_to):
    '''
    Python program to rename all file 
    names in your directory

    :param files_location: locate the folder 
    containing the files 

    :param rename_to: choose the name you 
    wish to have before the number
    '''
    os.chdir(files_location)

    for count, f in enumerate(os.listdir()):
        f_name, f_ext = os.path.splitext(f)
        f_name = rename_to + str(count)
    
        new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)