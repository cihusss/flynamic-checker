#!/usr/local/bin/python3

""" Flynamic image checker """
__author__ = "picka"

import argparse
import os
import re
from PIL import Image

def main():

	print("\nRunning spec validation...\n")

	# set up arguments
	parser = argparse.ArgumentParser(description="Flynamic Image Checker")
	parser.add_argument("-c", "--converge", help="Converge ID", required=False)
	parser.add_argument("-p", "--publisher", help="Publisher Name", required=False)
	parser.add_argument("-d", "--destination", help="Destination Directory", required=True)
	args = parser.parse_args()

	# define spec
	# spec =	{
	#   "logowidth": 300,
	#   "logosize": 30,
	#   "lifewidth": 960,
	#   "lifeheight": 960,
	#   "lifesize": 100
	# }

	spec = {
		"2x1": {
			"width": 480,
			"height": 480,
			"filesize": 100
		},
		"4x1": {
			"width": 960,
			"height": 480,
			"filesize": 100
		},
		"10x1": {
			"width": 960,
			"height": 240,
			"filesize": 100
		}
	}

	# read dirs in campaign
	dirs = os.listdir(args.destination)
	sets = []

	# structure
	def structure():

		# filter out sets
		for dir in dirs:
			
			if dir.startswith("set"):
				sets.append(dir)

		# filter out images
		for set in sets:
			
			number = -1
			paths = []
			ratios = os.listdir(f"{args.destination}{set}/ratios/")

			for ratio in ratios:
				paths.append(f"{args.destination}{set}/ratios/{ratio}/img/")
			
			for path in paths:
				number += 1
				ratio = ratios[number]
				images = (os.listdir(path))
				for image in images:
					try:
						image != ".DS_Store"
						validate(set, ratio, image, path)
					except Exception as e:
						print(f"{e}, skipping...\n")

	# validation
	def validate(set, ratio, image, path):

		print(f"Image: {image}")
		print(f"Ratio: {ratio}")
		print(f"Set: {set}")
		print(f"Path: {path}")

		filesize = round(os.stat(path + image).st_size / 1000)
		filedimensions = Image.open(path + image)

		# check bytes
		if filesize > spec.get(ratio).get("filesize"):
			print(f"Filesize FAIL: {filesize}kb")
		else:
			print(f"Filesize OK: {filesize}kb")
		#check widths
		if filedimensions.width != spec.get(ratio).get("width"):
			print(f"Width FAIL: {filedimensions.width}px")
		else:
			print(f"Width OK: {filedimensions.width}px")
		#check heights
		if filedimensions.height != spec.get(ratio).get("height"):
			print(f"Height FAIL: {filedimensions.height}px")
		else:
			print(f"Height OK: {filedimensions.height}px")
		print("")

	structure()

	print("Done!\n")

main()