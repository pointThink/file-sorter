from fileinput import filename
from genericpath import isfile
import file_types as ft
from sys import argv
from os import listdir, mkdir, rename
from os.path import isfile, isdir


# file class
class File():

	file_name: str
	file_path: str
	file_type: ft.FileType


# get directory from command line
directory = argv[1]

dir_contents = listdir(directory)

# filter out directories from dir_contents
files_temp = []

for item in dir_contents:
	if isfile(directory + "/" + item):
		files_temp.append(item)

# convert files to File objects
files = []

for file in files_temp:
	file_obj = File()
	file_obj.file_name = file
	file_obj.file_path = directory + "/" + file
	file_obj.file_type = ft.check_file_type(file) # assign the file type to the file object

	files.append(file_obj)

# sort the files
for file in files:
	# create folder if doesnt exists
	if not isdir(directory + "/" + file.file_type.folder_name):
		mkdir(directory + "/" + file.file_type.folder_name)

	# move file to folder
	rename(file.file_path, directory + "/" + file.file_type.folder_name + "/" + file.file_name)