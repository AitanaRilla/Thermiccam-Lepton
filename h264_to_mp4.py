#!/usr/bin/env python3

import os


MP4_names = []
file_names = []
lsFiles = []
lsDir = os.walk(os.path.normpath("original_videos/"))
lsDir_MP4 = os.walk(os.path.normpath("temp/"))

#Search all .h264 files in the video directory
for root, dirs, files in lsDir:
	for file in files:
		(namefile, extension) = os.path.splitext(file)
		if extension == ".h264" :
			lsFiles.append(str(root+"/" +namefile))
			file_names.append(str(namefile))
			#print (root+"/" + namefile + extension)

#Search previously evaluated files in the temp directory
lsMP4 = []
for root, dirs, files in lsDir_MP4:
	for file in files:
		(namefile, extension) = os.path.splitext(file)
		if extension == ".mp4" :
			lsMP4.append(str(namefile))
			#print (root+"/" + namefile + extension)

# Transform .h264 videos that haven't been evaluated to .mp4
for file in lsFiles:
	already_evaluated = list(set(file_names).intersection(set(lsMP4)))
	#print("h264: ",lsFiles)
	#print("mp4: ", lsMP4)
	print("evaluated previously: ",already_evaluated)
	print(file.split("/")[-1])
	if file.split("/")[-1] not in already_evaluated:
		os.system('MP4Box -fps 10 -add "{0}.h264" "{0}.mp4"'.format(file))

#Search for newly created .mp4 files and copy them to temp
lsMP4 = []
lsDir = os.walk(os.path.normpath("original_videos/"))
for root, dirs, files in lsDir:
	for file in files:
		(namefile, extension) = os.path.splitext(file)
		if extension == ".mp4" :
			new_root = "/".join(root.split("/")[1:])
			print (new_root)
			if not os.path.exists("temp/"+new_root):
				os.makedirs("temp/"+new_root)
			lsMP4.append(str(new_root +"/"+ namefile+extension))
			#print (root+"/" + namefile + extension)

for file in lsMP4:
	os.rename("original_videos/"+file, "temp/"+file)