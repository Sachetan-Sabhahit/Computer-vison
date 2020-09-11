import cv2
import numpy as np
cap = cv2.VideoCapture(0)

C1 = ([115, 95, 95], [120, 100, 100])
black = ([0, 0, 0], [0, 0, 0])
# green = ([67, 136, 0],[72, 138, 2])
# red = ([0, 0, 240], [100, 100, 255])
red = ([0, 0, 200], [5, 5, 255])
#green = ([0, 150, 0], [110, 255, 90])
#pink = ([90, 50, 240], [120, 75, 255])

green = ([0,189,150], [77,255,230])
orange = ([0,0,198],[93,50,253])
pink = ([100,7,193],[255,68,254])

L1 = 480
B1 = 640

L2 = 480
B2 = 640



def scale(x, y, L1, B1, L2, B2):
    x1 = int((x / L1) * L2)
    y1 = int((y / B1) * B2)
    return x1, y1

def filter(img, C):
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(C[0])
    upper = np.array(C[1])
    mask = cv2.inRange(img, lower, upper)
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    # res = cv2.bitwise_and(img, img, mask=mask)
    # return res
    return mask

while 1:
	my = np.zeros((L2, B2, 3), dtype="uint8")	
	ret, frame = cap.read()
	frame = frame[:, ::-1]
	# print(frame)
	frame = filter(frame, orange)#####################################
	print(my.shape)
	frame2, contours = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	print(type(contours))
	#exit()
	if type(contours) != None:
		print(contours)
	#exit()
		c = max(contours, key=cv2.contourArea)
		x, y, w, h = cv2.boundingArea(c)
		x, y = scale(x, y, L1, B1, L2, B2)
		cv2.circle(my, (x, y), 5, (255, 255, 255), -1)
	cv2.imshow("center", my)
	# print(frame[0, 0])
	cv2.imshow("test", frame)
	'''print(frame2)
	print(type(contours))'''
	#exit()
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break



cv2.destroyAllWindows()
cap.release()
