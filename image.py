# run this in any directory
# add -v for verbose
# get Pillow (fork of PIL) from
# pip before running -->
# pip install Pillow

# import required libraries
import os
import sys
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
root=Tk()
root.title('sanil compression')
root.iconbitmap()
root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
# define a function for
# compressing an image
qualit=int(input("Enter the quality in percentage= "))
h=os.path.basename(root.filename)
def compressMe(file, verbose = False):
	
	# Get the path of the file
	filepath = root.filename
	
	# open the image
	picture = Image.open(filepath)
	
	# Save the picture with desired quality
	# To change the quality of image,
	# set the quality variable at
	# your desired level, The more
	# the value of quality variable
	# and lesser the compression
	picture.save("Compressed_"+h,
				"JPEG",
				optimize = True,
				quality = qualit)
	return

# Define a main function
def main():
	
	verbose = False
	
	# checks for verbose flag
	if (len(sys.argv)>1):
		
		if (sys.argv[1].lower()=="-v"):
			verbose = True
					
	# finds current working dir
	# cwd = os.getcwd()

	# formats = ('.jpg', '.jpeg')
	
	# # looping through all the files
	# # in a current directory
   
	# for file in os.listdir(cwd):
		
	# 	# If the file format is JPG or JPEG
	# 	if os.path.splitext(file)[1].lower() in formats:
	print('compressing', h)
	compressMe(h, verbose)

	print("Done")


# Driver code
if __name__ == "__main__":
	main()
