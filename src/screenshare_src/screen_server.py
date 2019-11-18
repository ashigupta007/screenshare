import mss
import os
def captureScreen():
	while 1:
		with mss.mss() as sct:
			loc = os.path.join(settings.STATIC_ROOT ,'ijkl.png')
			filename = sct.shot(output=loc)
	return 'Anything'