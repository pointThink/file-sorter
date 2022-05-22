from posixpath import splitext

# base class for file types
class FileType():

	folder_name: str
	extensions: list

	def __init__(self, folder_name: str, extensions: list):
		self.folder_name = folder_name
		self.extensions = extensions


# define all the file types
type_audio = FileType("Audio", [".midi", ".mp3", ".aac", ".ogg", ".flac", ".alac", ".wav", ".aiff", ".dsd", ".pcm"])
type_video = FileType("Videos", [".mp4", ".mov", ".wmv", ".avi", ".avchd", ".mkv", ".webm"])
type_image = FileType("Images", [".png", ".jpg", ".jpeg", ".gif", ".bmp"])
type_docs = FileType("Documents", [".doc", ".docx", ".txt", ".pdf", ".htm", ".html", ".ppt", ".pptx"])
type_archives = FileType("Archives", [".rar", ".7z", ".zip", ".tar", ".iso"])
type_scripts = FileType("Scripts", [".ps1", ".py", ".sh", ".bat", ".vbs"])
type_imageproj = FileType("Image Projects", [".xcf", ".psd", ".kra"])
type_unknown = FileType("Unknown", [])

# check if file belongs to any of the types above
def check_file_type(file_name: str):
	# get file extension
	extension = splitext(file_name)[-1] # -1 instad of 1 to get last index of list

	if extension in type_audio.extensions:
		return type_audio
	elif extension in type_video.extensions:
		return type_video
	elif extension in type_image.extensions:
		return type_image
	elif extension in type_docs.extensions:
		return type_docs
	elif extension in type_archives.extensions:
		return type_archives
	elif extension in type_scripts.extensions:
		return type_scripts
	elif extension in type_imageproj.extensions:
		return type_imageproj
	else:
		return type_unknown
