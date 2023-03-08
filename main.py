try: from PIL.Image import open
except: from Image import open
from sys import stdout
from datetime import timedelta
from cv2 import VideoCapture, imencode, resize
from io import BytesIO
description = ""
def I2T(File):
	im = open(File)
	(w, h) = im.size
	mim = im.convert("1")
	data = list(mim.getdata())
	counter = 0
	field = True
	for pixel in data:
		if field:
			if pixel > 127: description = description + "0"
			else: description = description + "0"
		counter = counter + 1
		if counter >= w:
			counter = 0
			if field: description = description + "\\n"
			field = not field
vidcap = VideoCapture('./video.mp4')
success, image = vidcap.read()
index = 0
while success:
	index += 1
	print('blob\nmark :1\ndata 1\na\nreset refs/heads/master\ncommit refs/heads/master\nmark :2\nauthor jacorb91 <darkmanalways6@gmail.com> 0 +0000\ncommitter jacorb91 <darkmanalways6@gmail.com> 0 +0000\ndata 1\n\nM 100644 :1 a\n')
	I2T(BytesIO(imencode(".jpg", resize(image, (24, 32), interpolation = 3))[1]))
	print('git commit -m "Title" -m "Description ' + description + '";')
	print()
	vidcap.read()
	vidcap.read()
	success, image = vidcap.read()
