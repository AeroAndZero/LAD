import cv2
import numpy as np
import random
randomTries = 15
hRange = 50

def rgb_to_hsv(r, g, b): 
	r, g, b = r / 255.0, g / 255.0, b / 255.0
	cmax = max(r, g, b)
	cmin = min(r, g, b)
	diff = cmax-cmin
	if cmax == cmin: 
		h = 0
	elif cmax == r: 
		h = (60 * ((g - b) / diff) + 360) % 360
	elif cmax == g: 
		h = (60 * ((b - r) / diff) + 120) % 360
	elif cmax == b: 
		h = (60 * ((r - g) / diff) + 240) % 360
	if cmax == 0: 
		s = 0
	else: 
		s = (diff / cmax) * 100
	v = cmax * 100
	return [h, s, v]

def normalizeHSV(x,y,z):
	h = (x*255)/360
	s = (y*255)/100
	v = (z*255)/100

	return [h,s,v]

def main(image):
	#Intials
	frame = cv2.resize(image,(500,500))
	frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

	#Algorithm

	rh = random.randrange(0,frame.shape[0])
	rw = random.randrange(0,frame.shape[1])

	randomRGB = frame_rgb[rh,rw]
	randomHSV = rgb_to_hsv(randomRGB[0],randomRGB[1],randomRGB[2])
	normalHSV = normalizeHSV(randomHSV[0],randomHSV[1],randomHSV[2])
	
	lower_hsv = np.array([normalHSV[0]-hRange, normalHSV[1], normalHSV[2]])
	higher_hsv = np.array([normalHSV[0]+hRange, 255, 255])

	mask = cv2.inRange(frame_hsv,lower_hsv,higher_hsv)
	maskedOut = cv2.bitwise_and(frame,frame,mask = mask)

	print(rw,rh)

	for i in range(int(frame.shape[0]/randomTries),frame.shape[0],int(frame.shape[0]/randomTries)):
		rh = i
		rw = random.randrange(0,frame.shape[1])
		cv2.circle(maskedOut,(rw,rh),2,(255,0,255),3)

	return maskedOut

if __name__ == '__main__':
	image = cv2.imread('images/1.jpg')
	image = main(image)
	cv2.imshow('frame',image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()