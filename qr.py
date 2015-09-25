 # -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys, math
import os, io
from PIL import Image,ImageFont, ImageDraw

# from qrcode import *

# qr = QRCode(version=20, error_correction=ERROR_CORRECT_L)
# qr.make("Hello world") # Generate the QRCode itself

# # im contains a PIL.Image.Image object
# im = qr.make_image()

# # To save it
# im.save("filename.png")


import pyqrcode
import json
# url = pyqrcode.create('{name:"Shafeeq", id:"EPNSS010"}')
# url.png('code.png', scale=6)

# qr = Image.open('code.png')
# a = qr.size[0]
# qr_re = qr.resize((100,100))
# sample = Image.open('sample.jpg')

# draw = ImageDraw.Draw(sample)
# font = ImageFont.truetype("OpenSans-Regular.ttf", 33)
# draw.text((10, 25), "To be or not to be QWerty asdf jklm that is the question",(0,0,0), font=font)
# sample.paste(qr, (100,100))
# sample.paste(qr_re, (600,600))
# sample.save('fixed.png')


usersfile = open("u2.csv","r")
ustr = usersfile.readlines()
users = []
for i in ustr:
	id,fname, lname = i.split(',')
	fname = fname.upper()
	lname = lname.upper()
	lname = lname.strip()
	lname = lname[:20]
	name = fname + " " + lname
	name = name[:20]
	users.append((id,name))


qr_positions = [(435,570),(1208,570),(1976,570),(2744,570),(3510,570),(4277,570),
				(435,1651),(1208,1651),(1976,1651),(2744,1651),(3510,1651),(4277,1651),
				(435,2742),(1208,2742),(1976,2742),(2744,2742),(3510,2742),(4277,2742)
				]

id_positions = [(460,880),(1233,880),(2011,880),(2769,880),(3535,880),(4302,880),
				(460,1960),(1233,1960),(2011,1960),(2769,1960),(3535,1960),(4302,1960),
				(460,3050),(1233,3050),(2011,3050),(2769,3050),(3535,3050),(4302,3050)
				]

name_positions = [(435,958),(1208,958),(1976,958),(2744,958),(3510,958),(4277,958),
				(435,2045),(1208,2045),(1976,2045),(2744,2045),(3510,2045),(4277,2045),
				(435,3136),(1208,3136),(1976,3136),(2744,3136),(3510,3136),(4277,3136)
				]

print len(users)
print "last", users[-1]
for j in range(int(math.ceil(len(users)/18))+2):
	template = Image.open("idcmyk.jpg")
	buffer = []
	draw = ImageDraw.Draw(template)
	font = ImageFont.truetype("OpenSans-Regular.ttf", 33)
	
	for idx,i in enumerate(users[j*18:(j+1)*18]):
		qr = pyqrcode.create(i[0])
		buffer.append(io.BytesIO())
		qr.png(buffer[idx], scale=6)
		buffer[idx].seek(0)

		qrimg = Image.open(buffer[idx])
		qr_re = qrimg.resize((300,300)).convert('CMYK')

		draw.text(id_positions[idx], "%s"%i[0],fill=(0,0,0,0), font=font)
		draw.text(name_positions[idx], "%s"%i[1],(0,0,0), font=font)

		template.paste(qr_re,qr_positions[idx])

	base = template.convert('CMYK')
	base.save('cmyk/%d.jpg'%j)

