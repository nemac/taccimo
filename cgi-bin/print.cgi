#!/usr/bin/env python

# sudo yum install python-simplejson

import cgi, simplejson, sys, urllib
import Image
import os.path
import time

# Open a file
fo = open("foo.txt", "wb")
fo.write( "logging this junk!!\n");

params = cgi.FieldStorage()
try:
	settings = {}
	settings['width']   = int( params.getvalue("width") )
	settings['height']  = int( params.getvalue("height") )
	settings['tiles']   = simplejson.loads( params.getvalue("tiles") )
	settings['image']   = bool(int( params.getvalue("image",0) ))
	imgXList = [] 
	imgYList = []
	#1. read in the x and y coordinates
	for tile in settings['tiles']:
		# fo.write(str(tile)+"\n")
		for key, val in tile.iteritems():
			if (str(key)=='x'):
				imgXList.append(val)
			if (str(key)=='y'):
				imgYList.append(val)		
	fo.write("min x:"+str(min(imgXList))+"\n")
	fo.write("min y:"+str(min(imgYList))+"\n")
	#2. create new canvas and past onto it
	printCount = 0
	imgX = 0 
	imgY = 0
	new_im = Image.new('RGB', (settings['width']+256,settings['height']+256))
	fo.write("width:"+str(settings['width']+256)+"height:"+str(settings['height']+256)+"\n")
	# new_im = Image.new('RGB', (max(imgXList)-min(imgXList),max(imgYList)-min(imgYList)))
	# fo.write("width:"+str(max(imgXList)-min(imgXList))+"height:"+str(max(imgYList)-min(imgYList))+"\n")
	for tile in settings['tiles']:
		fo.write(str(tile)+"\n")
		for key, val in tile.iteritems():
			if (str(key)=='url'):
				urllib.urlretrieve(str(val), 'print_temp/'+str(printCount)+'.jpg')
			if (str(key)=='x'):
				imgX = str(val+abs(min(imgXList)))
				fo.write("new x:"+str(imgX)+"\n")
			if (str(key)=='y'):
				imgY = str(val+abs(min(imgYList)))
				fo.write("new y:"+str(imgY)+"\n")
		im = Image.open('print_temp/'+str(printCount)+'.jpg')
		# fo.write("bbox:"+str(im.getbbox())+"\n")
		if im.mode == 'RGBA':
			new_im.paste(im, (int(imgX),int(imgY)), im)
		else:
			new_im.paste(im, (int(imgX),int(imgY)))	
		printCount = printCount+1
	new_im.save("printed_map.jpg")	
except:
	fo.write("error occured\n")
	sys.exit(1)
# Close open file
fo.close()