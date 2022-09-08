import cv2
import numpy as np

video = cv2.VideoCapture("dove.mp4")
image = cv2.imread("bg2.jpg")

def nothing():
	pass

cv2.namedWindow("Project")
cv2.resizeWindow("Project", 300,300)

cv2.createTrackbar('L - H', "Project", 0, 179, nothing)
cv2.createTrackbar('L - S', "Project", 0, 255, nothing)
cv2.createTrackbar('L - v', "Project", 0, 255, nothing)
cv2.createTrackbar('U - H', "Project", 179, 179, nothing)
cv2.createTrackbar('U - S', "Project", 255, 255, nothing)
cv2.createTrackbar('U - V', "Project", 255, 255, nothing)

while True:
	ret, frame = video.read()
	frame = cv2.resize(frame, (640,480))
	image = cv2.resize(image, (640,480))
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# l_s = cv2.getTrackbarPos('L - S', "Project")
	# l_h = cv2.getTrackbarPos('L - H', "Project")
	# l_v = cv2.getTrackbarPos('L - V', "Project")
	# u_h = cv2.getTrackbarPos('U - H', "Project")
	# u_s = cv2.getTrackbarPos('U - S', "Project")
	# u_v = cv2.getTrackbarPos('U - V', "Project")
	# l_green = np.array([l_h, l_s, l_v])
	# u_green = np.array([u_h, u_s, u_v])
	l_green = np.array([32, 94, 132])
	u_green = np.array([179, 255, 255])
	mask = cv2.inRange(hsv, l_green, u_green)
	res = cv2.bitwise_and(frame, frame, mask = mask)
	f = frame - res
	green_screen = np.where(f == 0, image, f)
	cv2.imshow("Frame", frame)
	# cv2.imshow("Mask", mask)
	cv2.imshow("RES", green_screen)
	k = cv2.waitKey(1)
	if k == ord('q'):
		break
video.release()
cv2.destroyAllWindows()
