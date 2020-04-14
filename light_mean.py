import cv2
import numpy as np
import math

img = cv2.imread("images/5.jpg")
img = cv2.resize(img,(500,500))
cv2.imshow("Original",img)
copyImg = np.copy(img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Parameters
whiteMin = 180
blackMax = 128
avgThreshold = 70
whiteAvg = [0,0]
whiteCount = 0
blackAvg = [0,0]
blackCount = 0

_,whiteMask = cv2.threshold(img,whiteMin,255,cv2.THRESH_TRUNC)
img = cv2.bitwise_not(img)
_,blackMask = cv2.threshold(img,blackMax,255,cv2.THRESH_TRUNC)

#White Pixel Avg
for y in range(len(whiteMask)):
	for x in range(len(whiteMask[y])):
		if whiteMask[y,x] >= avgThreshold:
			whiteCount += 1
			whiteAvg[0] += x
			whiteAvg[1] += y

whiteAvg[0] = int(whiteAvg[0] / whiteCount)
whiteAvg[1] = int(whiteAvg[1] / whiteCount)

#Black Pixel Avg
for y in range(len(blackMask)):
	for x in range(len(blackMask[y])):
		if blackMask[y,x] >= avgThreshold:
			blackCount += 1
			blackAvg[0] += x
			blackAvg[1] += y

blackAvg[0] = int(blackAvg[0] / blackCount)
blackAvg[1] = int(blackAvg[1] / blackCount)

cv2.circle(copyImg,(whiteAvg[0],whiteAvg[1]),2,(0,255,0),3)	#White Average Display
cv2.circle(copyImg,(blackAvg[0],blackAvg[1]),2,(255,0,0),3)	#Black Average Display

#Angle Calculation
lightAngle = math.degrees(math.atan((whiteAvg[1] - blackAvg[1])/(whiteAvg[0] - blackAvg[0])))
lightAngleGreen = lightAngle
lightAngleBlue = lightAngle

#Checking quadrants
#Green is the head :
midPoint = [int((whiteAvg[0] + blackAvg[0])/ 2),int((whiteAvg[1]+blackAvg[1])/2)]
if whiteAvg[0] >= midPoint[0]:
	if whiteAvg[1] >= midPoint[1]:
		#Fourth quad
		lightAngleGreen = lightAngle - 180
elif whiteAvg[0] < midPoint[0]:
	if whiteAvg[1] >= midPoint[1]:
		#Third Quad
		lightAngleGreen = lightAngle + 180
	elif whiteAvg[1] < midPoint[1]:
		#Second Quad
		lightAngleGreen = lightAngle + 90

#Blue is the head:
lightAngleBlue = lightAngleGreen + 180
while lightAngleBlue > 360:
	lightAngleBlue -= 360
lightAngleBlue = 360 - lightAngleBlue

lightAngleBlue = abs(lightAngleBlue)
lightAngleGreen = abs(lightAngleGreen)
#Displaying angle
copyImg = cv2.putText(copyImg,'Light Angle : ' + str(int(lightAngleGreen)) + 'D Or ' + str(int(lightAngleBlue)) + 'D',(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

cv2.imshow("White Mask",whiteMask)
cv2.imshow("Black Mask",blackMask)
cv2.imshow("Test",copyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()