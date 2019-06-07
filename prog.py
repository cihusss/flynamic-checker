#!/usr/bin/python

""" Flynamic image checker """
__author__ = "picka"

import argparse
import os
from PIL import Image

def main():

	# set up arguments
	parser = argparse.ArgumentParser(description="Flynamic Image Checker")
	parser.add_argument("-c", "--converge", help="Converge ID", required=False)
	parser.add_argument("-p", "--publisher", help="Publisher Name", required=False)
	parser.add_argument("-d", "--destination", help="Destination Directory", required=True)
	args = parser.parse_args()

	# define spec
	spec =	{
	  "logowidth": 300,
	  "logosize": 30,
	  "lifewidth": 960,
	  "lifeheight": 960,
	  "lifesize": 100
	}

	# get filenames & set up dir
	basedir = args.destination + "/"
	images = os.listdir(basedir)

	print ("\nChecking specs in " + basedir + " ...\n")

	# loop through files, spec check & output
	for image in images:
		filesize = round(os.stat(basedir + image).st_size / 1000)
		filedimensions = Image.open(basedir + image)

		# check bytes
		if filesize > spec["lifesize"]:
			print("Wrong filesize > " + image + " >", str(filesize) + "kb")
		else:
			print("All good > " + image + " >", str(filesize) + "kb")

		# check widths
		if filedimensions.width != spec["lifewidth"]:
			print("Wrong width > " + image + " >", str(filedimensions.width) + "px")
		else:
			print("no error > " + image + " >", str(filedimensions.width) + "px")

		# check heights
		if filedimensions.height != spec["lifeheight"]:
			print("Wrong height > " + image + " >", str(filedimensions.width) + "px")
		else:
			print("no error > " + image + " >", str(filedimensions.height) + "px")

	print("")

main()

# print("Image stats:", images, file_size("img/thumb-ad.jpg"))
# print(f"File size in bytes of [{images}] ", file_size("img/thumb-ad.jpg"))

## argument values ##
# print ("Converge ID: %s" % args.converge )
# print ("Publisher: %s" % args.publisher )