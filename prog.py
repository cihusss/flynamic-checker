#!/usr/bin/python

""" Flynamic image checker """
__author__ = 'picka'

import argparse
import os
from PIL import Image

def main():

	# set up arguments
	parser = argparse.ArgumentParser(description='Flynamic Image Checker')
	parser.add_argument('-c', '--converge', help='Converge ID', required=False)
	parser.add_argument('-p', '--publisher', help='Publisher Name', required=False)
	args = parser.parse_args()

	# define spec
	spec =	{
	  "logowidth": 300,
	  "logosize": 30,
	  "lifewidth": 960,
	  "lifesize": 100
	}

	# get filenames & set up dir
	basedir = "img/"
	images = os.listdir(basedir)

	# loop through files, spec check & output
	for x in images:
		filesize = round(os.stat(basedir + x).st_size / 1000)
		filedimensions = Image.open(basedir + x)

		# check bytes
		if filesize > spec["lifesize"]:
			print("OUT OF SPEC! > " + x + " >", str(filesize) + "kb")
		else:
			print("no error > " + x + " >", str(filesize) + "kb")

		# check widths
		if filedimensions.width > spec["lifewidth"]:
			print("OUT OF SPEC! > " + x + " >", str(filedimensions.width) + "px")
		else:
			print("no error > " + x + " >", str(filedimensions.width) + "px")

main()

# print("Image stats:", images, file_size("img/thumb-ad.jpg"))
# print(f"File size in bytes of [{images}] ", file_size("img/thumb-ad.jpg"))

## argument values ##
# print ("Converge ID: %s" % args.converge )
# print ("Publisher: %s" % args.publisher )