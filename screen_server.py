import mss
import os
import requests
import numpy as np
from PIL import Image
import time
import socket    
hostname = socket.gethostname()    

def captureScreen():
	with mss.mss() as sct:
		while True:
			##############################################################################
			last_time = time.time()
			path_img= 'image_now.png'
			filename = sct.shot(output=path_img)
			# sct.compression_level = 6
			###################
			
			###################
			url = 'http://192.168.0.102:8000/server/'
			# with open(path_img, 'rb') as img:

			# 	name_img= os.path.basename(path_img)
			# 	files= {'image': (name_img,img,'multipart/form-data', {'Expires': '0'})}
			# 	with requests.Session() as s:
			# 		r = s.post(url,files=files)
			print('fps: {0}'.format(1 / (time.time()-last_time)))
			##############################################################################
	return 'Anything'



print("Streaming Now...")

captureScreen()